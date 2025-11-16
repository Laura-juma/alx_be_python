print('Welcome to weather advice programme:)')
weather = input('What is the weather like today? [sunny, rainy, cloudy] ')
weather=weather.lower()

if weather == 'sunny':
  print('Wear a t-shirt and sunglasses.')
elif weather == 'rainy':
  print("Don't forget your umbrella and a raincoat.")
elif weather == 'cloudy':
  print("Make sure to wear a warm coat and a scarf.")
else:
  print("Sorry, I don't have recommendations for this weather.")



