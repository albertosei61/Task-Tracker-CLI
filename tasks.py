import json
import os
import jsonpickle
import random

class Tasks:

    def __init__(self, task=None):
        self.task = task
        #task = input("Enter task: ")

    def add_task(self):
        self.task = input("Enter task: ")
        print("Task entered is", self.task)
        
        rand = random.randrange(1, 100)
        #rand_final = jsonpickle.encode(random_number)
        # above code was for json serializing through encoding   

        dictionary = {
            "id": rand,
            "name": self.task
        }
        
        json_object = json.dumps(dictionary, indent=4)
        json_file_path = os.path.join("json_sources", "tasks.json")
        with open(json_file_path, "a") as file:
            file.write(json_object)


p1 = Tasks()
p1.add_task()