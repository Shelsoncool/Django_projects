from django.shortcuts import render

# Create your views here.
def post(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'myapp/index.html')
