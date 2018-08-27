#from django.http import HttpResponse
from django.shortcuts import render

#import the time to display the day time of java

from django.utils import timezone

now = timezone.now()


from django.http import HttpRequest
request = HttpRequest()

def hello(request):
#	return HttpResponse("Hello world! This is my first attempt for the CAM2 Training Material")
	ip = get_client_ip(request)
	
	context = {}
	context['hello'] = 'Hello World! This is WHB Trying the Training Material!'
	context['timenow'] = now
	context['ipaddr' ] = ip
	return render(request, 'hello.html', context)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
