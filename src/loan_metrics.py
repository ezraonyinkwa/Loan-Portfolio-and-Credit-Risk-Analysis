(a.) Portfolio & Exposure.
 # 1.Total Amount Disbursed (2023-2025)
total_disbursed = loans_data[loans_data['transaction_type']=='Disbursement']['transaction_amount'].sum()

# 2.Exposure at Default (EAD-Balance weighted risk)
total_repaid = loans_data[(loans_data['transaction_type'] == 'Repayment') & (loans_data['loan_status'] == 'Active')]['transaction_amount'].sum()
print(f"Total Amount Disbursed From 2023-2025: KES {total_disbursed:,}")
print(f"Total Amount Repaid :KES {total_repaid:,}")

exposure_at_default =total_disbursed-total_repaid
print(f"Total Exposure At Default : KES {exposure_at_default:,}")

# Loan End Date
loans_data['approval_date'] = pd.to_datetime(loans_data['approval_date'])

loans_data['expected_repayment_date'] = (loans_data['approval_date'] +pd.to_timedelta(loans_data['loan_term_months'] *30 ,unit='D'))
mask = (loans_data['transaction_type'] == 'Repayment')&(loans_data['loan_status'] == 'Active')

loans_data['days_past_due']=(loans_data.loc[mask,'transaction_date']-loans_data['expected_repayment_date']).dt.days.clip(lower=0) #Remove loan days that were paid earlier (-ve days) to 'o'
#NAN Values are loans that 1.Either Due date is not reached yet 2.Repayment hasn't been done yet.


#3.Portfolio at Risk(PAR-30/60/90+)
par_30 = loans_data[loans_data['days_past_due'] >= 30]['transaction_amount'].sum()
par_60=loans_data[loans_data['days_past_due']>=60]['transaction_amount'].sum()
par_90=loans_data[loans_data['days_past_due']>=90]['transaction_amount'].sum()

print(f"Portfolio at Risk (PAR) - 30 days: KES {par_30:,}")
print(f"Portfolio at Risk (PAR) - 60 days: KES {par_60:,}")
print(f"Portfolio at Risk (PAR) - 90 days: KES {par_90:,}")

(b.) Credit Risk & Default Behaviour.
#4.Default Rate By Loan Type.
risk_analysis = loans_data.groupby(['loan_type'])['loan_status'].value_counts(normalize=True).unstack().fillna(0) * 100
print("Risk Analysis by Loan Type:")
print(risk_analysis)

#6. Loan performance distribution.
loan_performance = loans_data['loan_status'].value_counts(normalize=True) * 100
print("Loan Performance Distribution by (%):")
print(loan_performance)

#7 Loan-to-income ratio impact on default rates.
loan_to_income = loans_data['loan_amount'].sum() / loans_data['income'].sum()
print(f"Portfolio Wide [LTI] : {loan_to_income:.2f}")

defaulted=loans_data[loans_data['loan_status']=="Defaulted"]
lti_defaulted=defaulted['loan_amount'].sum()/defaulted['income'].sum()
print(f"LTI For Defaulted Loans : {lti_defaulted:.2f}")

(c.) Repayment Dynamics.
 #8.Repayment frequency.
total_repayments = loans_data[loans_data['loan_status']=='Closed']['transaction_amount'].sum()
total_due = loans_data[loans_data['loan_status']=='Active']['transaction_amount'].sum()
repayment_rate = (total_repayments / total_due) * 100       
print(f"Repayment Rate: {repayment_rate:.2f}%") 

(d.) Lending profile overview.
# 9. Average Loan Amount & Interest Rate.
average_loan_amount = loans_data['loan_amount'].mean()
print(f"Average Loan Amount: KES {average_loan_amount:.2f}")
average_interest_rate = loans_data['interest_rate'].mean()
print(f"Average Interest Rate: {average_interest_rate:.2f}%")

(e.) Concentration Risk - Exposure by customer segments and loan types.
# 10. Region Risk Concentration - Exposure by geographical regions.
#Total Exposure by Loans 
exposure_by_region = loans_data.groupby('region')['loan_amount'].sum()

# Defaulted exposure by region
defaulted_exposure_by_region = loans_data[loans_data['loan_status']=='Defaulted'].groupby('region')['loan_amount'].sum()

print(f"Total Exposure By Region KES")
print(exposure_by_region)
print(f"Total Defaulted Exposure By Region KES  {defaulted_exposure_by_region}")




