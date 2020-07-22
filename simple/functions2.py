def celsius_to_fahrenheit(celsius_temp: float) -> float:
    return celsius_temp * 1.8 + 32

celsius_temp = float(input('What is the temperature in Celsius? '))
fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
print(f'In old fashioned Fahrenheit degrees, that is {fahrenheit_temp}')
