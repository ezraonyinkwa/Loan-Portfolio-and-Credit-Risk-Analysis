# Data clean up function for the customers data
def clean_customer_data(customer_data):
    
    #Handling Null Values
    customer_data['gender'].fillna('Other',inplace=True)

    
    #Standardizing the customer data column
# Name should be consistent with no special characters and leading/trailing spaces
    customer_data['name']=customer_data['name'].str.strip()
    customer_data['name']=customer_data['name'].str.replace('_',' ',regex=True).str.title()

# Age Column should be in integer format
    customer_data['age']=customer_data['age'].replace({'twenty five':'25'})
# Gender Column should have consistent values either Male, Female, Other
    customer_data['gender']=customer_data['gender'].replace({'m':'Male','mael':'Male','female':'Female','femae':'Female','f':'Female','F':'Female'})

# Employment status should have unemployed,student,employed,self-employed and No Nulls
    customer_data['employment_status']=customer_data['employment_status'].str.strip()
    customer_data['employment_status']=customer_data['employment_status'].replace({'student':'Student','employed':'Employed','selfemployed':'Self-employed','selfemployed-':'Self-employed',
                                                                               'Self-Employed':'Self-employed','une-mployed':'Unemployed','Une-mployed':'Unemployed'})
                                                                              

# Income column should be in integer format and no null values
    customer_data['income']=customer_data['income'].str.replace('k','000',regex=True)

# Credit Score column should be in integer format and no null values
    customer_data['credit_score']=customer_data['credit_score'].str.replace(r"[A-Za-z]",'',regex=True)

# Region column should have consistent values
    customer_data['region']=customer_data['region'].str.strip() 
    customer_data['region']=customer_data['region'].replace({'nrb':'Nairobi','nrbi':'Nairobi','Ksm':'Kisumu','ksm':'Kisumu','kisumu':'Kisumu','naks':'Nakuru','naks]':'Nakuru',
                                                         'thika':'Thika','Coast':'Mombasa','coast':'Mombasa','eldy':'Eldoret','nakuru':'Nakuru'})

    return customer_data
