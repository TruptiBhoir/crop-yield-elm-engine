# check_imports.py
import sys
import os

# Add the 'src' folder to the system path so Python can find your files
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

print("=" * 60)
print("CHECKING PROJECT FILES")
print("=" * 60)

# Check data_processer.py (Note: check if you meant data_processor.py)
print("\n1. Checking data_processer.py...")
try:
    import data_processer as proven_preprocess
    
    print("✅ File loaded successfully")
    print("Available functions/classes:")
    
    # FIXED: Use the alias 'proven_preprocess' here, not 'data_processer'
    for item in dir(proven_preprocess):
        if not item.startswith("_"):
            print(f"   - {item}")
            
    # Check if file has specific functions
    if hasattr(proven_preprocess, 'preprocess_data'):
        print("\n✅ Found 'preprocess_data' function")
    if hasattr(proven_preprocess, 'transform'):
        print("✅ Found 'transform' function")
        
except Exception as e:
    print(f"❌ Error: {e}")

print("\n" + "=" * 60)
# FIXED: Updated the print statement to match the new file name
print("2. Checking elm_engine.py...")
try:
    import elm_engine as proven_elm 
    
    print("✅ File loaded successfully")
    print("Available functions/classes:")
    
    for item in dir(proven_elm):
        if not item.startswith("_"):
            print(f"   - {item}")
            
except Exception as e:
    print(f"❌ Error: {e}")

print("\n" + "=" * 60)
print("Please run: python check_imports.py")
print("And share the output with me!")