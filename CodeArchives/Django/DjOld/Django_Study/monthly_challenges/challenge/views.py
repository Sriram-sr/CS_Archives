from django.shortcuts import render
from django.http import Http404, HttpResponse,HttpResponseRedirect,HttpResponseNotFound

# Create your views here.
month_dict = {
    "January" : "<h1>This is january</h1>",
    "Febrauary" : "<h1>This is February</h1>",
    "March" : "<h1>This is March</h1>",
    "April" : "<h1>This is April</h1>"
}

def index(request):
    return render(request,"challenge/index.html",{'text_to_capitalise':"hello world",'month_list':list(month_dict.keys())})

def choose_month_number(request,month):
    month_list = list(month_dict.keys())
    display_month = month_list(month)
    return HttpResponseRedirect(f"challenge/{display_month}")

def choose_month(request,month):
    text_to_display = None
    if month == "January" :
       text_to_display = "<h1>The month is January</h1>" 
    elif month == "February" :
        text_to_display = "<h1>The month is February</h1>"
    elif month == "March" :
        text_to_display = "<h1>The month is March</h1>"    
    else :
        # return HttpResponseNotFound("<h1>Enter a valid month</h1>")
        return Http404()
    return HttpResponse(text_to_display)  



