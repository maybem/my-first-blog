from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

def post_list(request):
	return render(request,'blog/post_list.html',{})


#def another(request):
#	return HttpResponse("Ala ma kota, ale na innym widoku")

