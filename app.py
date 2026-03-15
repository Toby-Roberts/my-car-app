import streamlit as st

st.title("My Car!")

# Initialize garage in session state if it doesn't exist
if "garage" not in st.session_state:
    st.session_state.garage = []

# Input to add a car
car_input = st.text_input("What car did you see?").strip()
 

# Claim button checks there is an input and adds it to the garage. 
if st.button("My Car!"):
    if car_input == "":
        st.warning("Please enter a car name.")
    else:
        st.session_state.garage.append(car_input)
        st.success(f"{car_input} added to your garage!")

# Display the garage
st.subheader("Your Garage:")
if len(st.session_state.garage) == 0:
    st.info("Your garage is empty. Add some cars!")
else:  
    for i, car in enumerate(st.session_state.garage, start=1):
        st.write(f"{i}. {car}")