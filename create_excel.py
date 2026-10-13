# ==============================================================================
# Course: SY BCom FinTech | Subject: AI ML 1 - CCA2
# Admin Name: [Aryan]
# Admin PRN: [1302250491]
# File 2: Generates 'ml_input_data.xlsx'
# ==============================================================================

import pandas as pd

# Creating the dataset with 'Text' and 'Expected_Sentiment' 
# matching the exact column names the admin script is looking for.
dataset = {
    'Text': [
        'I absolutely love this new investment app!',
        'The UI is very confusing and frustrating to use.',
        'This is an amazing and incredible platform.',
        'The transaction failed, very bad experience.',
        'The app works fine, no major issues.'
    ],
    'Expected_Sentiment': ['Positive', 'Negative', 'Positive', 'Negative', 'Neutral']
}

df = pd.DataFrame(dataset)

# Save to Excel format
output_filename = "input_data.xlsx"
df.to_excel(output_filename, index=False)
print(f"Collaborator script finished: '{output_filename}' created successfully!")
