def convertCelsiusToKelvin(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins"""
    return round(celsius + 273.15, 2)

def convertCelsiusToFahrenheit(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Fahrenheit"""
    return round((celsius * 9/5) + 32.0, 2)

def convertFahrenheitToCelsius(fahrenheit):
    return round((fahrenheit - 32.0) * 5/9, 2)

def convertFahrenheitToKelvin(fahrenheit):
    return round((fahrenheit + 459.67) * 5/9, 2)

def convertKelvinToCelsius(kelvin):
    return round(kelvin - 273.15, 2)

def convertKelvinToFahrenheit(kelvin):
    return round((kelvin * 9/5) - 459.67, 2)
