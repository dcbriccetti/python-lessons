rateKph = float(eval(input('Rate (kilometers per hour)? ')))
rateKpm = rateKph / 60.0

print(('%f km per hour (%f km per minute)' % (rateKph, rateKpm)))
print('Time\tDistance')
print('(Mins)\t(km)')

for mins in range(16):
    dist = rateKpm * mins
    print(('%.2f \t %.2f' % (mins, dist)))
