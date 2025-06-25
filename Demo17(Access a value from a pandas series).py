import pandas as pd

# data
data = [10 ,20, 40, 60, 80]

# Create a Series using the series() method
s = pd.Series(data)

# Display the Series
print("Series:\n", s)

# Access a value
print("\n Value from a pandas series:\n" ,s[2])