#Pandas 
import pandas as pd
import numpy as np
"""d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
df['three']=pd.Series([10,20,30],index=['a','b','c'])
df['four']=df['one']+df['three']

print (df)

# using del function
print ("Deleting the first column using DEL function:")
del df['one']
print (df)

# using pop function
print ("Deleting another column using POP function:")
df.pop('two')
print (df)
"""
"""#FOR SELECTING ROW FROM THE DATA FRAME 
print(df.loc['c'])
print(df.iloc[2])
print (df[2:4])

#Addtion of rows using append function
df=df.append(pd.DataFrame([[2,3,4,5]],columns=['one','two','three','four']),ignore_index=False)
df.rename(index={0:'e'},inplace=True)
df=df.append(pd.DataFrame([[4,5,6,7]],columns=['one','two','three','four']),ignore_index=False)
df.rename(index={0:'f'},inplace=True)
print(df)

# for deletion of rows use drop(index_name or index_number) 
"""
######SERIES
#s=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
"""
1	axes	Returns a list of the row axis labels.
2	dtype	Returns the dtype of the object.
3	empty	Returns True if series is empty.
4	ndim	Returns the number of dimensions of the underlying data.
5	size	Returns the number of elements in the underlying data.
6	values	Returns the Series as ndarray.
7	head()	Returns the first n rows.
8	tail()	Returns the last n rows.

"""
"""
DATAFRAME
1	T	Transposes rows and columns.
2	axes	Returns a list with the row axis labels and column axis labels as the only members.
3	dtypes	Returns the dtypes in this object.
4	empty	True if NDFrame is entirely empty [no items]; if any of the axes are of length 0.
5	ndim	Number of axes / array dimensions.
6	shape	Returns a tuple representing the dimensionality of the DataFrame.
7	size	Number of elements in the NDFrame.
8	values	Numpy representation of NDFrame.
9	head()	Returns the first n rows.
10	tail()	Returns last n rows.
"""
"""
Statistics
1	count()	Number of non-null observations
2	sum()	Sum of values : while summation NaN will be consider as 0
3	mean()	Mean of Values
4	median()	Median of Values
5	mode()	Mode of values
6	std()	Standard Deviation of the Values
7	min()	Minimum Value
8	max()	Maximum Value
9	abs()	Absolute Value
10	prod()	Product of Values
11	cumsum()	Cumulative Sum
12	cumprod()	Cumulative Product
13 pct_change()  Percent change    (value_before-value_after)/value_before 
14 cov()      covarince 
15 corr()     correlation 
16 rank()     ranking of data
"""

"""
s=pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
def a(ele1,ele2):
   return ele1+ele2
print(s)
print(s.pipe(a,2))
print(s.apply(np.mean))
"""

"""
RE INDEXING RESHAPE DF1 INTO DF2
"""
df = pd.DataFrame(np.random.randn(7,3),columns=['col3','col2','col1'],index=[6,3,4,2,1,3,5])
"""
df2 = pd.DataFrame(np.random.randn(10,3),columns=['col1','col2','col3'])
print(df1)
print(df2)
df1=df1.reindex_like(df2,method='ffill')
print(df1)"""

"""df1.rename(columns={'col1':'c1'},inplace='True')
print(df1)
for key,value in df1.iteritems():
   print (key,value)
for row_index,row in df1.iterrows():
   print (row_index,row)
for row in df1.itertuples():
    print (row)

"""

"""
Sorting
df1=df1.sort_index(axis=0)  #df1=df1.sort_index() both are same 
df1=df1.sort_index(axis=1)
df1=df1.sort_index(axis=1,ascending=False)
df1.sort_values(by='col1',kind="mergesort")
"""



"""
1	lower()	      Converts strings in the Series/Index to lower case.
2	upper()	      Converts strings in the Series/Index to upper case.
3	len()	         Computes String length().
4	strip()	      Helps strip whitespace(including newline) from each string in the Series/index from both the sides.
5	split(' ')	      Splits each string with the given pattern.
6	cat(sep=' ')	  Concatenates the series/index elements with given separator.
7	get_dummies()  	Returns the DataFrame with One-Hot Encoded values.
8	contains(pattern)	Returns a Boolean value True for each element if the substring contains in the element, else False.
9	replace(a,b)  	Replaces the value a with the value b.
10	repeat(value) 	Repeats each element with specified number of times.
11	count(pattern)	Returns count of appearance of pattern in each element.
12	startswith(pattern)	Returns true if the element in the Series/Index starts with the pattern.
13	endswith(pattern)	Returns true if the element in the Series/Index ends with the pattern.
14	find(pattern)  	Returns the first position of the first occurrence of the pattern.
15	findall(pattern)	Returns a list of all occurrence of the pattern.
16	swapcase()	      Swaps the case lower/upper.
17	islower()     	Checks whether all characters in each string in the Series/Index in lower case or not. Returns Boolean
18	isupper()	      Checks whether all characters in each string in the Series/Index in upper case or not. Returns Boolean.
19	isnumeric()	  Checks whether all characters in each string in the Series/Index are numeric. Returns Boolean.
"""
s=pd.Series(["Tom","PaWan","PriyA","bisHT","SinHa"])
"""
df1.loc[:,['col3','col2']]
df.loc[:,'A']
df=pd.DataFrame(np.random.randn(10,3),index=['a','b','c','d','e','f','g','h','i','j'],columns=['A','B','C'])
df.loc['a']>0
df.loc[:,'A']>0 
"""

"""
Windows function
rolling(window=n).any_statistical function
expanding(min_periods=n).any_statistical function
print(df)
print(df.rolling(window=3).max())
print(df.expanding(min_periods=3).max())
"""

"""Handlind NaN values :
df.fillna(value)
df.dropna()
df.fillna(method='pad/ffill  and bfill )
"""





