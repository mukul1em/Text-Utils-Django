from django.http import HttpResponse

from django.shortcuts import render
import string
from string import digits 
import re

def index(request):
    
    return render(request,'index.html')
    #return HttpResponse('home')


def analyze(request):
    djtext=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    removedigit=request.GET.get('removedigit','off')
    stringlower=request.GET.get('stringlower','off')
    punctuations=string.punctuation
    
    print(removepunc)
    print(djtext)
    if removepunc == "on":
        analyzed=re.sub('[^A-Za-z0-9]+', ' ', djtext)
    if removedigit=='on':
        anal = str.maketrans('', '', digits) 
        analyzed =analyzed.translate(anal)
    if stringlower=='on':
        analyzed=analyzed.lower()
    params={'purpose':'remove punctuations','analyzed_text':analyzed}
    return render(request,'analyze.html',params)






