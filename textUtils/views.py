# I have created this file - Akash

# here we import http module
from django.http import HttpResponse

# here we import render from django.shortcuts to request template files like html
from django.shortcuts import render



# this function is for index page, where we transmit index file
def index(request):
    # rander takes three argument req, filename, dictonary
    return render(request, 'index.html')


# this function is for analyzed page, where we transmit analyzed file
def analyzed(request):

    # getting the text from user
    userText = request.POST.get('user-text', 'default')

    # getting the value of check box if its off
    removepunc = request.POST.get('removepunc', 'off')

    # getting the value of check box if its off
    fullcap = request.POST.get('fullcap', 'off')

    # getting the value of check box if its off
    lowercase = request.POST.get('lowercase', 'off')

    # getting the value of check box if its off
    charcount = request.POST.get('charcount', 'off')

    # getting the value of check box if its off
    newlineremove = request.POST.get('newlineremove', 'off')

    # getting the value of check box if its off
    removeextraspace = request.POST.get('removeextraspace', 'off')


    # condition for remove punc 
    if removepunc == 'on':

        # all character we have to remove
        punctuations = '''`~!@#$%^&*()_+-=}{[]:\"';><.,?/|'''

        # here we store pure text by loop
        analyzed = ""

        # loop to analyzed the text if they have special signs or not
        for char in userText:
            if char not in punctuations:
                analyzed = analyzed + char

        # updating user text value
        userText = analyzed

    # condition for upper case
    if fullcap == 'on':

        # here we store pure text by loop
        analyzed = ""

        # loop to analyzed the text if they are n upper case or not
        for char in userText:
            analyzed = analyzed + char.upper()

        # updating user text value
        userText = analyzed

    # condition for lower case
    if lowercase == 'on':

        # here we store pure text by loop
        analyzed = ""

        # loop to analyzed the text if they are n lower case or not
        for char in userText:
            analyzed = analyzed + char.lower()

        # updating user text value        
        userText = analyzed

    # condition for char count
    if charcount == 'on':

        # here we store pure text by loop
        analyzed = 0

        # loop to count the char
        for char in userText:
            if char == " ":
                pass
            else:
                analyzed = analyzed + 1

        # updating user text value        
        userText = analyzed

    # loop to analyzed the text if they have extra new line or not
    if newlineremove == 'on':

        # here we store pure text by loop
        analyzed = ""

        # loop to remove extra line
        for char in userText:
            if char != "\n" and char != "\r":
                analyzed =  analyzed + char

        # updating user text value        
        userText = analyzed

    # loop to analyzed the text if they have extra spaces or not
    if removeextraspace == 'on':

        # here we store pure text by loop
        analyzed = ""

        # loop to remove extra spaces
        for index, char in enumerate(userText):
            if userText[index] == " " and userText[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char

        # updating user text value        
        userText = analyzed

    # when every opration is off it gives error
    if removepunc != 'on' and fullcap != 'on' and lowercase != 'on' and charcount != 'on' and newlineremove != 'on' and removeextraspace != 'on':
        return HttpResponse("Error! you have not use any feature")

    # dictonary
    params = {'purpose': 'Your purefy text is', 'analyzed_text': analyzed}
    
    # returning data to analyzed page
    return render(request, 'analyzed.html', params)





# this function is for about us page, where we transmit about us file
def aboutus(request):
    return render(request, 'aboutus.html')

# this function is for contact us page, where we transmit contact us file
def contactus(request):
    return render(request, 'contactus.html')
