import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import pandas as pd
import math

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
        "cabinets_per_port_60": 2,
        "cabinets_per_port_120": 1,
        "120Hz_extra_price": 200,
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
        "cabinets_per_port_60": 4,
        "cabinets_per_port_120": 2,
        "120Hz_extra_price": 0,
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
        "cabinets_per_port_60": 2,
        "cabinets_per_port_120": 1,
        "120Hz_extra_price": 200,
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
        "cabinets_per_port_60": 4,
        "cabinets_per_port_120": 2,
        "120Hz_extra_price": 0,
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
        "cabinets_per_port_60": 7,
        "cabinets_per_port_120": 3,
        "120Hz_extra_price": 0,
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
        "cabinets_per_port_60": 11,
        "cabinets_per_port_120": 5,
        "120Hz_extra_price": 0,
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
        "cabinets_per_port_60": 2,
        "cabinets_per_port_120": 1,
        "120Hz_extra_price": 200,
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
        "cabinets_per_port_60": 4,
        "cabinets_per_port_120": 2,
        "120Hz_extra_price": 0,
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
        "cabinets_per_port_60": 7,
        "cabinets_per_port_120": 3,
        "120Hz_extra_price": 0,
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
        "cabinets_per_port_60": 11,
        "cabinets_per_port_120": 5,
        "120Hz_extra_price": 0,
    },
}

BOM_OPTIONS = {
    "支架": {
        "options": {
            "壁掛式": 300,
            "落地式": 350,
        },
        "unit": "m²",
    },
    "控制器": {
        "part_no": "X100 Pro 4U - 主機",
        "unit_price": 825,
        "unit": "pcs",
    },
    "控制器擴充卡_輸入卡": {
        "part_no": "4K HDMI/DP 輸入卡",
        "unit_price": 880,
        "unit": "pcs",
    },
    "控制器擴充卡_TX": {
        "part_no": "TX 10 port 發送卡",
        "unit_price": 578,
        "unit": "pcs",
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

frame_rate = st.sidebar.selectbox(
    "Frame Rate (Hz)",
    options=[60, 120],
    index=0
)

support_type = st.sidebar.selectbox(
    "Support Type",
    options=list(BOM_OPTIONS["支架"]["options"].keys()),
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
if frame_rate == 60:
    unit_price_usd_per_m2 = selected_product["unit_price_usd_per_m2"]
elif frame_rate == 120:
    unit_price_usd_per_m2 = selected_product["unit_price_usd_per_m2"] + selected_product["120Hz_extra_price"]
else:
    unit_price_usd_per_m2 = None


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

if frame_rate == 60:
    cabinets_per_port = selected_product["cabinets_per_port_60"]
elif frame_rate == 120:
    cabinets_per_port = selected_product["cabinets_per_port_120"]
else:
    cabinets_per_port = None

tx_qty = math.ceil(total_cabinet_qty / cabinets_per_port / 10)
ix_qty = math.ceil(total_resolution_w * total_resolution_h / (3840 * 2160))

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
c1.metric("LED Display Size (mm)", f"{led_width_mm:.0f} × {led_height_mm:.0f}")
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
        "Frame Rate (Hz)",
        "Support Type",
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
        frame_rate,
        support_type,
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

# -----------------------------
# BOM List
# -----------------------------
st.divider()
st.subheader("Key Component List (Quantity)")

# ---------- style ----------
header_style = "font-size:16px; font-weight:500; color:#9ca3af;"
text_style = "font-size:15px; font-weight:400;"
num_style = "font-size:15px; font-weight:600;"
total_style = "font-size:18px; font-weight:600;"

# -----------------------------
# Main parts
# -----------------------------
st.markdown("### Main parts")

h1, h2, h3, h4, h5 = st.columns([1.2,1.2,0.7,0.8,0.9])
for col, txt in zip([h1,h2,h3,h4,h5],
    ["Item","Part No.","Qty","Unit price (USD)","Total price (USD)"]):
    col.markdown(f"<span style='{header_style}'>{txt}</span>", unsafe_allow_html=True)



# LED cabinet
led_qty = display_area_m2
led_unit_price = unit_price_usd_per_m2
led_total_price = led_qty * led_unit_price

c1, c2, c3, c4, c5 = st.columns([1.2, 1.2, 0.7, 0.8, 0.9])
c1.markdown("**LED cabinet**")
c2.markdown(selected_model)
c3.markdown(f"**{led_qty:.1f} m²**")
c4.markdown(f"**{led_unit_price:,.0f}**")
c5.markdown(f"**{led_total_price:,.0f}**")

# 控制器
controller_part = BOM_OPTIONS["控制器"]["part_no"]
controller_qty = 1
controller_unit_price = BOM_OPTIONS["控制器"]["unit_price"]
controller_total_price = controller_qty * controller_unit_price

c1, c2, c3, c4, c5 = st.columns([1.2, 1.2, 0.7, 0.8, 0.9])
c1.markdown("**控制器**")
c2.markdown(controller_part)
c3.markdown(f"**{controller_qty} pcs**")
c4.markdown(f"**{controller_unit_price:,.0f}**")
c5.markdown(f"**{controller_total_price:,.0f}**")

# 控制器擴充卡 - 輸入卡
ix_part = BOM_OPTIONS["控制器擴充卡_輸入卡"]["part_no"]
ix_unit_price = BOM_OPTIONS["控制器擴充卡_輸入卡"]["unit_price"]
ix_total_price = ix_qty * ix_unit_price

c1, c2, c3, c4, c5 = st.columns([1.2, 1.2, 0.7, 0.8, 0.9])
c1.markdown("**控制器擴充卡**")
c2.markdown(ix_part)
c3.markdown(f"**{ix_qty} pcs**")
c4.markdown(f"**{ix_unit_price:,.0f}**")
c5.markdown(f"**{ix_total_price:,.0f}**")

# 控制器擴充卡 - TX
tx_part = BOM_OPTIONS["控制器擴充卡_TX"]["part_no"]
tx_unit_price = BOM_OPTIONS["控制器擴充卡_TX"]["unit_price"]
tx_total_price = tx_qty * tx_unit_price

c1, c2, c3, c4, c5 = st.columns([1.2, 1.2, 0.7, 0.8, 0.9])
c1.markdown("**控制器擴充卡**")
c2.markdown(tx_part)
c3.markdown(f"**{tx_qty} pcs**")
c4.markdown(f"**{tx_unit_price:,.0f}**")
c5.markdown(f"**{tx_total_price:,.0f}**")

# 支架
support_qty = display_area_m2
support_unit_price = BOM_OPTIONS["支架"]["options"][support_type]
support_total_price = support_qty * support_unit_price

c1, c2, c3, c4, c5 = st.columns([1.2, 1.2, 0.7, 0.8, 0.9])
c1.markdown("**支架**")
c2.markdown(support_type)
c3.markdown(f"**{support_qty:.1f} m²**")
c4.markdown(f"**{support_unit_price:,.0f}**")
c5.markdown(f"**{support_total_price:,.0f}**")

main_total = (
    led_total_price
    + controller_total_price
    + ix_total_price
    + tx_total_price
    + support_total_price
)

_, col_total = st.columns([1, 1])

with col_total:
    st.markdown(
        f"<div style='text-align:right; font-size:22px; font-weight:700; letter-spacing:0.5px;'>"
        f"Main Parts Total (USD): {main_total:,.0f}"
        f"</div>",
        unsafe_allow_html=True
    )

st.divider()

# -----------------------------
# Spare parts
# -----------------------------
st.markdown("### Spare parts")

h1,h2,h3,h4,h5 = st.columns([1.2,1.2,0.7,0.8,0.9])
for col, txt in zip([h1,h2,h3,h4,h5],
    ["Item","Part No.","Qty","Unit price (USD)","Total price (USD)"]):
    col.markdown(f"<span style='{header_style}'>{txt}</span>", unsafe_allow_html=True)


# spare options
spare_led_options = [0, 5, 10, 15, 20]
spare_pcs_options = [0, 1, 2, 3, 4, 5]

# LED cabinet spare
c1, c2, c3, c4, c5 = st.columns([1.2, 1.2, 0.7, 0.8, 0.9])
c1.markdown("**LED cabinet**")
c2.markdown(selected_model)
spare_led_ratio = c3.selectbox(
    "LED cabinet spare qty",
    options=spare_led_options,
    index=2,
    format_func=lambda x: f"{x} %",
    key="spare_led_ratio",
    label_visibility="collapsed"
)
spare_led_unit_price = led_total_price
spare_led_total_price = spare_led_unit_price * spare_led_ratio / 100.0
c4.markdown(f"**{spare_led_unit_price:,.0f}**")
c5.markdown(f"**{spare_led_total_price:,.0f}**")

# 控制器 spare
c1, c2, c3, c4, c5 = st.columns([1.2, 1.2, 0.7, 0.8, 0.9])
c1.markdown("**控制器**")
c2.markdown(controller_part)
spare_controller_qty = c3.selectbox(
    "Controller spare qty",
    options=spare_pcs_options,
    index=0,
    format_func=lambda x: f"{x} pcs",
    key="spare_controller_qty",
    label_visibility="collapsed"
)
spare_controller_unit_price = controller_unit_price
spare_controller_total_price = spare_controller_qty * spare_controller_unit_price
c4.markdown(f"**{spare_controller_unit_price:,.0f}**")
c5.markdown(f"**{spare_controller_total_price:,.0f}**")

# 輸入卡 spare
c1, c2, c3, c4, c5 = st.columns([1.2, 1.2, 0.7, 0.8, 0.9])
c1.markdown("**控制器擴充卡**")
c2.markdown(ix_part)
spare_ix_qty = c3.selectbox(
    "Input card spare qty",
    options=spare_pcs_options,
    index=1,
    format_func=lambda x: f"{x} pcs",
    key="spare_ix_qty",
    label_visibility="collapsed"
)
spare_ix_unit_price = ix_unit_price
spare_ix_total_price = spare_ix_qty * spare_ix_unit_price
c4.markdown(f"**{spare_ix_unit_price:,.0f}**")
c5.markdown(f"**{spare_ix_total_price:,.0f}**")

# TX card spare
c1, c2, c3, c4, c5 = st.columns([1.2, 1.2, 0.7, 0.8, 0.9])
c1.markdown("**控制器擴充卡**")
c2.markdown(tx_part)
spare_tx_qty = c3.selectbox(
    "TX card spare qty",
    options=spare_pcs_options,
    index=1,
    format_func=lambda x: f"{x} pcs",
    key="spare_tx_qty",
    label_visibility="collapsed"
)
spare_tx_unit_price = tx_unit_price
spare_tx_total_price = spare_tx_qty * spare_tx_unit_price
c4.markdown(f"**{spare_tx_unit_price:,.0f}**")
c5.markdown(f"**{spare_tx_total_price:,.0f}**")

spare_total = (
    spare_led_total_price
    + spare_controller_total_price
    + spare_ix_total_price
    + spare_tx_total_price
)


_, col_total = st.columns([1, 1])

with col_total:
    st.markdown(
        f"<div style='text-align:right; font-size:22px; font-weight:700; letter-spacing:0.5px;'>"
        f"Spare Parts Total (USD): {spare_total:,.0f}"
        f"</div>",
        unsafe_allow_html=True
    )

st.divider()

# -----------------------------
# Other parts
# -----------------------------
st.markdown("### Other parts")

h1,h2,h3,h4,h5 = st.columns([1.2,1.2,0.7,0.8,0.9])
for col, txt in zip([h1,h2,h3,h4,h5],
    ["Item","Part No.","Qty","Unit price (USD)","Total price (USD)"]):
    col.markdown(f"<span style='{header_style}'>{txt}</span>", unsafe_allow_html=True)

# 👉 箱體總價（Main + Spare LED）
cabinet_total_price = led_total_price + spare_led_total_price

other_ratio_options = [0, 1, 2, 3, 5]

# -----------------------------
# 包材
# -----------------------------
c1, c2, c3, c4, c5 = st.columns([1.2, 1.2, 0.7, 0.8, 0.9])
c1.markdown("**包材**")
c2.markdown("NA")

pack_ratio = c3.selectbox(
    "包材比例",
    options=other_ratio_options,
    index=2,
    format_func=lambda x: f"{x} %",
    key="pack_ratio",
    label_visibility="collapsed"
)

pack_unit_price = cabinet_total_price
pack_total_price = pack_unit_price * pack_ratio / 100

c4.markdown(f"**{pack_unit_price:,.0f}**")
c5.markdown(f"**{pack_total_price:,.0f}**")

# -----------------------------
# 工具 & 配件 & 線材
# -----------------------------
c1, c2, c3, c4, c5 = st.columns([1.2, 1.2, 0.7, 0.8, 0.9])
c1.markdown("**工具&配件&線材**")
c2.markdown("NA")

tool_ratio = c3.selectbox(
    "工具比例",
    options=other_ratio_options,
    index=2,
    format_func=lambda x: f"{x} %",
    key="tool_ratio",
    label_visibility="collapsed"
)

tool_unit_price = cabinet_total_price
tool_total_price = tool_unit_price * tool_ratio / 100

c4.markdown(f"**{tool_unit_price:,.0f}**")
c5.markdown(f"**{tool_total_price:,.0f}**")

# -----------------------------
# Other total
# -----------------------------
other_total = pack_total_price + tool_total_price

_, col_total = st.columns([1, 1])
with col_total:
    st.markdown(
        f"<div style='text-align:right; font-size:22px; font-weight:700;'>"
        f"Other Parts Total (USD): {other_total:,.0f}"
        f"</div>",
        unsafe_allow_html=True
    )

st.divider()

grand_total = main_total + spare_total + other_total  # 記得加 other

st.markdown(
    f"""
    <div style="
        margin-top:20px;
        padding:16px 20px;
        border-radius:10px;
        background:linear-gradient(90deg, #1f2937, #111827);
        border:1px solid #374151;
        display:flex;
        justify-content:space-between;
        align-items:center;
    ">
        <span style="font-size:18px; font-weight:600; color:#d1d5db;">
            Grand Total (USD)
        </span>
        <span style="font-size:26px; font-weight:800; color:#ffffff;">
            {grand_total:,.0f}
        </span>
    </div>
    """,
    unsafe_allow_html=True
)