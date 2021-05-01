import json


class Temp:
    def __init__(self, userId, task_completed):
        self.userId = userId
        self.task_completed = task_completed


class TempEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Temp):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)


with open('in.json', 'r') as f:
    data = json.load(f)

temp_result = {}
for obj in data:
    if obj['userId'] in temp_result.keys():
        temp_result[obj['userId']] += 1 if obj['completed'] else 0
    else:
        temp_result[obj['userId']] = 0

result = []
for i in temp_result.keys():
    result.append(Temp(i, temp_result[i]))

with open('out.json', 'w') as f:
    json.dump(result, f, indent=4, cls=TempEncoder)

