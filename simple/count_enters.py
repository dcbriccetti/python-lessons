from time import time, sleep

messages = ['How many times can you press enter in ten seconds?', 'Get ready', 3, 2, 1, 'Go!']

for message in messages:
    sleep(1)
    print(message)

start_time = time()
end_time = start_time + 10
presses = 0

while time() < end_time:
    input()
    presses += 1

print(f'You pressed enter {presses} times.')
