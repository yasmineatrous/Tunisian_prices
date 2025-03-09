import streamlit as st
from datetime import datetime, timedelta


def get_last_update_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def format_currency(amount):
    return f"{amount:.3f} TND"


def calculate_price_change(current, previous):
    return ((current - previous) / previous) * 100


def get_market_images():
    return {
        'header':
        "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1600",
        'vegetables': {
            'background':
            "https://images.unsplash.com/photo-1542838132-92c53300491e?w=800",
            'items': {
                'Tomatoes':
                'https://images.unsplash.com/photo-1592924357228-91a4daadcfea?w=400',
                'Potatoes':
                'https://images.unsplash.com/photo-1518977676601-b53f82aba655?w=400',
                'Onions':
                'https://images.unsplash.com/photo-1580201092675-a0a6a6cafbb1?w=400',
                'Carrots':
                'https://images.unsplash.com/photo-1447175008436-054170c2e979?w=400',
                'Peppers':
                'https://images.unsplash.com/photo-1563565375-f3fdfdbefa83?w=400'
            }
        },
        'meat': {
            'background':
            "https://images.unsplash.com/photo-1553163147-622ab57be1c7?w=800",
            'items': {
                'Beef':
                'https://images.unsplash.com/photo-1588347785134-01d68cd70ee7?w=400',
                'Lamb':
                'https://images.unsplash.com/photo-1608877907149-a206d75ba011?w=400',
                'Chicken':
                'https://images.unsplash.com/photo-1587593810167-a84920ea0781?w=400',
                'Turkey':
                'https://images.unsplash.com/photo-1587593810167-a84920ea0781?w=400',
                'Fish':
                'https://images.unsplash.com/photo-1615141982883-c7ad0e69fd62?w=400'
            }
        }
    }


def get_translations():
    return {
        'title': {
            'fr': 'Moniteur des Prix du Marché Tunisien',
            'ar': 'مراقب أسعار السوق التونسي'
        },
        'last_updated': {
            'fr': 'Dernière mise à jour',
            'ar': 'آخر تحديث'
        },
        'categories': {
            'Vegetables': {
                'fr': 'Légumes',
                'ar': 'خضروات'
            },
            'Meat': {
                'fr': 'Viande',
                'ar': 'لحوم'
            },
            'All': {
                'fr': 'Tout',
                'ar': 'الكل'
            }
        },
        'items': {
            'Tomatoes': {
                'fr': 'Tomates',
                'ar': 'طماطم'
            },
            'Potatoes': {
                'fr': 'Pommes de terre',
                'ar': 'بطاطا'
            },
            'Onions': {
                'fr': 'Oignons',
                'ar': 'بصل'
            },
            'Carrots': {
                'fr': 'Carottes',
                'ar': 'جزر'
            },
            'Peppers': {
                'fr': 'Poivrons',
                'ar': 'فلفل'
            },
            'Beef': {
                'fr': 'Boeuf',
                'ar': 'لحم بقر'
            },
            'Lamb': {
                'fr': 'Agneau',
                'ar': 'لحم غنم'
            },
            'Chicken': {
                'fr': 'Poulet',
                'ar': 'دجاج'
            },
            'Turkey': {
                'fr': 'Dinde',
                'ar': 'ديك رومي'
            },
            'Fish': {
                'fr': 'Poisson',
                'ar': 'سمك'
            }
        },
        'refresh': {
            'fr': 'Actualiser les prix',
            'ar': 'تحديث الأسعار'
        },
        'about': {
            'fr': 'À propos',
            'ar': 'حول'
        }
    }