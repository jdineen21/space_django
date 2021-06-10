import logging

from spacex.tasks import Database
from django.conf import settings
from django.core.management.base import BaseCommand

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Runs spacex api db update.'

    def handle(self, *args, **options):
        Database.update()
        