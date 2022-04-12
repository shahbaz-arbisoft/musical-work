from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
import csv
import os

from currencyrates.models import Currencies


class Command(BaseCommand):
    help = 'populates currencies table'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model_name = Currencies

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, help='filename for csv file')

    def get_current_app_path(self):
        return apps.get_app_config('currencyrates').path

    def get_csv_file(self, filename):
        app_path = self.get_current_app_path()
        file_path = os.path.join(app_path, "management",
                                 "commands", filename)
        return file_path

    def clear_model(self):
        try:
            self.model_name.objects.all().delete()
        except Exception as e:
            raise CommandError(
                f'Error in clearing {self.model_name}: {str(e)}'
            )

    def insert_currency_to_db(self, data):
        try:
            self.model_name.objects.create(
                code=data["code"],
                name=data["name"],
            )
        except Exception as e:
            raise CommandError(
                f'Error in inserting {self.model_name}: {str(e)}'
            )

    def handle(self, *args, **kwargs):
        filename = kwargs['filename']
        self.stdout.write(self.style.SUCCESS(f'filename:{filename}'))
        file_path = self.get_csv_file(filename)
        line_count = 0
        currency_code = []
        try:
            with open(file_path) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                self.clear_model()
                for row in csv_reader:
                    if row != '' and line_count >= 1:
                        data = {}
                        data['name'] = row[2]
                        data['code'] = row[3]
                        if data['code'] not in currency_code:
                            currency_code.append(data['code'])
                            self.insert_currency_to_db(data)
                    line_count += 1
            self.stdout.write(
                self.style.SUCCESS(
                    f'{line_count} entries added to Currencies'
                )
            )
        except FileNotFoundError:
            raise CommandError(f'File {file_path} does not exist')