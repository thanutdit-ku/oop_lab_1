import csv, os
from pathlib import Path

class DataLoader:
    """Handles loading CSV data files."""
    
    def __init__(self, base_path=None):
        """Initialize the DataLoader with a base path for data files.
        """
        if base_path is None:
            self.base_path = Path(__file__).parent.resolve()
        else:
            self.base_path = Path(base_path)
    
    def load_csv(self, filename):
        """Load a CSV file and return its contents as a list of dictionaries.
        """
        filepath = self.base_path / filename
        data = []
        
        with filepath.open() as f:
            rows = csv.DictReader(f)
            for row in rows:
                data.append(dict(row))
        
        return data

class DB:
    """Your code here"""
    def __init__(self):
        self.table = []
    def insert(self,table):
        self.table.append(table)
    def search(self,table_name):
        for table in self.table:
            if table.table_name == table_name:
                return table
        
class Table:
    def __init__(self, name, dict_list):
        self.table_name = name
        self.table = dict_list

    def filter(self, condition):
        filtered_list = []
        dict_list = self.table
        for item in dict_list:
            if condition(item):
                filtered_list.append(item)
        return Table("filtered", filtered_list)
    
    def aggregate(self, aggregation_function, aggregation_key):
        temps = []
        dict_list = self.table  
        for item in dict_list:
            try:
                temps.append(float(item[aggregation_key]))
            except ValueError:
                temps.append(item[aggregation_key])
        return aggregation_function(temps)
    
    def join(self,other_table,key):
        join_table = []
        for row in self.table:
            for other_row in other_table.table:
                if row[key] == other_row[key]:
                    break
            row.update(other_row)
            join_table.append(row)
        return Table(f"{self.table_name}_join_{other_table.table_name}",join_table)


    def __str__(self):
        return self.table_name + ':' + str(self.table)

loader = DataLoader()
cities = loader.load_csv('Cities.csv')
table1 = Table('cities', cities)
countries = loader.load_csv('Countries.csv')
table2 = Table('countries', countries)

my_DB = DB()
my_DB.insert(table1)
my_DB.insert(table2)

my_table1 = my_DB.search('cities')
print("List all cities in Italy:") 
my_table1_filtered = my_table1.filter(lambda x: x['country'] == 'Italy')
print(my_table1_filtered)
print()

print("Average temperature for all cities in Italy:")
print(my_table1_filtered.aggregate(lambda x: sum(x)/len(x), 'temperature'))
print()

my_table2 = my_DB.search('countries')
print("List all non-EU countries:") 
my_table2_filtered = my_table2.filter(lambda x: x['EU'] == 'no')
print(my_table2_filtered)
print()

print("Number of countries that have coastline:")
print(my_table2.filter(lambda x: x['coastline'] == 'yes').aggregate(lambda x: len(x), 'coastline'))
print()

my_table3 = my_table1.join(my_table2, 'country')
print("First 5 entries of the joined table (cities and countries):")
for item in my_table3.table[:5]:
    print(item)
print()

print("Cities whose temperatures are below 5.0 in non-EU countries:")
my_table3_filtered = my_table3.filter(lambda x: x['EU'] == 'no').filter(lambda x: float(x['temperature']) < 5.0)
print(my_table3_filtered.table)
print()

print("The min and max temperatures for cities in EU countries that do not have coastlines")
my_table3_filtered = my_table3.filter(lambda x: x['EU'] == 'yes').filter(lambda x: x['coastline'] == 'no')
print("Min temp:", my_table3_filtered.aggregate(lambda x: min(x), 'temperature'))
print("Max temp:", my_table3_filtered.aggregate(lambda x: max(x), 'temperature'))
print()




# import csv, os
# from pathlib import Path

# class DataLoader:
#     """Handles loading CSV data files."""
    
#     def __init__(self, base_path=None):
#         """Initialize the DataLoader with a base path for data files.
#         """
#         if base_path is None:
#             self.base_path = Path(__file__).parent.resolve()
#         else:
#             self.base_path = Path(base_path)
    
#     def load_csv(self, filename):
#         """Load a CSV file and return its contents as a list of dictionaries.
#         """
#         filepath = self.base_path / filename
#         data = []
        
#         with filepath.open() as f:
#             rows = csv.DictReader(f)
#             for row in rows:
#                 data.append(dict(row))
        
#         return data
    
# class Table:
#     def __init__(self, name, dict_list):
#         self.name = name
#         self.table = dict_list

#     def _filter(self, condition, dict_list):
#         filtered_list = []
#         for item in dict_list:
#             if condition(item):
#                 filtered_list.append(item)
#         return Table("filtered", filtered_list)
    
#     def _aggregate(self, aggregation_function, aggregation_key, dict_list):
#         temps = []
#         for item in dict_list:
#             try:
#                 temps.append(float(item[aggregation_key]))
#             except ValueError:
#                 temps.append(item[aggregation_key])
#         return aggregation_function(temps)

#     def filter(self, condition):
#         return self._filter(condition, self.table)
    
#     def aggregate(self, aggregation_function, aggregation_key):
#         return self._aggregate(aggregation_function, aggregation_key, self.table)

# loader = DataLoader()
# cities = loader.load_csv('Cities.csv')
# my_table1 = Table('cities', cities)

# # Print the average temperature of all the cities
# my_value = my_table1.aggregate(lambda x: sum(x)/len(x), 'temperature')
# print(my_value)
# print()

# # Print all cities in Germany
# my_cities = my_table1.filter(lambda x: x['country'] == 'Germany')
# cities_list = [[city['city'], city['country']] for city in my_cities.table]
# print("All the cities in Germany:")
# for city in cities_list:
#     print(city)
# print()

# # Print all cities in Spain with a temperature above 12°C
# my_cities = my_table1.filter(lambda x: x['country'] == 'Spain' and float(x['temperature']) > 12.0)
# cities_list = [[city['city'], city['country'], city['temperature']] for city in my_cities.table]
# print("All the cities in Spain with temperature above 12°C:")
# for city in cities_list:
#     print(city)
# print()

# # Count the number of unique countries
# my_countries = my_table1.aggregate(lambda x: len(set(x)), 'country')
# print("The number of unique countries is:")
# print(my_countries)
# print()

# # Print the average temperature for all the cities in Germany
# my_value = my_table1.filter(lambda x: x['country'] == 'Germany').aggregate(lambda x: sum(x)/len(x), 'temperature')
# print("The average temperature of all the cities in Germany:")
# print(my_value)
# print()

# # Print the max temperature for all the cities in Italy
# my_value = my_table1.filter(lambda x: x['country'] == 'Italy').aggregate(lambda x: max(x), 'temperature')
# print("The max temperature of all the cities in Italy:")
# print(my_value)
# print()
