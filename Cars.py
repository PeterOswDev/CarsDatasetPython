import pandas as pd
car = pd.read_csv(r"E:\2. Cars Data1.csv")
print(car.head())
print(car.shape)
print(car.isnull().sum())
print(car['Cylinders'].fillna(car['Cylinders'].mean(), inplace = True))
print(car)
print(car.head(2))
print(car['Make'].value_counts())
print(car[car['Origin'].isin(['Asia', 'Europe'])])
print(car[car['Weight'] > 4000])#Remove all the records, where Wight is above 4000
print(car[~(car['Weight'] > 4000)])
print(428-103)
print(car.head(2))

#print(car['MPG_City'] = car['MPG_City'].apply(lambda x:x+3))
