import pandas as pd

# data
data = [10 ,20, 40, 60, 80]

# Create a Series using the series() method
s = pd.Series(data, index =["RowA","RowB","RowC","RowD","RowE"])

# Display the Series
print("Series:\n", s)

# Access a value referring the label
print("\n A value from a pandas Series with label RowD\n ", s["RowD"])