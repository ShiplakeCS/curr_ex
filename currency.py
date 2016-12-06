rates = {"USD":1.25,
         "EUR":1.18,
         "CAD":1.69,
         "AUS":1.68}

def getConvertedAmount(amount, currency):
    global rates
    try:
        converted = float(amount) * rates[currency]
        return converted
    except KeyError:
        print("Error: Currency %s not found in rates dictionary." % currency)
        return None

def getCurrencyList():
    global rates
    return rates