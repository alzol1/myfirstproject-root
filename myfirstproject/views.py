from django.http import HttpResponse
from django.shortcuts import render


def about(request):
	return HttpResponse('Это страница "О нас"')


def home(request):
	return render(request, 'home.html', {'greeting':'Hello <br> <label for="w3review">Review of W3Schools:</label><textarea id="w3review" name="w3review" rows="4" cols="50">At w3schools.com you will learn how to make a website. They offer free tutorials in all web development technologies.</textarea>'})