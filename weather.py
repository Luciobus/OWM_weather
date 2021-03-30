from pyowm import OWM
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'

while True:
    city = input("Введите команду для выхода(exit) или введите город: ")
    if city == "exit":
        break

    owm = OWM(config.oauth, config_dict)

    try:
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(city)
        w = observation.weather
        temp = w.temperature('celsius')['temp']
        print("В городе " + city + " " + w.detailed_status + ", температура примерно равна " + str(temp) + "°C.")
        # break
    except Exception:
        print("Города " + city + " в нашей базе нет, попробуйте снова")
