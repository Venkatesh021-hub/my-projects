import streamlit as st
import pandas as pd
import folium
from geopy.distance import geodesic
from streamlit_folium import st_folium
from pathlib import Path


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Telangana Power Transmission Map",
    page_icon="⚡",
    layout="wide"
)


# ---------------- TITLE ----------------

st.title("⚡ Power Transmission Route Map")

st.subheader(
    "Power Generation at Srisailam to MGIT, Hyderabad"
)

st.info(
    "Interactive geographical mapping of power generation, "
    "transmission and distribution infrastructure in Telangana."
)


# ---------------- LOAD DATA ----------------

@st.cache_data
def load_data():

    csv_path = Path(__file__).resolve().parent / "power_TR.csv"

    try:
        df = pd.read_csv(csv_path)

        df.columns = df.columns.str.strip().str.upper()

        df["LATITUDE"] = pd.to_numeric(
            df["LATITUDE"], errors="coerce"
        )

        df["LONGITUDE"] = pd.to_numeric(
            df["LONGITUDE"], errors="coerce"
        )

        df = df.dropna(subset=["LATITUDE", "LONGITUDE"])

        return df

    except Exception as e:
        st.error(f"Unable to load CSV: {e}")
        return pd.DataFrame()

try:
    df = load_data()

except Exception as e:
    st.error(f"Unable to load CSV: {e}")
    st.stop()


# ---------------- DASHBOARD METRICS ----------------

st.subheader("Network Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Locations",
    len(df)
)

col2.metric(
    "Generation",
    df["FUNCTION"].str.contains(
        "generation", case=False, na=False
    ).sum()
)

col3.metric(
    "Transmission",
    df["FUNCTION"].str.contains(
        "transmission", case=False, na=False
    ).sum()
)

col4.metric(
    "Distribution",
    df["FUNCTION"].str.contains(
        "distribution", case=False, na=False
    ).sum()
)


# ---------------- MAP ----------------

st.subheader("Transmission Network Map")


m = folium.Map(
    location=[17.2, 78.5],
    zoom_start=7,
    tiles=None
)


# Map layers

folium.TileLayer(
    "OpenStreetMap",
    name="Street Map"
).add_to(m)

folium.TileLayer(
    "CartoDB dark_matter",
    name="Dark Map"
).add_to(m)


# Marker colours

def get_colour(function):

    function = str(function).lower()

    if "generation" in function:
        return "red"

    elif "transmission" in function:
        return "blue"

    elif "distribution" in function:
        return "orange"

    elif "load" in function:
        return "green"

    elif "evacuation" in function:
        return "purple"

    else:
        return "gray"

# ---------------- DISTANCE CALCULATION ----------------

from geopy.distance import geodesic

st.subheader("Route Distance")

# Identify generation station
start = df[
    df["FUNCTION"].str.contains(
        "generation",
        case=False,
        na=False
    )
]

# Identify MGIT load location
end = df[
    df["FUNCTION"].str.contains(
        "load",
        case=False,
        na=False
    )
]

if not start.empty and not end.empty:

    start_point = (
        start.iloc[0]["LATITUDE"],
        start.iloc[0]["LONGITUDE"]
    )

    end_point = (
        end.iloc[0]["LATITUDE"],
        end.iloc[0]["LONGITUDE"]
    )

    distance = geodesic(
        start_point,
        end_point
    ).kilometers

    st.metric(
        "Srisailam to MGIT (Straight-line distance)",
        f"{distance:.2f} km"
    )

else:
    st.warning(
        "Generation station or MGIT location not found."
    )
# Add locations

for _, row in df.iterrows():

    colour = get_colour(row["FUNCTION"])

    popup = f"""
    <b>{row['LOCATION']}</b><br>
    Function: {row['FUNCTION']}<br>
    Latitude: {row['LATITUDE']}<br>
    Longitude: {row['LONGITUDE']}
    """

    folium.Marker(

        location=[
            row["LATITUDE"],
            row["LONGITUDE"]
        ],

        tooltip=row["LOCATION"],

        popup=folium.Popup(
            popup,
            max_width=300
        ),

        icon=folium.Icon(
            color=colour,
            icon="bolt",
            prefix="fa"
        )

    ).add_to(m)

# ---------------- GEOGRAPHICAL REFERENCE LINE ----------------

# Identify starting and ending locations

start = df[
    df["FUNCTION"].str.contains(
        "generation", case=False, na=False
    )
]

end = df[
    df["FUNCTION"].str.contains(
        "load", case=False, na=False
    )
]

if not start.empty and not end.empty:

    start_location = [
        start.iloc[0]["LATITUDE"],
        start.iloc[0]["LONGITUDE"]
    ]

    end_location = [
        end.iloc[0]["LATITUDE"],
        end.iloc[0]["LONGITUDE"]
    ]

    folium.PolyLine(
        locations=[
            start_location,
            end_location
        ],
        color="red",
        weight=3,
        opacity=0.8,
        dash_array="10, 10",
        tooltip="Srisailam to MGIT - Straight-line reference only"
    ).add_to(m)
# Map controls

folium.LayerControl().add_to(m)


# Display map
# Automatically fit all station locations

locations = df[
    ["LATITUDE", "LONGITUDE"]
].values.tolist()

m.fit_bounds(locations)
st_folium(
    m,
    height=550,
    use_container_width=True
)


# ---------------- STATION DETAILS ----------------

st.subheader("Station Details")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)


# ---------------- DOWNLOAD ----------------

st.download_button(
    label="Download Station Data",
    data=df.to_csv(index=False),
    file_name="power_transmission_data.csv",
    mime="text/csv"
)


# ---------------- FOOTER ----------------

st.divider()

st.caption(
    "Telangana Power Transmission Mapping Project | "
    "Developed using Python and Streamlit"
)
