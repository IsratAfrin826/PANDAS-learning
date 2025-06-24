# Pandas DataFrame index attribute
# Code by Studyopedia

import pandas as pd

#Dataset

data = {
    'student' : ["Israt","Janie","Anika","Shomi","Rimi"],
    'Rank' : [1,4,3,5,2],
    'Marks' : [95,70,80,60,90]
}

# Create a DataFrame using the DataFrame() method with index
df = pd.DataFrame(data, index=['RowA','RowB','RowC','RowD','RowE'],)

print("Student Records\n\n", df)

print("\nDataFrame Index:\n",df.index)
