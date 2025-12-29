def clean_transaction_data(transaction_data):
#Renaming columns 
    transaction_data=transaction_data.rename(columns={'type':'transaction_type','date':'transaction_date','txn_amount':'transaction_amount'})

#Standadizing data in transaction_type column
    transaction_data['transaction_type']=transaction_data['transaction_type'].replace({'repayment':'Repayment','repay':'Repayment','rp,ment':'Repayment','repayy':'Repayment','disburse':'Disbursement'})

#Fomartting the transaction_dates
#standardize data to format yyyy-mm-dd
    transaction_data['transaction_date']=pd.to_datetime(transaction_data['transaction_date'],format='mixed')
    
    return transaction_data
