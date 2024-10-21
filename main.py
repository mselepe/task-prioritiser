def main():
    og_list = tasks_input()
    task_scores = create_task_score(og_list)
    imp = rank_importance(og_list)
    assign_task_score(task_scores, imp)
    diff = rank_difficulty(og_list)
    print(assign_task_score(task_scores, diff))
    task_timeframe(og_list)


if __main__ == "__name__":
    main()