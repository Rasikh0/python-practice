def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32


def celsius_to_kelvin(c):
    return c + 273.15


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


def fahrenheit_to_kelvin(f):
    return celsius_to_kelvin(fahrenheit_to_celsius(f))


def kelvin_to_celsius(k):
    return k - 273.15


def kelvin_to_fahrenheit(k):
    return celsius_to_fahrenheit(kelvin_to_celsius(k))


conversions = {
    ("C", "F"): celsius_to_fahrenheit, ("C", "K"): celsius_to_kelvin, ("F", "C"): fahrenheit_to_celsius, ("F", "K"): fahrenheit_to_kelvin, ("K", "C"): kelvin_to_celsius, ("K", "F"): kelvin_to_fahrenheit}

units = {"C": "Celsius", "F": "Fahrenheit", "K": "Kelvin"}


def convert(value, from_unit, to_unit):
    from_unit = from_unit.upper()
    to_unit = to_unit.upper()

    if from_unit not in units or to_unit not in units:
        raise ValueError("Units must be one of: C, F, K")

    if from_unit == to_unit:
        return value

    return conversions[(from_unit, to_unit)](value)


def prompt_unit(label):
    while True:
        unit = input(f"{label} (C/F/K): ").strip().upper()
        if unit in units:
            return unit
        print("Please enter C, F, or K.")


def prompt_value():
    while True:
        raw = input("Enter the temperature value: ").strip()
        try:
            return float(raw)
        except ValueError:
            print("Please enter a numeric value.")


def main():
    print("Temperature Converter")
    while True:
        from_unit = prompt_unit("Convert from")
        to_unit = prompt_unit("Convert to")
        value = prompt_value()

        result = convert(value, from_unit, to_unit)
        print(f"{value} degrees {units[from_unit]} = " f"{result:.2f} degrees {units[to_unit]}")

        again = input("Would you like to convert another value? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thank you! Goodbye!")
            break


if __name__ == "__main__":
    main()
