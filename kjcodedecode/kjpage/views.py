from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
import requests
import json
import datetime
from operator import itemgetter
from django.contrib import messages
import re
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import question,answer,Student
# Create your views here.
def home(request):
    u=request.META.get("HTTP_REFERER")
    # print(u.split("/"))
    print("////////")
    print(u)
    print("########")
    return render(request,"home.html")
@login_required
def code(request):
    x=re.split("^([0-9]{1,3})-([a-zA-Z]{3})-([0-9]{4})\s\(([0-9]{1,3}):([0-9]{1,3}):([0-9]{1,3})\)$",request.session["timer"])

    return render(request,"question.html",{"time":x})
def postdata(request):
    if request.method=='POST':
        code=request.POST['code']
        inputdata=request.POST['inputdata']
        lang=request.POST['lang']
        print(code,inputdata,lang)
        headers = {
        'authority': 'ide.geeksforgeeks.org',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://ide.geeksforgeeks.org',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'referer': 'https://ide.geeksforgeeks.org/',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,mr;q=0.7',
        'cookie': '__gads=Test; __utmz=245605906.1574330848.3.3.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utma=245605906.76497464.1571747970.1571828951.1574330845.3; _ga=GA1.2.76497464.1571747970; _gid=GA1.2.244651628.1579195481; _gat=1; _gat_gtag_UA_144087254_1=1',
        }
        print(type(code),type(inputdata))
        data = {
        'lang': lang,
        'code': code,
        'input': inputdata,
        'save': 'false'
        }
        rightanswer1='***********\n *********\n  *******\n   *****\n    ***\n     *\n'
        rightanswer2=3
        response = requests.post('https://ide.geeksforgeeks.org/main.php', headers=headers, data=data)
        output=response.json()['output']
        print(response.json())
        # print("//////////")
        # print(output)
        # print("##########")
        # u=request.META.get('HTTP_REFERER',"/")
        # prev_url=u.split("/")[-2]
        if output==rightanswer1 or int(output)==rightanswer2:
            o=True
            
        else:
            o=False
        # print("//////////")
        # print(o)
        # print("##########")
        
        # print("/////////////////")
        
        # print("############")

        return JsonResponse({'output':output,"result":o})

def mcq(request):
    if request.user.is_authenticated:
        print("//////////////////")
        print(request.user.id)
        print("###############")
        q=question.objects.all()
        answers=[]
        symbols=["A","B","C","D"]
        for i in q:
            answers.append(list(zip(i.answer_set.all(),symbols)))


        m=list(zip(q,answers))
        print(q,answers)
        print(m)
        for i in m:
            
            print(i)
           
            for j in i[1]:
                
                print(j)
                
        x=re.split("^([0-9]{2})-([a-zA-Z]{3})-([0-9]{4})\s\(([0-9]{2}):([0-9]{2}):([0-9]{2})\)$",request.session["timer"])
        for i in x:
            print(i)

        return render(request,"mcq.html",{"values":m,"time":x})
    else:
        
        return redirect("/")

def mcqpost(request):
    if request.method=="POST":
        marks1=request.POST["marks"]
        print("################")
        print(marks1)
        print("###########")
        s,created=Student.objects.get_or_create(user_id=request.user.id)
        s.marks=marks1
        s.save()
        
    return redirect("/score/")
@login_required
def score(request):
    q=question.objects.all()
    s=Student.objects.get(user_id=request.user.id)
    correct=s.marks
    wrong=len(q)-correct
    result="PASS" if correct>wrong else "FAIL"
    x=re.split("^([0-9]{2})-([a-zA-Z]{3})-([0-9]{4})\s\(([0-9]{2}):([0-9]{2}):([0-9]{2})\)$",request.session["timer"])

    return render(request,"score.html",{"total":len(q),"c":correct,"w":wrong,"r":result,"time":x})

@login_required
def algo(request):
    x=re.split("^([0-9]{2})-([a-zA-Z]{3})-([0-9]{4})\s\(([0-9]{2}):([0-9]{2}):([0-9]{2})\)$",request.session["timer"])

    return render(request,"algorithm.html",{"time":x})

@login_required
def submit(request):
    S=Student.objects.get(user_id=request.user.id)
    time=datetime.datetime.strptime(request.session["timer"],"%d-%b-%Y (%H:%M:%S)")
    time_calc=time-datetime.datetime.now()

    mins=time_calc.seconds//60
    seconds = time_calc.seconds%60
    mins_diff=60-mins-1
    sec_diff=60-seconds
    total_diff=f"{mins_diff} : {sec_diff}"
    print(time_calc,mins,seconds)
    print(total_diff)
    S.time=total_diff
    S.save()
    return redirect("leaderboard")
@login_required
def leaderboard(request):
    s=Student.objects.all()
    win=[]
    k=1
    for i in s:
        if i.time!="":
            win.append([k,i.user.first_name+" "+i.user.last_name,i.time,int(i.time[:2]),int(i.time[4:])])
    print(win)
    win_calc=sorted(win,key=itemgetter(3,4))   
    for i in win_calc:
        i[0]=k
        k+=1
    print(win_calc)    
    return render(request,"leaderboard.html",{"students":win_calc})