def convert_length(val, from_unit, to_unit):
    meters = {
        "m": 1,
        "cm": 0.01,
        "mm": 0.001,
        "km": 1000,
        "in": 0.0254,
        "ft": 0.3048,
        "yd": 0.9144,
        "mi": 1609.34
    }

    if from_unit not in meters or to_unit not in meters:
        return None

    value_in_meters = val * meters[from_unit]
    return value_in_meters / meters[to_unit]

def convert_temp(val, from_unit, to_unit):
    if from_unit == "c":
        if to_unit == "f":
            return (val * 9/5) + 32
        elif to_unit == "k":
            return val + 273.15
        elif to_unit == "c":
            return val
    elif from_unit == "f":
        if to_unit == "c":
            return (val - 32) * 5/9
        elif to_unit == "k":
            return (val - 32) * 5/9 + 273.15
        elif to_unit == "f":
            return val
    elif from_unit == "k":
        if to_unit == "c":
            return val - 273.15
        elif to_unit == "f":
            return (val - 273.15) * 9/5 + 32
        elif to_unit == "k":
            return val
    return None

def convert_currency(val, from_unit, to_unit):
    rates = {
        "usd": 1.0,
        "inr": 85.56,
        "eur": 0.85,
        "gbp": 0.73,
        "jpy": 143.08
    }

    if from_unit not in rates or to_unit not in rates:
        return None

    in_usd = val / rates[from_unit]
    return in_usd * rates[to_unit]

def main():
    print("Unit Converter – Length / Temperature / Currency")
    print("Type 'exit' anytime to quit.\n")

    while True:
        conv_type = input("Choose type (length / temp / currency): ").strip().lower()
        if conv_type == "exit":
            break

        if conv_type not in ["length", "temp", "currency"]:
            print("Invalid type. Try again.")
            continue

        value = input("Enter value: ").strip()
        if value.lower() == "exit":
            break

        try:
            value = float(value)
        except:
            print("Not a number.")
            continue

        from_unit = input("From unit: ").strip().lower()
        if from_unit == "exit":
            break

        to_unit = input("To unit: ").strip().lower()
        if to_unit == "exit":
            break

        if conv_type == "length":
            result = convert_length(value, from_unit, to_unit)
        elif conv_type == "temp":
            result = convert_temp(value, from_unit, to_unit)
        elif conv_type == "currency":
            result = convert_currency(value, from_unit, to_unit)
        else:
            result = None

        if result is None:
            print("Conversion failed. Inputs may be wrong.")
        else:
            print(f"{value} {from_unit} = {round(result, 4)} {to_unit}\n")

if __name__ == "__main__":
    main()
