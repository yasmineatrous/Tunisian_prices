import streamlit as st
import time
from data_generator import MarketDataGenerator
from components import create_price_card, create_price_trend_chart, display_header_image
from styles import apply_custom_styles
from utils import get_last_update_time, get_market_images, get_translations

# Page configuration must be the first Streamlit command
st.set_page_config(
    page_title="Prix du Marché Tunisien",
    page_icon="🏪",
    layout="wide"
)

# Debug logging can now safely be added
st.write("Starting application...")

# Apply custom styles
st.write("Applying custom styles...")
apply_custom_styles()

# Initialize session state
if 'data_generator' not in st.session_state:
    st.session_state.data_generator = MarketDataGenerator()
if 'last_update' not in st.session_state:
    st.session_state.last_update = get_last_update_time()
if 'price_data' not in st.session_state:
    st.session_state.price_data = st.session_state.data_generator.generate_daily_prices()

st.write("Session state initialized...")

# Get translations and images
translations = get_translations()
market_images = get_market_images()

# Header
display_header_image(
    market_images['header'],
    f"{translations['title']['fr']}\n{translations['title']['ar']}"
)

# Last update info
st.markdown(f"{translations['last_updated']['fr']}/{translations['last_updated']['ar']}: {st.session_state.last_update}")

# Category selector
category_options = ["All", "Vegetables", "Meat"]
category_labels = [f"{translations['categories'][cat]['fr']} / {translations['categories'][cat]['ar']}" 
                  for cat in category_options]
selected_index = st.selectbox(
    "",
    range(len(category_options)),
    format_func=lambda x: category_labels[x]
)
category = category_options[selected_index]

# Refresh button
if st.button(f"🔄 {translations['refresh']['fr']} / {translations['refresh']['ar']}"):
    with st.spinner("Mise à jour..."):
        time.sleep(1)  # Simulate API call
        st.session_state.price_data = st.session_state.data_generator.generate_daily_prices()
        st.session_state.last_update = get_last_update_time()
        st.experimental_rerun()

# Display prices
col1, col2 = st.columns(2)

with col1:
    if category in ["All", "Vegetables"]:
        st.markdown(f"### 🥬 {translations['categories']['Vegetables']['fr']} / {translations['categories']['Vegetables']['ar']}")
        vegetables_data = st.session_state.price_data[
            st.session_state.price_data['Category'] == 'Vegetables'
        ]
        for _, row in vegetables_data.iterrows():
            create_price_card(
                row['Item'],
                row['Price'],
                row['Previous_Price'],
                market_images['vegetables']['items'].get(row['Item'])
            )

        st.plotly_chart(
            create_price_trend_chart(st.session_state.price_data, 'Vegetables'),
            use_container_width=True
        )

with col2:
    if category in ["All", "Meat"]:
        st.markdown(f"### 🥩 {translations['categories']['Meat']['fr']} / {translations['categories']['Meat']['ar']}")
        meat_data = st.session_state.price_data[
            st.session_state.price_data['Category'] == 'Meat'
        ]
        for _, row in meat_data.iterrows():
            create_price_card(
                row['Item'],
                row['Price'],
                row['Previous_Price'],
                market_images['meat']['items'].get(row['Item'])
            )

        st.plotly_chart(
            create_price_trend_chart(st.session_state.price_data, 'Meat'),
            use_container_width=True
        )

# Footer
st.markdown("---")
st.markdown(f"### {translations['about']['fr']} / {translations['about']['ar']}")
st.markdown("""
Cette application affiche les prix quotidiens du marché pour divers produits en Tunisie.
Les prix sont mis à jour régulièrement et affichés en Dinar Tunisien (TND).

هذا التطبيق يعرض أسعار السوق اليومية لمختلف المنتجات في تونس.
يتم تحديث الأسعار بانتظام وعرضها بالدينار التونسي.
""")