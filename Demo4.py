# Name your indexes in a pandas DataFrame
#Code by Studyopedia

import pandas as pd

#DataSet

data = {
    'Student': ["Israt", "Asma", "Nitu", "Sathi", "Riya"],
    'Rank': [1, 4, 3, 5, 2],
    'Marks': [95, 70, 80, 60, 90]
}

# Use the index argument to set your indexes

df = pd.DataFrame(data,index = ['Student1','Student2','Student3','Student4','Student5'])

print("Student Records\n\n", df)