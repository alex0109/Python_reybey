from pyowm import OWM

city = input('Какой город вас интересует: ') 

owm = OWM('4857a9eace853f6f5bb32126c9a6b7bf')
mgr = owm.weather_manager()

observation = mgr.weather_at_place(city)
w = observation.weather
temparature = w.temperature('celsius')['temp']


print("В городе " +  city + " сейчас " + str(temparature) + " C")
input()