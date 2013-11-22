from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

def logout_page():
    return "ok"

def main():
    return "ok"

def main_page(request):
    return render_to_response('index.html')
