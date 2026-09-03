# Store visitor IDs from two different days in separate sets. Determine:
# - Unique visitors across both days
# - Returning visitors
# - Visitors who came only on the first day
# - Visitors who came only on the second day

def unique_visitors(day1, day2):
    return day1 | day2


def returning_visitors(day1, day2):
    return day1 & day2


def only_day1(day1, day2):
    return day1 - day2


def only_day2(day1, day2):
    return day2 - day1


if __name__ == "__main__":
    day1_visitors = {"V001", "V002", "V003", "V004"}
    day2_visitors = {"V003", "V004", "V005", "V006"}

    print(f"Day 1 visitors: {day1_visitors}")
    print(f"Day 2 visitors: {day2_visitors}")
    print(f"Unique visitors: {unique_visitors(day1_visitors, day2_visitors)}")
    print(f"Returning visitors: {returning_visitors(day1_visitors, day2_visitors)}")
    print(f"Only Day 1: {only_day1(day1_visitors, day2_visitors)}")
    print(f"Only Day 2: {only_day2(day1_visitors, day2_visitors)}")
