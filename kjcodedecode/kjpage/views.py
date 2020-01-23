from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
import requests
import json
from .models import question,answer,Student
# Create your views here.
def home(request):
    return render(request,"home.html")
def code(request):
    return render(request,"question.html")
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

        response = requests.post('https://ide.geeksforgeeks.org/main.php', headers=headers, data=data)
        output=response.json()['output']
        print(output)
        
        return JsonResponse({'output':output})
def mcq(request):
    q=question.objects.all()
    answers=[]
    symbols=["A","B","C","D"]
    for i in q:
        answers.append(list(zip(i.answer_set.all(),symbols)))
        
    
    m=list(zip(q,answers))
    print(q,answers)
    print(m)
    for i in m:
        print("**********")
        print(i)
        print("**********")
        for j in i[1]:
            print("#######")
            print(j)
            print("#######")


    return render(request,"mcq.html",{"values":m})

def mcqpost(request):
    print(request.POST)
    return redirect("/")