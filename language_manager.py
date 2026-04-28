"""
Language/Internationalization Manager
Handles multi-language support
"""

import json
from typing import Dict, Optional
import streamlit as st

class LanguageManager:
    def __init__(self, lang_dir: str = "languages"):
        self.lang_dir = lang_dir
        self.current_lang = "en"
        self.translations = {}
        self.load_language("en")
    
    def load_language(self, lang_code: str):
        """Load language file"""
        try:
            with open(f"{self.lang_dir}/{lang_code}.json", "r", encoding="utf-8") as f:
                self.translations[lang_code] = json.load(f)
            self.current_lang = lang_code
        except FileNotFoundError:
            st.error(f"Language file for {lang_code} not found")
    
    def get(self, key: str, default: Optional[str] = None) -> str:
        """Get translation for key"""
        return self.translations.get(self.current_lang, {}).get(key, default or key)
    
    def set_language(self, lang_code: str):
        """Change current language"""
        if lang_code in self.translations:
            self.current_lang = lang_code
        else:
            self.load_language(lang_code)