from django.core.management.base import BaseCommand
from measurements.utils import import_measurement

class Command(BaseCommand):
    help = "IMPORT MEASUREMENTS from CSV"

    def add_arguments(self, parser):
        parser.add_argument("n", type=int, help="liczba powtórzeń")

    def handle(self, *args, **options):
        n = options["n"]
        import_measurement(n)
        print('Measurements imported successfully.')
