import conversions

def testCtoK():
    try:
        assert conversions.convertCelsiusToKelvin(0) == 273.15
        assert conversions.convertCelsiusToKelvin(100) == 373.15
        assert conversions.convertCelsiusToKelvin(-273.15) == 0.00
        assert conversions.convertCelsiusToKelvin(-40) == 233.15
        assert conversions.convertCelsiusToKelvin(37) == 310.15
        return True
    except AssertionError:
        return False

def testCtoF():
    try:
        assert conversions.convertCelsiusToFahrenheit(0) == 32.00
        assert conversions.convertCelsiusToFahrenheit(100) == 212.00
        assert conversions.convertCelsiusToFahrenheit(-40) == -40.00
        assert conversions.convertCelsiusToFahrenheit(37) == 98.6
        assert conversions.convertCelsiusToFahrenheit(-273.15) == -459.67
        return True
    except AssertionError:
        return False

def testFtoC():
    try:
        assert conversions.convertFahrenheitToCelsius(32) == 0.00
        assert conversions.convertFahrenheitToCelsius(212) == 100.00
        assert conversions.convertFahrenheitToCelsius(-40) == -40.00
        assert conversions.convertFahrenheitToCelsius(98.6) == 37
        assert conversions.convertFahrenheitToCelsius(-459.67) == -273.15
        return True
    except AssertionError:
        return False

def testftoK():
    try:
        assert conversions.convertFahrenheitToKelvin(32) == 273.15
        assert conversions.convertFahrenheitToKelvin(212) == 373.15
        assert conversions.convertFahrenheitToKelvin(-459.67) == 0
        assert conversions.convertFahrenheitToKelvin(-40) == 233.15
        assert conversions.convertFahrenheitToKelvin(98.6) == 310.15
        return True
    except AssertionError:
        return False

def testKtoC():
    try:
        assert conversions.convertKelvinToCelsius(273.15) == 0.00
        assert conversions.convertKelvinToCelsius(373.15) == 100.00
        assert conversions.convertKelvinToCelsius(0) == -273.15
        assert conversions.convertKelvinToCelsius(310.15) == 37
        assert conversions.convertKelvinToCelsius(233.15) == -40
        return True
    except AssertionError:
        return False

def testKtoF():
    try:
        assert conversions.convertKelvinToFahrenheit(273.15) == 32.00
        assert conversions.convertKelvinToFahrenheit(310.15) == 98.6
        assert conversions.convertKelvinToFahrenheit(0) == -459.67
        assert conversions.convertKelvinToFahrenheit(373.15) == 212.00
        assert conversions.convertKelvinToFahrenheit(233.15) == -40.00
        return True
    except AssertionError:
        return False

if __name__ == "__main__":
    tests = True
    if testCtoK() == False:
        tests = False
        print(f"C to K conversion did not work")
    if testCtoF() == False:
        tests = False
        print(f"C to F conversion did not work")
    if testFtoC() == False:
        tests = False
        print(f"F to C conversion did not work")
    if testFtoC() == False:
        tests = False
        print(f"F to K conversion did not work")
    if testKtoC() == False:
        tests = False
        print(f"K to C conversion did not work")
    if testKtoC() == False:
        tests = False
        print(f"K to F conversion did not work")
    elif tests == True:
        print("All conversion tests passed!")
