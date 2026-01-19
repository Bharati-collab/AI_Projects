import streamlit as st
import langchainhelper

st.title("Restaurant Concept Generator (Structured Output)")

cuisine = st.sidebar.selectbox(
    "Pick a Cuisine",
    ("Indian", "Italian", "Mexican", "Arabic", "American")
)

if cuisine:
    data = langchainhelper.get_restaurant_name_and_items(cuisine)

    st.subheader("Restaurant Name")
    st.write(data["restaurant_name"])

    st.subheader("Tagline")
    st.write(data["tagline"])

    st.subheader("Concept")
    col1, col2, col3 = st.columns(3)
    col1.metric("Cuisine", data["cuisine"])
    col2.metric("Price Range", data["price_range"])
    col3.metric("Target", data["target_customer"])

    st.subheader("Menu Items")
    st.write(", ".join(data["menu_items"]))


    show_json = st.checkbox("Show raw JSON (for debugging)", value=False)
    if show_json:
        st.subheader("Raw JSON")
        st.json(data)
