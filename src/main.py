import pandas as pd
import argparse
#cd Documents/education/galvanize/code/grader

parser = argparse.ArgumentParser(descrption='Find top students')
parser.add_argument('filename', metavar='F',type=str)
parser.add_argument('percentage', metavar='F',type=int)
args = parser.parse_args()
print('args:', args)
filename = args.filename
percentage = args.percentage

#df = pd.read_csv('data/grades.csv')

df = pd.read_csv(filename)
#df.head(2)
df1 = df.iloc[:,[0,1,3,5]]
#df1.head(2)
#df1.apply(lambda z: print(type(z)))
#df1.apply(lambda z: print(len(z)))
df1.apply(lambda row: (row[1]), axis=1)
#df1.head(2)
df1['final'] = df1.apply(lambda row: (row[1]+row[2]+(2*row[3]))/400, axis=1)
#df1.head(2)
#df1.head(2)
#num_students = int(len(df) * 0.01)
num_students = int(len(df1) * percentage/100)
#num_students
indicies = df1.final.argsort()
#indicies.head()
#df1.final[1424]
filtered_students = df.iloc[indicies[-num_students:]][::-1]
#filtered_students
filtered_students.student_id.values
ids = filtered_students.student_id.values
print(ids)