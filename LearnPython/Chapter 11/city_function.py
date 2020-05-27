#11-1. City, Country:
def city_country_name(city, country, population=0):
	if population:
		formatted = f"{city.title()}, {country.title()} - population {population}" 
	else:
	 	formatted = f"{city.title()}, {country.title()}"
	return formatted

