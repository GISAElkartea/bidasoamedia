from project.feeds.models import Feed

def feed_list(request):
    return {'feed_list': Feed.objects.iterator()}
