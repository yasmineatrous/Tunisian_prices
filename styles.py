import streamlit as st

def apply_custom_styles():
    st.markdown("""
        <style>
        .stApp {
            max-width: 1200px;
            margin: 0 auto;
        }

        .header-container {
            position: relative;
            width: 100%;
            margin-bottom: 2rem;
        }

        .header-image {
            width: 100%;
            height: 400px;
            object-fit: cover;
            border-radius: 15px;
        }

        .header-overlay {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            padding: 2rem;
            background: linear-gradient(transparent, rgba(0,0,0,0.7));
            border-radius: 0 0 15px 15px;
        }

        .header-overlay h1 {
            color: white;
            margin: 0;
            font-size: 2.5rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }

        .price-card {
            background-color: white;
            padding: 1.5rem;
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
            margin-bottom: 1rem;
        }

        .price-card:hover {
            transform: translateY(-5px);
        }

        .card-header {
            display: flex;
            align-items: center;
            margin-bottom: 1rem;
        }

        .item-image {
            width: 80px;
            height: 80px;
            object-fit: cover;
            border-radius: 10px;
            margin-right: 1rem;
        }

        .card-header h3 {
            margin: 0;
            color: #262730;
            font-size: 1.2rem;
        }

        .card-header small {
            color: #666;
            font-size: 0.9rem;
        }

        .price-info {
            text-align: right;
        }

        .price-value {
            font-size: 1.5rem;
            font-weight: bold;
            color: #262730;
            margin: 0;
        }

        .currency {
            color: #666;
            font-size: 0.9rem;
        }

        .animation-container {
            animation: fadeIn 0.5s ease-in;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .stButton button {
            background-color: #FF6B6B;
            color: white;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 5px;
            font-weight: bold;
            transition: background-color 0.3s ease;
        }

        .stButton button:hover {
            background-color: #FF5252;
        }
        </style>
    """, unsafe_allow_html=True)