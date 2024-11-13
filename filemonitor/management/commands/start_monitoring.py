from django.core.management.base import BaseCommand
from filemonitor.filemonitor import start_file_monitor

class Command(BaseCommand):
    help = 'Starts file monitoring to restrict file copy outside the root folder'

    def handle(self, *args, **kwargs):
        self.stdout.write("Starting file monitoring...")
        start_file_monitor()
