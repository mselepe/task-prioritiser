import os
import curses
import calendar
from datetime import datetime

def display_calendar(stdscr, year, month):
    os.system("clear") # Clear the terminal

    cal = calendar.Calendar()
    month_days = cal.monthdayscalendar(year, month) # Get the month as a list of weeks

    selected_row, selected_col = 0, 0 # Used to indicate the position (row and column) of the highlighted day

    # Draws the calendar and allows user to make a selection
    while True:
        stdscr.clear()
        stdscr.addstr(0, 8, f"{calendar.month_name[month]} {year}", curses.A_BOLD | curses.A_UNDERLINE)
        stdscr.addstr(1, 0, "Mo Tu We Th Fr Sa Su")

        for row_idx, week in enumerate(month_days):
            for col_idx, day in enumerate(week):
                day_str = f"{day:2}" if day != 0 else "  "

                if row_idx == selected_row and col_idx == selected_col:
                    # Invert the colour of the highlighted day
                    stdscr.addstr(row_idx + 2, col_idx * 3, day_str, curses.A_REVERSE) 
                else:
                    stdscr.addstr(row_idx + 2, col_idx * 3, day_str)

        stdscr.refresh()
        key = stdscr.getch() # Captures the key that the user pressed

        if key == curses.KEY_UP:
            selected_row = max(0, selected_row - 1)
        elif key == curses.KEY_DOWN:
            selected_row = min(len(month_days) - 1, selected_row + 1)
        elif key == curses.KEY_LEFT:
            selected_col = max(0, selected_col - 1)
        elif key == curses.KEY_RIGHT:
            selected_col = min(6, selected_col + 1)
        elif key == ord('\n'):
            selected_day = month_days[selected_row][selected_col]
            if selected_day != 0:
                return selected_day

        # Ensure selection doesn't land on empty days (0)
        if month_days[selected_row][selected_col] == 0:
            selected_col = next((i for i, day in enumerate(month_days[selected_row]) if day != 0), selected_col)

def select_date(year:int, month:int):
    selected_day = curses.wrapper(display_calendar, year, month)
    return f"{year}-{month:02}-{selected_day:02}"

