from celery import task

from project.feeds.models import Feed


@task
def update_feeds():
    ( feed.update() for feed in Feed.objects.iterator() )
