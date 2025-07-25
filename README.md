# PANDAS-learning
### What is PANDAS ?
pandas is a powerful and easy-to-use open-source tool built on top of the python programming language.

It is useful for data analysis and manipulation.Python with pandas is widely used in Statistics,Finance

Neuroscience,Economics,Web Analysis,Advertising.etc.


To work with data sets,clean them,and make them relevant for Data Science is what Pandas do.With that,

easily load and read data sets in Excel,CSV,JSON,XML,etc. formats with Pandas and work on them.Easily clean 

the wrong format data,remove duplicates , and do other tasks with Pandas.


The Python Pandas library was initially developed by Wes McKinney in 2008. After 4 years in 2012 , Chang She joined 

Wes as another contributor to the library.

### PANDAS - FEATURES

The following are the features of the Pandas Library :

      Analyze Data

      Manipulate Data

      Columns can be inserted and deleted from the DataFrame

      Group the rows/columns of a DataFrame/Series

      Plotting is possible

      Read CSV/Excel/JSON

      Fix the inaccurate data

      Clean the Data completely

      Handle Duplicates

### What is a PANDAS DataFrame ? How to Create ?

The Pandas DataFrame is a two-dimensional , tabular data , table with rows and columns. The **DataFrame()** method is used to

create a DataFrame and has the following parameters :

       data    : The data to be stored in the Pandas DataFrame

       index   : The index values to be provided for the resultant frame.

       columns : Set the column labels for the resultant frame if data does not mention before

       dtype   : It is the datatype and only a single type is allowed.

       copy    : To copy the input data

### PANDAS - Create a DataFrame

### 1. Create a Pandas DataFrame

       To create a DataFrame in pandas , use the pandas.DataFrame() method.

        Example : Demo1

### 2. Access a group of row or columns in a Pandas DataFrame

       The dataframe.loc is used in Pandas to access a group of rows or columns in a DataFrame.

           Example : Demo2

### 3. Access a group of rows or columns by integer positions in a Pandas DataFrame

        The dataframe.iloc is used to access a group of rows or columns by integers. We have also 

        set columns and indexes.

             Example : Demo3

### 4. Name your indexes in a Pandas DataFrame

       The index argument is used to set and name your own indexes in a DataFrame. 

              Example : Demo4

### 5. Iterate a Pandas DataFrame to display the cilumn names

       To iterate a DataFrame and display the column names , use the for loop as in the below 

             Example : Demo5

### DATAFRAME - Attributes and Methods

The Pandas DataFrame is a Two-dimensional , tabular data , that uses the DataFrame() method to create a 

DataFrame. It also uses different built-in attributes and methods for basic functionalities. 

        1. dtypes : Return the dtypes in the DataFrame

        2. ndim   : Return the number of dimensions of the DataFrame

        3. size   : Return the number of elements in the DataFrame

        4. shape  : Return the dimensionality of the DataFrame in the form of a tuple.

        5. index  : Return the index of the DataFrame

        6. T      : Transpose the rows and columns

        7. head() : Return the first n rows.

        8. tail() : Return the last n rows.

### 1. Pandas DataFrame - DTYPES

       The pandas.DataFrame.dtypes is used to return the dtypes in the DataFrame.

            Example : Demo6(dtypes)

### 2. Pandas DataFrame - NDIM

       The pandas.DataFrame.ndim is used to return the number of dimensions of the

       DataFrame.

            Example : Demo7(ndim)

### 3. Pandas DataFrame - SIZE

       The pandas.DataFrame.size is used to return the number of elements in the DataFrame.

             Example : Demo8(size)  

### 4. Pandas DataFrame - SHAPE

       The pandas.DataFrame.shape is used to return the dimensionality of the DataFrame in the form of a tupple

               Example : Demo9(shape)

### 5. Pands DataFrame - INDEX

       The pandas.DataFrame.index is used to return the index of the DataFrame

                Example : Demo10(index)

### 6. Pandas DataFrame - T

       The pandas.DataFrame.T is used to Transpose the rows and columns

                 Example : Demo11(T)

### 7. Pandas DataFrame - HEAD()

       The pandas.DataFrame.head() is used to return the first n rows

                 Example : Demo12(head)

### 8. Pandas DataFrame - TAIL()

       The pandas.DataFrame.tail() is used to return the last n rows

                 Example : Demo13(tail)

### JOIN PANDAS DATAFRAME

      In Python, we can easily join Pandas DataFrames using the join() method.This will join the 

      columns of the two different DataFrames.

                 Example : Demo14(Join DataFrame)

### CONCATENATE PANDAS DATAFRAME

    In this lesson, learn to concatenate the Pandas DataFrames in Python using the concat() method.
    
    This will concatenate the content of the DataFrames

                Example : Demo15(concatenate)

### What is a Series in Pandas ? How to create ?

     Series in Pandas is a one-dimensional array,like a column in a table. It is a labeled array that

     can hold data of any type. The Series() method is used for this and has the following parameters :

                 1. data  : The data to be stored in the Pandas Series.

                 2. index : The index values should have the same length as the data.

                 3. dtype : It is the datatype for the output Series.

                 4. name  : Set the series name with the name parameter.

                 5. copy  : To copy the input data.

**Create a Pandas Series**

To create a series in python, we use the Series() method.

                Example : Demo16(create a pandas series)

**Access a value from a Pandas Series**

The [] is used to access a value.Set the index of the value you want to display inside[] :

                Example : Demo17(Access a value from a pandas series)

**Name your indexes in a pandas series**

The index argument is used to set and name your own indexes in a Series, the labels can be 

set accordingly.

                  Example : Demo18(Name your indexes)

**Access a value from a pandas series with labels**

                  Example : Demo19(Access a value with labels)
