# Custom file created - Astrophile :D
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlinerem = request.POST.get('newlinerem', 'off')
    spacerem = request.POST.get('spacerem', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == 'on':
        punctuations = '''!()=[]{};:'"\,<>./?@#$%^&*_~|'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        djtext = analyzed
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)

    if fullcaps == 'on':
        analyzed = djtext.upper()
        djtext = analyzed
        params = {'purpose': 'UpperCased Text', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)

    if newlinerem == 'on':
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed += char
        djtext = analyzed
        params = {'purpose': 'Remove New lines', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)

    if spacerem == 'on':
        analyzed = ""
        for ind,char in enumerate(djtext):
            if not(djtext[ind] == djtext[ind+1] == " "):
                analyzed += char
        djtext = analyzed
        params = {'purpose': 'Remove New lines', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)

    if charcount == 'on':
        analyzed = "Total number of characters in your text is: "
        count = 0
        punctuations = '''!()=[]{};:'"\,<>./?@#$%^&*_~| '''
        for char in djtext:
            if char not in punctuations or char != "\n":
                count += 1
        analyzed += str(count)
        params = {'purpose': 'Character Counter', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)

    # params = {'purpose': 'Test Original text', 'analyzed_text': djtext}
    if removepunc == fullcaps == newlinerem == spacerem == charcount == 'off':
        return HttpResponse("Error")
    
    return render(request, 'analyze.html', params)