from django.http import HttpResponse
from django.shortcuts import render
def show(request):
    return HttpResponse("Hello Sachin")
def grow(request):
    return HttpResponse("This is sachin Jaiswal and I'm in Pain Please Understand me")
def index(request):
    return render(request, 'index.html')
def student(request):
    checking=request.GET.get('check1','off')
    text_area=request.GET.get('text','default')
    print(checking)
    print(text_area)
def indexing(request):
    return render(request, 'index1.html')

def textareacheck(request):
    textchecking = request.GET.get('textcheck','off')
    text = request.GET.get('textcheck1','default')
    removepun= request.GET.get('removepunc','off')
    upcaser= request.GET.get('uppercase','off')
    punctuation='''!()[]{}/?";:^'*@&#$%\|<>,.'''
    analyzed=" "
    print(text)
    print(textchecking)
    print(removepun)
    print(upcaser)
    if textchecking=="on" and removepun=="on" and upcaser=="on":
        for char in text:
            if char not in punctuation:
                analyzed=analyzed+char.upper()
        return HttpResponse(f"Text with textcheck and punctuation and uppercase: {analyzed}")
    elif textchecking=="on" and removepun=="on":
        for char in text:
            if char not in punctuation:
                analyzed=analyzed+char
        return HttpResponse(f"Text with textcheck and punctuation: {analyzed}")

    elif upcaser=="on" and textchecking=="on":
        for char in text:
            analyzed=analyzed+char.upper()
        return HttpResponse(f"YOUR Upper TEXT and textcheck is: {analyzed}")
    elif removepun=="on" and upcaser=="on":
       for char in text:
           if char not in punctuation:
               analyzed=analyzed+char.upper()
       return HttpResponse(f"Text with textcheck and punctuation and uppercase: {analyzed}")
    elif textchecking=="on":
        return HttpResponse(f"Hello {text}")
    elif removepun=="on":
        for char in text:
            if char not in punctuation:
                analyzed=analyzed+char
        return HttpResponse(f"Text without punctuation: {analyzed}")
    elif upcaser=="on":
        for char in text:
            analyzed=analyzed+char.upper()
        return HttpResponse(f"YOUR CAPS TEXT: {analyzed}")
    return render(request,'index.html',{'textcheck1':text})