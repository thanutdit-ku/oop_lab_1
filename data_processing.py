import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def filter(condition, dict_list):
    temps= []
    for item in dict_list:
        if condition(item, temps):
            temps.append(item)
    return temps


def aggregate(aggregation_key, aggregation_function, dict_list):
    tmp = [float(item[aggregation_key]) for item in dict_list]
    return aggregation_function(tmp)

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)
print()
# Print the average temperature of all the cities
print("The average temperature of all the cities:")
avg_temp = aggregate("temperature", lambda x: sum(x)/len(x), cities)
print(avg_temp)
print()

# Print all cities in Germany

print("All cities in Germany:")
germany_cities = filter(lambda city, _: city["country"] == "Germany", cities)
print([c["city"] for c in germany_cities])
print()

# Print all cities in Spain with a temperature above 12°C

print("All cities in Spain with a temperature above 12°C:")
spain_hot = filter(lambda city, _: city["country"] == "Spain" and float(city["temperature"]) > 12, cities)
print([c["city"] for c in spain_hot])
print()

# Count the number of unique countries

print("Number of unique countries:")
unique_countries = filter(lambda city, filtered: city["country"] not in [f["country"] for f in filtered], cities)
print(len(unique_countries))
print()

# Print the average temperature for all the cities in Germany

print("Average temperature for all the cities in Germany:")
germany_temps = filter(lambda city, _: city["country"] == "Germany", cities)
avg_germany = aggregate("temperature", lambda x: sum(x)/len(x), germany_temps)
print(avg_germany)
print()

# Print the max temperature for all the cities in Italy
print("Max temperature for all the cities in Italy:")
italy_temps = filter(lambda city, _: city["country"] == "Italy", cities)
max_italy = aggregate("temperature", max, italy_temps)
print(max_italy)
print()
