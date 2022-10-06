PAUSE_MS = 10
SPEED_DIVISOR = 20
FRICTION_MULTIPLIER = 0.5
TILT_IGNORE_THRESHOLD = 10  # In milligravity units

x = 0.0  # world unit coordinates (from -1 to 1)
y = 0.0
speed_x = 0.0
speed_y = 0.0

def world_to_led(coordinate: float):
    'Convert a coordinate in world units (-1 to 1) to LED units (0 to 4)'
    return Math.round(pins.map(coordinate, -1, 1, 0, 4))

def adjusted_acceleration(dimension: float):
    acceleration = input.acceleration(dimension)
    enough_tilt = abs(acceleration) > TILT_IGNORE_THRESHOLD
    return acceleration / 1000 / SPEED_DIVISOR if enough_tilt else 0.0

while True:
    basic.clear_screen()
    x_led = world_to_led(x)
    y_led = world_to_led(y)
    led.plot(x_led, y_led)
    music.play_tone(pins.map(x_led, 0, 4, 440, 880), 10)
    music.play_tone(pins.map(y_led, 0, 4, 880*2, 440*2), 10)

    speed_x += adjusted_acceleration(Dimension.X)
    x = Math.constrain(x + speed_x, -1, 1)
    if abs(x) == 1:
        speed_x = 0
    speed_x *= FRICTION_MULTIPLIER

    speed_y += adjusted_acceleration(Dimension.Y)
    y = Math.constrain(y + speed_y, -1, 1)
    if abs(y) == 1:
        speed_y = 0
    speed_y *= FRICTION_MULTIPLIER

    pause(PAUSE_MS)
