import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import pandas as pd

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="Flat LED Display Specification Simulator",
    page_icon="yenrich.png",
    layout="wide"
)

# -----------------------------
# Matplotlib dark style
# -----------------------------
plt.style.use("dark_background")

# -----------------------------
# Fixed cabinet size (mm)
# -----------------------------
CABINET_WIDTH_MM = 600.0
CABINET_HEIGHT_MM = 337.5

# -----------------------------
# Product catalog
# -----------------------------
PRODUCT_CATALOG = {
    "FC series - P0.93": {
        "pixel_pitch_mm": 0.9375,
        "resolution_w": 640,
        "resolution_h": 360,
        "unit_price_usd_per_m2": 5200,
        "color_depth": "16 bit",
        "contrast_ratio": "8,000 : 1",
        "power_consumption_per_cabinet_w": 40,
        "brightness_nits": 1000,
        "refresh_rate": "≥7680Hz",
        "view_angle_h": "170°",
        "view_angle_v": "170°",
        "led_lifetime": "100,000 Hrs",
        "maintenance": "Front",
        "ip_rating": "IP30",
    },
    "FC series - P1.25": {
        "pixel_pitch_mm": 1.25,
        "resolution_w": 480,
        "resolution_h": 270,
        "unit_price_usd_per_m2": 3500,
        "color_depth": "16 bit",
        "contrast_ratio": "9,000 : 1",
        "power_consumption_per_cabinet_w": 40,
        "brightness_nits": 1000,
        "refresh_rate": "≥7680Hz",
        "view_angle_h": "170°",
        "view_angle_v": "170°",
        "led_lifetime": "100,000 Hrs",
        "maintenance": "Front",
        "ip_rating": "IP30",
    },
    "VC series - P0.93": {
        "pixel_pitch_mm": 0.9375,
        "resolution_w": 640,
        "resolution_h": 360,
        "unit_price_usd_per_m2": 3526,
        "color_depth": "13 bit",
        "contrast_ratio": "8,000 : 1",
        "power_consumption_per_cabinet_w": 60,
        "brightness_nits": 1000,
        "refresh_rate": "≥3,840 Hz",
        "view_angle_h": "160°",
        "view_angle_v": "160°",
        "led_lifetime": "100,000 Hrs",
        "maintenance": "Front",
        "ip_rating": "IP30",
    },
    "VC series - P1.25": {
        "pixel_pitch_mm": 1.25,
        "resolution_w": 480,
        "resolution_h": 270,
        "unit_price_usd_per_m2": 1913,
        "color_depth": "13 bit",
        "contrast_ratio": "9,000 : 1",
        "power_consumption_per_cabinet_w": 60,
        "brightness_nits": 1000,
        "refresh_rate": "≥3,840 Hz",
        "view_angle_h": "160°",
        "view_angle_v": "160°",
        "led_lifetime": "100,000 Hrs",
        "maintenance": "Front",
        "ip_rating": "IP30",
    },
    "VC series - P1.56": {
        "pixel_pitch_mm": 1.5625,
        "resolution_w": 384,
        "resolution_h": 216,
        "unit_price_usd_per_m2": 1643,
        "color_depth": "13 bit",
        "contrast_ratio": "10,000:1",
        "power_consumption_per_cabinet_w": 60,
        "brightness_nits": 1000,
        "refresh_rate": "≥3,840 Hz",
        "view_angle_h": "160°",
        "view_angle_v": "160°",
        "led_lifetime": "100,000 Hrs",
        "maintenance": "Front",
        "ip_rating": "IP30",
    },
    "VC series - P1.87": {
        "pixel_pitch_mm": 1.875,
        "resolution_w": 320,
        "resolution_h": 180,
        "unit_price_usd_per_m2": 1468,
        "color_depth": "13 bit",
        "contrast_ratio": "10,000:1",
        "power_consumption_per_cabinet_w": 60,
        "brightness_nits": 1000,
        "refresh_rate": "≥3,840 Hz",
        "view_angle_h": "160°",
        "view_angle_v": "160°",
        "led_lifetime": "100,000 Hrs",
        "maintenance": "Front",
        "ip_rating": "IP30",
    },
    "HC series - P0.93": {
        "pixel_pitch_mm": 0.9375,
        "resolution_w": 640,
        "resolution_h": 360,
        "unit_price_usd_per_m2": 5254,
        "color_depth": "19 bit",
        "contrast_ratio": "15,000:1",
        "power_consumption_per_cabinet_w": 80,
        "brightness_nits": 800,
        "refresh_rate": "3840",
        "view_angle_h": "160",
        "view_angle_v": "160",
        "led_lifetime": "100,000",
        "maintenance": "Front",
        "ip_rating": "IP20",
    },
    "HC series - P1.25": {
        "pixel_pitch_mm": 1.25,
        "resolution_w": 480,
        "resolution_h": 270,
        "unit_price_usd_per_m2": 2489,
        "color_depth": "19 bit",
        "contrast_ratio": "15,000:1",
        "power_consumption_per_cabinet_w": 75,
        "brightness_nits": 800,
        "refresh_rate": "3840",
        "view_angle_h": "160",
        "view_angle_v": "160",
        "led_lifetime": "100,000",
        "maintenance": "Front",
        "ip_rating": "IP20",
    },
    "HC series - P1.56": {
        "pixel_pitch_mm": 1.5625,
        "resolution_w": 384,
        "resolution_h": 216,
        "unit_price_usd_per_m2": 2341,
        "color_depth": "19 bit",
        "contrast_ratio": "15,000:1",
        "power_consumption_per_cabinet_w": 70,
        "brightness_nits": 800,
        "refresh_rate": "3840",
        "view_angle_h": "160",
        "view_angle_v": "160",
        "led_lifetime": "100,000",
        "maintenance": "Front",
        "ip_rating": "IP20",
    },
    "HC series - P1.87": {
        "pixel_pitch_mm": 1.875,
        "resolution_w": 320,
        "resolution_h": 180,
        "unit_price_usd_per_m2": 1916,
        "color_depth": "19 bit",
        "contrast_ratio": "15,000:1",
        "power_consumption_per_cabinet_w": 65,
        "brightness_nits": 800,
        "refresh_rate": "3840",
        "view_angle_h": "160",
        "view_angle_v": "160",
        "led_lifetime": "100,000",
        "maintenance": "Front",
        "ip_rating": "IP20",
    },
}

# -----------------------------
# Sidebar inputs
# -----------------------------
st.sidebar.header("Input Parameters")
st.sidebar.caption("(All fields are required.)")


selected_model = st.sidebar.selectbox(
    "Model Select",
    options=list(PRODUCT_CATALOG.keys()),
    index=0
)

wall_width_mm = st.sidebar.number_input(
    "Wall Width (mm)", min_value=1000.0, value=6000.0, step=100.0
)

wall_height_mm = st.sidebar.number_input(
    "Wall Height (mm)", min_value=1000.0, value=3000.0, step=100.0
)

bottom_offset_mm = st.sidebar.number_input(
    "Bottom Offset (mm)",
    min_value=0.0,
    value=500.0,
    step=50.0
)

cabinet_qty_h = st.sidebar.number_input(
    "Cabinet Qty Horizontal", min_value=1, value=6, step=1
)

cabinet_qty_v = st.sidebar.number_input(
    "Cabinet Qty Vertical", min_value=1, value=6, step=1
)

# -----------------------------
# Selected product info
# -----------------------------
selected_product = PRODUCT_CATALOG[selected_model]

cabinet_resolution_w = selected_product["resolution_w"]
cabinet_resolution_h = selected_product["resolution_h"]
unit_price_usd_per_m2 = selected_product["unit_price_usd_per_m2"]

# -----------------------------
# Calculation
# -----------------------------
led_width_mm = cabinet_qty_h * CABINET_WIDTH_MM
led_height_mm = cabinet_qty_v * CABINET_HEIGHT_MM

margin_left_mm = (wall_width_mm - led_width_mm) / 2

draw_led_x = max(margin_left_mm, 0)
draw_led_y = bottom_offset_mm

fit_ok = (
    (led_width_mm <= wall_width_mm) and
    (draw_led_y + led_height_mm <= wall_height_mm)
)

total_cabinet_qty = cabinet_qty_h * cabinet_qty_v
total_resolution_w = cabinet_qty_h * cabinet_resolution_w
total_resolution_h = cabinet_qty_v * cabinet_resolution_h
display_area_m2 = (led_width_mm * led_height_mm) / 1_000_000
wall_area_m2 = (wall_width_mm * wall_height_mm) / 1_000_000
reference_total_price_usd = display_area_m2 * unit_price_usd_per_m2
total_power_w = selected_product["power_consumption_per_cabinet_w"] * total_cabinet_qty
# -----------------------------
# Header
# -----------------------------
st.image("yenrich.png", width=130)

st.markdown(
    """
    <h1 style='margin:0; font-size:34px;'>
    Flat LED Display Specification Simulator
    </h1>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# KPI Section
# -----------------------------
st.divider()

c1, c2, c3, c4 = st.columns(4)
c1.metric("LED Display Size (mm)", f"{led_width_mm:.0f} × {led_height_mm:.0f} ")
c2.metric("Resolution", f"{total_resolution_w} × {total_resolution_h}")
c3.metric("Display Area", f"{display_area_m2:.2f} m²")
c4.metric("Total Power", f"{total_power_w:.1f} W")

st.divider()

# -----------------------------
# Product Specification
# -----------------------------
st.subheader("Product Specification")

spec_df = pd.DataFrame({
    "Product": [
        "Selected Model",
        "Pixel Pitch (mm)",
        "Resolution (W×H)",
        "LED Display Size (mm)",
        "Display Area (m²)",
        "Color Depth",
        "Contrast Ratio",
        "Maximum Power Consumption (W)",
        "Brightness (nits)",
        "Refresh Rate",
        "View Angle (H)",
        "View Angle (V)",
        "LED Lifetime",
        "Maintenance",
        "IP Rating",
        "Reference Total Price (USD)",
        "Fit Check",
    ],
    "Flat Display": [
        selected_model,
        selected_product["pixel_pitch_mm"],
        f"{total_resolution_w} × {total_resolution_h}",
        f"{led_width_mm:.1f} × {led_height_mm:.1f}",
        f"{display_area_m2:.2f}",
        selected_product["color_depth"],
        selected_product["contrast_ratio"],
        selected_product["power_consumption_per_cabinet_w"] * total_cabinet_qty,
        selected_product["brightness_nits"],
        selected_product["refresh_rate"],
        selected_product["view_angle_h"],
        selected_product["view_angle_v"],
        selected_product["led_lifetime"],
        selected_product["maintenance"],
        selected_product["ip_rating"],
        f"{reference_total_price_usd:,.0f}",
        "Pass" if fit_ok else "Fail",
    ]
})

spec_df["Flat Display"] = spec_df["Flat Display"].astype(str)
st.table(spec_df.set_index("Product"))

# -----------------------------
# Preview
# -----------------------------
st.divider()
st.subheader("Flat Display Layout Preview")

fig, ax = plt.subplots(figsize=(10, 6))

wall = Rectangle(
    (0, 0),
    wall_width_mm,
    wall_height_mm,
    fill=False,
    edgecolor="white",
    linewidth=2
)
ax.add_patch(wall)

led_color = "#8c8c8c" if fit_ok else "#aa4444"
led = Rectangle(
    (draw_led_x, draw_led_y),
    led_width_mm,
    led_height_mm,
    facecolor=led_color,
    edgecolor="white",
    linewidth=2
)
ax.add_patch(led)

for i in range(cabinet_qty_h + 1):
    x = draw_led_x + i * CABINET_WIDTH_MM
    ax.plot(
        [x, x],
        [draw_led_y, draw_led_y + led_height_mm],
        color="white",
        linewidth=0.8,
        linestyle="--",
        alpha=0.5
    )

for j in range(cabinet_qty_v + 1):
    y = draw_led_y + j * CABINET_HEIGHT_MM
    ax.plot(
        [draw_led_x, draw_led_x + led_width_mm],
        [y, y],
        color="white",
        linewidth=0.8,
        linestyle="--",
        alpha=0.5
    )

ax.text(
    wall_width_mm / 2,
    wall_height_mm - 50,
    f"Wall Width = {wall_width_mm:.0f} mm",
    ha="center",
    va="top",
    color="white"
)

ax.text(
    wall_width_mm - 50,
    wall_height_mm / 2,
    f"Wall Height = {wall_height_mm:.0f} mm",
    rotation=90,
    ha="right",
    va="center",
    color="white"
)

ax.text(
    draw_led_x + led_width_mm / 2,
    draw_led_y + led_height_mm / 2,
    f"LED\n{led_width_mm:.0f} × {led_height_mm:.0f} mm",
    ha="center",
    va="center",
    color="white",
    bbox=dict(facecolor="black", alpha=0.6, edgecolor="none")
)

ax.plot(
    [draw_led_x - 100, draw_led_x - 100],
    [0, draw_led_y],
    color="white",
    linewidth=1
)

ax.text(
    draw_led_x - 120,
    draw_led_y / 2,
    f"{draw_led_y:.0f} mm",
    rotation=90,
    va="center",
    ha="right",
    color="white"
)

ax.set_xlim(0, wall_width_mm)
ax.set_ylim(0, wall_height_mm)

ax.set_aspect("equal", adjustable="box")
ax.margins(0)

ax.set_title("Wall and LED Display Layout")

st.pyplot(fig, use_container_width=True)
plt.close(fig)