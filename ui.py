'''
ui.py
Helper functions for rendering UI components.
Keeps all the HTML and styling out of app.py.
'''

import streamlit as st

def empty_card():
    """Renders an empty garage slot card."""
    st.markdown(
        """
        <div style="border: 2px dashed #555; border-radius: 0.625rem; 
        padding: 1.25rem; text-align: center; color: #888; min-height: 7.5rem;
        display: flex; align-items: center; justify-content: center;">
            Empty
        </div>
        """,
        unsafe_allow_html=True
    )

def car_card(car):
    """Renders a filled garage slot card for a given car."""
    st.markdown(
        f"""
        <div style="border: 2px solid #4a9eff; border-radius: 0.625rem; 
        padding: 1.25rem; text-align: center; min-height: 7.5rem;">
            <div style="font-size: 0.875rem; font-weight: bold;">{car['name']}</div>
            <div style="color: #4a9eff; margin-top: 0.5rem;">${car['value']:,}</div>
            <div style="color: #888; font-size: 0.75rem;">{car['category']}</div>
        </div>
        """,
        unsafe_allow_html=True
    )