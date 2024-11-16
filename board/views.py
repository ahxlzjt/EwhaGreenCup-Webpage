from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
import uuid

def board(request):

    if request.method == "GET":
        return render(request, 'page/index.html')