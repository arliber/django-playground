from django.http import HttpResponse, JsonResponse
from .models import Post, Author
from django.utils import timezone
from django.core.serializers import serialize

def posts(request):
    posts_serialized = serialize('json', Post.objects.all())
    return HttpResponse(posts_serialized, content_type='application/json')    


def authors(request):
    authors_serialized = serialize('json', Author.objects.all())
    return HttpResponse(authors_serialized, content_type='application/json') 


def new_post(request):
    new_post = Post(body=request.POST['body'], )
    try:
        selected_author = Author.objects.get(pk=request.POST['author'])
        new_post = Post(body=request.POST['body'], category=request.POST['category'], pub_date=timezone.now(), author=selected_author)
        new_post.save()
    except ():
        return JsonResponse({'error': 'unable to save post'})
    else:
        return posts(request)


def recently_published_posts(request):
    return JsonResponse({'count': 6}, safe=False) 
    