from typing import Any, Optional
from django.core.management.base import BaseCommand
from psycopg2 import OperationalError as PsyError

from django.db.utils import OperationalError
import time


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("Waiting for DB....")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default',])
                db_up = True
            except (PsyError, OperationalError) as e:
                print(e)
                self.stdout.write("Database unavailable, wait for 1 sec....")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS(
            "Database available!"))
