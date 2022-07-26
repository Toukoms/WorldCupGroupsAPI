import json

from data.models import Group, Team

with open('2022_world_cup_group.json') as f:
    data = json.load(f)

groups = data['groups']

for group in groups:
    g = Group.objects.create(name=group)
    for team in groups[group]:
        Team.objects.create(name=team['name'], logo=team['logo'], group=g)