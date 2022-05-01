import pandas as pd

import acquisition1 as aq

preciotungsteno=aq.tungsten_timeseries
preciotungsteno.drop(['success','timeseries', 'start_date','end_date', 'base'], axis=1, inplace=True)
preciotungsteno.index.name='Date'
preciotungsteno=preciotungsteno.rates.apply(pd.Series)
preciotungsteno.drop('USD', axis=1, inplace=True)
preciotungsteno['Tungsten Price']= (1/preciotungsteno['TUNGSTEN'])*32151
preciotungsteno.drop('TUNGSTEN',axis=1, inplace=True)
preciotungsteno.to_csv('tungsten_daily_price.csv')