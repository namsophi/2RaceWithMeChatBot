from countryinfo import CountryInfo
from scripts.utils import text_to_speech


def get_location_data(city, country):
    country_info = CountryInfo(country)
    capital = country_info.capital()
    bordering_countries = len(country_info.borders())
    country_size = country_info.area()
    if bordering_countries == 0:
        response = f"Welcome to {city}, a city in {country}! " \
                   f"{country} is a country that is {country_size} " \
                   f"square kilometers big. {capital} is the capital city of " \
                   f"{country}, and there are no" \
                   f"countries bordering {country}. In this video we will explore"
    elif bordering_countries == 1:
        response = f"Welcome to {city}, a city in {country}! " \
                   f"{country} is a country that is {country_size} " \
                   f"square kilometers big. {capital} is the capital city of " \
                   f"{country}, and there is one" \
                   f"country bordering {country}. In this video we will explore"
    else:
        response = f"Welcome to {city}, a city in {country}! " \
                   f"{country} is a country that is {country_size} " \
                   f"square kilometers big. {capital} is the capital city of " \
                   f"{country}, and there are {bordering_countries}" \
                   f"countries bordering {country}. In this video we will explore"
    text_to_speech(response)
    return response
