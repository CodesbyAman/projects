print("Welcome to Aman todolist Project")
class todolist:
    tasks=[]
    def add_task(self,task): 
        self.task=task
        todolist.tasks.append(self.task) 
 
    def view_task(self):
        if not todolist.tasks :
            print("no any task is added")
        else:
            for task in todolist.tasks:
                print(task)
        # print(self.tasks)
    def delete_task(self,taskName):
         self.taskName=taskName
         if self.taskName in todolist.tasks:
             todolist.tasks.remove(self.taskName)
             print(f"{taskName}is deleted successfully from task list") 
         else:
             print("tere is no such task is present in list")    
    def save_task(self,fileName):
        self.file=open(fileName,'w')
        for task in todolist.tasks:
           # for adding each task in new line
           self.file.write(task+'\n')
        print('tasks are save successfully in a file')   
        self.file.close()             
    def load_task(self,fileName):
        self.task=[]
        try:
            self.file=open(fileName,'r')
            for line in self.file.readlines():
                self.task.append(line.strip())
            print(f"task is loaded successfully from {fileName}")    
        except FileNotFoundError:
            print(f"{fileName} is not found")
        
t1=todolist()
while True:
     print("Select the following tasks...😎")
     print("1. Add Your Tasks!!")
     print("2.View Your Tasks!!")
     print("3.Delete Your Completed Tasks!!")
     print("4.Save Your Tasks in File!!")
     print("5.load Your Tasks in List!!")
     print("6. Exit")
     n=int(input())
     match n:     
          case 1:
            t1.add_task(input("Enter your task\n"))
            print("your tasks is added successfuly in list of tasks👍")
          case 2:
            t1.view_task()
            print("Your task is view🧐")
          case 3:
            taskName = input("Enter the task name to delete: ")
            t1.delete_task(taskName)  
          case 4:
            t1.save_task('listOfTasks.txt')
            print("tasks is save successfully in your file👊")
          case 5:
            t1.load_task('listOfTasks.txt')
            print("task is loaded in list😎")
          case 6:
             print("You exit from todolist 🙏")   
             break
          case _:
            print("invalid choice please select valid option🙂")              

    
   