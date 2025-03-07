import streamlit as st

# Initialize the session state for the calculator expression if it doesn't exist.
if 'expression' not in st.session_state:
    st.session_state.expression = ""

def update_expression(char):
    """Update the current expression based on the button pressed."""
    if char == "C":
        st.session_state.expression = ""
    elif char == "=":
        try:
            # Evaluate the expression and update it with the result.
            result = str(eval(st.session_state.expression))
            st.session_state.expression = result
        except Exception:
            st.error("Invalid Input")
            st.session_state.expression = ""
    else:
        st.session_state.expression += str(char)

# Display the title and the current expression.
st.title("Python Calculator")
st.text_input("Expression", value=st.session_state.expression, key="display", disabled=True)

# Define the layout of the calculator buttons.
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', 'C', '=', '+']
]

# Create a grid layout for the buttons.
for row in buttons:
    cols = st.columns(len(row))
    for idx, char in enumerate(row):
        if cols[idx].button(char):
            update_expression(char)
            # Rerun the script to update the displayed expression.
            st.experimental_rerun()
