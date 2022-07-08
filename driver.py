from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
import os
import sys

app_path=os.path.dirname(sys.executable)

now=datetime.now()
# MMDDYY
day_month_year=now.strftime("%d%m%Y")

website = 'https://www.thesun.co.uk/sport/football/'
path = 'E:\Trash\chromedriver'  # introduce path here

# headless-mode
options=Options()
options.headless=True

# Creating the driver
driver_service = Service(executable_path=path)
driver = webdriver.Chrome(service=driver_service, options=options)
driver.get(website)

# Finding Elements
containers = driver.find_elements(by='xpath', value='//div[@class="teaser__copy-container"]')

titles = []
subtitles = []
links = []
for container in containers:
    title = container.find_element(by='xpath', value='./a/h2').text
    subtitle = container.find_element(by='xpath', value='./a/p').text
    link = container.find_element(by='xpath', value='./a').get_attribute('href')
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

# Exporting data to a CSV file
my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}
df_headlines = pd.DataFrame(my_dict)

file_name=f'headline{day_month_year}.csv'
final_destination=os.path.join(app_path, file_name)

df_headlines.to_csv(final_destination)

driver.quit()