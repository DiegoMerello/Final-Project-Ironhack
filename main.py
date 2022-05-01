import requests
import pandas as pd
from pandas import json_normalize
import json
from datetime import datetime, timedelta
import plotly.express as px

def today():
    dia=datetime.today().weekday()
    if dia == 5:
        d = datetime.today() - timedelta(days=1)
        date_time_str = d.strftime("%Y-%m-%d")
        return (date_time_str)
    
    elif dia == 6:
        d = datetime.today() - timedelta(days=2)
        date_time_str = d.strftime("%Y-%m-%d")
        return (date_time_str)
    
    else:
        d=datetime.today()
        date_time_str = d.strftime("%Y-%m-%d")
        print(date_time_str)
        return (date_time_str)
var = today()
var

def daily_prices_api2(endpoint, end_date):
    if endpoint == "latest":
        
        base_currency = 'USD'
        symbols = 'ALU,TUNGSTEN,TIN,IRON,XCU'  
        #endpoint = 'latest'
        access_key = '7myuqdqx0i07a7n2n0w24au06vypf8v92ubqo3v6xqja3j76p0eadav2dkqk'
        resp5 = requests.get(
            'https://www.metals-api.com/api/'+endpoint+'?access_key='+access_key+'&base='+base_currency+'&symbols='+symbols)
        
        return (resp5.json())
    else:
        base_currency = 'USD'
        symbol = 'TUNGSTEN'
        access_key = '7myuqdqx0i07a7n2n0w24au06vypf8v92ubqo3v6xqja3j76p0eadav2dkqk'
        endpoint = 'timeseries'
        start_date = '2022-02-04'
        #end_date = '2022-04-27'
        resp=requests.get(
            'https://www.metals-api.com/api/'+endpoint+'?access_key='+access_key+ '&start_date=' + start_date +'& end_date='+end_date+'&base='+base_currency+'&symbols='+symbol)

        return (resp.json())

end_list = ["latest", "timeseries"]
results =[]
for end in end_list:
    results.append(daily_prices_api2(end, var))

tungsten_timeseries= pd.DataFrame.from_dict(results[1])
tungsten1= tungsten_timeseries.drop(['success','timeseries', 'start_date','end_date', 'base'], axis=1, inplace=True)
tungsten1.index.name='Date'

tungsten2=tungsten1.rates.apply(pd.Series)
tungsten3 = tungsten2.drop('USD', axis=1, inplace=True)
tungsten3['Tungsten Price']= (1/tungsten3['TUNGSTEN'])*32151
tungstenfinal= tungsten3.drop('TUNGSTEN',axis=1, inplace=True)
    
metals_prices= pd.DataFrame.from_dict(results[0])
metals_prices.index.name='Metal'
metals1 = metals_prices.drop(['success', 'timestamp', 'base'], axis=1, inplace=True)
tonne_troy=32151
metals1.rename(columns={'rates':'Price','date':'Date'}) 
metals1['USD per tonne']=((1/metals1.rates)*tonne_troy)
metals2=metals1.rename(columns={'rates':'Price','date':'Date'})
metalsfinal = metals2.drop(['Price','unit'], axis=1, inplace=True)
    
fig= px.line(tungstenfinal, x='Date', y='Tungsten Price',
             title='Tungsten price evolution', markers=True)
fig['data'][0]['line']['color']="#00ff00"
fig.show()