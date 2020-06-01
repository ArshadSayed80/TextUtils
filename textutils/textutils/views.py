# I Have created this file - Arshad
from django.http import HttpResponse
from django.shortcuts import render


def index(requests):
    return render(requests, 'index.html')


def about(requests):
    return HttpResponse("About")


def removepunc(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    newline = request.POST.get('newline', 'off')
    space = request.POST.get('space', 'off')
    charcount = request.POST.get('charcount', 'off')
    purpose = ""
    if removepunc == "on":
        puntuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in puntuations:
                analyzed = analyzed + char
        purpose = "Puntuations Removed"
        djtext = analyzed
    if capitalize == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        purpose = "Converted to upper case"
        djtext = analyzed
    if newline == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        purpose = "Removed New Line"
        djtext = analyzed
    if space == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        purpose = "Removed spaces"
        djtext = analyzed
    if charcount == "on":
        analyzed = ""
        count = 0
        for char in djtext:
            analyzed = analyzed + char
            if char != "\n" and char != " ":
                count = count + 1
        analyzed = analyzed + "is having " + str(count) + " characters excluding spaces"
        purpose = "Character counter"
    if charcount == "off" and space == "off" and newline == "off" and capitalize == "off" and removepunc == "off":
        analyzed = ""
        purpose = "Invalid Option/Error"
        analyzed = "You did not select any radio button"

    params = {'purpose': purpose, 'analyzed_text': analyzed}
    return render(request, 'removepunc.html', params)
