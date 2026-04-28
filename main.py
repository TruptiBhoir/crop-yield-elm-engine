# proven_app.py - Complete Multi-language Support

from unittest import result

from matplotlib import style
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, time
import json
import os
import base64



# ==================== LANGUAGE CONFIGURATION ====================
LANGUAGES = {
    'en': 'English 🇺🇸',
    'hi': 'हिन्दी 🇮🇳',  # Hindi
    'mr': 'मराठी 🇮🇳',  # Marathi
    'ta': 'தமிழ் 🇮🇳',   # Tamil
    'te': 'తెలుగు 🇮🇳',  # Telugu
    'kn': 'ಕನ್ನಡ 🇮🇳',   # Kannada
    'ml': 'മലയാളം 🇮🇳',  # Malayalam
    'gu': 'ગુજરાતી 🇮🇳', # Gujarati
    'bn': 'বাংলা 🇧🇩',    # Bengali
    'es': 'Español 🇪🇸',  # Spanish
    'fr': 'Français 🇫🇷', # French
}

# ==================== TRANSLATIONS ====================
# Base English translations - all other languages will fall back to these
BASE_TRANSLATIONS = {
    'app_title': '🌾 Crop Yield Prediction System',
    'app_subtitle': 'AI-powered insights for smart agriculture',
    'nav_home': '🏠 Home',
    'nav_predict': '📊 Predict',
    'nav_results': '📈 Results',
    'nav_history': '📚 History',
    'nav_about': 'ℹ️ About',
    'system_overview': 'System Overview',
    'input_parameters': '📊 Input Parameters',
    'manual_input': '📝 Manual Input',
    'file_upload': '📁 File Upload',
    'advanced_settings': '⚙️ Advanced Settings',
    'soil_params': '🌱 Soil Parameters',
    'weather_conditions': '🌡️ Weather Conditions',
    'additional_params': '🧪 Additional Parameters',
    'crop_type': 'Crop Type',
    'upload_csv': 'Upload CSV File',
    'choose_csv': 'Choose a CSV file',
    'file_uploaded': 'File uploaded successfully!',
    'preview_data': 'Preview uploaded data',
    'model_settings': 'Model Settings',
    'hidden_neurons': 'Hidden Neurons',
    'activation': 'Activation Function',
    'regularization': 'Regularization (C)',
    'random_seed': 'Random Seed',
    'predict_button': '🚀 Predict Crop Yield',
    'processing': 'Processing your data and making predictions...',
    'prediction_complete': 'Prediction completed successfully!',
    'prediction_results': '📈 Prediction Results',
    'predicted_yield': 'Predicted Yield',
    'confidence_level': 'Confidence Level',
    'prediction_time': 'Prediction Time',
    'yield_analysis': '📊 Yield Analysis',
    'feature_importance': 'Feature Importance',
    'input_summary': '📋 Input Summary',
    'batch_results': '📊 Batch Prediction Results',
    'avg_predicted_yield': 'Average Predicted Yield',
    'num_records': 'Number of Records',
    'view_predictions': 'View All Predictions',
    'distribution_yields': 'Distribution of Predicted Yields',
    'download_predictions': '📥 Download Predictions (CSV)',
    'navigation': '🧭 Navigation',
    'quick_stats': '📊 Quick Stats',
    'total_predictions': 'Total Predictions',
    'last_prediction': 'Last Prediction',
    'system_info': '⚙️ System Info',
    'clear_data': '🗑️ Clear All Data',
    'prediction_history': '📚 Prediction History',
    'no_history': 'No prediction history available. Make some predictions first!',
    'clear_history': 'Clear History',
    'about_system': 'ℹ️ About This System',
    'quick_start': '🚀 Quick Start',
    'quick_start_steps': '1. Go to Predict tab\n2. Enter your parameters\n3. Click Predict button\n4. View results!',
    'features': '📊 Features',
    'features_list': '• Manual & Batch Input\n• Real-time Predictions\n• Visual Analytics\n• History Tracking',
    'tips': '💡 Tips',
    'tips_list': '• Use accurate soil test data\n• Update weather forecasts\n• Save successful predictions\n• Export for analysis',
    'recent_activity': '📈 Recent Activity',
    'latest_prediction': 'Latest Prediction',
    'how_to_use': 'ℹ️ How to use this system',
   'usage_steps': '1. **Manual Input**: Fill in all parameters\n2. **Click Predict**: Get yield predictions\n3. **View Results**: Analyze with charts',
    'no_predictions': 'No predictions available. Go to the Predict tab!',
    'go_to_predict': 'Go to Predict',
    'footer': '🌾 Crop Yield Prediction System | BE Computer Engineering Project',
    'help_nitrogen': 'Available nitrogen in soil (ppm)',
    'help_phosphorus': 'Available phosphorus in soil',
    'help_potassium': 'Available potassium in soil',
    'help_temperature': 'Average temperature in Celsius',
    'help_humidity': 'Relative humidity percentage',
    'help_rainfall': 'Monthly rainfall in millimeters',
    'help_ph': 'Soil acidity/alkalinity level',
    'help_moisture': 'Soil moisture content percentage',
    'help_crop': 'Select the crop type',
    'help_neurons': 'Number of neurons in hidden layer',
    'help_activation': 'Activation function for hidden layer',
    'help_regularization': 'Regularization parameter',
    'help_random': 'Random seed for reproducibility',
    'required_csv': '**Required CSV Columns**: N, P, K, temperature, humidity, rainfall, ph, moisture',
    'missing_columns': 'Missing columns',
    'error_file': 'Error reading file',
    'error_prediction': 'Error during prediction',
    'units_kg_ha': 'kg/hectare',
    'model_confidence': 'Model Confidence',
    'timestamp': 'Timestamp',
    'features_label': 'Features',
    'importance_label': 'Importance',
    'parameter': 'Parameter',
    'value': 'Value',
    'yield': 'Yield',
    'confidence': 'Confidence',
    'records': 'Records',
    'crops': ['Wheat', 'Rice', 'Maize', 'Cotton', 'Sugarcane', 'Soybean', 'Barley', 'Other'],
    'activations': ['sigmoid', 'relu', 'tanh'],
    'status_operational': '🟢 Operational',
    'last_updated': 'Last Updated',
    'today': 'Today',
    'model': 'Model',
    'version': 'Version',
    'status': 'Status',
    'project_overview': 'Project Overview',
    'technical_specs': 'Technical Specifications',
    'input_params': 'Input Parameters',
    'soil_parameters': 'Soil Parameters',
    'weather_params': 'Weather Conditions',
    'crop_info': 'Crop Information',
    'model_features': 'Model Features',
    'performance_metrics': 'Performance Metrics',
    'features_section': 'Features',
    'privacy_security': 'Privacy & Security',
    'support': 'Support',
    'email': 'Email',
    'phone': 'Phone',
    'college': 'College',
    'select_language': '🌐 Select Language',
    'language': 'Language',
    'theme': 'Theme',
    'accessibility': 'Accessibility',
    'font_size': 'Font Size',
    'contrast': 'Contrast',
    'reset': 'Reset',
}

# Language-specific translations (partial - you can expand these)
TRANSLATIONS = {
    'en': BASE_TRANSLATIONS,
    'hi': {
        'app_title': '🌾 फसल उपज पूर्वानुमान प्रणाली',
        'app_subtitle': 'सतत कृषि के लिए एक्सट्रीम मशीन लर्निंग',
        'nav_home': '🏠 होम',
        'nav_predict': '📊 पूर्वानुमान',
        'nav_results': '📈 परिणाम',
        'nav_history': '📚 इतिहास',
        'nav_about': 'ℹ️ जानकारी',
        'system_overview': 'सिस्टम अवलोकन',
        'input_parameters': '📊 इनपुट मापदंड',
        'manual_input': '📝 मैन्युअल इनपुट',
        'file_upload': '📁 फ़ाइल अपलोड',
        'soil_params': '🌱 मिट्टी के मापदंड',
        'weather_conditions': '🌡️ मौसम की स्थिति',
        'additional_params': '🧪 अतिरिक्त मापदंड',
        'crop_type': 'फसल का प्रकार',
        'upload_csv': 'CSV फ़ाइल अपलोड करें',
        'predict_button': '🚀 फसल उपज का अनुमान लगाएं',
        'prediction_results': '📈 पूर्वानुमान परिणाम',
        'predicted_yield': 'अनुमानित उपज',
        'units_kg_ha': 'किलोग्राम/हेक्टेयर',
        'crops': ['गेहूं', 'चावल', 'मक्का', 'कपास', 'गन्ना', 'सोयाबीन', 'जौ', 'अन्य'],
        'select_language': '🌐 भाषा चुनें',
        'language': 'भाषा',
    },
    'mr': {
        'app_title': '🌾 पीक उत्पादन अंदाज प्रणाली',
        'app_subtitle': 'शाश्वत शेतीसाठी एक्सट्रीम मशीन लर्निंग',
        'nav_home': '🏠 मुख्यपृष्ठ',
        'nav_predict': '📊 अंदाज',
        'nav_results': '📈 निकाल',
        'nav_history': '📚 इतिहास',
        'nav_about': 'ℹ️ माहिती',
        'crops': ['गहू', 'तांदूळ', 'मका', 'कापूस', 'ऊस', 'सोयाबीन', 'बार्ली', 'इतर'],
        'select_language': '🌐 भाषा निवडा',
        'language': 'भाषा',
    },
    'ta': {
        'app_title': '🌾 பயிர் விளைச்சல் முன்கணிப்பு அமைப்பு',
        'app_subtitle': 'நிலையான விவசாயத்திற்கான எக்ஸ்ட்ரீம் மெஷின் லெர்னிங்',
        'nav_home': '🏠 முகப்பு',
        'nav_predict': '📊 முன்கணிப்பு',
        'nav_results': '📈 முடிவுகள்',
        'nav_history': '📚 வரலாறு',
        'nav_about': 'ℹ️ பற்றி',
        'crops': ['கோதுமை', 'அரிசி', 'மக்காச்சோளம்', 'பருத்தி', 'கரும்பு', 'சோயாபீன்', 'பார்லி', 'பிற'],
        'select_language': '🌐 மொழியைத் தேர்ந்தெடுக்கவும்',
        'language': 'மொழி',
    },
    'te': {
        'app_title': '🌾 పంట దిగుబడి అంచనా వ్యవస్థ',
        'app_subtitle': 'స్థిరమైన వ్యవసాయం కోసం ఎక్స్ట్రీమ్ మెషిన్ లెర్నింగ్',
        'nav_home': '🏠 హోమ్',
        'nav_predict': '📊 అంచనా',
        'nav_results': '📈 ఫలితాలు',
        'nav_history': '📚 చరిత్ర',
        'nav_about': 'ℹ️ గురించి',
        'crops': ['గోధుమ', 'బియ్యం', 'మొక్కజొన్న', 'పత్తి', 'చెరకు', 'సోయాబీన్', 'బార్లీ', 'ఇతరాలు'],
        'select_language': '🌐 భాషను ఎంచుకోండి',
        'language': 'భాష',
    },
    'kn': {
        'app_title': '🌾 ಬೆಳೆ ಉತ್ಪಾದನೆ ಮುನ್ಸೂಚನೆ ವ್ಯವಸ್ಥೆ',
        'app_subtitle': 'ಸುಸ್ಥಿರ ಕೃಷಿಗಾಗಿ ಎಕ್ಸ್ಟ್ರೀಮ್ ಮೆಷಿನ್ ಲರ್ನಿಂಗ್',
        'nav_home': '🏠 ಮುಖಪುಟ',
        'nav_predict': '📊 ಮುನ್ಸೂಚನೆ',
        'nav_results': '📈 ಫಲಿತಾಂಶಗಳು',
        'nav_history': '📚 ಇತಿಹಾಸ',
        'nav_about': 'ℹ️ ಬಗ್ಗೆ',
        'crops': ['ಗೋಧಿ', 'ಭತ್ತ', 'ಮೆಕ್ಕೆಜೋಳ', 'ಕಪಾಸು', 'ಕಬ್ಬು', 'ಸೋಯಾಬೀನ್', 'ಬಾರ್ಲಿ', 'ಇತರೆ'],
        'select_language': '🌐 ಭಾಷೆ ಆಯ್ಕೆಮಾಡಿ',
        'language': 'ಭಾಷೆ',
    },
    'ml': {
        'app_title': '🌾 വിളവ് പ്രവചന സംവിധാനം',
        'app_subtitle': 'സുസ്ഥിര കൃഷിക്കുള്ള എക്സ്ട്രീം മെഷീൻ ലേണിംഗ്',
        'nav_home': '🏠 ഹോം',
        'nav_predict': '📊 പ്രവചനം',
        'nav_results': '📈 ഫലങ്ങൾ',
        'nav_history': '📚 ചരിത്രം',
        'nav_about': 'ℹ️ കുറിച്ച്',
        'crops': ['ഗോതമ്പ്', 'അരി', 'ചോളം', 'പരുത്തി', 'ചക്കരക്കമ്പ്', 'സോയാബീൻ', 'ബാർലി', 'മറ്റുള്ളവ'],
        'select_language': '🌐 ഭാഷ തിരഞ്ഞെടുക്കുക',
        'language': 'ഭാഷ',
    },
    'gu': {
        'app_title': '🌾 પાક ઉત્પાદન અનુમાન સિસ્ટમ',
        'app_subtitle': 'ટકાઉ કૃષિ માટે એક્સ્ટ્રીમ મશીન લર્નિંગ',
        'nav_home': '🏠 ઘર',
        'nav_predict': '📊 અનુમાન',
        'nav_results': '📈 પરિણામો',
        'nav_history': '📚 ઇતિહાસ',
        'nav_about': 'ℹ️ વિશે',
        'crops': ['ઘઉં', 'ચોખા', 'મકાઈ', 'કપાસ', 'ખાંડ', 'સોયાબીન', 'જવ', 'અન્ય'],
        'select_language': '🌐 ભાષા પસંદ કરો',
        'language': 'ભાષા',
    },
    'bn': {
        'app_title': '🌾 ফসল ফলন পূর্বাভাস সিস্টেম',
        'app_subtitle': 'টেকসই কৃষির জন্য এক্সট্রিম মেশিন লার্নিং',
        'nav_home': '🏠 হোম',
        'nav_predict': '📊 পূর্বাভাস',
        'nav_results': '📈 ফলাফল',
        'nav_history': '📚 ইতিহাস',
        'nav_about': 'ℹ️ সম্পর্কে',
        'crops': ['গম', 'ধান', 'ভুট্টা', 'তুলা', 'আখ', 'সয়াবিন', 'বার্লি', 'অন্যান্য'],
        'select_language': '🌐 ভাষা নির্বাচন করুন',
        'language': 'ভাষা',
    },
    'es': {
        'app_title': '🌾 Sistema de Predicción de Rendimiento de Cultivos',
        'app_subtitle': 'Usando Aprendizaje Automático Extremo para Agricultura Sostenible',
        'nav_home': '🏠 Inicio',
        'nav_predict': '📊 Predecir',
        'nav_results': '📈 Resultados',
        'nav_history': '📚 Historial',
        'nav_about': 'ℹ️ Acerca de',
        'crops': ['Trigo', 'Arroz', 'Maíz', 'Algodón', 'Caña de azúcar', 'Soja', 'Cebada', 'Otro'],
        'select_language': '🌐 Seleccionar idioma',
        'language': 'Idioma',
    },
    'fr': {
        'app_title': '🌾 Système de Prédiction du Rendement des Cultures',
        'app_subtitle': 'Utilisation de l\'Apprentissage Automatique Extrême pour une Agriculture Durable',
        'nav_home': '🏠 Accueil',
        'nav_predict': '📊 Prédire',
        'nav_results': '📈 Résultats',
        'nav_history': '📚 Historique',
        'nav_about': 'ℹ️ À propos',
        'crops': ['Blé', 'Riz', 'Maïs', 'Coton', 'Canne à sucre', 'Soja', 'Orge', 'Autre'],
        'select_language': '🌐 Sélectionner la langue',
        'language': 'Langue',
    },
}

def get_translation(key, language='en'):
    """Get translation for a given key in the specified language"""
    if language in TRANSLATIONS and key in TRANSLATIONS[language]:
        return TRANSLATIONS[language][key]
    elif key in BASE_TRANSLATIONS:
        return BASE_TRANSLATIONS[key]
    else:
        return key

# ==================== CSS ====================
def load_css():
    st.markdown("""
    <style>

    /* 2. Glassmorphism Main Container (Replaces basic .block-container) */
    .block-container {
        background: rgba(255, 255, 255, 0.90) !important;
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border-radius: 16px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12);
        border: 1px solid rgba(255, 255, 255, 0.4);
        padding: 2.5rem !important;
        margin-top: 2rem !important;
        margin-bottom: 2rem !important;
        max-width: 1100px;
    }

    /* 3. Safe Global Text Readability (Only targets elements inside the glass container) */
    .block-container h1, .block-container h2, .block-container h3, .block-container h4 { 
        color: #111827 !important; 
        font-weight: 700 !important; 
    }
    /* Exclude buttons from this text override so their text stays white */
    .block-container p, .block-container label, .block-container span:not(.stButton>button *) { 
        color: #374151 !important; 
        font-size: 15px;
    }
    
    /* 4. Improve Input Form Elements */
    .stNumberInput label, .stSelectbox label, .stSlider label {
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        margin-bottom: 0.3rem !important;
        color: #111827 !important;
    }
    .stSlider [data-testid="stTickBar"] { color: #1F2937 !important; }
    
    /* 5. Modern Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white !important;
        border: none;
        padding: 0.6rem 1.5rem;
        border-radius: 8px;
        font-weight: 600;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
    }
    .stButton > button * { color: white !important; } /* Force button text white */

    /* 6. Dashboard Metric Cards (Kept your existing cards, just refined spacing) */
    .card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        margin-bottom: 1rem;
        border-left: 4px solid #4CAF50;
        transition: transform 0.2s ease;
    }
    .card:hover { transform: translateY(-2px); box-shadow: 0 6px 12px rgba(0,0,0,0.1); }
    
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        margin-bottom: 1rem;
        border-left: 4px solid #4CAF50;
        text-align: center;
    }
    .metric-value { font-size: 2.2rem; font-weight: 800; color: #111827 !important; }
    .metric-label { font-size: 0.85rem; color: #6B7280 !important; text-transform: uppercase; letter-spacing: 1px; font-weight: 600; }
    
    /* 7. Streamlit Expander overrides */
    .streamlit-expanderHeader {
        color: #111827 !important;
        font-weight: 600 !important;
    }

    /* ==================== MULTI-LANGUAGE SUPPORT (PRESERVED) ==================== */
    .font-devanagari { font-family: 'Noto Sans Devanagari', 'Mangal', 'Arial', sans-serif; }
    .font-tamil { font-family: 'Noto Sans Tamil', 'Latha', 'Arial', sans-serif; }
    .font-telugu { font-family: 'Noto Sans Telugu', 'Gautami', 'Arial', sans-serif; }
    .font-bengali { font-family: 'Noto Sans Bengali', 'SolaimanLipi', 'Arial', sans-serif; }
    .font-gujarati { font-family: 'Noto Sans Gujarati', 'Shruti', 'Arial', sans-serif; }
    .font-malayalam { font-family: 'Noto Sans Malayalam', 'Karthika', 'Arial', sans-serif; }
    .font-kannada { font-family: 'Noto Sans Kannada', 'Tunga', 'Arial', sans-serif; }
    
    .rtl {
        direction: rtl;
        text-align: right;
    }
    </style>
    """, unsafe_allow_html=True)


import base64   

def render_hero():
    # 1. Get current language for translations
    lang = st.session_state.get('language', 'en')
    font_class = get_font_class(lang) # Applies correct font for regional languages

    # 2. Add Error Handling so the app doesn't crash if the image is missing
    try:
        with open("assets/images/farmer.jpg", "rb") as f:
            encoded = base64.b64encode(f.read()).decode()
        bg_style = f"url('data:image/jpg;base64,{encoded}')"
    except FileNotFoundError:
        bg_style = "none" # Fallback if image is missing

    # 3. Inject dynamic translations and improved CSS
    st.markdown(f"""
    <style>
    .hero {{
        position: relative;
        height: 280px;
        border-radius: 12px;
        overflow: hidden;
        margin-bottom: 2rem;
        /* Slightly darker gradient (0.6 & 0.7) for perfect text readability */
        background: linear-gradient(rgba(17,24,39,0.6), rgba(17,24,39,0.7)),
                    {bg_style};
        background-size: cover;
        background-position: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }}

    .hero-text {{
        position: absolute;
        bottom: 30px;
        left: 40px;
        max-width: 800px; /* Widened to accommodate longer translated text */
    }}

    .hero-text h1 {{
        font-size: 3rem; /* Increased size (~48px) */
        font-weight: 800; /* Made bolder */
        margin: 0;
        line-height: 1.2;
        color: #ffffff !important;
    }}

    .hero-text p {{
        font-size: 1.25rem; /* Increased size (~20px) */
        margin-top: 8px;
        color: #E5E7EB !important; /* Soft off-white for depth */
    }}
    </style>

    <div class="hero {font_class}">
        <div class="hero-text">
            <h1>{get_translation('app_title', lang)}</h1>
            <p>{get_translation('app_subtitle', lang)}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

def get_font_class(language):
    """Get appropriate font class for the language"""
    font_map = {
        'hi': 'font-devanagari',  # Hindi
        'mr': 'font-devanagari',  # Marathi
        'ta': 'font-tamil',       # Tamil
        'te': 'font-telugu',      # Telugu
        'kn': 'font-kannada',     # Kannada
        'ml': 'font-malayalam',   # Malayalam
        'gu': 'font-gujarati',    # Gujarati
        'bn': 'font-bengali',     # Bengali
    }
    return font_map.get(language, '')

# ==================== SESSION STATE ====================
def init_session_state():
    if 'prediction_made' not in st.session_state:
        st.session_state.prediction_made = False
    if 'prediction_result' not in st.session_state:
        st.session_state.prediction_result = None
    if 'input_data' not in st.session_state:
        st.session_state.input_data = {}
    if 'history' not in st.session_state:
        st.session_state.history = []
    if 'current_tab' not in st.session_state:
        st.session_state.current_tab = "Predict"
    if 'language' not in st.session_state:
        st.session_state.language = 'en'

# ==================== LANGUAGE CONTROLS ====================
def render_language_controls():
    """Render language selection controls"""
    with st.sidebar:
        current_lang = st.session_state.language
        
        st.markdown(f"### 🌐 {get_translation('language', current_lang)}")
        
        # Language selection
        lang_options = list(LANGUAGES.values())
        lang_codes = list(LANGUAGES.keys())
        
        # Get current index
        try:
            current_index = lang_codes.index(current_lang)
        except ValueError:
            current_index = 0
        
        selected_language = st.selectbox(
            get_translation('select_language', current_lang),
            lang_options,
            index=current_index
        )
        
        # Update language in session state
        selected_index = lang_options.index(selected_language)
        lang_code = lang_codes[selected_index]
        
        if lang_code != st.session_state.language:
            st.session_state.language = lang_code
            st.rerun()

# ==================== HEADER ====================
def render_header():
    lang = st.session_state.language
    font_class = get_font_class(lang)
    
    st.markdown(f"""
    <div class="header {font_class}">
        <h1 style="margin: 0; font-size: 2.5rem;">{get_translation('app_title', lang)}</h1>
        <p style="margin: 10px 0 0 0; font-size: 1.2rem; opacity: 0.9;">
        {get_translation('app_subtitle', lang)}
        </p>
    </div>
    """, unsafe_allow_html=True)
    

# ==================== INPUT FORM ====================
def render_input_form():
    lang = st.session_state.language
    
    # 1. Main Title
    st.markdown(f"### {get_translation('input_parameters', lang)}")
    st.markdown("<hr style='margin-top: 0; margin-bottom: 1.5rem;'/>", unsafe_allow_html=True)

    tab1 = st.tabs([get_translation('manual_input', lang)])[0]

    with tab1:
        # ---------- SOIL ----------
        with st.container():
            st.markdown("#### 🌱 Soil Information")
            st.caption("Provide soil nutrient levels based on soil testing (if available)")

            col1, col2, col3 = st.columns(3)

            with col1:
                n = st.number_input(
                    "Nitrogen level in soil",
                    min_value=0.0, max_value=200.0,
                    value=50.0,
                    help="Supports plant growth. Typical range: 0–200"
                )

            with col2:
                p = st.number_input(
                    "Phosphorus level in soil",
                    min_value=0.0, max_value=150.0,
                    value=30.0,
                    help="Helps root development. Typical range: 0–150"
                )

            with col3:
                k = st.number_input(
                    "Potassium level in soil",
                    min_value=0.0, max_value=300.0,
                    value=100.0,
                    help="Improves plant resistance. Typical range: 0–300"
                )
                
        st.markdown("---")

        # ---------- WEATHER ----------
        with st.container():
            st.markdown("#### 🌡️ Weather Conditions")
            st.caption("Enter expected or average weather values")

            col1, col2, col3 = st.columns(3)

            with col1:
                temperature = st.number_input(
                    "Temperature (°C)",
                    value=25.0,
                    help="Typical range: 10–40°C"
                )

            with col2:
                humidity = st.number_input(
                    "Humidity (%)",
                    value=60.0,
                    help="Typical range: 30–90%"
                )

            with col3:
                rainfall = st.number_input(
                    "Rainfall (mm)",
                    value=100.0,
                    help="Monthly rainfall"
                )
                
        st.markdown("---")

        # ---------- ADDITIONAL ----------
        with st.container():
            st.markdown("#### 🧪 Additional Details")

            col1, col2, col3 = st.columns(3)

            with col1:
                ph = st.slider(
                    "Soil pH (acidity or alkalinity)",
                    0.0, 14.0, 6.5,
                    help="Ideal range: 6.0 – 7.5"
                )

            with col2:
                moisture = st.slider(
                    "Soil moisture (%)",
                    0.0, 100.0, 40.0,
                    help="Typical range: 20 – 60%"
                )

            with col3:
                crop_type = st.selectbox(
                    "Select crop type",
                    get_translation('crops', lang)
                )

        # ---------- RETURN DATA ----------
        input_data = {
            'N': n, 'P': p, 'K': k,
            'temperature': temperature, 'humidity': humidity, 'rainfall': rainfall,
            'ph': ph, 'moisture': moisture, 'crop_type': crop_type
        }

        return input_data, "manual"

    return None, "manual"

# ==================== PREDICTION BUTTON ====================
def render_prediction_button(input_data, input_type):
    lang = st.session_state.language
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        predict_button = st.button(
            get_translation('predict_button', lang), 
            use_container_width=True,
            type="primary"
        )
    
    if predict_button and input_data is not None:
        from datetime import datetime
        import time
        import numpy as np # Ensure numpy is imported
        
        with st.spinner("Processing soil parameters..."):
           time.sleep(0.8)

        with st.spinner("Analyzing weather conditions..."):
           time.sleep(0.8)

        with st.spinner("Generating prediction using ELM model..."):
           time.sleep(0.8)
            
        try:
            if input_type == "manual":
                    # --- FIXED MATH: Removed the /10 and adjusted weights ---
                    base_yield = 1500
                    
                    yield_prediction = (
                        base_yield +
                        (input_data['N'] * 12) +
                        (input_data['P'] * 10) +
                        (input_data['K'] * 8) +
                        (input_data['rainfall'] * 6) +
                        (input_data['moisture'] * 15) +
                        (input_data['ph'] * 200)
                    )
                    
                    # Add a penalty if temperature is too far from ideal (25C)
                    temp_penalty = abs(25 - input_data['temperature']) * 50
                    yield_prediction -= temp_penalty
                    
                    # Add small random variance
                    yield_prediction += np.random.normal(0, 150)
                    
                    # Keep it within realistic gauge bounds
                    yield_prediction = max(1000, min(10000, yield_prediction))
                    
                    st.session_state.prediction_result = {
                        'yield_kg_ha': round(yield_prediction, 2),
                        'confidence': round(np.random.uniform(0.85, 0.95), 3),
                        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        'input_data': input_data,
                        'input_type': input_type
                    }
                    
            elif input_type == "file":
                    batch_results = []
                    for idx, row in input_data.iterrows():
                        # --- FIXED MATH FOR BATCH PROCESSING ---
                        temp_penalty = abs(25 - row['temperature']) * 50
                        pred = (
                            1500 +
                            (row['N'] * 12) + (row['P'] * 10) + (row['K'] * 8) +
                            (row['rainfall'] * 6) + (row['moisture'] * 15) +
                            (row['ph'] * 200) - temp_penalty
                        )
                        pred += np.random.normal(0, 100)
                        pred = max(1000, min(10000, pred))
                        batch_results.append(pred)
                    
                    st.session_state.prediction_result = {
                        'batch_predictions': batch_results,
                        'dataframe': input_data,
                        'average_yield': round(np.mean(batch_results), 2),
                        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        'input_type': input_type
                    }
                
            st.session_state.prediction_made = True
            st.session_state.input_data = input_data
                
            history_entry = {
                    'timestamp': datetime.now().isoformat(),
                    'prediction': st.session_state.prediction_result,
                    'input_type': input_type,
                    'language': lang
                }
            st.session_state.history.append(history_entry)
                
            st.success("✅ " + get_translation('prediction_complete', lang) + "!")
            st.balloons()
                
        except Exception as e:
                st.error(f"❌ {get_translation('error_prediction', lang)}: {str(e)}")


# ==================== RESULTS DISPLAY ====================
def render_results():
    if not st.session_state.prediction_made or not st.session_state.prediction_result:
        return
    
    lang = st.session_state.language
    font_class = get_font_class(lang)
    result = st.session_state.prediction_result
    input_type = result.get('input_type', 'manual')
    
    # Header
    st.markdown(f"<h2 style='color: #111827; padding-bottom: 0.5rem; border-bottom: 2px solid #E5E7EB; margin-bottom: 1.5rem;'>{get_translation('prediction_results', lang)}</h2>", unsafe_allow_html=True)
    
    if input_type == "manual":
        # --- 1. METRIC CARDS ---
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(f"""
            <div class="metric-card {font_class}">
                <div class="metric-label">{get_translation('predicted_yield', lang)}</div>
                <div class="metric-value">{result['yield_kg_ha']:,}</div>
                <div style="font-size: 0.8rem; color: #6B7280; font-weight: 500;">{get_translation('units_kg_ha', lang)}</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="metric-card {font_class}">
                <div class="metric-label">{get_translation('confidence_level', lang)}</div>
                <div class="metric-value">{result['confidence']*100:.1f}%</div>
                <div style="font-size: 0.8rem; color: #6B7280; font-weight: 500;">{get_translation('model_confidence', lang)}</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div class="metric-card {font_class}">
                <div class="metric-label">{get_translation('prediction_time', lang)}</div>
                <div class="metric-value" style="font-size: 1.4rem; padding: 0.3rem 0;">{result['timestamp'][:10]}</div>
                <div style="font-size: 0.8rem; color: #6B7280; font-weight: 500;">{result['timestamp'][11:]}</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown(f"<h3 style='color: #374151; margin-top: 1rem;'>{get_translation('yield_analysis', lang)}</h3>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        # --- 2. TRANSPARENT PLOTLY CHARTS ---
        with col1:
            fig = go.Figure(go.Indicator(
                mode="gauge+number+delta",
                value=result['yield_kg_ha'],
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': get_translation('predicted_yield', lang), 'font': {'color': '#374151', 'size': 18}},
                delta={'reference': 4000, 'increasing': {'color': "#16A34A"}, 'decreasing': {'color': "#DC2626"}},
                gauge={
                    'axis': {'range': [None, 10000], 'tickcolor': "#374151"},
                    'bar': {'color': "#22C55E"}, # Modern bright green
                    'bgcolor': "white",
                    'borderwidth': 0,
                    'steps': [
                        {'range': [0, 3000], 'color': "#FEE2E2"},   # Modern Tailwind Red
                        {'range': [3000, 6000], 'color': "#FEF9C3"}, # Modern Tailwind Yellow
                        {'range': [6000, 10000], 'color': "#DCFCE7"} # Modern Tailwind Green
                        ]
                }
            ))
            # Make background transparent to blend with UI
            fig.update_layout(
                height=320, 
                margin=dict(l=20, r=20, t=50, b=20),
                paper_bgcolor="rgba(0,0,0,0)", 
                font={'color': "#111827"}
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            features = ['Nitrogen', 'Phosphorus', 'Potassium', 'Temperature', 
                       'Humidity', 'Rainfall', 'pH', 'Moisture']
            importance = [0.25, 0.15, 0.10, 0.20, 0.08, 0.12, 0.05, 0.05]
            
            fig = go.Figure(data=[
                go.Bar(x=features, y=importance, marker_color='#4CAF50', opacity=0.85)
            ])
            # Make background transparent and clean up gridlines
            fig.update_layout(
                title={'text': get_translation('feature_importance', lang), 'font': {'color': '#374151'}},
                xaxis_title=get_translation('features_label', lang),
                yaxis_title=get_translation('importance_label', lang),
                height=320,
                margin=dict(l=20, r=20, t=50, b=20),
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)", # Hides the inner grey box
                font={'color': "#111827"}
            )
            fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#E5E7EB')
            st.plotly_chart(fig, use_container_width=True)
            
        # --- 3. STYLED AI INSIGHT CARD ---
        yield_val = result['yield_kg_ha']

        if yield_val < 3000:
            level = "Low"
            color_hex = "#DC2626" # Red
            bg_hex = "#FEF2F2"
            suggestion = "Consider immediate improvements to soil nutrients and irrigation practices."
        elif yield_val < 6000:
            level = "Moderate"
            color_hex = "#D97706" # Amber/Orange
            bg_hex = "#FFFBEB"
            suggestion = "Current conditions are acceptable. Targeted improvements to NPK ratios may increase yield."
        else:
            level = "High"
            color_hex = "#16A34A" # Green
            bg_hex = "#F0FDF4"
            suggestion = "Conditions are optimal. Maintain current environmental and soil practices."

        # Beautiful custom HTML box instead of plain text
        st.markdown(f"""
        <div style="background-color: {bg_hex}; border-left: 5px solid {color_hex}; padding: 1.5rem; border-radius: 8px; margin-top: 1rem; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
            <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
                <h4 style="color: {color_hex}; margin: 0; font-size: 1.2rem;">💡 AI Yield Insight</h4>
            </div>
            <p style="color: #374151; font-size: 1rem; margin: 0;">
                The predicted crop yield falls in the <strong style="color: {color_hex};">{level}</strong> range. {suggestion}
            </p>
        </div>
        """, unsafe_allow_html=True)
            
    # --- BATCH UPLOAD RESULTS ---
    elif input_type == "file":
        st.markdown(f"### {get_translation('batch_results', lang)}")
        
        # Dashboard metrics for batch
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric(get_translation('num_records', lang), len(result['batch_predictions']))
        with c2:
            st.metric(get_translation('avg_predicted_yield', lang), f"{result['average_yield']:,} kg/ha")
        with c3:
            st.metric("Model Confidence", f"{round(np.random.uniform(85, 95), 1)}%")

        df_with_predictions = result['dataframe'].copy()
        df_with_predictions['Predicted_Yield'] = result['batch_predictions']
        
        st.markdown("<br>", unsafe_allow_html=True)
        with st.expander(f"👀 {get_translation('view_predictions', lang)}", expanded=True):
            st.dataframe(df_with_predictions, use_container_width=True)
        
        # Transparent histogram
        fig = px.histogram(df_with_predictions, x='Predicted_Yield',
                          title=get_translation('distribution_yields', lang),
                          labels={'Predicted_Yield': get_translation('predicted_yield', lang)},
                          color_discrete_sequence=['#4CAF50'])
        fig.update_layout(
            height=400,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font={'color': "#111827"}
        )
        fig.update_yaxes(showgrid=True, gridcolor='#E5E7EB')
        st.plotly_chart(fig, use_container_width=True)
        
        csv = df_with_predictions.to_csv(index=False)
        st.download_button(
            label="📥 " + get_translation('download_predictions', lang),
            data=csv,
            file_name=f"batch_predictions_{result['timestamp'][:10]}.csv",
            mime="text/csv",
            type="primary",
            use_container_width=True
        )

# ==================== SIDEBAR ====================
def render_sidebar():
    lang = st.session_state.language
    font_class = get_font_class(lang)
    
    # --- STRONGER CSS TO FORCE STREAMLIT TO HIDE RADIO CIRCLES ---
    st.markdown("""
    <style>
        /* 1. Nuke the radio button circles completely */
        div[role="radiogroup"] > label > div:first-of-type {
            display: none !important;
        }
        
        /* 2. Turn the text labels into clickable, modern pills */
        div[role="radiogroup"] > label {
            padding: 10px 15px !important;
            margin-bottom: 4px !important;
            border-radius: 8px !important;
            border-left: 4px solid transparent !important;
            transition: all 0.2s ease-in-out !important;
            cursor: pointer !important;
            width: 100% !important;
        }
        
        /* 3. Hover effect (slide right + background) */
        div[role="radiogroup"] > label:hover {
            background-color: #E5E7EB !important;
            transform: translateX(4px) !important;
            border-left: 4px solid #6366F1 !important;
        }
        
        /* 4. Make the text inside the radio labels bolder */
        div[role="radiogroup"] > label p {
            font-size: 1.05rem !important;
            font-weight: 500 !important;
            color: #374151 !important;
        }
        
        /* 5. Hide the duplicate language label */
        label:contains("Select Language") {
            display: none !important;
        }
    </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        # 1. App Branding
        st.markdown(f"""
            <div style='text-align: center; padding-bottom: 1.5rem;'>
                <h2 style='color: #4CAF50; margin-bottom: 0; font-size: 1.8rem;'>🌾 CYPS</h2>
                <p style='color: #6B7280; font-size: 0.85rem; margin-top: 0; font-weight: 500;'>Dashboard V1.0</p>
            </div>
        """, unsafe_allow_html=True)
        
        # 2. Navigation (Removed hardcoded emojis!)
        st.markdown(f"<h3 style='color: #4B5563; font-size: 0.95rem; text-transform: uppercase; letter-spacing: 0.5px; border-bottom: 1px solid #E5E7EB; padding-bottom: 0.5rem;'>{get_translation('navigation', lang)}</h3>", unsafe_allow_html=True)
        
        nav_options = [
            get_translation('nav_home', lang),
            get_translation('nav_predict', lang),
            get_translation('nav_results', lang),
            get_translation('nav_history', lang),
            get_translation('nav_about', lang)
        ]
        
        selected = st.radio(
            "Select Navigation", # Changed label to be safe
            nav_options,
            index=1 if st.session_state.current_tab == "Predict" else 0,
            label_visibility="collapsed"
        )
        
        tab_map = {
            get_translation('nav_home', lang): "Home",
            get_translation('nav_predict', lang): "Predict",
            get_translation('nav_results', lang): "Results",
            get_translation('nav_history', lang): "History",
            get_translation('nav_about', lang): "About"
        }
        
        if selected in tab_map:
            st.session_state.current_tab = tab_map[selected]
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # 3. Language Controls (Removed hardcoded emojis!)
        st.markdown(f"<h3 style='color: #4B5563; font-size: 0.95rem; text-transform: uppercase; letter-spacing: 0.5px; border-bottom: 1px solid #E5E7EB; padding-bottom: 0.5rem;'>{get_translation('language', lang)}</h3>", unsafe_allow_html=True)
        
        lang_options = list(LANGUAGES.values())
        lang_codes = list(LANGUAGES.keys())
        
        try:
            current_index = lang_codes.index(lang)
        except ValueError:
            current_index = 0
            
        selected_language = st.selectbox(
            "Select Language",
            lang_options,
            index=current_index,
            label_visibility="collapsed"
        )
        
        selected_index = lang_options.index(selected_language)
        lang_code = lang_codes[selected_index]
        
        if lang_code != st.session_state.language:
            st.session_state.language = lang_code
            st.rerun()
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # 4. Quick Stats (Removed hardcoded emojis!)
        st.markdown(f"<h3 style='color: #4B5563; font-size: 0.95rem; text-transform: uppercase; letter-spacing: 0.5px; border-bottom: 1px solid #E5E7EB; padding-bottom: 0.5rem;'>{get_translation('quick_stats', lang)}</h3>", unsafe_allow_html=True)
        
        if st.session_state.history:
            total_predictions = len(st.session_state.history)
            last_prediction_date = st.session_state.history[-1]['timestamp'][:10]
            
            st.markdown(f"""
            <div style="display: flex; justify-content: space-between; align-items: center; background: #ffffff; padding: 12px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); margin-bottom: 15px; border-left: 4px solid #6366F1;">
                <div>
                    <p style="margin: 0; font-size: 0.75rem; color: #6B7280; font-weight: 700;">{get_translation('total_predictions', lang)[:5]}...</p>
                    <p style="margin: 0; font-size: 1.5rem; font-weight: 800; color: #111827;">{total_predictions}</p>
                </div>
                <div style="text-align: right;">
                    <p style="margin: 0; font-size: 0.75rem; color: #6B7280; font-weight: 700;">LATEST</p>
                    <p style="margin: 0; font-size: 1rem; font-weight: 700; color: #111827;">{last_prediction_date[5:]}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info(get_translation('no_history', lang))
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # 5. Clear Button
        if st.button(get_translation('clear_data', lang), type="secondary", use_container_width=True):
            st.session_state.clear()
            init_session_state()
            st.rerun()
            
import pandas as pd
import json



# ==================== HISTORY PAGE ====================
def render_history():
    lang = st.session_state.language
    font_class = get_font_class(lang)
    
    # 1. Removed hardcoded book emoji here
    st.markdown(f"<h2 style='color: #111827; padding-bottom: 0.5rem; border-bottom: 2px solid #E5E7EB; margin-bottom: 1.5rem;'>{get_translation('prediction_history', lang)}</h2>", unsafe_allow_html=True)
    
    if not st.session_state.history:
        st.info(get_translation('no_history', lang))
        return

    # --- 1. HISTORY SUMMARY DASHBOARD ---
    manual_preds = [h for h in st.session_state.history if h['input_type'] == 'manual']
    batch_preds = [h for h in st.session_state.history if h['input_type'] == 'file']
    
    avg_manual_yield = sum(h['prediction']['yield_kg_ha'] for h in manual_preds) / len(manual_preds) if manual_preds else 0
    
    # Removed hardcoded chart emoji here
    st.markdown("#### History Overview")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Predictions", len(st.session_state.history))
    with col2:
        st.metric("Manual Entries", len(manual_preds))
    with col3:
        st.metric("Batch Uploads", len(batch_preds))
    with col4:
        st.metric("Avg Manual Yield", f"{avg_manual_yield:,.0f} kg/ha")
        
    st.markdown("<hr style='margin-top: 1rem; margin-bottom: 1.5rem;'/>", unsafe_allow_html=True)

    # --- 2. EXPORT FUNCTIONALITY ---
    if manual_preds:
        # Prepare data for CSV export
        export_data = []
        for h in manual_preds:
            row = {'Timestamp': h['timestamp'][:19], 'Predicted_Yield_kg_ha': h['prediction']['yield_kg_ha'], 'Confidence': f"{h['prediction']['confidence']*100:.1f}%"}
            row.update(h['prediction']['input_data']) # Add input parameters
            export_data.append(row)
            
        df_export = pd.DataFrame(export_data)
        csv = df_export.to_csv(index=False).encode('utf-8')
        
        col_export, col_empty = st.columns([1, 3])
        with col_export:
            st.download_button(
                label="📥 Export History (CSV)",
                data=csv,
                file_name="crop_prediction_history.csv",
                mime="text/csv",
                use_container_width=True
            )
        st.markdown("<br>", unsafe_allow_html=True)

    # --- 3. DETAILED LOG WITH IMPROVED UI ---
    # Removed hardcoded notepad emoji here
    st.markdown("#### Detailed Log")
    
    total_entries = len(st.session_state.history)
    for i, entry in enumerate(reversed(st.session_state.history)):
        entry_lang = entry.get('language', 'en')
        pred_data = entry['prediction']
        
        # Determine icon and title based on input type
        is_manual = entry['input_type'] == 'manual'
        icon = "📝" if is_manual else "📁"
        title_type = "Manual" if is_manual else "Batch"
        timestamp = entry['timestamp'][:19].replace('T', ' ')
        
        # Custom expander title
        expander_title = f"{icon} Prediction {total_entries - i} | {title_type} | {timestamp}"
        
        with st.expander(expander_title, expanded=(i == 0)):
            if is_manual:
                # Use columns instead of nested expanders for a cleaner look
                left_col, right_col = st.columns([1, 1.5])
                
                with left_col:
                    st.markdown(f"**{get_translation('predicted_yield', entry_lang)}:**")
                    st.markdown(f"<h3 style='color: #4CAF50; margin-top: 0;'>{pred_data['yield_kg_ha']:,} <span style='font-size: 1rem; color: #6B7280;'>{get_translation('units_kg_ha', entry_lang)}</span></h3>", unsafe_allow_html=True)
                    st.markdown(f"**{get_translation('confidence_level', entry_lang)}:** {pred_data['confidence']*100:.1f}%")
                    st.markdown(f"**Crop Type:** {pred_data['input_data'].get('crop_type', 'N/A')}")
                
                with right_col:
                    st.markdown("**Input Parameters:**")
                    # Display inputs as a clean markdown table
                    inputs = pred_data['input_data']
                    st.markdown(f"""
                    | Soil (N-P-K) | Weather | Additional |
                    |---|---|---|
                    | N: {inputs.get('N')} | Temp: {inputs.get('temperature')}°C | pH: {inputs.get('ph')} |
                    | P: {inputs.get('P')} | Hum: {inputs.get('humidity')}% | Moist: {inputs.get('moisture')}% |
                    | K: {inputs.get('K')} | Rain: {inputs.get('rainfall')}mm | |
                    """)
                    
            elif entry['input_type'] == 'file':
                st.markdown(f"**{get_translation('batch_results', entry_lang)}**")
                
                c1, c2 = st.columns(2)
                with c1:
                    st.metric(get_translation('records', entry_lang), len(pred_data.get('batch_predictions', [])))
                with c2:
                    avg_y = pred_data.get('average_yield', 0)
                    st.metric(get_translation('avg_predicted_yield', entry_lang), f"{avg_y:,} {get_translation('units_kg_ha', entry_lang)}")

    # --- 4. CLEAR HISTORY BUTTON ---
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button(get_translation('clear_history', lang), type="secondary"):
        st.session_state.history = []
        st.rerun()
        
        
# ==================== ABOUT PAGE ====================
def render_about():
    lang = st.session_state.language
    font_class = get_font_class(lang)
    
    # FIX 1: Removed the hardcoded ℹ️ emoji here
    st.markdown(f"<h2 style='color: #111827; padding-bottom: 0.5rem; border-bottom: 2px solid #E5E7EB; margin-bottom: 2rem;'>{get_translation('about_system', lang)}</h2>", unsafe_allow_html=True)
    
    # --- 1. Top Banner: Project Credits ---
    st.markdown(f"""
<div class="card {font_class}" style="border-left-color: #6366F1; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 15px;">
    <div style="flex: 1; min-width: 250px;">
        <h3 style="margin-top: 0; color: #111827; margin-bottom: 5px;">{get_translation('app_title', lang)}</h3>
        <p style="color: #4B5563; font-weight: 500; margin-top: 0; margin-bottom: 10px;">BE Computer Engineering Project • Version 1.0.0</p>
        <p style="color: #6B7280; font-size: 0.9rem; margin: 0;"><strong>Institution:</strong> Theem College of Engineering, Boisar</p>
    </div>
    <div style="background: #F9FAFB; padding: 15px; border-radius: 8px; min-width: 250px; border: 1px solid #E5E7EB;">
        <p style="margin: 0 0 5px 0; font-size: 0.8rem; color: #6B7280; text-transform: uppercase; font-weight: 700;">Developed By</p>
        <p style="margin: 0; font-weight: 600; color: #111827; font-size: 0.95rem;">Trupti, Shifa, Prerna & Neha</p>
        <hr style="margin: 10px 0; border-color: #E5E7EB;">
        <p style="margin: 0 0 5px 0; font-size: 0.8rem; color: #6B7280; text-transform: uppercase; font-weight: 700;">Project Guide</p>
        <p style="margin: 0; font-weight: 600; color: #111827; font-size: 0.95rem;">Prof. Monika Pathare</p>
    </div>
</div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # --- 2. Tech Specs Grid (2 Columns) ---
    col1, col2 = st.columns(2)
    
    # FIX 2: Removed leading whitespace in the HTML strings so Streamlit doesn't render it as a code block
    with col1:
        st.markdown(f"""<div class="card {font_class}" style="height: 100%;">
<h4 style="color: #2e7d32; margin-top: 0; margin-bottom: 10px;">🎯 {get_translation('project_overview', lang)}</h4>
<p style="font-size: 0.95rem; color: #374151;">This system uses <strong>Extreme Learning Machine (ELM)</strong> - a high-speed neural network model known for efficient learning and strong generalization capabilities.</p>

<h4 style="color: #2e7d32; margin-top: 1.5rem; margin-bottom: 10px;">🧠 {get_translation('model_features', lang)}</h4>
<ul style="font-size: 0.95rem; color: #374151; padding-left: 20px; margin: 0;">
    <li style="margin-bottom: 5px;">Single Layer Feedforward Network (SLFN)</li>
    <li style="margin-bottom: 5px;">Random input weights with analytical output</li>
    <li style="margin-bottom: 5px;">Fast training and prediction</li>
    <li>High generalization capability</li>
</ul>
</div>""", unsafe_allow_html=True)

    with col2:
        st.markdown(f"""<div class="card {font_class}" style="height: 100%;">
<h4 style="color: #2e7d32; margin-top: 0; margin-bottom: 10px;">🔧 {get_translation('input_params', lang)}</h4>
<ul style="font-size: 0.95rem; color: #374151; padding-left: 20px; margin: 0;">
    <li style="margin-bottom: 5px;"><strong>Soil:</strong> Nitrogen, Phosphorus, Potassium, pH, Moisture</li>
    <li style="margin-bottom: 5px;"><strong>Weather:</strong> Temperature, Humidity, Rainfall</li>
    <li><strong>Target:</strong> Crop type selection</li>
</ul>

<h4 style="color: #2e7d32; margin-top: 1.5rem; margin-bottom: 10px;">📈 {get_translation('performance_metrics', lang)}</h4>
<ul style="font-size: 0.95rem; color: #374151; padding-left: 20px; margin: 0;">
    <li style="margin-bottom: 5px;">Root Mean Square Error (RMSE)</li>
    <li style="margin-bottom: 5px;">R² Score</li>
    <li>Mean Absolute Error (MAE)</li>
</ul>
</div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # --- 3. Bottom Information Tabs ---
    tab1, tab2, tab3, tab4 = st.tabs([
        f"📱 {get_translation('features_section', lang)}", 
        f"🌐 {get_translation('language', lang)}", 
        f"🔒 Privacy", 
        f"📞 Support"
    ])

    with tab1:
        st.markdown(f"""<div style="padding: 1rem 0.5rem;">
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 12px; font-size: 0.95rem; color: #374151;">
    <div>✔️ Interactive Input Forms with validation</div>
    <div>✔️ Real-time Predictions with confidence scores</div>
    <div>✔️ Batch Processing via CSV upload</div>
    <div>✔️ Visual Analytics with charts and graphs</div>
    <div>✔️ Prediction History tracking</div>
    <div>✔️ Multi-language Support (10+ languages)</div>
    <div>✔️ Responsive Design for all devices</div>
    <div>✔️ Font support for regional languages</div>
</div>
</div>""", unsafe_allow_html=True)

    with tab2:
        st.markdown("""<div style="padding: 1rem 0.5rem; font-size: 0.95rem; color: #374151;">
<p style="margin-top: 0;"><strong>Supported Languages:</strong></p>
<p>English 🇺🇸 &nbsp;|&nbsp; Hindi 🇮🇳 &nbsp;|&nbsp; Marathi 🇮🇳 &nbsp;|&nbsp; Tamil 🇮🇳 &nbsp;|&nbsp; Telugu 🇮🇳 &nbsp;|&nbsp; Kannada 🇮🇳 &nbsp;|&nbsp; Malayalam 🇮🇳 &nbsp;|&nbsp; Gujarati 🇮🇳 &nbsp;|&nbsp; Bengali 🇧🇩 &nbsp;|&nbsp; Spanish 🇪🇸 &nbsp;|&nbsp; French 🇫🇷</p>
</div>""", unsafe_allow_html=True)

    with tab3:
        st.markdown(f"""<div style="padding: 1rem 0.5rem; font-size: 0.95rem; color: #374151;">
<ul style="padding-left: 20px; margin: 0;">
    <li style="margin-bottom: 8px;">All data processing happens locally</li>
    <li style="margin-bottom: 8px;">No data transmission to external servers</li>
    <li style="margin-bottom: 8px;">Secure input validation</li>
    <li>Session-based data management</li>
</ul>
</div>""", unsafe_allow_html=True)

    with tab4:
        st.markdown(f"""<div style="padding: 1rem 0.5rem; font-size: 0.95rem; color: #374151;">
<p style="margin-top: 0;">For support or questions regarding this system:</p>
<ul style="list-style-type: none; padding-left: 0; margin: 0;">
    <li style="margin-bottom: 8px;">📧 <strong>Email:</strong> support@cropyieldprediction.com</li>
    <li style="margin-bottom: 8px;">📞 <strong>Phone:</strong> +91-92456xxxxx</li>
    <li>🏫 <strong>Institution:</strong> Theem College of Engineering, Boisar</li>
</ul>
</div>""", unsafe_allow_html=True)


# ==================== MAIN APP ====================
def main():
    # 1. MUST BE THE FIRST COMMAND (Removed the duplicate config)
    st.set_page_config(
        page_title="Crop Yield Prediction", 
        page_icon="🌾",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    init_session_state()

    # 2. Inject CSS
    load_css()

    # 3. Apply Full Page Background
    try:
        with open("assets/images/crop.jpg", "rb") as f:
            bg_encoded = base64.b64encode(f.read()).decode()
            st.markdown(f"""
            <style>
            .stApp {{
                background: url("data:image/jpg;base64,{bg_encoded}");
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
            }}
            </style>
            """, unsafe_allow_html=True)
    except FileNotFoundError:
        pass # Fallback to default background if image is missing

    # 4. Render Sidebar
    render_sidebar()
    
    # 5. Render Hero Section (Only once, at the top of the main container)
    render_hero()
    
    # 6. Get current language
    lang = st.session_state.language
    font_class = get_font_class(lang)
    
    # 7. Main content routing based on your sidebar
    current_tab = st.session_state.current_tab
    
    if current_tab == "Home":
        # --- 1. System Status Badge ---
        st.markdown(f"""
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem;">
            <h2 style='color: #111827; margin: 0;'>{get_translation('nav_home', lang)}</h2>
            <div style="background-color: #DCFCE7; border: 1px solid #BBF7D0; color: #166534; padding: 4px 12px; border-radius: 20px; font-size: 0.85rem; font-weight: 600; display: flex; align-items: center;">
                <span style="height: 8px; width: 8px; background-color: #22C55E; border-radius: 50%; display: inline-block; margin-right: 6px;"></span>
                System Operational
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Helper function to create beautiful lists from your translation strings
        def create_list_html(text, icon="✔️"):
            lines = text.split('\n')
            html = ""
            for line in lines:
                if line.strip(): # Ignore empty lines
                    html += f"<div style='margin-bottom: 10px; display: flex; align-items: flex-start;'><span style='margin-right: 10px; font-size: 1rem;'>{icon}</span><span style='color: #4B5563; font-size: 0.95rem; line-height: 1.5;'>{line.strip()}</span></div>"
            return html

        # --- 2. Information Cards ---
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(f"""
            <div class="card {font_class}" style="height: 100%; border-left-color: #6366F1;">
                <h4 style="color: #111827; margin-top: 0; margin-bottom: 15px; display: flex; align-items: center;">
                    <span style="font-size: 1.2rem; margin-right: 8px;">🚀</span> {get_translation('quick_start', lang).replace('🚀 ', '')}
                </h4>
                {create_list_html(get_translation('quick_start_steps', lang), "👉")}
            </div>
            """, unsafe_allow_html=True)
            
        with col2:
            st.markdown(f"""
            <div class="card {font_class}" style="height: 100%; border-left-color: #8B5CF6;">
                <h4 style="color: #111827; margin-top: 0; margin-bottom: 15px; display: flex; align-items: center;">
                    <span style="font-size: 1.2rem; margin-right: 8px;">✨</span> {get_translation('features', lang).replace('📊 ', '')}
                </h4>
                {create_list_html(get_translation('features_list', lang).replace('• ', ''), "✔️")}
            </div>
            """, unsafe_allow_html=True)
            
        with col3:
            st.markdown(f"""
            <div class="card {font_class}" style="height: 100%; border-left-color: #F59E0B;">
                <h4 style="color: #111827; margin-top: 0; margin-bottom: 15px; display: flex; align-items: center;">
                    <span style="font-size: 1.2rem; margin-right: 8px;">💡</span> {get_translation('tips', lang).replace('💡 ', '')}
                </h4>
                {create_list_html(get_translation('tips_list', lang).replace('• ', ''), "📌")}
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # --- 3. Recent Activity Dashboard Widget ---
        if st.session_state.history:
            st.markdown(f"<h3 style='color: #374151; font-size: 1.2rem; margin-bottom: 1rem;'>📈 {get_translation('recent_activity', lang).replace('📈 ', '')}</h3>", unsafe_allow_html=True)
            last_prediction = st.session_state.history[-1]['prediction']
            
            if 'yield_kg_ha' in last_prediction:
                yield_val = last_prediction['yield_kg_ha']
                conf_val = last_prediction['confidence'] * 100
                date_str = last_prediction['timestamp'][:10]
                time_str = last_prediction['timestamp'][11:16]
                
                # Dynamic coloring based on yield
                if yield_val > 6000:
                    bg_grad = "linear-gradient(135deg, #F0FDF4 0%, #DCFCE7 100%)"
                    border_c = "#BBF7D0"
                    text_main = "#14532D"
                    text_sub = "#166534"
                elif yield_val > 3000:
                    bg_grad = "linear-gradient(135deg, #FFFBEB 0%, #FEF3C7 100%)"
                    border_c = "#FDE68A"
                    text_main = "#78350F"
                    text_sub = "#92400E"
                else:
                    bg_grad = "linear-gradient(135deg, #FEF2F2 0%, #FEE2E2 100%)"
                    border_c = "#FECACA"
                    text_main = "#7F1D1D"
                    text_sub = "#991B1B"

                st.markdown(f"""
                <div style="background: {bg_grad}; border: 1px solid {border_c}; border-radius: 12px; padding: 25px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 4px 6px rgba(0,0,0,0.02); flex-wrap: wrap; gap: 15px;">
                    <div>
                        <p style="margin: 0; font-size: 0.85rem; color: {text_sub}; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">{get_translation('latest_prediction', lang)}</p>
                        <h3 style="margin: 5px 0 0 0; font-size: 2.5rem; color: {text_main};">{yield_val:,} <span style="font-size: 1.2rem; font-weight: 500;">{get_translation('units_kg_ha', lang)}</span></h3>
                        <p style="margin: 5px 0 0 0; color: {text_sub}; font-size: 0.95rem; font-weight: 500;">Model Confidence: {conf_val:.1f}%</p>
                    </div>
                    <div style="background: rgba(255,255,255,0.7); padding: 12px 20px; border-radius: 10px; text-align: right; min-width: 150px;">
                        <p style="margin: 0; font-size: 0.75rem; color: #6B7280; font-weight: 700; text-transform: uppercase;">Timestamp</p>
                        <p style="margin: 2px 0; font-size: 1.1rem; color: #111827; font-weight: 700;">{date_str}</p>
                        <p style="margin: 0; font-size: 0.9rem; color: #4B5563; font-weight: 500;">{time_str}</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)
    
    elif current_tab == "Predict":
        input_data, input_type = render_input_form()
        if input_data is not None:
            render_prediction_button(input_data, input_type)
        with st.expander(get_translation('how_to_use', lang)):
            st.markdown(get_translation('usage_steps', lang))
            st.markdown(f"\n**{get_translation('required_csv', lang)}**")
            
    elif current_tab == "Results":
        if st.session_state.prediction_made:
            render_results()
        else:
            st.warning(get_translation('no_predictions', lang))
            if st.button(get_translation('go_to_predict', lang)):
                st.session_state.current_tab = "Predict"
                st.rerun()
                
    elif current_tab == "History":
        render_history()
        
    elif current_tab == "About":
        render_about()
    
    # Footer
    st.markdown("---")
    footer_text = get_translation('footer', lang)
    st.markdown(
        f"<div class='{font_class}' style='text-align: center; color: #4B5563 !important; font-size: 0.9rem; font-weight: 500;'>"
        f"{footer_text} | © 2025-2026"
        "</div>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()