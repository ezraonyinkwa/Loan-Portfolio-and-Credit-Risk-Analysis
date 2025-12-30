Part 2:Exploratory Data Analysis (EDA) and Visualization

# 1. Loan distribution by type and City.
plt.figure(figsize=(10,6))
sns.countplot(data=loans_data, x='region', hue='loan_type')
plt.title('Loan Distribution by Type and Region')
plt.xlabel('Region') 
plt.ylabel('Number of Loans')
plt.show()

# 2. Calculate default rate (fraction of loans that are 'Defaulted') per loan type
default_rate = (
    loans_data
    .assign(is_default = loans_data['loan_status'] == 'Defaulted')
    .groupby('loan_type')['is_default']
    .mean()
    .reset_index(name='default_rate')
)

# convert to percentage for better readability
default_rate['default_rate'] = default_rate['default_rate'] * 100

plt.figure(figsize=(10,6))
sns.barplot(data=default_rate, x='loan_type', y='default_rate')
plt.title('Default Rate by Loan Product Type')
plt.xlabel('Loan Type')
plt.ylabel('Default Rate (%)')
plt.ylim(0, default_rate['default_rate'].max() * 1.1)
plt.show()

# 3. Correlation between loan amounts and customer credit scores/default likelihood.
# Ensure numeric
loans_data['loan_amount'] = pd.to_numeric(loans_data['loan_amount'], errors='coerce')
loans_data['credit_score'] = pd.to_numeric(loans_data['credit_score'], errors='coerce')

# Correlation
loan_credit_corr = loans_data['loan_amount'].corr(loans_data['credit_score'])

print(f"Correlation (Loan Amount vs Credit Score): {loan_credit_corr:.2f}")

# Create default flag
loans_data['default_flag'] = (loans_data['loan_status'] == 'Defaulted').astype(int)

# Correlation
loan_default_corr = loans_data['loan_amount'].corr(loans_data['default_flag'])

print(f"Correlation (Loan Amount vs Default Likelihood): {loan_default_corr:.2f}")

# Create default flag
loans_data['default_flag'] = (loans_data['loan_status'] == 'Defaulted').astype(int)

# Select numeric columns
corr_data = loans_data[
    ['loan_amount', 'interest_rate', 'loan_term_months', 'income', 'credit_score', 'default_flag']
].dropna()

# Compute correlation matrix
corr_matrix = corr_data.corr()

# Heatmap
plt.figure(figsize=(10,10))
sns.heatmap(corr_matrix,annot=True,cmap='coolwarm')
