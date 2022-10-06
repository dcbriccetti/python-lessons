from microbit import *
import music

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
    return round(scale(coordinate, from_=(-1, 1), to=(0, 4)))

def adjusted_acceleration(acceleration: float):
    enough_tilt = abs(acceleration) > TILT_IGNORE_THRESHOLD
    return acceleration / 1000 / SPEED_DIVISOR if enough_tilt else 0.0

def constrain(value: float, low: float, high: float):
    return min(max(value, low), high)

while True:
    display.clear()
    x_led = world_to_led(x)
    y_led = world_to_led(y)
    display.set_pixel(x_led, y_led, 9)
    music.pitch(scale(x_led, from_=(0, 4), to=(440, 880)))
    sleep(10)
    music.pitch(scale(y_led, from_=(0, 4), to=(880*2, 440*2)))
    sleep(10)
    music.stop()

    speed_x += adjusted_acceleration(accelerometer.get_x())
    x = constrain(x + speed_x, -1, 1)
    if abs(x) == 1:
        speed_x = 0
    speed_x *= FRICTION_MULTIPLIER

    speed_y += adjusted_acceleration(accelerometer.get_y())
    y = constrain(y + speed_y, -1, 1)
    if abs(y) == 1:
        speed_y = 0
    speed_y *= FRICTION_MULTIPLIER

    sleep(PAUSE_MS)
