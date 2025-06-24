# Pandas DataFrame head() method
# Code by Studyopedia

import pandas as pd

#Dataset

data = {
    'student' : ["Israt","Janie","Anika","Shomi","Rimi","Nadia"],
    'Rank' : [1,4,3,5,6,2],
    'Marks' : [95,70,80,60,55,90]
}

# Create a DataFrame using the DataFrame() method with index
df = pd.DataFrame(data, index=['RowA','RowB','RowC','RowD','RowE','RowF'],)

print("Student Records\n\n", df)

print("\nFirst 5 rows:\n",df.head())
print("\nFirst 2 rows:\n",df.head(2))
