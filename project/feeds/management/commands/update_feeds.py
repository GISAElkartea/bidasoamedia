from django.core.management.base import BaseCommand, CommandError

from project.feeds.models import Feed


class Command(BaseCommand):
    args = 'none'
    help = 'update feeds'

    def handle(self, *args, **kwargs):
        for feed in Feed.objects.iterator():
            feed.update()
