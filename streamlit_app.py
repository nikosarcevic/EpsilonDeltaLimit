import streamlit as st
import functions


st.set_page_config(page_title="Epsilon-Delta Limit Checker", layout="centered")

# Sidebar for navigation
st.sidebar.title("Navigation")
selected_page = st.sidebar.radio("Choose a page:", ["Theoretical Explanation", "Calculations", "About"])

if selected_page == "Theoretical Explanation":
    st.title("Theoretical Explanation of Epsilon-Delta Definition of Limits")

    st.write("""
    The ε-δ (epsilon-delta) definition is a formal mathematical definition of the limit of a function. 
    The definition states:

    For every real number ε > 0, there exists a real number δ > 0 such that if 0 < |x - c| < δ, 
    then |f(x) - L| < ε.

    - \( ε \) (epsilon) represents how close the function values (outputs) get to the limit L.
    - \( δ \) (delta) represents how close the input values (x) need to be to c (a point of interest) to ensure the function values are within ε of L.

    Essentially, this definition provides a way to make the function values as close as we want to the limit L 
    by choosing the input values sufficiently close to c.
    """)

elif selected_page == "Calculations":
    st.title("Epsilon-Delta Checker")

    # Dropdown for function selection
    selected_function = st.selectbox(
        "Select a function:",
        list(functions.FUNCTIONS.keys())
    )

    # Slider for the point of interest
    point_of_interest = st.slider(
        "Select the point of interest (x₀):",
        -10.0,
        10.0,
        0.0,
        0.1
    )

    # Text input for the limit value
    limit_value = st.number_input("Enter the expected limit value:", value=0.0)

    # Slider for epsilon
    epsilon = st.slider(
        "Choose an epsilon value:",
        0.01,
        1.0,
        0.1,
        0.01
    )

    # Calculate delta based on the given function, point, limit, and epsilon
    delta = functions.epsilon_delta_check(functions.FUNCTIONS[selected_function], point_of_interest, limit_value, epsilon)
    st.write(f"For ε = {epsilon}, δ = {delta:.5f}")

    # Plot using the function from functions module
    fig = functions.plot_epsilon_delta(
        selected_function,
        functions.FUNCTIONS[selected_function],
        point_of_interest,
        limit_value,
        epsilon,
        delta
    )

    st.pyplot(fig)

elif selected_page == "About":
    st.title("About this App")
    st.write("""
    This app is designed to provide a visual and computational representation of the epsilon-delta definition of limits. 
    It helps to understand how changing the values of epsilon impacts the needed delta for a given function at a specific point.
    """)

    st.write("App made by Niko Sarcevic [GitHub](https://github.com/nikosarcevic) upon request by Steve McCormick.")
