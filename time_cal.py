import datetime
import calendar

def display_current_time():
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))

def display_june_2024_calendar():
    cal = calendar.monthcalendar(2024, 6)
    print("2024年6月のカレンダー")
    print("月 火 水 木 金 土 日")
    for week in cal:
        print(" ".join(f"{day:2}" if day != 0 else "  " for day in week))

if __name__ == "__main__":
    display_current_time()
    print()
    display_june_2024_calendar()
