from tasks import Tasks
import argparse



def cli_add():
    task_inst = Tasks()
    task_inst.add_task()
    id = task_inst.tas
    
parser = argparse.ArgumentParser(prog="Tasks",
                                 description="Task management")
parser.add_argument('command', choices=['add'], help="Command to execute")


args = parser.parse_args()

if args.command == 'add':
    cli_add()
    fstring = f"Task added successfully! ID: {}"
    print(type(id))
    print(fstring)
    
    

else:
    print("Please provide a valid command") 
