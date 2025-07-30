To_do = []


def add_list():
    while True:
        add = input("What do you want to add to the list? ")

        if add in To_do:
            print(f"You already have {add} in the list")
            continue
        else:
            print(f"{add} has been added to the list")
            To_do.append(add)
            break


def remove_list():
    while True:
        remove = input("What do you want to remove from the list? ")

        if remove not in To_do:
            print(f"{remove} does not exist in the list")
            continue
        else:
            print(f"{remove} has been removed to the list")
            To_do.remove(remove)
            break


def view_list():
    for items in To_do:
        print(f"-{items}")


def exit_menu():
    print("Alright bye!")
    exit()


def main():
    while True:
        options = input("What do you want to do with the list?\n1.add\n2.remove\n3.view list\n4.exit\n")

        if options == "1":
            add_list()
        elif options == "2":
            remove_list()
        elif options == "3":
            view_list()
        elif options == "4":
            exit_menu()
        else:
            print("Please pick one of the options")


if __name__ == "__main__":
    main()