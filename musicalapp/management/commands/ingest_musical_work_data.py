import csv

from django.core.management.base import BaseCommand, CommandError

from musicalapp.models import Work, Contributor


class Command(BaseCommand):
    help = 'Ingest Musical Work Data into DB table'

    def add_arguments(self, parser):
        parser.add_argument('filepath', type=str, help='File path for csv file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['filepath']
        try:
            with open(file_path) as csv_file:
                csv_dict_reader = csv.DictReader(csv_file, delimiter=',')
                field_names = next(csv_dict_reader)
                for row in csv_dict_reader:
                    print(row)
                    # contributors = [meta.strip() for meta in row['contributors'].split('|')]
                    # contributors_lst = list()
                    # for contributor in contributors:
                    #     obj, created = Contributor.objects.get_or_create(name=contributor)
                    #     contributors_lst.append(obj)
                    #     print(contributors_lst)
                    #
                    # obj, created = Work.objects.update_or_create(title=row['title'], ISWC=row['iswc'])
                    # obj.contributors.bulk_update(contributors_lst, ['contributors'])
                    # print(dir(obj))
                    # print(dir(obj.contributors))

                    # obj.contributors.set.add(contributors_lst)
                    # obj.save()
                    # Work.objects.bulk_update(contributors_lst, ['contributors'])

            self.stdout.write(
                self.style.SUCCESS(
                    f'{1} entries added to Musical Work'
                )
            )
        except FileNotFoundError:
            raise CommandError(f'File at this path "{file_path}" does not exist')
