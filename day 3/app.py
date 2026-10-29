
import streamlit as st

st.set_page_config(
    page_title="Campus Energy Monitoring",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ Campus Energy Monitoring System")
st.write("Monitor electricity usage and calculate estimated energy costs.")

st.sidebar.header("Energy Details")

building = st.sidebar.selectbox(
    "Select Building",
    ["Engineering Block", "Library", "Computer Lab", "Hostel"]
)

units = st.sidebar.number_input(
    "Electricity Consumed (kWh)",
    min_value=0.0,
    value=500.0,
    step=50.0
)

rate = st.sidebar.number_input(
    "Cost per Unit (₹)",
    min_value=0.0,
    value=8.0,
    step=0.5
)

bill = units * rate

st.subheader(f"Energy Report: {building}")

col1, col2, col3 = st.columns(3)

col1.metric("Energy Consumption", f"{units:,.0f} kWh")
col2.metric("Cost per Unit", f"₹{rate:,.2f}")
col3.metric("Estimated Electricity Bill", f"₹{bill:,.2f}")

st.divider()

st.subheader("Sample Building Consumption")

energy_data = {
    "Building": [
        "Engineering Block",
        "Library",
        "Computer Lab",
        "Hostel"
    ],
    "Consumption (kWh)": [650, 350, 500, 800]
}

st.bar_chart(
    energy_data,
    x="Building",
    y="Consumption (kWh)"
)

st.caption("Day 3 Assignment | Streamlit App Deployment")
