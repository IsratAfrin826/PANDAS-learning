# Join DataFrame in Pandas
# Code by Studyopedia

import pandas as pd

# DataSet
data1={
    'Id': ["S01","S02","S03","S04","S05"],
     'Student' :["Israt","Janie","Anika","Antor","Shihub"],
     'Roll':[534,551,555,557,570]

}
data2={
    'Rank':[1,4,3,5,2],
    'Marks':[95,70,80,60,90]

}

#DataFrame
dataFrame1=pd.DataFrame(data1)
print("DataFrame1=\n",dataFrame1)
dataFrame2=pd.DataFrame(data2)
print("DataFrame2=\n",dataFrame2)


# Join two DataFrame
resultDF= dataFrame1.join(dataFrame2)
print("\nJoining two DataFrame\n",resultDF)