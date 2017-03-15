from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    header = '<h1>My Application</h1>'
    options = '<p>Optional Resources:'
    options += '/n1+n2, /n1-n2, /n1*n2, /n1+n2.</p>'
    response = header + options
    return HttpResponse(response)

def add(request, num1, num2):
    result = int(num1) + int(num2);
    response = '<h3>ADDITION</h3>'
    response += '<p>%s + %s = %d</p>' % (num1, num2, result)
    return HttpResponse(response)

def sub(request, num1, num2):
    result = int(num1) - int(num2);
    response = '<h3>SUBTRACTION</h3>'
    response += '<p>%s - %s = %d</p>' % (num1, num2, result)
    return HttpResponse(response)

def mult(request, num1, num2):
    result = int(num1) * int(num2);
    response = '<h3>MULTIPLICATION</h3>'
    response += '<p>%s * %s = %d</p>' % (num1, num2, result)
    return HttpResponse(response)

def div(request, num1, num2):
    if int(num2) == 0:
        response = '<h3>DIVISION ERROR!</h3>'
        response += '<p>Not possible to divide by zero'
    else:
        result = float(int(num1) / int(num2));
        response = '<h3>DIVISION</h3>'
        response += '<p>%s / %s = %f</p>' % (num1, num2, result)
        return HttpResponse(response)
    return HttpResponse(response)

def resourceError(request):
    message = ('<h3>Resource not available.</h3>')
    options = '<p>Optional Resources:'
    options += '/n1+n2, /n1-n2, /n1*n2, /n1+n2.</p>'
    response = message + options
    return HttpResponse(response)
