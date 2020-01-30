import pandas as pd
df = pd.DataFrame()
print(df)

data = [1,2,3,4,5]
df = pd.DataFrame(data)
print('\nSetting values to dataframe')
print(df)

print('\nSetting name and age in dataframe')
data = [['Nishant',10],['Kartik',12],['Harsh',15]]
df = pd.DataFrame(data,columns=['Name','Age'])
print(df)

print('\nSetting name and age with float values')
df = pd.DataFrame(data,columns=['Name','Age'],dtype=float)
print(df)

print('\nReading csv file')
dfTitanic = pd.read_csv('/Users/exam/Documents/Nishant/ML/titanic-csv.csv')
print(dfTitanic.head(10))
print(dfTitanic.shape)

print('\nAdding columns')
dataframe = pd.DataFrame()
dataframe['Name'] = ['Nishant','Harsh','Hardik','Pavan']
dataframe['Age'] = [30,23,22,18]
dataframe['Faculty'] = ['yes','no','no','yes']
dataframe['Gender'] = ['M','M','M','F']

print(dataframe)
print(dataframe.shape)
print(dataframe.describe())

print('\nConcatinating dataframes')
left = pd.DataFrame({
        'id':[1,2,3],
        'name':['Nishant','Harsh','Hardik'],
        'subject':['sub1','sub2','sub3']})
right = pd.DataFrame({
        'id':[4,5,6],
        'name':['Pavan','Dharmik','Kartik'],
        'subject':['sub4','sub5','sub6']})
print('\nLeft')
print(left)
print('\nRight')
print(right)
print('\nConcatinated')
print(pd.concat([left,right]))

print('Dataset')
url = 'titanic-csv.csv'
dfTitanic = pd.read_csv(url)
print(dfTitanic.head(5))




























