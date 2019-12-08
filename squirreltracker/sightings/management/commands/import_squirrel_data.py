from django.core.management.base import BaseCommand, CommandError
from sightings.models import Squirrel
from django.conf import settings
import os
import csv
import datetime

class Command(BaseCommand):
    help = 'Import csv file into database'

    def add_arguments(self,parser):
        parser.add_argument('file_path',help = 'file path of csv file')

    def import_data_from_csv(self,filename):
        with open(filename,'r') as csv_file:
            data = csv.reader(csv_file, delimiter = ',')
            headers = next(data)
            for item in data:
                longitude = item[0]
                latitude = item[1]
                unique_squirrel_id = item[2]
                shift = item[4]
                date = datetime.datetime.strptime(item[5].strip(),'%m%d%Y').date()
                age = item[7]
                primary_fur_color = item[8]
                location = item[12]
                specific_location = item[14]
                running_ = item[15]
                running = True if "true" in running_.lower() else False
                chasing_ = item[16] 
                chasing = True if "true" in chasing_.lower() else False
                climbing_ = item[17]
                climbing  = True if "true" in climbing_.lower() else False
                eating_ = item[18]
                eating = True if "true" in eating_.lower() else False
                foraging_ = item[19]
                foraging = True if "true" in foraging_.lower() else False
                other_activities = item[20]
                kuks_ = item[21]
                kuks = True if "true" in kuks_.lower() else False
                quaas_ = item[22]
                quaas = True if "true" in quaas_.lower() else False
                moans_ = item[23]
                moans  = True if "true" in moans_.lower() else False
                tail_flags_ = item[24] 
                tail_flags = True if "true" in tail_flags_.lower() else False
                tail_twitches_ = item[25]
                tail_twitches  = True if "true" in tail_twitches_.lower() else False
                approaches_ = item[26]
                approaches  = True if "true" in approaches_.lower() else False
                indifferent_ = item[27]
                indifferent = True if "true" in indifferent_.lower() else False
                runs_from_ = item[28]
                runs_from = True if "true" in runs_from_.lower() else False

                try:
                    sightings, created = Squirrel.objects.get_or_create(
                            unique_squirrel_id = unique_squirrel_id,
                            longitude = longitude,
                            latitude = latitude,
                            shift = shift,
                            date = date,
                            age = age,
                            primary_fur_color = primary_fur_color,
                            location = location,
                            specific_location = specific_location,
                            running = running,
                            chasing = chasing,
                            climbing = climbing
                            eating = eating,
                            foraging = foraging,
                            other_activities = other_activities,
                            kuks = kuks,
                            quaas = quaas,
                            moans = moans,
                            tail_flags = tail_flags,
                            tail_twiches = tail_twiches,
                            approaches = approaches,
                            indifferent = indifferent,
                            runs_from = runs_from
                            )
                            if created:
                                sightings.save()
                                display_format = '\nSquirrels, {}, saved successfully'
                                print(display_format(sighting))
                except Exception
                    print('Exception')

    def handle(self,*args,**options):
        file_path = options['file_path']
        self.import_data_from_csv(file_path)


