#Access a group of rows or columns by integer positions in a pandas DataFrame
# Code by Studyopedia

import pandas as pd

# Dataset
data = {
    'Student': ["Israt","Asma","Nitu","Sathi","Riya"],
    'Rank': [1,4,3,5,2],
    'Marks': [95,70,80,60,90]
}

df = pd.DataFrame(data,index =['RowA','RowB','RowC','RowD','RowE'])

print("Student Records\n\n",df)

# Access using rows or columns by integer position
print("\nValue =\n",df.iloc[[3,4]])
