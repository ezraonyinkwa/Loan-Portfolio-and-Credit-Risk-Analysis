#Checking for Uniqueness of IDs across the three datasets
assert customer_data["customer_id"].is_unique
assert loan_data["loan_id"].is_unique
assert transaction_data["transaction_id"].is_unique

print("All IDs are unique")

#Merging customer and loan datasets
merged_data=pd.merge(loan_data,customer_data,on='customer_id',how='left')

#Aggregate transactions data at loan_id and transaction_type level
txn_aggregate=transaction_data.groupby(['loan_id','transaction_type']).agg({'transaction_amount':'sum','transaction_id':'count','transaction_date':'max'}).reset_index()


#Meging the data without duplicates 
loans_data=pd.merge(merged_data,txn_aggregate,on='loan_id',how='left')


#Checking for null values in the merged data
print(loans_data.shape)
print(loans_data.isnull().mean().sort_values(ascending=False).head(10))
