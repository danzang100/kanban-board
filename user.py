#Logic for the user login
import json
import os.path

class User:
    def __init__(self, id):
        file_path = f'./userKanbanBoards/user{id}.json'
        if os.path.isfile(file_path):
            with open(file_path, "r") as file:
                self.data = json.load(file)
        else:
            with open("defaultKanban.json", "r") as file:
                self.data = json.load(file)
        
        self.id = id

    def display(self):
        userData = self.data['tasks']
        if len(userData) != 0:
            to_do = [task for task in self.data["tasks"] if task['status'] == "to-do"]
            in_progress = [task for task in self.data["tasks"] if task['status'] == "in-progress"]
            to_validate = [task for task in self.data["tasks"] if task['status'] == "to_validate"]
            completed = [task for task in self.data["tasks"] if task['status'] == "completed"]
            print("--------TO DO------------")
            if len(to_do) == 0:
                print("=====No tasks currently======\n")
            for task in to_do:
                print(f"ID: {task['id']} - Task: {task['task']} - Priority: {task['priority']}\n")
            
            print("--------IN PROGRESS------------")
            if len(in_progress) == 0:
                print("=======No tasks currently======\n")
            for task in in_progress:
                print(f"ID: {task['id']} - Task: {task['task']} - Priority: {task['priority']}\n")

            print("--------TO BE VALIDATED------------")
            if len(to_validate) == 0:
                print("===No tasks currently======\n")
            for task in to_validate:
                print(f"ID: {task['id']} - Task: {task['task']} - Priority: {task['priority']}\n")

            print("--------COMPLETED------------")
            if len(completed) == 0:
                print("===No tasks currently======\n")
            for task in completed:
                print(f"ID: {task['id']} - Task: {task['task']} - Priority: {task['priority']}\n")
        
        else:
            print("No tasks present on your board. Please create a new task.")
        

    def edit(self):
        edit_choice = input('''Press 1 to update task status.\nPress 2 to update task priority.\nPress 5 to exit edit mode.\n''')
        if edit_choice == '5': return
        task_choice = input('''Type the task number to select: ''')
        chosen_task = {}
        for task in self.data['tasks']:
            if task['id'] == task_choice:
                chosen_task = task
                break

        else:
            new_tasks = [new_task for new_task in self.data['tasks'] if new_task != chosen_task]
            
            if edit_choice == '1':
                curr_status = chosen_task['status']
                if curr_status == "to-do":
                    chosen_task['status'] = "in-progress"
                elif curr_status == "in-progress":
                    chosen_task['status'] = "to-validate"
            
            elif edit_choice == '2':
                new_priority = input('''Press 1 for high, 2 for medium, 3 for low.''')
                if new_priority == "1":
                    chosen_task['priority'] = 'high'
                elif new_priority == '2':
                    chosen_task['priority'] = 'medium'
                elif new_priority == '3':
                    chosen_task['priority'] = 'low'

            if edit_choice != '3':
                new_tasks.append(chosen_task)
            self.data['tasks'] = new_tasks

    def run(self):
        exit_flag = False
        while not exit_flag:
            choice = input('''\nPress 1 to display/edit your Kanban Board,\nPress 3 to exit: ''')
            if choice == "3":
                exit_flag = True
                with open(f"./userKanbanBoards/user{self.id}.json", 'w') as file:
                    json.dump(self.data, file)
                continue

            elif choice == "1":
                self.display()
                self.edit()