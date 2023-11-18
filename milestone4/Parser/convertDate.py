import pandas as pd

# Load the CSV file with the original date format
df = pd.read_csv("output/test-entities.csv")

def convert_date_format(date_str):
    # Check if the date_str is a non-empty string
    if isinstance(date_str, str) and len(date_str) > 0:
        # Split the date string by "-"
        parts = date_str.split('-')
        
        # Define month names
        month_names = {
            'JAN': '01', 'FEB': '02', 'MAR': '03',
            'APR': '04', 'MAY': '05', 'JUN': '06',
            'JUL': '07', 'AUG': '08', 'SEP': '09',
            'OCT': '10', 'NOV': '11', 'DEC': '12'
        }
        
        # Check if the parts have the expected format
        if len(parts) == 3:
            # Convert month abbreviation to a number
            month = month_names.get(parts[1], '00')
            
            # Construct the ISO 8601 date format
            iso_date = f"{parts[2]}-{month}-{parts[0]}"
            
            return iso_date

    # Return an empty string for missing or empty date values
    return ""

# Apply the date format conversion to the 'incorporation_date', 'inactivation_date', and 'struck_off_date' columns
df['incorporation_date'] = df['incorporation_date'].apply(convert_date_format)
df['inactivation_date'] = df['inactivation_date'].apply(convert_date_format)
df['struck_off_date'] = df['struck_off_date'].apply(convert_date_format)

# Save the modified DataFrame back to a CSV file
df.to_csv("test-entities-updated.csv", index=False)