from numpy import add
import pandas as pd
from pandas import ExcelWriter

data = pd.read_csv('scraped_data.csv')
additionals = data['additionals']
new_additional=[]
for additional in additionals:
    start = additional.find('>')
    end = additional.find('</p>')
    additional=additional[start+1:end]
    additional= additional.replace('<br/>',', ')
    additional= additional.replace('<br/>',', ')
    additional= additional.replace('<br>',', ')
    additional=additional.replace('&amp;', '&')    
    additional = additional.replace('<b>Rates</b>','')
    additional = additional.replace('<strong>','')
    additional = additional.replace('</strong>','')
    new_additional.append(additional[2:])


rates = data['rates']
new_rates=[]
for rate in rates:
    rate = rate.replace('<p style="font-size: 15px;">','')
    rate= rate.replace('<br/>',', ')
    rate= rate.replace(',','')
    rate= rate.replace('[','')
    rate= rate.replace(']','')
    rate= rate.replace('&amp;', '&')
    rate= rate.replace('</p>', '&')
    rate= rate.replace('*P.H. – Per Head&', '&')
    rate= rate.replace('<span style="font-size: 15px; letter-spacing: -0.27px; text-align: center;">*P.H. – Per Head</span>&', '&')
    new_rates.append(rate)

data['additionals'] = pd.Series(new_additional)
data['rates'] = pd.Series(new_rates)

writer = ExcelWriter('Final.xlsx')
data.to_excel(writer,'Sheet1')
writer.save()
