import pandas as pd
import numpy as np

dft1 = pd.read_excel('data/Jul2016.xlsx')
dft2 = pd.read_excel('data/Jan2017.xlsx')

df = pd.concat([dft1,dft2], axis= 0)
df = df.drop(columns= ['Email Id'])
df2 = pd.read_excel('data/level2.xlsx')
df2 = df2.drop(columns= ['Email'])
df2 = df2.fillna(0)

new_names1 = list()
old_names = list(df["Name"])
for name in old_names :
    temp = str()
    for word in name.lower().split() :
        temp = temp + word
    new_names1.append(temp)
    temp = str()

df["Name"] = new_names1

new_names2 = list()
old_names = list(df2["Name"])
for name in old_names :
    temp = str()
    for word in name.lower().split() :
        temp = temp + word
    new_names2.append(temp)
    temp = str()

df2["Name"] = new_names2

#Merging rows in past data

df = df.groupby('Name')['Enrolled courses count','Scholarship request count','Approved','Exam Reg Count','Score from assignment','Exam score','Final score','Exam count','Topper count'].sum()
new_names1 = list(df.index.values)
df.index = list(range(0,1171)) 
df = pd.concat([pd.DataFrame(new_names1, columns= ['Name']),df], axis= 1)

#Counting overlap
count_old = int(0)
for name in new_names1 :
    if name in new_names2 :
        count_old += 1
print(count_old)

#Creating master dataframe for new candidates
master = list()
masternames = sorted(new_names2)

for name in new_names2 :
    row = df2[df2["Name"] == name]
    if name not in new_names1 :
        PEnC,PSchReq,PSchApp,PExamReg,PAssignScore,PExamScore,PFinalScore,PExamCs,PTopper = 0,0,0,0,0,0,0,0,0
    else :
        row1 = df[df["Name"] == name]
        PEnC,PSchReq,PSchApp,PExamReg,PAssignScore,PExamScore,PFinalScore,PExamCs,PTopper = row1.iloc[0,1], row1.iloc[0,2], row1.iloc[0,3],row1.iloc[0,4], row1.iloc[0,5], row1.iloc[0,6], row1.iloc[0,7], row1.iloc[0,8], row1.iloc[0,9]

    CurEnrol,CurGradYear,CurSchol = row.iloc[0,1], row.iloc[0,2], row.iloc[0,5]
    if CurEnrol > 4 :
        CurEnrol = 4
    if PSchApp >= 1 or PTopper >=1 :
        CurAssignScore = np.random.randint(50,101)
    else :
        CurAssignScore = np.random.randint(0,101)
    master.append([name,PEnC,PSchReq,PSchApp,PExamReg,PAssignScore,PExamScore,PFinalScore,PExamCs,PTopper,CurEnrol,CurGradYear,CurAssignScore,CurSchol])

master = pd.DataFrame(master, columns= ['Name','PEnC','PSchReq','PSchApp','PExamReg','PAssignScore','PExamScore','PFinalScore','PExamCs','PTopper','CurEnrol','CurGradYear','CurAssignScore','CurSchol'])
master.to_csv("data/master.csv", index= False)