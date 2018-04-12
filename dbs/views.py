from django.shortcuts import render
from django.http import HttpResponse
from .models import studentdb
from django.template.loader import get_template
from datetime import datetime

# Create your views here.
def homepage(request):
    template = get_template('index.html')
    students = studentdb.objects.all()
    print(students)
    html = template.render(locals())
    # post_lists = list()
    # for count, post in enumerate(posts):
    #     post_lists.append("No.{}:".format(str(count)) + str(post) + "<br>")
    #     post_lists.append("<small>" + str(post.body.encode('utf-8')) + "</small> <br><br>")
    return HttpResponse(html)