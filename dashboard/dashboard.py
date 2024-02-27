import streamlit as st
import pandas as pd

import streamlit_shadcn_ui as ui
from local_components import card_container

# CONFIGS
YEAR = 2018
PREVIOUS_YEAR = 2017
CITIES = ["SP", "MG", "PR"]
DATA_URL = "https://raw.githubusercontent.com/azissukmawan/sales-analysis-dashboard/main/dashboard/main_data.csv"
BAR_CHART_COLOR = "#000000"

st.set_page_config(page_title="Sales Dashboard", page_icon="📈")
st.title(f"Sales Dashboard", anchor=False)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


@st.cache_data
def get_and_prepare_data(data):
    df = pd.read_csv(data).assign(
        year_month=lambda df: pd.to_datetime(df["year_month"]).dt.to_period("M"),
        month=lambda df: df["year_month"].dt.month,
        year=lambda df: df["year_month"].dt.year,
    )
    return df


df = get_and_prepare_data(data=DATA_URL)

city_revenues = (
    df.groupby(["seller_state", "year"])["revenue"]
    .sum()
    .unstack()
    .assign(change=lambda x: x.pct_change(axis=1)[YEAR] * 100)
)


columns = st.columns(3)
for i, city in enumerate(CITIES):
    with columns[i]:
        ui.metric_card(
            title=city,
            content=f"$ {city_revenues.loc[city, YEAR]:,.2f}",
            description=f"vs. Last Year: {city_revenues.loc[city, 'change']:.2f}% change",
            key=f"card{i}",
        )


analysis_type = ui.tabs(
    options=["Month", "Product Category"],
    default_value="Month",
    key="analysis_type",
)

selected_city = ui.select("Select a city:", CITIES)

previous_year_toggle = ui.switch(
    default_checked=False, label="Previous Year", key="switch_visualization"
)
visualization_year = PREVIOUS_YEAR if previous_year_toggle else YEAR
st.write(f"**Sales for {visualization_year}**")

if analysis_type == "Product Category":
    filtered_data = (
        df.query("seller_state == @selected_city & year == @visualization_year")
        .groupby("product_category_name_english", dropna=False)["revenue"]
        .sum()
        .nlargest(5)
        .reset_index()
    )
else:
    filtered_data = (
        df.query("seller_state == @selected_city & year == @visualization_year")
        .groupby("month", dropna=False)["revenue"]
        .sum()
        .reset_index()
    )
    filtered_data["month"] = filtered_data["month"].apply(lambda x: f"{x:02d}")

vega_spec = {
    "mark": {"type": "bar", "cornerRadiusEnd": 4},
    "encoding": {
        "x": {
            "field": filtered_data.columns[0],
            "type": "nominal",
            "axis": {
                "labelAngle": 0,
                "title": None,
                "grid": False,
            },
        },
        "y": {
            "field": "revenue",
            "type": "quantitative",
            "axis": {
                "title": None,
                "grid": False,
            },
        },
        "color": {"value": BAR_CHART_COLOR},
    },
    "data": {
        "values": filtered_data.to_dict(
            "records"
        )
    },
}
with card_container(key="chart"):
    st.vega_lite_chart(vega_spec, use_container_width=True)