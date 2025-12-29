#==========================================
# Data Cleaning function 
#==========================================
def cleanded_data(loan_data):
    
    # Handling Null Values
    loan_data['loan_status'].fillna('Defaulted', inplace=True)

    # Renaming columns
    loan_data = loan_data.rename(columns={'ln_amnt': 'loan_amount', 'ln_trm_mnths': 'loan_term_months', 'apprvl_dte': 'approval_date', 'ln_sts': 'loan_status'})

    #Handling Nulls
    loan_data['loan_status'].fillna('Defaulted',inplace=True)    

#Loan Amount Column
    loan_data['loan_amount'].unique()
    loan_data['loan_amount'] = loan_data['loan_amount'].str.replace('k', '000', regex=True) 


#loan Interest Rate Column
    loan_data['interest_rate']=loan_data['interest_rate'].replace({'eight point three six':"8.6"})

#Loan Type Column
    loan_data['loan_type']=loan_data['loan_type'].astype('string')
    loan_data['loan_type']=loan_data['loan_type'].str.strip()
    loan_data['loan_type']=loan_data['loan_type'].replace({'mortgage':'Mortgage'})

#Loan Term Column
    loan_data['loan_term_months']=loan_data['loan_term_months'].replace({'sixty':'60'})

# Aprroval Date (Dates to be in the yyyy-mm-dd format.)
    loan_data['approval_date']=pd.to_datetime(loan_data['approval_date'], format='mixed')

#Loan Status Column.
    loan_data['loan_status']=loan_data['loan_status'].str.strip()
    loan_data['loan_status']=loan_data['loan_status'].replace({'defaulted':'Defaulted','aactive':'Active'})


#Formatting data type of the different columns.
    loan_data['loan_amount']=loan_data['loan_amount'].astype('int64')
    loan_data['interest_rate']=loan_data['interest_rate'].astype('float')
    loan_data['loan_term_months']=loan_data['loan_term_months'].astype('int64')    

 #Error logging
    error_log = []
    for index, row in loan_data.iterrows():
        if row['loan_amount'] <= 0:
            print(f"Error: Invalid loan amount {row['loan_amount']} at index {index}")
        if row['interest_rate'] < 0 or row['interest_rate'] > 100:
            print(f"Error: Invalid interest rate {row['interest_rate']} at index {index}")
        if row['loan_term_months'] <= 0:
            print(f"Error: Invalid loan term {row['loan_term_months']} at index {index}")   

    return loan_data,error_log
print(loan_data.head())
