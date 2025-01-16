import pandas
housing_data = pandas.read_csv('./housing_data.csv')
print(housing_data)
print('---------------')
print(housing_data.shape) # (1460, 81)
print('---------------')
print(housing_data.info())