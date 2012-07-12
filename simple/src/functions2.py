def celToFahr(celciusTemp):
    return celciusTemp * 1.8 + 32

celciusTemp = int(input('What is the temperature in Celcius? '))
print('In old fashioned Fahrenheit degrees, that is', celToFahr(celciusTemp))
