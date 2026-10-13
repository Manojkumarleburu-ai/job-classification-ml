import streamlit as st
from main import X_test, X_train, Y_train, Y_test, le
from main import y
import pandas as pd
from main import df
import numpy as np
from main import Temparary_Dataframe
st.title('Job Classification using Machine Learning Algorithms')
st.text("""Explore Different Algorithms To Find out Best Algorithm""")
Algorithms=st.sidebar.selectbox("Select Algorithm",("Naive Bayes","Support Vector Machine","Random Forest","Decision Tree","K Neirest Neighbbour"))
st.write(Algorithms)
st.write("Dataset  Shapes",df.shape)
st.write("Number Of Classes In The Dataset",len(np.unique(y)))

if st.checkbox("Show Dataset"):
    number = st.number_input("Number of Rows to view", 5, 850)
    st.dataframe(df.head(number))
if st.button("Column Names"):
    st.write(df.columns)
if st.checkbox("Summary"):
    st.write("The summary", df.describe())


def get_algorithm(Algorithm):
    par=dict()
    if Algorithm=='K Neirest Neighbbour':
       print("a")
    elif Algorithm=="Support Vector Machine":
        print("a")
    elif Algorithm=="Random Forest":
        print("a")
    elif Algorithm=="Naive Bayes":
        print("a")
    elif Algorithm=="Decision Tree":
        print("a")
    return par
parms=get_algorithm(Algorithms)
from sklearn.ensemble import RandomForestClassifier

def get_algorithm_parm(classifier,parms):
    if classifier=="Support Vector Machine":
        from sklearn.svm import SVC
        clf = SVC(C=0.23)
    elif classifier=="Random Forest":
        from sklearn.ensemble import RandomForestClassifier
        clf= RandomForestClassifier(max_depth=4, n_estimators=9,random_state=0)
    elif classifier=="K Neirest Neighbbour":
        from sklearn.neighbors import KNeighborsClassifier
        clf = KNeighborsClassifier(n_neighbors=15)
    elif classifier=="Naive Bayes":
        from sklearn.naive_bayes import GaussianNB
        clf=GaussianNB(var_smoothing=1e-09)

    else:
        from sklearn.tree import DecisionTreeClassifier
        clf = DecisionTreeClassifier(random_state=5, max_depth=8)
    return clf
from sklearn.metrics import accuracy_score,mean_squared_error
clf1=get_algorithm_parm(Algorithms,parms)
clf1.fit(X_train,Y_train)
y_pred = clf1.predict(X_test)
acc = accuracy_score(Y_test, y_pred)
mean=mean_squared_error(y_pred,Y_test)
st.write(f'Classifier = {Algorithms}')
st.write(f'Accuracy =', acc)
st.subheader("Our Prediction")

data=pd.read_csv('jobclassinfo2.csv')
single_col_to_list=data['JobFamilyDescription'].values.tolist()
Ch_to_Set=set(single_col_to_list)
Ch_to_List=list(Ch_to_Set)
# Family1 = st.number_input("Select Family Job",1, 28)
options = list(range(len(Ch_to_List)))
value = st.selectbox("Select Family Job", options=[x for x in Ch_to_List])
for i in range(1,len(Ch_to_List)+1):
    if value=='Accounting And Finance':
        value=1
        break
    elif value=='Administrative Support':
        value=2
        break
    elif value=='Baker':
        value=3
        break
    elif value=='Buildings And Facilities':
        value=4
        break
    elif value =='Buyer':
        value=5
        break

    elif value =='Cashier':
        value=6
        break

    elif value =='Communications And Media':
        value=7
        break

    elif value =='Corporate Research':
        value=8
        break

    elif value =='Finance  And Accounting':
        value=9
        break

    elif value =='Human Resources':
        value=10
        break

    elif value =='Meat Cutter':
        value=11
        break

    elif value =='Produce':
        value=12
        break

    elif value =='Secretary':
        value=13
        break

    elif value=='Stockkeeping':
        value=14
        break

    elif value=='Systems Analyst':
        value=15
        break
    else:
        continue





st.write(value)

PayGrade = st.number_input("Enter The PayGrade", 1, 10)
EducationLevel = st.number_input("Enter The EducationLevel", 1, 6)
Experience = st.number_input("Enter The Experience", 0, 10)
OrgImpact = st.number_input("Enter The OrgImpact", 1, 6)
ProblemSolving = st.number_input("Enter The ProblemSolving", 1, 6)
Supervision = st.number_input("Enter The Supervision", 1, 7)
ContactLevel = st.number_input("Enter The ContactLevel", 1, 8)
FinancialBudget = st.number_input("Enter The FinancialBudget", 1, 11)

l = [value,PayGrade, EducationLevel, Experience, OrgImpact, ProblemSolving, Supervision, ContactLevel, FinancialBudget]
n111 = np.array(l)
st.write(value,PayGrade, EducationLevel, Experience, OrgImpact, ProblemSolving, Supervision, ContactLevel, FinancialBudget)
clf= RandomForestClassifier(n_estimators=600, random_state=42, min_samples_leaf=1, max_features="sqrt",
                                    max_depth=40, bootstrap=False)
clf.fit(X_train,Y_train)
hh = clf.predict(n111.reshape(1,-1))
predicted_value=str()
st.write("Prediction :", le.inverse_transform([hh[0]])[0])
Data_To_List=Temparary_Dataframe['JobClassDescription'].values.tolist()
_Set=set(Data_To_List)
_List=list(_Set)
List=[]
for Iterable in range(1,21):
    List.append(Iterable)
dict={}
for a,b in zip(List,Data_To_List):
    dict[a]=b
    if str(a)==str(16):
        print()
        st.write(b)
        #st.write(type(b))
    else:
        continue