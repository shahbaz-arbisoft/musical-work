import csv

from django.core.cache import cache
from django.core.management.base import BaseCommand, CommandError

from musicalapp.models import MusicalWork, Contributor


class Command(BaseCommand):
    help = 'Reconciled Work Data into Database'

    def add_arguments(self, parser):
        parser.add_argument('filepath', type=str, help='File path for csv file')

    def add_contributors(self, obj, contributors, flag):
        if flag:
            contributors = [Contributor.objects.get_or_create(name=contributor)[0] for contributor in contributors]
            obj.contributors.add(*contributors)

    def invalidate_cache(self, created, ISWC):
        if created:
            cache.delete(ISWC)

    def handle(self, *args, **kwargs):
        file_path = kwargs['filepath']
        try:
            with open(file_path) as csv_file:
                csv_dict_reader = csv.DictReader(csv_file, delimiter=',')
                row_count = 0
                for row in csv_dict_reader:
                    flag = True
                    file_contributors = [contributor.strip() for contributor in row['contributors'].split('|')]
                    if row['iswc']:
                        musical, created = MusicalWork.objects.get_or_create(title=row['title'], ISWC=row['iswc'])
                    else:
                        try:
                            musical = MusicalWork.objects.get(title=row['title'])
                            db_contributors = musical.contributors.values_list('name', flat=True)
                            flag = created = bool(set(db_contributors) & set(file_contributors))
                        except MusicalWork.DoesNotExist:
                            continue
                    self.add_contributors(musical, file_contributors, flag)
                    self.invalidate_cache(created, row['iswc'])
                    row_count += 1
            self.stdout.write(
                self.style.SUCCESS(
                    f'{row_count} rows executed from this file'
                )
            )
        except FileNotFoundError:
            raise CommandError(f'File at this path "{file_path}" does not exist')
        except Exception as ex:
            print(ex)
            self.stdout.write(self.style.ERROR(ex))
