import conversions

def convertMilesToYards(miles):
    return round(miles * 1760, 2)

def convertMilesToMeters(miles):
    return round(miles * 1609.344, 2)

def convertYardsToMiles(yards):
    return round(yards / 1760, 2)

def convertYardsToMeters(yards):
    return round(yards * 0.9144, 2)

def convertMetersToMiles(meters):
    return round(meters / 1609.344, 2)

def convertMetersToYards(meters):
    return round(meters / 0.9144, 2)


class ConversionNotPossible(Exception):
    pass


def convert(fromUnit, toUnit, value):
    conversionFunctions = {
        ("Celsius", "Kelvin"): conversions.convertCelsiusToKelvin,
        ("Celsius", "Fahrenheit"): conversions.convertCelsiusToFahrenheit,
        ("Fahrenheit", "Celsius"): conversions.convertFahrenheitToCelsius,
        ("Fahrenheit", "Kelvin"): conversions.convertFahrenheitToKelvin,
        ("Kelvin", "Celsius"): conversions.convertKelvinToCelsius,
        ("Kelvin", "Fahrenheit"): conversions.convertKelvinToFahrenheit,
        ("Miles", "Yards"): convertMilesToYards,
        ("Miles", "Meters"): convertMilesToMeters,
        ("Yards", "Miles"): convertYardsToMiles,
        ("Yards", "Meters"): convertYardsToMeters,
        ("Meters", "Miles"): convertMetersToMiles,
        ("Meters", "Yards"): convertMetersToYards
    }

    conversion = (fromUnit, toUnit)
    if conversion in conversionFunctions:
        return conversionFunctions[conversion](value)
    else:
        raise ConversionNotPossible(f"Can't convert from {fromUnit} to {toUnit}")

if __name__ == "__main__":
    pass
#    print(convert("Celsius","Fahrenheit", -40))
#    print(convert("Miles","Meters", 15))
#    print(convert("Yards","Meters", 15))

