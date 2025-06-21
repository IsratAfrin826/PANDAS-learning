# Pandas DataFrame size attribute
# Code by Studyopedia

import pandas as pd

#DataSet

data = {
    'Student' : ["Israt","Asma","Nitu","Janie","Anika"],
    'Rank'    : [1,4,3,5,2],
    'Marks'   :[95,70,80,60,90]
}

# Create a DataFrame using the DataFrame() method with index
df = pd.DataFrame(data,index=['RowA','RowB','RowC','RowD','RowE'],)

print("Student Records\n\n", df)

print("\nNumber of elements:\n",df.size)