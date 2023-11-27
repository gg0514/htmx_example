from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse("Hello, htmx!")


def basic(request):
    
    context= { "key": "value" }
    return render(request, "basic.html", context)


def get_user_data(request):

    print("get_user_data()")

    str= '''
    <div class="user-profile">
    <h2>John Doe</h2
    <p>Software Developer at XYZ Corp.</p>
    </div>
    '''
    
    return HttpResponse(str)


def dummy(request):

    print("dummy()")

    return HttpResponse(status= 200)
