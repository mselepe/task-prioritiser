import os
import calendar
from datetime import datetime, date
from date_selector import select_date

def tasks_input():
    """Retrieves the list of tasks that is to be ranked by the programme

    Returns:
        list: List of tasks to be ranked
    """    
    os.system("clear") # Clear the terminal

    # Get the list of tasks that are to be prioritised
    finalised = False
    while finalised == False:
        tasks_to_do = input("List the tasks you want to complete: \n").strip().lower()
        tasks_to_do = {task.strip() for task in tasks_to_do.split(",") if task not in [" ", ""]}

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


def create_task_score(tasks_to_do:list):
    """The tasks will be assigned a score per category. 
    This function creates the dictionary that will store the scores.

    Args:
        tasks_to_do (list): The tasks to be ranked

    Returns:
        dict: The keys are the tasks and the values are the scores which are initially each = 0
    """    
    task_scores = {}
    for task in tasks_to_do:
        task_scores.update({task : 0})

    return task_scores


def assign_overall_task_score(task_scores:dict, ranked_tasks_list:list):
    """This keeps track of the overall scores considering all of the criteria.

    Args:
        task_scores (dict): The accumulated score of the tasks 
        ranked_tasks_list (list): The ranked list by a specific criteria

    Returns:
        dict: Updated dictionary with scores
    """    
    # The maximum score is the length of the list and the min is 1
    maximum_score = len(ranked_tasks_list)

    for task in ranked_tasks_list:
        task_scores[task] += maximum_score
        maximum_score -= 1

    return task_scores


def assign_specific_task_score(tasks_list:list):
    """This keeps track of the scores considering a specific criteria.

    Args:
        tasks_list (list): The ranked list by a specific criteria

    Returns:
        dict: Updated dictionary with scores
    """ 
    task_scores = {}
    for task in tasks_list:
        task_scores.update({task : 0})

    maximum_score = len(tasks_list)

    for task in tasks_list:
        task_scores[task] += maximum_score
        maximum_score -= 1

    return task_scores


def task_importance(tasks_to_do:list):
    """The user ranks the tasks by order of importance

    Args:
        tasks_to_do (list): _description_

    Returns:
        dict: Updated dictionary with scores
    """    
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
def task_difficulty(tasks_to_do:list):
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
def task_timeframe(tasks_to_do:list):
    os.system("clear") # Clear the terminal

    task_dates_difference = {}
    current_date = date.today()
    current_year = current_date.year
    current_month = current_date.month

    for task in tasks_to_do:
        print(f"For the following task: {task}")
        while True:
            try: 
                year = int(input("Enter the year your task should be completed by: "))
                month = int(input("Enter the month your task should be completed by (e.g. 4): "))
                if 1 > month > 12:
                    raise ValueError("Month must be between 1 and 12")
                elif year < current_year:
                    raise ValueError("Year must be in the future")
                elif year == current_year and month < current_month:
                    raise ValueError("Month must be in the future")

                selected_date = select_date(year, month)
                num_days_difference = calc_num_days(current_date, selected_date)
                task_dates_difference.update({task : num_days_difference})
                break

            except ValueError:
                print("The month entered should be in the formm of an integer.")
        print("\n")

    tasks_by_timeframe = rank_tasks_by_time(task_dates_difference)
    return tasks_by_timeframe
    

def calc_num_days(current_date:datetime.date, selected_date_str:str):
    selected_date_list = selected_date_str.split("-")
    selected_year = int(selected_date_list[0])
    selected_month = int(selected_date_list[1])
    selected_day = int(selected_date_list[2])
    selected_date_dtime = date(selected_year, selected_month, selected_day)

    return (selected_date_dtime - current_date).days


def rank_tasks_by_time(tasks_dictionary:dict):
    
    sorted_tasks_by_score = dict(sorted(tasks_dictionary.items(), key=lambda x:x[1]))
    sorted_tasks_list = sorted_tasks_by_score.keys()
    
    return list(sorted_tasks_list)


def rank_tasks(tasks_dictionary:dict):
    
    sorted_tasks_by_score = dict(sorted(tasks_dictionary.items(), key=lambda x:x[1], reverse=True))
    sorted_tasks_list = sorted_tasks_by_score.keys()
    
    return list(sorted_tasks_list)




