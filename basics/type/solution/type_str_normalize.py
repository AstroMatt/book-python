"""
>>> result
'Jana Twardowskiego III'
"""

DATA = 'UL. jana \tTWArdoWskIEGO 3'

result = (
    DATA.upper()                # Convert to common format
        .replace('\t', '')      # Remove unwanted whitespaces
        .replace('.', '')       # Remove unwanted special characters
        .replace('UL', '')      # Remove unwanted text
        .replace('3', 'III')    # Substitute text
        .title()                # Formatting
        .replace('Iii', 'III')  # Clean-up
        .strip()
)
