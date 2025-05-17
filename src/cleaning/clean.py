import pandas as pd

df = pd.read_csv('data/raw/Workforce and Wage by Location.csv')

clean_df = df.drop(['Temp', 'ID PUMA', 'Year', 'Workforce Status', 'ID Workforce Status', 'Slug PUMA'], 
                   axis=1)

clean_df = clean_df.rename(columns={'ID Year': 'Year'})


clean_df['Average Wage'] = clean_df['Average Wage'].round(2)
clean_df['Growth'] = clean_df['Growth'].round(2)


clean_df['Growth'] = clean_df['Growth'].fillna('N/A')


clean_df.to_csv('data/processed/cleaned_avg_wage_data.csv', index=False)


print(clean_df.head())