import pandas as pd
import bs4
import requests
import csv

def main():
    url = "https://www.mnstate.edu/information-technology/email/"
    r = requests.get(url) #returns the HTML of the page, can be done through urlopen as well
    soup = bs4.BeautifulSoup(r.content)
    containers = soup.findAll("div",{"class":"elementor-widget-wrap"})
    scrape(containers)

def scrape(containers):
    result = []
    with open('scraped_data.csv', 'w', newline='',encoding="utf-8") as fp:
        a = csv.writer(fp, delimiter=',')
        a.writerows([['title','location','subtitle','rates','additionals','availability']])


        for container in containers:
            title = container.findAll('h5',{"class":"elementor-heading-title elementor-size-default"})
            location = container.find_all('h6',{"class":"elementor-heading-title elementor-size-default"})
            subtitle = container.find_all('h6',{"class":"elementor-heading-title elementor-size-default"})
            rates = container.find_all('div',{"class":"elementor-text-editor elementor-clearfix"})
            additionals = container.find_all('div',{"class":"elementor-text-editor elementor-clearfix"})
            availability = container.find_all('span',{"class":"elementor-alert-description"})
        
            try:
                title = title[0].text.strip()
            except:
                title = ''

            try:    
                location = location[0].text.strip() if len(location)>0 else ''
            except:
                location = ''

            try: 
                subtitle = subtitle[1].text.strip()
            except:
                subtitle='' 

            for rate in rates:
                rate = rate.find_all('p')   

            for additional in additionals:
                additional = additional.find_all('p')   

            try: 
                availability = availability[0].text.strip()
            except:
                availability=''

            if title!='':
                data = [[title,location, subtitle, rate, additional, availability]]
                a.writerows(data)
    print('Please check scraped_data.csv')

if __name__ == "__main__":
    main()

