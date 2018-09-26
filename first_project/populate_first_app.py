import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()
 

## Fake pop script
import random
from first_app.models import AccessRecord, Topic, Webpage
from faker import Faker

fakegen = Faker()
topic = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
	t = Topic.objects.get_or_create(top_name=random.choice(topic))[0] # Retrive the model if it already exists else create it
	t.save()
	return t


def populate(N=5):
	for entry in range(N):
		top = add_topic()
		
		# Create fake data
		fake_url = fakegen.url()
		fake_date = fakegen.date()
		fake_name = fakegen.company()

		webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

		acc_red = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]


if __name__ == '__main__':
	print('populating script!')
	populate(20)
	print('Populating complete!')