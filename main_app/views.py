from django.shortcuts import render

# Create your views here.

# TODO Temporary DUMMY Database - REMOVE THIS AFTER ADDING BOOKMARK MODEL
bookmarks = [
    {'id': '3150',
     'date_created': '04/23/2024', 
     'title' : 'CSS Anchor Is The Best New CSS Feature Since Flexbox', 
     'url' : 'https://www.youtube.com/shorts/fO0XD75u2TI'},
    {'id': '2677',
     'date_created': '05/02/2024', 
     'title' : 'Google apprenticeships for 2024 US', 
     'url' : 'https://www.reddit.com/r/google/comments/18b4tr2/google_apprenticeships_for_2024_us/'},
    {'id': '8142',
     'date_created': '04/29/2024', 
     'title' : 'IBM Apprenticeships', 
     'url' : 'https://www.ibm.com/careers/search?q=apprentice'},
    {'id': '4721',
     'date_created': '05/02/2024', 
     'title' : 'USA Google Software Apprenticeships', 
     'url' : 'https://www.google.com/about/careers/applications/jobs/results/?distance=50&hl=en_US&jlo=en_US&location=United%20States&q=%22Software%20Engineering%20(SWE)%20Apprenticeship%22&src=Online%2FGoogle%20Website%2FByF&utm_campaign=&utm_medium=information_technology_apprenticeship_us&utm_source=byf'},
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def bookmarks_index(request):
    return render(request, 'bookmarks/index.html', {
        'bookmarks': bookmarks
    })