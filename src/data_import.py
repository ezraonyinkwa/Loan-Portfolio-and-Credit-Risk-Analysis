#Importing  the loans data
loan_data = pd.read_csv(r"C:\Users\Ezra\Downloads\loans_data.csv")
print("data imported successfully with : {} rows and {} columns".format(loan_data.shape[0],loan_data.shape[1]))

#Importing the transactions dataset
transaction_data=pd.read_csv(r"C:\Users\Ezra\Downloads\transactions_data.csv")
print("data imported successfully with : {} rows and {} columns".format(transaction_data.shape[0],transaction_data.shape[1]))

#Importing the Customers Dataset
customer_data = pd.read_csv(r"C:\Users\Ezra\Downloads\customer_data.csv")
print("data imported successfully with : {} rows and {} columns".format(loan_data.shape[0],loan_data.shape[1]))
