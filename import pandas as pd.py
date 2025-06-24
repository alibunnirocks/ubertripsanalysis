import pandas as pd
import matplotlib.pyplot as plt
uber_df= pd.read_csv("C:/Users/alira/.vscode/uber-raw-data-sep14.csv")
#Converts column from string to datetime (data type for dates)
uber_df['Date/Time']=pd.to_datetime(uber_df['Date/Time'])
#Creates a new column called 'day' by taking the 'date/time' column and separating day
uber_df['Day'] = uber_df['Date/Time'].apply(lambda x: x.day)

uber_df['Hour'] = uber_df['Date/Time'].apply(lambda x: x.hour)
uber_df['Weekday'] = uber_df['Date/Time'].apply(lambda x: x.weekday())
#Density of rides per day in a month
'''fig,ax = plt.subplots(figsize=(12,6))
plt.hist(uber_df.Day, width=0.6, bins=30, color='pink')
plt.title('Density of Rides per Day')
plt.xlabel('Day')
plt.ylabel('Number of Rides')
plt.show()'''
#Density of Rides per weekday
'''
fig,ax = plt.subplots(figsize=(12,6))
plt.hist(uber_df.Weekday, width=0.7, bins=7, range=(0,6.5), color='purple')
plt.title('Density of Rides per Weekday')
plt.xlabel('Weekday')
plt.ylabel('Density of Rides')
plt.show()'''
#Density of Rides per Location
fig,ax = plt.subplots(figsize = (12,6))
x= uber_df.Lon
y= uber_df.Lat
plt.scatter(x, y, color= "purple")
plt.title("Density of trips per Hour", fontsize=16)
plt.xlabel("Hour", fontsize=14)
plt.ylabel("Density of rides", fontsize=14)
plt.show()