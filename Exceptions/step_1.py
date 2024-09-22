# a = 3
# b = '2'
# c = a ** b
# print(c)
#
# d = c ** 2
# print(d)


def get_weather_for(city):
    if city != "Moscow":
        raise ValueError("Invalid city")
    return {
        "temp": 12,
        "humidity": 50,
        "rain_chance": 0,
    }


def rain_tomorrow(city):
    print('Will it rain tomorrow?', city)
    try:
        weather = get_weather_for(city)
        return weather['rain_chance'] > 50
    except ValueError:
        return


print(rain_tomorrow("Moscow"))
print(rain_tomorrow("Sochi"))
print(rain_tomorrow("Perm"))