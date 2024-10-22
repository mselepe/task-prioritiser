from data_input import *
from datetime import datetime, date

def display_rankings(rank_choice:str, ranked_tasks:list):

    print(f"Here are your tasks ranked by {rank_choice}:")
    for num, task in enumerate(ranked_tasks, start=1):
        print(f"{num}) {task}")

def main():
    original_task_list = tasks_input()
    overall_task_scores = create_task_score(original_task_list)

    importance = task_importance(original_task_list)
    difficulty = task_difficulty(original_task_list)
    timeframe = task_timeframe(original_task_list)

    importance_task_scores = assign_overall_task_score(overall_task_scores, importance)
    diffic_task_scores = assign_specific_task_score(difficulty)
    timeframe_task_scores = assign_specific_task_score(timeframe)

    assign_overall_task_score(overall_task_scores, difficulty) # scores by importance and difficulty
    overall_task_scores = assign_overall_task_score(overall_task_scores, timeframe) 

    ranked_by_importance = rank_tasks(importance_task_scores)
    ranked_by_difficulty = rank_tasks(diffic_task_scores)
    ranked_by_timeframe = rank_tasks(timeframe_task_scores)
    overall_ranked_tasks = rank_tasks(overall_task_scores)

    
    done = False
    while done == False:
        os.system("clear") # Clear the terminal
        print("""Your tasks have been ranked by importance, timeframe, difficulty and overall, 
considering all of these factors.\n""")

        priority_choice = input("""Enter the ranking you would like to see. \n
'Importance', 'Difficulty', 'Timeframe', or 'Overall': """).strip().lower()
        
        if priority_choice in ['importance', 'difficulty', 'timeframe', 'overall', 'quit', 'q']:
            if priority_choice == "importance":
                display_rankings(priority_choice, ranked_by_importance)
                done = True
            elif priority_choice == "difficulty":
                display_rankings(priority_choice, ranked_by_difficulty)
                done = True
            elif priority_choice == "timeframe":
                display_rankings(priority_choice, ranked_by_timeframe)
                done = True
            elif priority_choice == "overall":
                display_rankings(priority_choice, overall_ranked_tasks)
                done = True
            else:
                done = True
            
        else:
            print("Please enter a valid input.")


    


if "__main__" == __name__:
    main()
