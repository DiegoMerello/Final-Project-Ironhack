import requests
import pandas as pd
from datetime import datetime, timedelta

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
var=today()

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
        access_key = 'm29rswz853qlppfxspn1tprffref065jsc4ihybl7h7tzf7yo04yrvw34wqp'
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
tungsten_timeseries

metals_prices= pd.DataFrame.from_dict(results[0])
metals_prices