import streamlit as st

# Function to convert units
def convert_units(value, from_unit, to_unit):
    conversion_factors = {
        'Length': {
            'meters': 1,
            'kilometers': 0.001,
            'miles': 0.000621371,
            'feet': 3.28084,
            'inches': 39.3701
        },
        'Weight': {
            'grams': 1,
            'kilograms': 0.001,
            'pounds': 0.00220462,
            'ounces': 0.035274
        },
        'Temperature': {
            'Celsius': lambda x: x,
            'Fahrenheit': lambda x: (x * 9/5) + 32,
            'Kelvin': lambda x: x + 273.15
        }
    }

    if from_unit in conversion_factors['Length']:
        return value * conversion_factors['Length'][to_unit] / conversion_factors['Length'][from_unit]
    elif from_unit in conversion_factors['Weight']:
        return value * conversion_factors['Weight'][to_unit] / conversion_factors['Weight'][from_unit]
    elif from_unit in conversion_factors['Temperature']:
        if from_unit == 'Celsius':
            if to_unit == 'Fahrenheit':
                return (value * 9/5) + 32
            elif to_unit == 'Kelvin':
                return value + 273.15
        elif from_unit == 'Fahrenheit':
            if to_unit == 'Celsius':
                return (value - 32) * 5/9
            elif to_unit == 'Kelvin':
                return (value - 32) * 5/9 + 273.15
        elif from_unit == 'Kelvin':
            if to_unit == 'Celsius':
                return value - 273.15
            elif to_unit == 'Fahrenheit':
                return (value - 273.15) * 9/5 + 32

    return None

# Streamlit app layout
st.title("Unit Converter App")

# Select conversion type
conversion_type = st.selectbox("Select conversion type", ["Length", "Weight", "Temperature"])

# Input value
value = st.number_input("Enter value to convert", min_value=0.0)

# Select units
if conversion_type == "Length":
    from_unit = st.selectbox("From unit", ['meters', 'kilometers', 'miles', 'feet', 'inches'])
    to_unit = st.selectbox("To unit", ['meters', 'kilometers', 'miles', 'feet', 'inches'])
elif conversion_type == "Weight":
    from_unit = st.selectbox("From unit", ['grams', 'kilograms', 'pounds', 'ounces'])
    to_unit = st.selectbox("To unit", ['grams', 'kilograms', 'pounds', 'ounces'])
elif conversion_type == "Temperature":
    from_unit = st.selectbox("From unit", ['Celsius', 'Fahrenheit', 'Kelvin'])
    to_unit = st.selectbox("To unit", ['Celsius', 'Fahrenheit', 'Kelvin'])

# Convert button
if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit)
    if result is not None:
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
    else:
        st.error("Conversion not possible.")