'''
app.py
Main app file that ties everything together, and defines the UI. 
'''

import streamlit as st
from models import CATEGORIES, create_car
from logic import GARAGE_SIZE, can_claim, claim_car, display_garage, reset_garage, total_value
from ui import empty_card, car_card

st.title("My Car!")
st.write("Spot cars on the road and fill your garage!")

# Initialize garage in session state if it doesn't exist
if "garage" not in st.session_state:
    st.session_state.garage = []


# Display Garage
st.subheader(f"Your Garage ({len(st.session_state.garage)}/{GARAGE_SIZE})")

slots = display_garage(st.session_state.garage)
cols = st.columns(GARAGE_SIZE) 

for i, col in enumerate(cols):
    with col:
        if slots[i] is None:
            empty_card()
        else:
            car_card(slots[i])


if len(st.session_state.garage) > 0:
    st.metric("Total Garage Value", f"${total_value(st.session_state.garage):,}")



# Car input and category selection
st.divider()

car_input = st.text_input("What car did you see?").strip()
category_key = st.selectbox(
    "What type of car is it?",
    options=list(CATEGORIES.keys()),
    format_func=lambda key: CATEGORIES[key]["label"]
)


# Claim button checks there is an input and adds it to the garage. 
if st.button("My Car!"):
    if car_input == "":
        st.warning("Please enter a car name.")
    elif not can_claim(st.session_state.garage):
        st.error(f"Your garage is full! You can only hold {GARAGE_SIZE} cars.")
    else:
        new_car = create_car(car_input, category_key)
        st.session_state.garage = claim_car(st.session_state.garage, new_car)
        st.success(f"{car_input} added to your garage!")
        st.rerun()  # Refresh to show the new car in the garage 


# Reset Game button
st.divider()
if st.button("Reset Game"):
    st.session_state.garage = reset_garage()
    st.success("Garage reset! Start spotting cars again.")
    st.rerun()