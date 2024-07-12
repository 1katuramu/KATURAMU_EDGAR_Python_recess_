# Libraries for web scraping
# Request, BeautifulSoup, lxml, Scrapy, Selenium
# API keys 
# Exercises, openweathermap.org 

# Step 1
# Import libraries
import requests
from bs4 import BeautifulSoup
import csv
import json

# Step 2 Fetch the web pages
url ='http://ryeko.org'
response = requests.get(url)
html_content = response.text
api_key = ''

# Step 3: Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Step 4: Find the specific data
data = []
for item in soup.find_all('a'):
    title = item.text.strip()
    link = item.get('href')
    data.append({'title':title, 'link': link})

# Step 5: Save the data to a csv file
csv_file = 'scrapped_data.csv'
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["title", "link"])  # header row
    for item in data:
        writer.writerow([item["title"], item["link"]])

# Step 6: Save the data to json file
json_file = 'scrapped_data.json'
with open(json_file, 'w') as file:
    json.dump(data, file)

print(f'Data saved successfully to {csv_file} and {json_file} format!')

# Exercise 1 Scrape data from the https://openweathermap.org
# Current weatherdata

import requests
import json

API_key = "629dc4108fd8d3fda848f602b160c334"
city_name = "Kampala"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}"
response = requests.get(url)
data = response.json()

current_weather_data = []

# Extract city names
city_name = data['name']

# Extract temperature values
temperature_value = data['main']['temp']

# Extract weather descriptions
weather_description = data['weather'][0]['description']

# Combine data into a list of dictionaries
current_weather_data.append({
    'city_name': city_name,
    'temperature': temperature_value,
    'weather_description': weather_description
})

# Print the extracted data
for weather_data in current_weather_data:
    print(f"City: {weather_data['city_name']}")
    print(f"Temperature: {weather_data['temperature']}")
    print(f"Weather Description: {weather_data['weather_description']}")
    print()