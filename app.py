# ============================================================
# Temperature Converter - a simple Streamlit web app
# ============================================================
# Streamlit turns a normal Python script into a web page.
# Every time the user changes something on the page, Streamlit
# re-runs this whole file from top to bottom.
# ============================================================


# ------------------------------------------------------------
# SECTION 1: Import the library we need
# ------------------------------------------------------------
# "st" is a short nickname for streamlit, so we can write
# st.title() instead of streamlit.title().
import streamlit as st


# ------------------------------------------------------------
# SECTION 2: Page settings
# ------------------------------------------------------------
# This sets the browser tab's title and icon, and centers the
# content on the page. It must be the first Streamlit command.
st.set_page_config(
    page_title="Temperature Converter",
    page_icon="🌡️",
    layout="centered",
)


# ------------------------------------------------------------
# SECTION 3: Conversion functions
# ------------------------------------------------------------
# A function is a reusable block of code. You give it an input
# (the temperature) and it gives back ("returns") an answer.

def celsius_to_fahrenheit(celsius):
    """Convert a Celsius temperature to Fahrenheit."""
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert a Fahrenheit temperature to Celsius."""
    return (fahrenheit - 32) * 5 / 9


# ------------------------------------------------------------
# SECTION 4: Page header
# ------------------------------------------------------------
st.title("🌡️ Temperature Converter")
st.write("Convert temperatures between **Celsius** and **Fahrenheit** instantly.")

# A thin horizontal line to separate sections visually.
st.divider()


# ------------------------------------------------------------
# SECTION 5: User inputs
# ------------------------------------------------------------
# st.radio shows a set of buttons where the user picks ONE option.
# Whatever they pick is stored in the variable "conversion_type".
conversion_type = st.radio(
    "Choose a conversion:",
    ["Celsius → Fahrenheit", "Fahrenheit → Celsius"],
    horizontal=True,  # show the options side by side
)

# st.number_input shows a box where the user types a number.
# value=0.0 is the starting number; step=1.0 is how much the
# +/- buttons change it; format="%.2f" shows 2 decimal places.
temperature = st.number_input(
    "Enter a temperature:",
    value=0.0,
    step=1.0,
    format="%.2f",
)


# ------------------------------------------------------------
# SECTION 6: Do the conversion
# ------------------------------------------------------------
# "if / else" lets the program choose what to do based on the
# user's selection.
if conversion_type == "Celsius → Fahrenheit":
    result = celsius_to_fahrenheit(temperature)
    from_unit = "°C"
    to_unit = "°F"
    # The formula written in LaTeX (a format for math symbols).
    formula = r"°F = (°C \times \frac{9}{5}) + 32"
    # The same formula with the user's actual numbers filled in.
    worked_example = f"({temperature:.2f} × 9/5) + 32 = {result:.2f}"
else:
    result = fahrenheit_to_celsius(temperature)
    from_unit = "°F"
    to_unit = "°C"
    formula = r"°C = (°F - 32) \times \frac{5}{9}"
    worked_example = f"({temperature:.2f} − 32) × 5/9 = {result:.2f}"


# ------------------------------------------------------------
# SECTION 7: Show the result
# ------------------------------------------------------------
st.divider()

# st.columns splits the page into side-by-side boxes.
col1, col2 = st.columns(2)

# st.metric displays a big, easy-to-read number with a label.
with col1:
    st.metric(label="You entered", value=f"{temperature:.2f} {from_unit}")
with col2:
    st.metric(label="Converted result", value=f"{result:.2f} {to_unit}")


# ------------------------------------------------------------
# SECTION 8: Show the formula
# ------------------------------------------------------------
st.subheader("📐 Formula used")

# st.latex draws the formula with proper math symbols.
st.latex(formula)

# st.info shows text inside a colored box.
st.info(f"**Step by step:** {worked_example}")


# ------------------------------------------------------------
# SECTION 9: Footer
# ------------------------------------------------------------
st.divider()
st.caption("Fun fact: −40° is the same in both Celsius and Fahrenheit!")
