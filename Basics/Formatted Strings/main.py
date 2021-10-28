temprature = input('Enter temperature:')
weather = 'sunny'
humidity = 54
feels_like = 'cold'

if float(temprature) > 20:
    feels_like = 'warm'

summary = f'It\'s {weather}.\nTemperature: +{temprature}C. Humidity: {humidity}%. \nFeels like it\'s {feels_like}.'

print(summary)
