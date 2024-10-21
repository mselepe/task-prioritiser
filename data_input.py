import os
import calendar
from datetime import datetime
from date_selector import select_date
# import questionary

def tasks_input():
    finalised = False
    while finalised == False:
        tasks_to_do = input("List the tasks you want to complete: \n").strip().lower()
        tasks_to_do = {task.strip() for task in tasks_to_do.split(",") if task not in [" ", ""]}
        # tasks_to_do = tasks_to_do.strip().split(",")

        print("\nInputted tasks:")
        for num, task in enumerate(tasks_to_do, start=1):
            print(f"{num}) {task}")

        confirmed_tasks = input("""\nAre these all the tasks you would like to prioritise? (Type 'yes' or 'no') """).strip().lower()
        if confirmed_tasks in ["y", "yes", "yeah", "yah"]:
            finalised == True
            break
        elif confirmed_tasks in ["n", "no", "nah"]:
            continue
        else:
            print("Incorrect input. Start again.\n")
            continue

    return list(tasks_to_do)


def create_task_score(tasks_to_do):
    task_scores = {}
    for task in tasks_to_do:
        task_scores.update({task : 0})

    return task_scores


def assign_task_score(task_scores, tasks_list):
    # Assign the tasks scores according to importance.
    # The maximum score being the length of the list and min being 1
    maximum_score = len(tasks_list)

    for task in tasks_list:
        task_scores[task] += maximum_score
        maximum_score -= 1

    return task_scores


# most important
def rank_importance(tasks_to_do):
    os.system("clear") # Clear the terminal

    finalised = False
    while finalised == False:
        # List the tasks for user   
        print("Here are your tasks:")
        for num, task in enumerate(tasks_to_do, start=1):
                print(f"{num}) {task}")

        # Retrieve the importance of the tasks
        tasks_by_importance = input("""\nList the above tasks in order of importance:
(The first task being most important. The last task being least important.)\n""").strip().lower()
        tasks_by_importance = [task.strip() for task in tasks_by_importance.split(",") if task not in [" ", ""]]

        if all(task in tasks_by_importance for task in tasks_to_do) and len(tasks_by_importance) == len(tasks_to_do):
            finalised = True
        else:
            print("""You have entered a task that isn't in the original list of inputted tasks.
Try again.""")
            continue
                
    return tasks_by_importance


# hardest to easiest
def rank_difficulty(tasks_to_do):
    os.system("clear") # Clear the terminal

    finalised = False
    while finalised == False:
        # List the tasks for user   
        print("Here are your tasks:")
        for num, task in enumerate(tasks_to_do, start=1):
                print(f"{num}) {task}")

        # Retrieve the importance of the tasks
        tasks_by_difficulty = input("""\nList the above tasks in order of difficulty:
(The first task being the hardest. The last task being the easiest.)\n""").strip().lower()
        tasks_by_difficulty = [task.strip() for task in tasks_by_difficulty.split(",") if task not in [" ", ""]]

        if all(task in tasks_by_difficulty for task in tasks_to_do) and len(tasks_by_difficulty) == len(tasks_to_do):
            finalised = True
        else:
            print("""You have entered a task that isn't in the original list of inputted tasks.
Try again.""")
            continue
                
    return tasks_by_difficulty


# time-frame for each task
def task_timeframe(tasks_to_do):
    task_dates = {}

    for task in tasks_to_do:
        print("task")
        while True:
            try: 
                year = 2024
                month = int(input("Enter the month your task should be done by (e.g. 4): "))
                if 1 > month > 12:
                    raise ValueError("Month must be between 1 and 12")
                selected_date = select_date(year, month)

                print(f"You selected: {selected_date}")
                break
            except ValueError:
                print("The month entered should be in the formm of an integer.")
    
    # for task in tasks_to_do:
    #     action = questionary.select(
    #             "When should the following tas_to_do:
    #     action = questionary.select(
    #             "When should the following task, {task}, be completed:",
    #             choices=[
    #                 "Volunteer for a slot",
    #                 "Cancel a volunteering slot"
    #             ]).ask()
    #     return action


    # text_calendar = calendar.TextCalendar()
    # print(text_calendar.prmonth(2024, 1))

    current_datetime = datetime.now()
    current_date = current_datetime.date()




def rank_tasks(tasks):

    pass



# hardest task


og_list = tasks_input()
# task_scores = create_task_score(og_list)
# imp = rank_importance(og_list)
# assign_task_score(task_scores, imp)
# diff = rank_difficulty(og_list)
# print(assign_task_score(task_scores, diff))
# task_timeframe(og_list)

