import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

''' Load oil data'''
df_oil = pd.read_csv('Oil.csv')
df_oil.columns = ['Date_oil', 'Price_oil']
print(df_oil)

''' Load gold data'''
gold_price = pd.ExcelFile('Gold.xlsx')
df_gold = gold_price.parse("Daily", skiprows=8, usecols=range(3, 5))
df_gold.columns = ['Date_gold', 'Price_gold']
print(df_gold)

''' Convert to pandas datetime '''
df_oil['Date_oil'] = pd.to_datetime(df_oil['Date_oil'], errors='coerce')
df_oil = df_oil.resample('M', on='Date_oil').mean()
df_oil = df_oil.reset_index()
print(df_oil)

df_gold['Date_gold'] = pd.to_datetime(df_gold['Date_gold'], errors='coerce')
df_gold = df_gold.resample('M', on='Date_gold').mean()
df_gold = df_gold.reset_index()
print(df_gold)

'''Merge cells'''
final_df = pd.merge(df_oil.assign(grouper_date=df_oil['Date_oil'].dt.to_period('M')),
                    df_gold.assign(grouper_date=df_gold['Date_gold'].dt.to_period('M')),
                    how='left', on='grouper_date')

print(final_df)


''' Visualize the results '''
''' remove rows belong to 1987 '''
final_df = final_df.iloc[8:]
# final_df = final_df.drop(final_df.index[:3], inplace=True)
print(final_df)

''' show results '''
plt.plot(final_df['Date_oil'], final_df['Price_gold'], label='Gold price')
plt.plot(final_df['Date_oil'], final_df['Price_oil'], label='Oil price')
plt.legend()
plt.grid(True)
plt.xlabel('Years')
plt.ylabel('Price ($)')
plt.title('Oil and Gold price comparison')


plt.show()
