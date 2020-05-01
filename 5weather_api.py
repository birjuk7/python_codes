import requests
baseUrl = 'http://api.openweathermap.org/data/2.5/forecast'
parameters ={'APPID':'1ce0ff78703bb61b77ebf78e8f3e252b','q':'Seattle,US'}
response =requests.get(baseUrl, params=parameters)
print(response.content)