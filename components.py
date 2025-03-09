import streamlit as st
import plotly.graph_objects as go
from utils import get_translations

def create_price_card(item, price, previous_price, image_url=None, currency="TND"):
    translations = get_translations()
    item_trans = translations['items'][item]

    price_change = price - previous_price
    change_color = "#4CAF50" if price_change <= 0 else "#F44336"
    change_arrow = "↓" if price_change <= 0 else "↑"

    card_content = f"""
        <div class="price-card animation-container">
            <div class="card-header">
                <img src="{image_url}" alt="{item}" class="item-image"/>
                <h3>{item_trans['fr']}<br><small>{item_trans['ar']}</small></h3>
            </div>
            <div class="price-info">
                <p class="price-value">{price:.3f} <span class="currency">{currency}</span></p>
                <p style="color: {change_color}; margin-top: 5px;">
                    {change_arrow} {abs(price_change):.3f} {currency}
                </p>
            </div>
        </div>
    """
    st.markdown(card_content, unsafe_allow_html=True)

def create_price_trend_chart(df, category):
    translations = get_translations()
    category_trans = translations['categories'][category]['fr']

    category_data = df[df['Category'] == category]

    fig = go.Figure()

    for item in category_data['Item'].unique():
        item_data = category_data[category_data['Item'] == item]
        item_trans = translations['items'][item]['fr']

        fig.add_trace(go.Bar(
            name=item_trans,
            x=[item_trans],
            y=[item_data['Price'].iloc[0]],
            text=[f"{item_data['Price'].iloc[0]:.3f} TND"],
            textposition='auto',
        ))

    fig.update_layout(
        title=f'{category_trans} - Prix actuels',
        yaxis_title='Prix (TND)',
        showlegend=False,
        height=400,
        margin=dict(l=20, r=20, t=40, b=20),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )

    return fig

def display_header_image(image_url, caption):
    st.markdown(f"""
        <div class="header-container">
            <img src="{image_url}" class="header-image" alt="{caption}">
            <div class="header-overlay">
                <h1>{caption}</h1>
            </div>
        </div>
    """, unsafe_allow_html=True)