import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)

# # Print the average temperature of all the cities
# print("The average temperature of all the cities:")
# temps = []
# for city in cities:
#     temps.append(float(city['temperature']))
# print(sum(temps)/len(temps))
# print()

# # Print the average temperature of all the cities
# print("The average temperature of all the cities:")
# temps = [float(city['temperature']) for city in cities]
# print(sum(temps)/len(temps))
# print()

# # Print all cities in Germany

# print("All cities in Germany:")
# temps = []
# for city in cities:
#     if city['country'] == 'Germany':
#         temps.append(city)
# print(temps)
# print()

# # Print all cities in Spain with a temperature above 12°C

# print("All cities in Spain with a temperature above 12°C:")
# for city in cities:
#     if city['country'] == 'Spain':
#         if float(city["temperature"]) > 12:
#             print(city['city'])

# # Count the number of unique countries

# for city in cities:
#     unique = set(city["country"])
# print("The number of unique countries")
# print(f"{len(unique)}")

# # Print the average temperature for all the cities in Germany

# print("Average temperature for all the cities in Germany")
# temps = []
# for city in cities:
#     if city['country'] == 'Germany':
#         temps.append(float(city['temperature']))
# print(sum(temps)/len(temps))
# print()
# # Print the max temperature for all the cities in Italy

# print("Max temperature for all the cities in Germany")
# temps = []
# for city in cities:
#     if city['country'] == 'Germany':
#         temps.append(float(city['temperature']))
# print(max(temps))
# print()
def filter(condition, dict_list):
    temps= []
    for item in dict_list:
        if condition(item):
            temps.append(item)
    return temps
filtered_list = filter(lambda x: x['country'] == 'Germany', cities)
print(filtered_list)
# def aggragate(aggregation_key, agrregation, dict_list):
