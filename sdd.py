import pandas as pd
import sqlalchemy as db

# Function to extract domain from email
def extract_domain(email):
    if '@' in email:
        domain = email.split('@')[-1].lower()
        if '.' in domain:
            return domain.split('.')[0]
    return ""

# Read CSV file into pandas DataFrame
lead_data = pd.read_csv(r"C:\Users\Admin\Desktop\PANDAS\lead.csv")

# Convert Lead_phoneno to string
lead_data["Lead_phoneno"] = lead_data["Lead_phoneno"].astype(str)

# Establish connection to Oracle database
engine = db.create_engine('oracle+cx_oracle://team26_roopa:team26_roopa@orcl-aws.c8sefhobaih4.ap-south-1.rds.amazonaws.com:1521/orcl')

# Save lead_data to Oracle table
lead_data.to_sql('lead_data2', engine, if_exists='replace', index=False)

# Extract email domain and create Lead_emailDomain column
lead_data['Lead_emailDomain'] = lead_data['Lead_emailId'].apply(lambda x: extract_domain(x))

# Separate data into accepted (gmail) and rejected (yahoo) datasets
accepted_data = lead_data[lead_data['Lead_emailDomain'] == 'gmail']
rejected_data = lead_data[lead_data['Lead_emailDomain'] == 'yahoo']

# Save accepted_data, rejected_data, and other data to Oracle tables
error_data = lead_data[lead_data["Lead_phoneno"].str.len() != 10]
valid_data = lead_data[lead_data["Lead_phoneno"].str.len() == 10]
duplicate_data = lead_data[lead_data['Lead_phoneno'].duplicated(keep=False)]

error_data.to_sql('error_table', engine, if_exists='replace', index=False)
valid_data.to_sql('valid_table', engine, if_exists='replace', index=False)
duplicate_data.to_sql('duplicate_rows', engine, if_exists='replace', index=False)
