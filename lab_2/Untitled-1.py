#%%
import numpy as np
import pandas as pd
pd.set_option('display.max.columns', 100)
# to draw pictures in jupyter notebook
# matplotlib inline 
import matplotlib.pyplot as plt
import seaborn as sns

#%%
data = pd.read_csv('C:/jupWork2/data/adult.data.csv' )
data.head()
#%%
#1. How many men and women (sex feature) are represented in this dataset?
data['sex'].value_counts()

#%%
#2. What is the average age (age feature) of women?
data_fem = data[data['sex']==' Female']
data_fem.head()
data_fem['age'].mean()
#%%
#3. What is the percentage of German citizens (native-country feature)? 
((data['native-country']==' Germany').sum()/data['age'].count()*100)

#%%
#4-5. What are the mean and standard deviation of age for those who earn more than 50K per year (salary feature) and those who earn less than 50K per year?
ages1 = data.loc[data['salary'] == ' >50K', 'age']
ages2 = data.loc[data['salary'] == ' <=50K', 'age']
print("rich: {0} +- {1} years, \npoor: {2} +- {3} years.".format(
    round(ages1.mean()), round(ages1.std(), 1),
    round(ages2.mean()), round(ages2.std(), 1)))
#%%
#6. Is it true that people who earn more than 50K have at least high school education? (education – Bachelors, Prof-school, Assoc-acdm, Assoc-voc, Masters or Doctorate feature)
#data.loc[data['salary'] == ' >50K', 'education'].unique()
data.loc[(data['salary'] == ' >50K') & 
(~data['education'].isin([' Bachelors', ' Prof-school', ' Assoc-acdm',
 ' Assoc-voc', ' Masters',' Doctorate feature']))]
#%%
#7. Display age statistics for each race (race feature) and each gender (sex feature). Use groupby() and describe(). Find the maximum age of men of Amer-Indian-Eskimo race.
for (race, sex), sub_df in data.groupby(['race', 'sex']):
    print("Race: {0}, sex: {1}".format(race, sex))
    print(sub_df['age'].describe())

#%%
#8. Among whom the proportion of those who earn a lot(>50K) is more: among married or single men (marital-status feature)? Consider married those who have a marital-status starting with Married (Married-civ-spouse, Married-spouse-absent or Married-AF-spouse), the rest are considered bachelors.
data.loc[(data['sex'] == ' Male') &
     (data['marital-status'].isin([' Never-married', ' Separated', ' Divorced',
      ' Widowed'])), 'salary'].value_counts()
#%%
data.loc[(data['sex'] == ' Male') &
     (data['marital-status'].str.startswith(' Married')), 'salary'].value_counts()
#%%
data['marital-status'].value_counts()

#%%
#9. What is the maximum number of hours a person works per week (hours-per-week feature)? How many people work such a number of hours and what is the percentage of those who earn a lot among them?
maxh = data['hours-per-week'].max()
num = data[data['hours-per-week'] == maxh].shape[0]
pers = float(data[(data['hours-per-week'] == maxh)
                 & (data['salary'] == ' >50K')].shape[0]) / num
print("There are {a} men with {b} hpw and there is a percentage of rich among them {c}%".format(a=num,b=maxh,c=int(100 * pers)))  
#%%
#10. Count the average time of work (hours-per-week) those who earning a little and a lot (salary) for each country (native-country).
for (country, salary), sub_df in data.groupby(['native-country', 'salary']):
    print(country, salary, round(sub_df['hours-per-week'].mean(), 2))   

