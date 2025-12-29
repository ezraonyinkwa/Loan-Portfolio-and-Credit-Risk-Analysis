#Checking for region names that do not match the required names.
customer_data['region'].unique().tolist()

#NAN Values
customer_data.isna().sum()
customer_data[customer_data['gender'].isna()]

#Checking for different data types.
transaction_data.dtypes
#Checking for any unrequired transaction type
transaction_data['transaction_type'].unique().tolist()
#Checking the datasets columns names
transaction_data.columns

#Null Values.
transaction_data.isna().sum() 
#Unique names
loan_data['loan_type'].unique()
loan_data['interest_rate'].unique()
loan_data['loan_type'].unique()
loan_data['loan_term_months'].unique()
loan_data['loan_'].unique()
loan_data['approval_date'].unique()
loan_data['loan_status'].unique()
loan_data['loan_amount'].unique()

#Different Data Types
loan_data.dtypes
loan_data.isna().sum() 


