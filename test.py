
import pandas as pd

pd.__version__
mall_data = pd.read_json('datasets\Mall_Customers.json')
mall_data.head(5)
average_income = mall_data['annual_income'].mean()

print(average_income)

print( mall_data )
# mall_data = pd.read_json('Mall_Customers.json')



