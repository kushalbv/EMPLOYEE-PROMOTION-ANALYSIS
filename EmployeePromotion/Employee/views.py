from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth 
from django.contrib import messages
from .models import EmployeePromotion
# Create your views here.
def index(request):
    return render(request,"index.html")


def register(request):
    if request.method=="POST":
        first=request.POST['fname']
        last=request.POST['lname']
        uname=request.POST['uname']
        email=request.POST['email']
        psw=request.POST['psw']
        psw1=request.POST['psw1']
        if psw==psw1:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"Username Exists")
                return render(request,"register.html")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Exists")
                return render(request,"register.html")
            else:
                user=User.objects.create_user(first_name=first,
                last_name=last,email=email,username=uname,password=psw)
                user.save()
                return redirect('login')
        else:
            messages.info(request,"Password not matching")
            return render(request,"register.html")
    return render(request,"register.html")

def login(request):
    if request.method=="POST":
        username=request.POST['uname']
        psw=request.POST['psw']
        user=auth.authenticate(username=username,password=psw)
        if user is not None:
            auth.login(request,user)
            return redirect('data')
        else:
            messages.info(request,"Invalid Credentials")
            return render(request,"login.html")
    return render(request,"login.html")

def data(request):
    if request.method=="POST":
        dept=request.POST['dept']
        edu=request.POST['edu']
        gender=request.POST['gender']
        recruit=request.POST['recruitment']
        training=int(request.POST['training'])
        age=int(request.POST['age'])
        previous=int(request.POST['previous'])
        length=int(request.POST['length'])
        awards=int(request.POST['awards'])
        avg=int(request.POST['avg'])
        import pandas as pd 
        df=pd.read_csv(r"static/EmployeePromotion.csv")
        print(df.head())
        from sklearn.preprocessing import LabelEncoder
        l=LabelEncoder()
        dept1=l.fit_transform([dept])
        edu1=l.fit_transform([edu])
        gender1=l.fit_transform([gender])
        recruit1=l.fit_transform([recruit])
        
        print(df.isnull().sum())
        print(df.dropna(inplace=True))
        df=df.drop(["employee_id","region"],axis=1)
        import seaborn as sns 
        import matplotlib.pyplot as plt
        sns.set_style('darkgrid')
        sns.catplot(x ='is_promoted', kind='count', data=df)
        plt.show()
        df.hist(bins = 20, figsize = (20,10), color = 'g')
        plt.show()
        plt.figure(figsize=(12, 10))
        sns.catplot(x ='department', kind='count', data=df, palette='husl')
        plt.xticks(rotation=45, horizontalalignment='right')
        plt.show()
        plt.figure(figsize=(12, 10))
        sns.catplot(x='department', hue='is_promoted', kind='count', data=df, palette='husl')
        plt.xticks(rotation=45, horizontalalignment='right')
        plt.show()
        plt.figure(figsize=(12, 10))
        sns.catplot(x ='education', kind='count', data=df, palette='Set1')
        plt.show()
        department=l.fit_transform(df["department"])
        education=l.fit_transform(df["education"])
        gender_2=l.fit_transform(df["gender"])
        recruitment_channel=l.fit_transform(df["recruitment_channel"])

        df=df.drop(["department","education","gender","recruitment_channel"],axis=1)
        df["Department"]=department
        df["Education"]=education
        df["Gender"]=gender_2
        df["Recruitment"]=recruitment_channel

        
        X=df.drop("is_promoted",axis=1)
        y=df["is_promoted"]

        from sklearn.naive_bayes import GaussianNB
        gb=GaussianNB()
        gb.fit(X,y)
        import numpy as np 

        data=np.array([[dept1,edu1,gender1,recruit1,training,age,
        previous,length,awards,avg]],dtype=object)

        prediction=gb.predict(data)
        emp=EmployeePromotion.objects.create(Department=dept,Education=edu,
        Gender=gender,Recruitment=recruit,No_Of_Trainings=training,
        Age=age,Previous_Year_Ratings=previous,Length_Of_Service=length,
        Awards_Won=awards,Average_Trainings=avg,Employee_Promotion=prediction)
        emp.save()
        print(prediction)
        return render(request,"predict.html",{"dept":dept,"edu":edu,
        "gender":gender,"recruit":recruit,"training":training,
        "age":age,"previous":previous,"length":length,
        "awards":awards,"avg":avg,"prediction":prediction})

    return render(request,"data.html")

def predict(request):
    return render(request,"predict.html")

def logout(request):
    auth.logout(request)
    return redirect('/')