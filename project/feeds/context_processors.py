from itertools import chain

from project.feeds.models import Feed

def feed_list(request):
    feeds = chain(( feed.parse() for feed in Feed.objects.iterator() ))
    return {'feed_list': feeds}
