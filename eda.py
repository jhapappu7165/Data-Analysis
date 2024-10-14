### https://www.youtube.com/watch?v=Liv6eeb1VfE 22:18

#Series is a one-dimensional labeled array that holds a single data type, whereas DataFrame is a two-dimensional labeled data structure that can hold multiple data types across different columns.

#df[df['Continent'].str.contains('Oceania', case=False, na=False
#Series method applied: df['Continent'].str.contains('Oceania') returns True/False



import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("rockyou-20.txt", skip_blank_lines=False, keep_default_na=True)

print(df.head()) #first five line of the dataset with 1 column

#create a new column for the length of password- an empty string in place of NaN values whose length will be 0
df['password_length'] = df['PASSWORDS'].fillna('').apply(len)

print('\n', df)

#pd.set_option('display.float_format', lambda x: '%.2f' %x) #for floating-point numbers

print('\n', 'LINE=BY-LINE Identification of which line has null value')
print(df.isnull()) #line-by-line which password is NaN

print('\n', 'number of null values in each column')
print(df.isnull().sum()) #number of passwords missing/empty

print('\n', 'Number of unique values')
print(df.nunique()) #no. of unique values in a column and data type of result (no. of unique values - dtype: int64)


#sort string values in ascending order based on ASCII values
print('\n', "PASSWORDS IN ASCENDING ORDER")
print(df.sort_values(by="PASSWORDS")) #In string, comparison done character-by-character: Becz 0<1 in 0123456789 and 101010, so 0123456789 smaller than 101010 as strings


print('\n', "TOP 5 PASSWORDS IN DESCENDING ORDER")
print(df.sort_values(by="PASSWORDS", ascending = False).head())
#top 5 passwords in descending order on ASCII values: zxcvbnm, yellow, xavier, winnie, william

print('\n', "TOP 5 PASSWORD LENGTH IN DESCENDING ORDER")
print(df.sort_values(by="password_length", ascending = False).head())

print('\n', "TOP 5 PASSWORD LENGTH IN ASCENDING ORDER")
print(df.sort_values(by="password_length", ascending = True).head())

print('\n', 'No. of values in both columns - PASSWORDS & password_length')
print(df.count())
#print(df.corr) #NOT possible in 1 column of dataset




### CONVERT CATEGORICAL DATA (like passwords) into NUMERICAL FORMAT

#df['PASSWORDS'] access the list of passwords; .dropna() removes NaN (null) values- no numerical encoding of null; .unique() return array of unique values in PASSWORDS column; enumerate() returns pair of (index, password) in tuples - index start from zero; {} creates dictionary; map() maps each password with its respective encoded value

print('\n', 'ENCODING PASSWORD To NUMERICAL VALUES')
password_mapping = {password: index for index, password in enumerate(df['PASSWORDS'].dropna().unique())}

#password_mapping[None] = -1 #NOT needed here - map NaN values with -1
df['PASSWORDS_ENCODED'] = df['PASSWORDS'].map(password_mapping)
df['PASSWORDS_ENCODED'] = df['PASSWORDS_ENCODED'].fillna(-1).astype(int) #astype() change the data type of a DataFrame or Series
print(df.head())



print('\n', 'DATA TYPES OF EACH COLUMN')
print(df.dtypes)

print('\n', 'INFO. OF DATASET')
print(df.info())

print('\n', 'Describe the dataset')
print(df.describe())


##USE to_csv() method to save DataFrame to a CSV file (or a text file)

##index = False to ensure row index(0,1,2..) aren't in text file and sep='\t' ensure title & value are separated by tab-default is comma

df.to_csv("UPDATED rockyou-20.txt", sep="\t", index=False)
print('\n', 'Hurray! NEW TEXT FILE WITH 3 COLUMNS CREATED SUCCESSFULLY')



## corr() calculates the pairwise CORRELATION of columns containing numerical values in a DataFrame-how related 1 variable is with another

print('\n', 'Finding CORRELATION between numeric columns')
numeric_col = df.select_dtypes(include=['int64'])
print(numeric_col.corr())



### DATA VISUALIZATION

#sns.heatmap(numeric_col.corr(), annot = True)
#plt.show()



### GROUPING OF DATA

print('\n', 'GROUPING BY PASSWORD LENGTH')
#create groups based on password length & find no.of pw in each group
print(df.groupby('password_length').size())

#mean of each group - colns must be numeric to find mean
print('\n', 'GROUPING BY PASSWORD GROUP MEAN')
print(numeric_col.groupby('password_length').mean().sort_values(by='password_length', ascending = False))


print('\n', 'PRINTING df2')
df2 = numeric_col.groupby('password_length').count().sort_values(by='PASSWORDS_ENCODED')
print(df2)


### TRANSPOSE OF DATA FRAME - rows to cols & cols to rows
print('\n', 'TRANSPOSE OF DATA FRAME')
print(df.transpose())



### LINE GRAPH
#numeric_col.plot()
#plt.show()


print('\n', 'LIST OF COLUMNS','\n', df.columns)


## BOX PLOT
#numeric_col.boxplot()
#plt.show()


print('\n', 'TOP 5 ROWS IN DATASET', '\n', df.head())
print('\n', 'TOP 5 ROWS with - object - datatype IN DATASET', '\n', df.select_dtypes(include='object').head())
print('\n', 'TOP 5 ROWS with - INT64 - datatype IN DATASET', '\n', df.select_dtypes(include='int64').head())





###  DATA CLEANING IN PANDAS

df = df.drop_duplicates() #drop duplicates data

df = df.drop(columns='password_length') #drop unnecessary column
print('Dropped Column: password_length', '\n', df.head(), '\n') 

df['PASSWORDS'] = df["PASSWORDS"].str.lstrip("...")
df['PASSWORDS'] = df["PASSWORDS"].str.lstrip("/")
df['PASSWORDS'] = df["PASSWORDS"].str.rstrip("_")

print(df['PASSWORDS'].isna().sum())  

#Replace non(A-Z, a-z, 0-9) with nothing; regex=True for regular expression
df['PASSWORDS'] = df["PASSWORDS"].str.replace('[^a-zA-Z0-9]','', regex=True)

print('\n', df.head())

## Convert data type of PASSWORDS to string to add '#' in betn
df['PASSWORDS'] = df['PASSWORDS'].apply(lambda x:str(x))

## ADDING '#' in between characters of a word
df['PASSWORDS'] = df['PASSWORDS'].apply(lambda x: x[0:2] + '#' + x[2:])

print('\n', df.head())

### Remove '#' from in-between of words
df['PASSWORDS'] = df["PASSWORDS"].str.replace('[^a-zA-Z0-9]','', regex=True)
print('\n', df.head())

### Replace 'nan' with empty string
df['PASSWORDS'] = df['PASSWORDS'].str.replace('nan', '', regex = True)
print('\n', df.head())




### ****************LEARNING************************


##***** SPLIT "Address" column into Street_Address, State, Zip_Code - NOT For this dataset | Note: Each element from the split becomes a new column in the DataFrame

#df[["Street_Address", "State", "Zip_Code"]] = df["Address"].str.split(',', 2, expand=True) #split on basis of comma (2 commas)


##***** Replace 'Yes' to 'Y' and 'No' to 'N'
#df["Paying Customer"] = df["Paying Customer"].str.replace('Yes', 'Y')
#df["Paying Customer"] = df["Paying Customer"].str.replace('No', 'N')


##***** FILL NAN VALUES OF ENTIRE DATASET WITH BLANK
#df.fillna('')


##***** DROP A ROW BASED ON A PARTICULAR CONDITION | Note: With inplace=True, changes are applied directly to the existing DataFrame, and NO new DataFrame is created

for x in df.index: #index of each row (0,1,2,...)
    #drop the entire row if "Do_Not_Contact" is Y for that row
    if df.loc[x, "Do_Not_Contact"] == 'Y':
        df.drop(x, implace = True)
    
    #drop the entire row if "Phone_Number" is blank there
    if df.loc[x, "Phone_Number"] == '':
        df.drop(x, implace = True)



###**** After dropping some rows, reset UNORDERED index values (0,2,3,5) in ordered form (0,1,2...)
df.reset_index(drop = True)
