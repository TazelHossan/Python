import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np
colum1=[0,1,2,3,4,5]
cse_101 =pd.read_excel("C:\\Users\\Tazel\\Desktop\\xlsx\\input.xlsx",sheet_name="Sheet1",skiprows=9,nrows=62,usecols =colum1)
n = 63


print("============================================================================")
print("                    Course Code CSE-101 ,Credits=3")
print("============================================================================")

Average = []
for i in range(62):
        dif=abs(cse_101.iloc[i:i+1]['Internal'] - cse_101.iloc[i:i+1]['External'])
        x = int(dif)
        if x>12:
            j = i
            x1 =abs(cse_101.iloc[j:j+1]['Internal'] -cse_101.iloc[j:j+1]['3rd_Examiner'] )
            dif1 = int(x1)
            x2 =abs(cse_101.iloc[j:j+1]['External'] -cse_101.iloc[j:j+1]['3rd_Examiner'] )
            dif2 = int(x2)
            if dif1>dif2:
                m = (cse_101.iloc[j:j+1]['External'] + cse_101.iloc[j:j+1]['3rd_Examiner'])/2
                Average.append(m)
            else:
                n = (cse_101.iloc[j:j+1]['External'] + cse_101.iloc[j:j+1]['3rd_Examiner'])/2
                Average.append(n)

        else:
            o = (cse_101.iloc[i:i + 1]['Internal'] + cse_101.iloc[i:i + 1]['External']) / 2
            Average.append(o)
temp1 = []
temp1= pd.concat(Average)
cse_101['Average']= temp1
cse_101['Total_Marks'] = cse_101['Average'] + cse_101['Tutorial(40)']
#print(cse_101['Total_Marks'])
Result = []
for sum in cse_101['Total_Marks']:
    if sum >= 80 and sum <= 100:
        Result.append(4.00)
    elif sum >= 75 and sum < 80:
        Result.append(3.75)
    elif sum >= 70 and sum < 75:
        Result.append(3.50)
    elif sum >= 65 and sum < 70:
        Result.append(3.25)
    elif sum >= 60 and sum < 65:
        Result.append(3.00)
    elif sum >= 55 and sum < 60:
        Result.append(2.75)
    elif sum >= 50 and sum < 55:
        Result.append(2.50)
    elif sum >= 45 and 50:
        Result.append(2.25)
    elif sum >= 40 and sum < 45:
        Result.append(2.00)
    else:
        Result.append(0.00)
cse_101['GPA'] = Result
#print(cse_101)









print("============================================================================")
print("                    Course Code CSE-103 ,Credits=3")
print("============================================================================")

colum2=[0,1,2,3,4,5]
cse_103 =pd.read_excel("C:\\Users\\Tazel\\Desktop\\xlsx\\input.xlsx",sheet_name="Sheet1",skiprows=74,nrows=62,usecols =colum2)
Average = []
for i in range(62):
        dif=abs(cse_103.iloc[i:i+1]['Internal'] - cse_103.iloc[i:i+1]['External'])
        x = int(dif)
        if x>12:
            j = i
            x1 =abs(cse_103.iloc[j:j+1]['Internal'] -cse_103.iloc[j:j+1]['3rd_Examiner'] )
            dif1 = int(x1)
            x2 =abs(cse_103.iloc[j:j+1]['External'] -cse_103.iloc[j:j+1]['3rd_Examiner'] )
            dif2 = int(x2)
            if dif1>dif2:
                m = (cse_103.iloc[j:j+1]['External'] + cse_103.iloc[j:j+1]['3rd_Examiner'])/2
                Average.append(m)
            else:
                n = (cse_103.iloc[j:j+1]['External'] + cse_103.iloc[j:j+1]['3rd_Examiner'])/2
                Average.append(n)

        else:
            o = (cse_103.iloc[i:i + 1]['Internal'] + cse_103.iloc[i:i + 1]['External']) / 2
            Average.append(o)
temp1 = []
temp1= pd.concat(Average)
cse_103['Average']= temp1
cse_103['Total_Marks'] = cse_103['Average'] + cse_103['Tutorial']
Result = []
for sum in cse_103['Total_Marks']:
    if sum >= 80 and sum <= 100:
        Result.append(4.00)
    elif sum >= 75 and sum < 80:
        Result.append(3.75)
    elif sum >= 70 and sum < 75:
        Result.append(3.50)
    elif sum >= 65 and sum < 70:
        Result.append(3.25)
    elif sum >= 60 and sum < 65:
        Result.append(3.00)
    elif sum >= 55 and sum < 60:
        Result.append(2.75)
    elif sum >= 50 and sum < 55:
        Result.append(2.50)
    elif sum >= 45 and 50:
        Result.append(2.25)
    elif sum >= 40 and sum < 45:
        Result.append(2.00)
    else:
        Result.append(0.00)
cse_103['GPA'] = Result
#print(cse_103)









print("============================================================================")
print("                    Course Code CSE-105 ,Credits=3")
print("============================================================================")

colum3=[0,1,2,3,4,5]
cse_105 =pd.read_excel("C:\\Users\\Tazel\\Desktop\\xlsx\\input.xlsx",sheet_name="Sheet1",skiprows=139,nrows=62,usecols =colum3)
Average = []
for i in range(62):
        dif=abs(cse_105.iloc[i:i+1]['Internal'] - cse_105.iloc[i:i+1]['External'])
        x = int(dif)
        if x>12:
            j = i
            x1 =abs(cse_105.iloc[j:j+1]['Internal'] -cse_105.iloc[j:j+1]['3rd_Examiner'] )
            dif1 = int(x1)
            x2 =abs(cse_105.iloc[j:j+1]['External'] -cse_105.iloc[j:j+1]['3rd_Examiner'] )
            dif2 = int(x2)
            if dif1>dif2:
                m = (cse_105.iloc[j:j+1]['External'] + cse_105.iloc[j:j+1]['3rd_Examiner'])/2
                Average.append(m)
            else:
                n = (cse_105.iloc[j:j+1]['External'] + cse_105.iloc[j:j+1]['3rd_Examiner'])/2
                Average.append(n)

        else:
            o = (cse_105.iloc[i:i + 1]['Internal'] + cse_105.iloc[i:i + 1]['External']) / 2
            Average.append(o)
temp1 = []
temp1= pd.concat(Average)
cse_105['Average']= temp1
cse_105['Total_Marks'] = cse_105['Average'] + cse_105['Tutorial']
Result = []
for sum in cse_105['Total_Marks']:
    if sum >= 80 and sum <= 100:
        Result.append(4.00)
    elif sum >= 75 and sum < 80:
        Result.append(3.75)
    elif sum >= 70 and sum < 75:
        Result.append(3.50)
    elif sum >= 65 and sum < 70:
        Result.append(3.25)
    elif sum >= 60 and sum < 65:
        Result.append(3.00)
    elif sum >= 55 and sum < 60:
        Result.append(2.75)
    elif sum >= 50 and sum < 55:
        Result.append(2.50)
    elif sum >= 45 and 50:
        Result.append(2.25)
    elif sum >= 40 and sum < 45:
        Result.append(2.00)
    else:
        Result.append(0.00)
cse_105['GPA'] = Result
#print(cse_105)





print("============================================================================")
print("                    Course Code CSE-107 ,Credits=3")
print("============================================================================")

colum4=[0,1,2,3,4,5]
cse_107 =pd.read_excel("C:\\Users\\Tazel\\Desktop\\xlsx\\input.xlsx",sheet_name="Sheet1",skiprows=204,nrows=62,usecols =colum4)
Average = []
for i in range(62):
        dif=abs(cse_107.iloc[i:i+1]['Internal'] - cse_107.iloc[i:i+1]['External'])
        x = int(dif)
        if x>12:
            j = i
            x1 =abs(cse_107.iloc[j:j+1]['Internal'] -cse_107.iloc[j:j+1]['3rd_Examiner'] )
            dif1 = int(x1)
            x2 =abs(cse_107.iloc[j:j+1]['External'] -cse_107.iloc[j:j+1]['3rd_Examiner'] )
            dif2 = int(x2)
            if dif1>dif2:
                m = (cse_107.iloc[j:j+1]['External'] + cse_107.iloc[j:j+1]['3rd_Examiner'])/2
                Average.append(m)
            else:
                n = (cse_107.iloc[j:j+1]['External'] + cse_107.iloc[j:j+1]['3rd_Examiner'])/2
                Average.append(n)
        else:
            o = (cse_107.iloc[i:i + 1]['Internal'] + cse_107.iloc[i:i + 1]['External']) / 2
            Average.append(o)
temp1 = []
temp1= pd.concat(Average)
cse_107['Average']= temp1
cse_107['Total_Marks'] = cse_107['Average'] + cse_107['Tutorial']
Result = []
for sum in cse_107['Total_Marks']:
    if sum >= 80 and sum <= 100:
        Result.append(4.00)
    elif sum >= 75 and sum < 80:
        Result.append(3.75)
    elif sum >= 70 and sum < 75:
        Result.append(3.50)
    elif sum >= 65 and sum < 70:
        Result.append(3.25)
    elif sum >= 60 and sum < 65:
        Result.append(3.00)
    elif sum >= 55 and sum < 60:
        Result.append(2.75)
    elif sum >= 50 and sum < 55:
        Result.append(2.50)
    elif sum >= 45 and 50:
        Result.append(2.25)
    elif sum >= 40 and sum < 45:
        Result.append(2.00)
    else:
        Result.append(0.00)
cse_107['GPA'] = Result
#print(cse_107)






print("============================================================================")
print("                    Course Code CSE-109 ,Credits=3")
print("============================================================================")
colum5=[0,1,2,3,4,5]
cse_109 =pd.read_excel("C:\\Users\\Tazel\\Desktop\\xlsx\\input.xlsx",sheet_name="Sheet1",skiprows=269,nrows=62,usecols =colum5)
Average = []
for i in range(62):
        dif=abs(cse_109.iloc[i:i+1]['Internal'] - cse_109.iloc[i:i+1]['External'])
        x = int(dif)
        if x>12:
            j = i
            x1 =abs(cse_109.iloc[j:j+1]['Internal'] -cse_109.iloc[j:j+1]['3rd_Examiner'] )
            dif1 = int(x1)
            x2 =abs(cse_109.iloc[j:j+1]['External'] -cse_109.iloc[j:j+1]['3rd_Examiner'] )
            dif2 = int(x2)
            if dif1>dif2:
                m = (cse_109.iloc[j:j+1]['External'] + cse_109.iloc[j:j+1]['3rd_Examiner'])/2
                Average.append(m)
            else:
                n = (cse_109.iloc[j:j+1]['External'] + cse_109.iloc[j:j+1]['3rd_Examiner'])/2
                Average.append(n)
        else:
            o = (cse_109.iloc[i:i + 1]['Internal'] + cse_109.iloc[i:i + 1]['External']) / 2
            Average.append(o)
temp1 = []
temp1= pd.concat(Average)
cse_109['Average']= temp1
cse_109['Total_Marks'] = cse_109['Average'] + cse_109['Tutorial']
Result = []
for sum in cse_109['Total_Marks']:
        if sum >= 80 and sum <= 100:
            Result.append(4.00)
        elif sum >= 75 and sum < 80:
            Result.append(3.75)
        elif sum >= 70 and sum < 75:
            Result.append(3.50)
        elif sum >= 65 and sum < 70:
            Result.append(3.25)
        elif sum >= 60 and sum < 65:
            Result.append(3.00)
        elif sum >= 55 and sum < 60:
            Result.append(2.75)
        elif sum >= 50 and sum < 55:
            Result.append(2.50)
        elif sum >= 45 and 50:
            Result.append(2.25)
        elif sum >= 40 and sum < 45:
            Result.append(2.00)
        else:
            Result.append(0.00)
cse_109['GPA'] = Result
#print(cse_109)





print("============================================================================")
print("                    Course Code CSE-111 ,Credits=2")
print("============================================================================")
colum6=[0,1,2,3,4,5]
cse_111 =pd.read_excel("C:\\Users\\Tazel\\Desktop\\xlsx\\input.xlsx",sheet_name="Sheet1",skiprows=334,nrows=64,usecols =colum6)
Average = []
for i in range(63):
        dif=abs(cse_111.iloc[i:i+1]['Internal'] - cse_111.iloc[i:i+1]['External'])
        x = int(dif)
        if x>12:
            j = i
            x1 =abs(cse_111.iloc[j:j+1]['Internal'] -cse_111.iloc[j:j+1]['3rd_Examiner'] )
            dif1 = int(x1)
            x2 =abs(cse_111.iloc[j:j+1]['External'] -cse_111.iloc[j:j+1]['3rd_Examiner'] )
            dif2 = int(x2)
            if dif1>dif2:
                m = (cse_111.iloc[j:j+1]['External'] + cse_111.iloc[j:j+1]['3rd_Examiner'])/2
                Average.append(m)
            else:
                n = (cse_111.iloc[j:j+1]['External'] + cse_111.iloc[j:j+1]['3rd_Examiner'])/2
                Average.append(n)
        else:
            o = (cse_111.iloc[i:i + 1]['Internal'] + cse_111.iloc[i:i + 1]['External']) / 2
            Average.append(o)
temp1 = []
temp1= pd.concat(Average)
cse_111['Average']= temp1
cse_111['Total_Marks'] = cse_111['Average'] + cse_111['Tutorial']
Result = []
for sum in cse_111['Total_Marks']:
        if sum >= 40 and sum <= 50:
            Result.append(4.00)
        elif sum >= 37.5 and sum < 40:
            Result.append(3.75)
        elif sum >= 35 and sum < 37.5:
            Result.append(3.50)
        elif sum >= 32.5 and sum < 35:
            Result.append(3.25)
        elif sum >= 30 and sum < 32.5:
            Result.append(3.00)
        elif sum >= 27.5 and sum < 30:
            Result.append(2.75)
        elif sum >= 25 and sum < 27.5:
            Result.append(2.50)
        elif sum >= 22.5 and 25:
            Result.append(2.25)
        elif sum >= 20 and sum < 22.5:
            Result.append(2.00)
        else:
            Result.append(0.00)
cse_111['GPA'] = Result
#print(cse_111)




print("============================================================================")
print("                    Course Code CSE-108 ,Credits=1")
print("============================================================================")
colum6=[0,1,2,3,4]
cse_108 =pd.read_excel("C:\\Users\\Tazel\\Desktop\\xlsx\\input.xlsx",sheet_name="Sheet1",skiprows=401,nrows=63,usecols =colum6)
cse_108['Total(CSE-108)'] = cse_108['Class test'] + cse_108['Final']
Result = []
for sum in cse_108['Total(CSE-108)']:
        if sum>=80 and sum<=100:
                Result.append(4.00)
        elif sum>=75 and sum<80:
            Result.append(3.75)
        elif sum >= 70 and sum <75 :
            Result.append(3.50)
        elif sum >= 65 and sum<70:
            Result.append(3.25)
        elif sum >= 60 and sum <65 :
            Result.append(3.00)
        elif sum >= 55 and sum <60:
            Result.append(2.75)
        elif sum >= 50 and sum <55:
            Result.append(2.50)
        elif sum >= 45 and 50 :
            Result.append(2.25)
        elif sum >= 40 and sum<45:
            Result.append(2.00)
        else:
            Result.append(0.00)
cse_108['GPA'] = Result
#print(cse_108)




print("============================================================================")
print("                    Course Code CSE-114 ,Credits=1")
print("============================================================================")
colum7=[0,1,2,3,4]
cse_114 =pd.read_excel("C:\\Users\\Tazel\\Desktop\\xlsx\\input.xlsx",sheet_name="Sheet1",skiprows=468,nrows=63,usecols =colum7)
cse_114['Total(CSE-114)'] = cse_114['Class test'] + cse_114['Final']
Result = []
for sum in cse_114['Total(CSE-114)']:
        if sum >= 40 and sum <= 50:
            Result.append(4.00)
        elif sum >= 37.5 and sum < 40:
            Result.append(3.75)
        elif sum >= 35 and sum < 37.5:
            Result.append(3.50)
        elif sum >= 32.5 and sum < 35:
            Result.append(3.25)
        elif sum >= 30 and sum < 32.5:
            Result.append(3.00)
        elif sum >= 27.5 and sum < 30:
            Result.append(2.75)
        elif sum >= 25 and sum < 27.5:
            Result.append(2.50)
        elif sum >= 22.5 and 25:
            Result.append(2.25)
        elif sum >= 20 and sum < 22.5:
            Result.append(2.00)
        else:
            Result.append(0.00)
cse_114['GPA'] = Result
#print(cse_114)




print("============================================================================")
print("                    Course Code CSE-100 ,Credits=1")
print("============================================================================")
colum8=[0,1,2]
cse_100 =pd.read_excel("C:\\Users\\Tazel\\Desktop\\xlsx\\input.xlsx",sheet_name="Sheet1",skiprows=537,nrows=63,usecols =colum8)
cse_114['Total(CSE-114)'] = cse_114['Class test'] + cse_114['Final']
Result = []
for sum in cse_100['Total(CSE-100)']:
        if sum >= 40 and sum <= 50:
            Result.append(4.00)
        elif sum >= 37.5 and sum < 40:
            Result.append(3.75)
        elif sum >= 35 and sum < 37.5:
            Result.append(3.50)
        elif sum >= 32.5 and sum < 35:
            Result.append(3.25)
        elif sum >= 30 and sum < 32.5:
            Result.append(3.00)
        elif sum >= 27.5 and sum < 30:
            Result.append(2.75)
        elif sum >= 25 and sum < 27.5:
            Result.append(2.50)
        elif sum >= 22.5 and 25:
            Result.append(2.25)
        elif sum >= 20 and sum < 22.5:
            Result.append(2.00)
        else:
            Result.append(0.00)
cse_100['GPA'] = Result
#print(cse_100)


df = pd.DataFrame( { 'Exam_Roll':cse_111['Exam_Roll'] ,'CSE-100':cse_100['GPA'] ,'CSE-101':cse_101['GPA'],
                     'CSE-103':cse_103['GPA'] ,'CSE-105':cse_105['GPA'],'CSE-107':cse_107['GPA'],'CSE-108':cse_108['GPA'] ,'CSE-109':cse_109['GPA'],
                     'CSE-111':cse_111['GPA'] ,'CSE-114':cse_114['GPA'] } ,
                   index=[0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,
                          34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62])

#print(df.describe())
df['Total_Credits'] = df['CSE-100']*1+ df['CSE-101']*3 + df['CSE-103']*3 +df['CSE-105']*3 +df['CSE-107']*3 +df['CSE-108']*1 +df['CSE-109']*3 + df['CSE-111']*2 +df['CSE-114']*1
df['CGPA'] = round(df['Total_Credits']/20 ,2)

print("============================================================================")
print("                         Result Corresponding Exam Roll ")
print("============================================================================")
print(df[['Exam_Roll' ,'CGPA']][0:63])





print("============================================================================")
print("                         Result Analysis ")
print("============================================================================")
print(df['CGPA'].describe())





print("============================================================================")
print("                         Creating Result into an Excel Sheet ")
print("============================================================================")
writer = ExcelWriter("C:\\Users\\Tazel\\Desktop\\xlsx\\result.xlsx")
df.to_excel(writer,'Sheet1',index=False)
writer.save()
print("Write Successful")
print("============================================================================")


print("============================================================================")
print("                         Result Section ")
print("============================================================================")

colum=[0,1,2,3,4,5,6,7,8,9,10,11]
cse_result =pd.read_excel("C:\\Users\\Tazel\\Desktop\\xlsx\\result.xlsx",sheet_name="Sheet1",nrows=63,usecols =colum)
choice = int(input("Enter The Exam Roll::"))
print(cse_result.loc[cse_result['Exam_Roll']==choice])
