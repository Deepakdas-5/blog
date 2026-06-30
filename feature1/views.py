from django.shortcuts import render

# Create your views here.
def landing_page(request):
    return render(request,"feature1/index.html")

def post_list(request):
    pass


def post_description(request):
    pass