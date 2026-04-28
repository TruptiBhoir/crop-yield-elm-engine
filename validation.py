"""
Crop Validation Module
Ensures input data stays within biological limits for accurate ML inference.
"""

from typing import Dict, List, Any

# Biological constants for technical reference
AGRICULTURAL_STANDARDS = {
    "Wheat": {
        "temp_range": (15, 25),
        "ph_range": (6.0, 7.5),
        "rainfall_range": (450, 650)
    }
}

class InputValidator:
    """Handles logic for checking if environmental inputs are realistic."""

    @staticmethod
    def check_ranges(crop: str, temp: float, ph: float) -> List[str]:
        """
        Validates inputs against biological standards.
        
        Returns:
            List[str]: A list of warning messages. Empty if all good.
        """
        warnings = []
        limits = AGRICULTURAL_STANDARDS.get(crop)
        
        if not limits:
            return ["Crop standard not found in database."]

        if not (limits["temp_range"][0] <= temp <= limits["temp_range"][1]):
            warnings.append(f"Temperature {temp}°C is outside optimal {limits['temp_range']} range.")
            
        if not (limits["ph_range"][0] <= ph <= limits["ph_range"][1]):
            warnings.append(f"Soil pH {ph} is outside optimal {limits['ph_range']} range.")
            
        return warnings