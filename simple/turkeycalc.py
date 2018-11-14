LBS_PER_KG = 2.205
COOK_MINUTES_PER_KG = 31

si = input('Do you use the International System of Units (Metric System)? (y/n) ') == 'y'
if si:
    weight = int(input('How many kilograms is your turkey? '))
else:
    print("Oh, I'm sorry. You must be in one of those three backward countries that haven't adopted it.")
    weight = int(input('How many backwards-country-pounds is your turkey? ')) / LBS_PER_KG

stuffed = input('Is your turkey stuffed? (y/n) ') == 'y'

minutes = weight * COOK_MINUTES_PER_KG
if stuffed:
    minutes += 20

print('Please cook your turkey for', int(minutes), 'minutes.')

if not si:
    print('Enjoy life in your backwards country.')
