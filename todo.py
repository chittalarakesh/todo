class Todolist:
    def __init__(self):
        self.tasks=[]
    def add.task(self,task):
        self.tasks.append(task)
    def display_tasks(self):
        print("Tasks:")
        for task in self.tasks:
            print(task)

    
if __name__=="__main__":
    todo_list=Todolist()
    todo_list.add_task("complete work")
    todo_list.add_task("completed work")
    todo_list.add_task("writing the code")
    todo_list.add_task("learning the git")
    todo_list.add_task("fast api")
