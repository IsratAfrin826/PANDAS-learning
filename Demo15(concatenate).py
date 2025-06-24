# Concatenate two Pandas DataFrame
# Code by Studyopedia

import pandas as pd

# DataSet
data1={
    'Id': ["S01","S02","S03","S04","S05"],
     'Student' :["Israt","Janie","Anika","Antor","Shihub"],
     'Roll':[534,551,555,557,570]

}
data2={
    'Id':["S06","S07","S08"],
    'Student':["Soma","Nipa","Anu"],
    'Roll':[571,572,573]

}

#DataFrame
dataFrame1=pd.DataFrame(data1,index=["Student1","Student2","Student3","Student4","Student5"])
print("DataFrame1=\n",dataFrame1)
dataFrame2=pd.DataFrame(data2,index=["Student6","Student7","Student8"])
print("DataFrame2=\n",dataFrame2)


# Concatenate two DataFrames
resultDF = pd.concat([dataFrame1,dataFrame2])
print("\nConcatenating DataFrames =\n" ,resultDF)