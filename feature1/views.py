from django.shortcuts import render
from datetime import date


post=[
    {
        "slug":"hike_in the_mountain",
        "image":"mountains.jpg",
        "author":"Deepak",
        "Date":date(2022,8,12),
        "title":"Mountain_hiking",
        "excerpt":"These mountains are an epitome of grandeur and resilience,a living testament to the earth's might.",
        "content":"""Lorem ipsum dolor sit amet consectetur adipisicing elit. Consequatur, adipisci sit distinctio officia maiores laborum veniam
         iste possimus ab officiis consequuntur illum ratione. Perferendis, cupiditate aliquam quas quos dicta architecto?
         
         Lorem ipsum dolor sit amet consectetur adipisicing elit. Consequatur, adipisci sit distinctio officia maiores laborum veniam
         iste possimus ab officiis consequuntur illum ratione. Perferendis, cupiditate aliquam quas quos dicta architecto?
         
         Lorem ipsum dolor sit amet consectetur adipisicing elit. Consequatur, adipisci sit distinctio officia maiores laborum veniam
         iste possimus ab officiis consequuntur illum ratione. Perferendis, cupiditate aliquam quas quos dicta architecto?
         
         Lorem ipsum dolor sit amet consectetur adipisicing elit. Consequatur, adipisci sit distinctio officia maiores laborum veniam
         iste possimus ab officiis consequuntur illum ratione. Perferendis, cupiditate aliquam quas quos dicta architecto?"""
    },
    {
        "slug":"mountain",
        "image":"woods.jpg",
        "author":"Deepak",
        "Date":date(2026,7,5),
        "title":"Mountain_hiking",
        "excerpt":"These mountains are an epitome of grandeur and resilience,a living testament to the earth's might.",
        "content":"""Lorem ipsum dolor sit amet consectetur adipisicing elit. Consequatur, adipisci sit distinctio officia maiores laborum veniam
         iste possimus ab officiis consequuntur illum ratione. Perferendis, cupiditate aliquam quas quos dicta architecto?
         
         Lorem ipsum dolor sit amet consectetur adipisicing elit. Consequatur, adipisci sit distinctio officia maiores laborum veniam
         iste possimus ab officiis consequuntur illum ratione. Perferendis, cupiditate aliquam quas quos dicta architecto?
         
         Lorem ipsum dolor sit amet consectetur adipisicing elit. Consequatur, adipisci sit distinctio officia maiores laborum veniam
         iste possimus ab officiis consequuntur illum ratione. Perferendis, cupiditate aliquam quas quos dicta architecto?
         
         Lorem ipsum dolor sit amet consectetur adipisicing elit. Consequatur, adipisci sit distinctio officia maiores laborum veniam
         iste possimus ab officiis consequuntur illum ratione. Perferendis, cupiditate aliquam quas quos dicta architecto?"""
    },
    {
        "slug":"hike_mountain",
        "image":"mountains.jpg",
        "author":"Deepak",
        "Date":date(2023,2,12),
        "title":"Mountain_hiking",
        "excerpt":"These mountains are an epitome of grandeur and resilience,a living testament to the earth's might.",
        "content":"""Lorem ipsum dolor sit amet consectetur adipisicing elit. Consequatur, adipisci sit distinctio officia maiores laborum veniam
         iste possimus ab officiis consequuntur illum ratione. Perferendis, cupiditate aliquam quas quos dicta architecto?
         
         Lorem ipsum dolor sit amet consectetur adipisicing elit. Consequatur, adipisci sit distinctio officia maiores laborum veniam
         iste possimus ab officiis consequuntur illum ratione. Perferendis, cupiditate aliquam quas quos dicta architecto?
         
         Lorem ipsum dolor sit amet consectetur adipisicing elit. Consequatur, adipisci sit distinctio officia maiores laborum veniam
         iste possimus ab officiis consequuntur illum ratione. Perferendis, cupiditate aliquam quas quos dicta architecto?
         
         Lorem ipsum dolor sit amet consectetur adipisicing elit. Consequatur, adipisci sit distinctio officia maiores laborum veniam
         iste possimus ab officiis consequuntur illum ratione. Perferendis, cupiditate aliquam quas quos dicta architecto?"""
    }
    
]

# Create your views here.
def get_date(post):
    return post['Date']

def landing_page(request):
    sorted_date=sorted(post,key=get_date)
    last_post=sorted_date[:3]
    return render(request,"feature1/index.html",{
        "post":last_post
    })

def post_list(request):
    return render(request,"feature1/post_page.html")


def post_description(request,slug):
    return render(request,"feature1/singlepost.html")