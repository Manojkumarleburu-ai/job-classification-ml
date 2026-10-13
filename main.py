import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
le=LabelEncoder()
df1=pd.read_csv('jobclassinfo2.csv')

df1=df1.astype(str)
df1['PG']=le.fit_transform(df1['PG'])
for jdDescription in range(len(df1['JobClassDescription'])):
    Temparary_Variale=df1['JobClassDescription'][jdDescription]
    List=Temparary_Variale.split()
    if List[0]=='Accountant':
        df1['JobClassDescription'][jdDescription]='Accountant'
    else:
        continue

for jdDescription in range(len(df1['JobClassDescription'])):
    Temparary_Variale = df1['JobClassDescription'][jdDescription]
    List = Temparary_Variale.split()
    if List[0]=='Admin':
        df1['JobClassDescription'][jdDescription]='Admin'
    else:
        continue

for jdDescription in range(len(df1['JobClassDescription'])):
    Temparary_Variale = df1['JobClassDescription'][jdDescription]
    List = Temparary_Variale.split()
    if List[0]=='Administrative':
        df1['JobClassDescription'][jdDescription] = 'Administrative'
    else:
        continue

for jdDescription in range(len(df1['JobClassDescription'])):
    Temparary_Variale = df1['JobClassDescription'][jdDescription]
    List = Temparary_Variale.split()
    if List[0] == 'Baker':
        df1['JobClassDescription'][jdDescription] = 'Baker'
    else:
        continue

for jdDescription in range(len(df1['JobClassDescription'])):
    Temparary_Variale = df1['JobClassDescription'][jdDescription]
    List = Temparary_Variale.split()
    if List[0] == 'Facilities':
        df1['JobClassDescription'][jdDescription] = 'Facilities'
    else:
        continue

for jdDescription in range(len(df1['JobClassDescription'])):
    Temparary_Variale = df1['JobClassDescription'][jdDescription]
    List = Temparary_Variale.split()
    if List[0] == 'Maintenance':
        df1['JobClassDescription'][jdDescription] = 'Maintenance'
    else:
        continue

for jdDescription in range(len(df1['JobClassDescription'])):
    Temparary_Variale = df1['JobClassDescription'][jdDescription]
    List = Temparary_Variale.split()
    if List[0] == 'Buyer':
        df1['JobClassDescription'][jdDescription] = 'Buyer'
    else:
        continue

for jdDescription in range(len(df1['JobClassDescription'])):
    Temparary_Variale = df1['JobClassDescription'][jdDescription]
    List = Temparary_Variale.split()
    if List[0] == 'Cashier':
        df1['JobClassDescription'][jdDescription] = 'Cashier'
    else:
        continue

for jdDescription in range(len(df1['JobClassDescription'])):
    Temparary_Variale = df1['JobClassDescription'][jdDescription]
    List = Temparary_Variale.split()
    if List[0] == 'Communications':
        df1['JobClassDescription'][jdDescription] = 'Communications'
    else:
        continue

for jdDescription in range(len(df1['JobClassDescription'])):
    Temparary_Variale = df1['JobClassDescription'][jdDescription]
    List = Temparary_Variale.split()
    if List[0] == 'Photographer':
        df1['JobClassDescription'][jdDescription] = 'Photographer'
    else:
        continue

for jdDescription in range(len(df1['JobClassDescription'])):
    Temparary_Variale = df1['JobClassDescription'][jdDescription]
    List = Temparary_Variale.split()
    if List[0] == 'Printing':
        df1['JobClassDescription'][jdDescription] = 'Printing'
    else:
        continue

for jdDescription in range(len(df1['JobClassDescription'])):
    Temparary_Variale = df1['JobClassDescription'][jdDescription]
    List = Temparary_Variale.split()
    if List[0] == 'Data':
        df1['JobClassDescription'][jdDescription] = 'Data Scientist'
    else:
        continue

for jdDescription in range(len(df1['JobClassDescription'])):
    Temparary_Variale = df1['JobClassDescription'][jdDescription]
    List = Temparary_Variale.split()
    if List[0] == 'Research':
        df1['JobClassDescription'][jdDescription] = 'Research  Analyst'
    else:
        continue

for jdDescription in range(len(df1['JobClassDescription'])):
    Temparary_Variale = df1['JobClassDescription'][jdDescription]
    List = Temparary_Variale.split()
    if List[0] == 'Financial':
        df1['JobClassDescription'][jdDescription] = 'Financial  Officer'
    else:
        continue


for jdDescription in range(len(df1['JobClassDescription'])):
    Temparary_Variale = df1['JobClassDescription'][jdDescription]
    List = Temparary_Variale.split()
    if List[0] == 'Human':
        df1['JobClassDescription'][jdDescription] = 'Human Resources'
    else:
        continue

for jdDescription in range(len(df1['JobClassDescription'])):
    Temparary_Variale = df1['JobClassDescription'][jdDescription]
    List = Temparary_Variale.split()
    if List[0] == 'Meat':
        df1['JobClassDescription'][jdDescription] = 'Meat Cutter'
    else:
        continue

for jdDescription in range(len(df1['JobClassDescription'])):
    Temparary_Variale = df1['JobClassDescription'][jdDescription]
    List = Temparary_Variale.split()
    if List[0] == 'Produce':
        df1['JobClassDescription'][jdDescription] = 'Produce'
    else:
        continue

for jdDescription in range(len(df1['JobClassDescription'])):
    Temparary_Variale = df1['JobClassDescription'][jdDescription]
    List = Temparary_Variale.split()
    if List[0] == 'Secretary':
        df1['JobClassDescription'][jdDescription] = 'Secretary'
    else:
        continue

for jdDescription in range(len(df1['JobClassDescription'])):
    Temparary_Variale = df1['JobClassDescription'][jdDescription]
    List = Temparary_Variale.split()
    if List[0] == 'StockKeeper':
        df1['JobClassDescription'][jdDescription] = 'StockKeeper'
    else:
        continue

for jdDescription in range(len(df1['JobClassDescription'])):
    Temparary_Variale = df1['JobClassDescription'][jdDescription]
    List = Temparary_Variale.split()
    if List[0] == 'Systems':
        df1['JobClassDescription'][jdDescription] = 'Systems Analyst'
    else:
        continue

df1.drop(['ID', 'JobClass', 'JobFamilyDescription'], axis=1, inplace=True)
Temparary_Dataframe=df1
from sklearn.ensemble import RandomForestClassifier
df1['JobClassDescription']=le.fit_transform(df1['JobClassDescription'])

df2=df1
df3=df1
df4=df1
df5=df1
df6=df1
df7=df1
df8=df1
df9=df1
df10=df1
df11=df1
df12=df1
df13=df1

df=pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13],axis=0)
y=df['JobClassDescription']
x=df[[ 'JobFamily', 'PayGrade', 'EducationLevel', 'Experience','OrgImpact', 'ProblemSolving', 'Supervision', 'ContactLevel','FinancialBudget']]
X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=0.3,random_state=0)
model=RandomForestClassifier()
model.fit(X_train,Y_train)
# model.feature_importances_
# # #model.feature_importances_
# # #array([0.17805327, 0.0949804 , 0.10650154, 0.11402224, 0.07051124,0.08095129, 0.06878235, 0.09952623, 0.10440676, 0.08226467])
from sklearn.naive_bayes import GaussianNB
model=GaussianNB()
model.fit(X_train,Y_train)
y_pred=model.predict(X_test)

