Processes the filters data from the file Cities.csv



File structure: oop_lab_1/ |-- README.md # This file |-- Cities.csv # The dataset |-- data_processing.py # The analysis code

Loads data from `Cities.csv` located in the same directory as the Python file.  

The Table class is initialized with a given name and dataset, setting them as public attributes.
The filter method invokes the internal _filter function, which applies a specified condition to the table’s data and returns a new Table instance containing only the matching records.
The aggregate method calls the internal _aggregate function, passing in the dataset, an aggregation function, and a key to operate on. It then returns the computed aggregated result.

Testing can be performed by updating the data in Cities.csv and executing data_processing.py directly.
Make sure that both files are located in the same directory.