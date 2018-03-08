# Intially Lets import few Libraries
# Numirical Pyhton Library to perform operations in Arrays
import numpy as np

# Pandas to perform operations on DataFrames
import pandas as pd

# Import the dataset from NSE CSV File
DfFutureConsumer = pd.DataFrame.from_csv('FConsumer.csv')

# Print the dataset
print(DfFutureConsumer)

#Let's Initially Perform few Operations on Dataframes

# How to Work with Columns
X = DfFutureConsumer[:-1]
print(X)

X = DfFutureConsumer[1:2]
print(X)

# Print from column to column
DfFutureConsumer.loc[:,"PC":"TTQ"]

# Here we are setting index As Date so that we can travers datewise on Y Axis
Df2 = DfFutureConsumer.set_index("Date")
# Print the same and verify
print(Df2)

# Now We can also use the subfunction iloc to verify range selection
DfFutureConsumer.iloc[0:3,0:4]

# Let's Find out some Max Values and Mean
# We are finding the max value from Previous Close Price Column
DfFutureConsumer['PC'].max()
DfFutureConsumer['PC'].min()

# Now if we print the column New_Add : we can see the Percent Change
# Here We have Multiple Formulaes to Calculate the Same
# Consider Your Column has Variables from B0..B1..Bn
# Then (B1/B0)*100 = Val - 100 = Change in Percent
DfFutureConsumer['New_Add'] = DfFutureConsumer['PC'].pct_change()*100

# This Will print the value only if it is greater than 1 
# From this trade we have 82 times change greater than 1%
DfPc =  DfFutureConsumer[DfFutureConsumer.New_Add > 1.0]
print(DfPc)
print(DfPc.head())


# This Will print the value only if it is less than 1
# From this trade we have 166 times change less than 1%
DfPc =  DfFutureConsumer[DfFutureConsumer.New_Add < 1.0]
print(DfPc)
print(DfPc.head())



# Delete On of the Colums from the datasets


