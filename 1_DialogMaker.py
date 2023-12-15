import time

isCreating = True
conversation_order = []
people_list = []


class Person:
    def __init__(self, name, dialog, time):
        self.name = name
        self.dialog = dialog
        self.time = time

    def talk(dialog):
        print(f"{people.name}: {people.dialog}")


def create_dialog():
    if len(people_list) == 0:
        person_name = input("What is the name of your first character?: ").capitalize()
        people_list.append(person_name)

    else:
        people_str = ",".join(people_list)

        person_name = input(
            f"Choose the next character (Or create one!) [{people_str}]: "
        ).capitalize()
        if person_name not in people_list:
            people_list.append(person_name)

    person_dialog = input("What will they say?: ")
    person_time = 0
    while person_time <= 0:
        try:
            person_time = float(input("For how many seconds should they pause?: "))
        except:
            continue

    newPerson = Person(person_name, person_dialog, person_time)
    conversation_order.append(newPerson)


def excecute_dialogs():
    for people in conversation_order:
        people.talk()
        time.sleep(people.time)


while isCreating:
    print("-------------------------------------------------------------------------")
    userAction = input(f"Action (0 -> new dialog, 1 -> excucute): ")
    print("-------------------------------------------------------------------------")

    if userAction != "0" and userAction != "1":
        continue

    elif userAction == "0":
        create_dialog()
    elif userAction == "1":
        excecute_dialogs()
        break
