# list to store tasks
tasks = []

# run program continuously
while True:
    # menu options
    print("\n1.Add  2.Show  3.Remove  4.Exit")
    ch = input("Enter choice: ")

    # add task
    if ch == "1":
        t = input("Enter task: ")
        tasks.append(t)
        print("Added")

    # show tasks
    elif ch == "2":
        if len(tasks) == 0:
            print("No tasks")
        else:
            i = 1
            for x in tasks:
                print(f"{i}. {x}")
                i += 1

    # remove task
    elif ch == "3":
        num = int(input("Enter task number: "))
        if num > 0 and num <= len(tasks):
            tasks.pop(num-1)
            print("Removed")
        else:
            print("Wrong number")

    # exit program
    elif ch == "4":
        print("Bye")
        break

    # invalid input
    else:
        print("Invalid")