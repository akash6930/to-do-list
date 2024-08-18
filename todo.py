def task():
    tasks = []
    print("_welcome to task mamanger")

    total_task=int(input("Enter how many task u want to add = "))
    for i in range(1,total_task+1):
        task_name = input(f"Enter task {i} = ")
        tasks.append((task_name))

    print(f"today task are\n{task}")

    while True:
        operation = int(input("Enter 1-Add 2-Update 3-Delete 4-view 5 -exit"))
        if operation == 1:
            add = input("enter task to add")
            tasks.append(add)
            print(f"Task{add} has been added successfully")
        elif operation ==2:
            updated_val = input("enter the task name u want update=")
            if updated_val in tasks:
                up = input("enter new task =")
                ind = tasks.index(updated_val)
                tasks[ind]=up
                print(f"updated task{up}")

        elif operation == 3:
            del_val = int(input("enter what u have to delete"))
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"Task{del_val}has deleted")

        elif operation==4:
            print(f"total tasks = {tasks}")

        elif operation ==5:
            print("closing the program")
            break
        else:
            print("invalid input")
task()