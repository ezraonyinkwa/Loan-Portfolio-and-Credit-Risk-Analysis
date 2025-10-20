## Project Overview

This project focuses on analyzing a financial institution’s loan portfolio performance and credit risk exposure using Python. It simulates a real-world scenario where a data analyst supports lending and risk management teams by identifying trends in loan defaults, repayments, and portfolio health.

The goal is to demonstrate how Python can be applied in financial analytics to drive data-informed decisions in banking, microfinance, and fintech environments.

### Objectives

- Analyze loan performance and customer repayment behavior.
  
- Identify trends in loan defaults and delinquency rates.

- Evaluate credit risk exposure using metrics like Non-Performing Loan (NPL) Ratio and Portfolio at Risk (PAR).

- Provide data-driven insights to improve portfolio quality and credit decision-making.

### Dataset Description

The dataset represents a simplified version of financial data typically available in a lending institution and includes the following key variables:

Customer_ID, Names, Gender, Age, Region, Employment_Status	Demographic and employment attributes of customers
Loan Information	Loan_ID, Loan_Amount, Interest_Rate, Loan_Type, Loan_Term, Loan_Status	Details about the loan product and repayment outcome
Repayment Data	Payment_Date, Due_Date, Outstanding_Balance, Overdue_Days	Used to calculate PAR and repayment behavior

### Tools and Technologies

- Python Core data analysis and visualization
- Pandas & NumPy	Data cleaning, wrangling, and aggregation
- Matplotlib & Seaborn	Data visualization and trend analysis
- Jupyter Notebook	Interactive data exploration and reporting

### Key Metrics

- Total Loan Portfolio	Total value of loans disbursed
  
- Default Rate	% of loans classified as defaulted
  
- NPL Ratio	Proportion of loans overdue by more than 90 days
  
- Portfolio at Risk (PAR)	Risk exposure at different overdue thresholds (30/60/90 days)
  
- Repayment Rate	Percentage of loans being repaid on schedule
  
- Average Loan Size	Average disbursed amount per customer segment

### Analysis Conducted

- Loan Status Analysis – Distribution of performing vs. defaulted loans.

- Credit Risk Segmentation – NPL and default rate across loan types and regions.

- Repayment Behavior – On-time vs. late repayment trends.

- Portfolio at Risk (PAR) Analysis – Early detection of high-risk segments.

- Customer Insights – Risk trends by gender, region, and employment type.
