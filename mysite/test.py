from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index3.html')


def analyzer(request):
    global params

    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    newlineremov = request.POST.get('newlineremov', 'off')
    spaceremover = request.POST.get("spaceremover", "off")
    charcount = request.POST.get("charcount", "off")
    if removepunc == "on":
        punctuations = '''"!#$%&()*+,-./:;<=>?@[\]^`'{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {"purpose": "Remove Punctuations", "analyzed_text": analyzed}
        djtext = analyzed

    if capitalize == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {"purpose": "Char in Capitalization", "analyzed_text": analyzed}
        djtext = analyzed

    if newlineremov == 'on':
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {"purpose": "New Line Removed", "analyzed_text": analyzed}
        djtext = analyzed

    if spaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {"purpose": "Space Remover", "analyzed_text": analyzed}
        djtext = analyzed

    if charcount == 'on':
        analyzed = ""
        for char in djtext:
            if len(char) != 0:
                analyzed = analyzed + char
        params = {"purpose": "Char Count", "analyzed_text": len(analyzed)}

    if removepunc != "on" and capitalize != "on" and newlineremov != "on" and spaceremover != "on" and charcount != "on":
        return HttpResponse("Please Select any One Option to Continue")

    return render(request, "analyze.html", params)
