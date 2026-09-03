# Create two sets:
# - Students present in the morning session
# - Students present in the afternoon session
#
# Find:
# - Students present in both sessions
# - Students present only in the morning
# - Students present only in the afternoon
# - Students present in at least one session

def both_sessions(morning, afternoon):
    return morning & afternoon


def only_morning(morning, afternoon):
    return morning - afternoon


def only_afternoon(morning, afternoon):
    return afternoon - morning


def at_least_one_session(morning, afternoon):
    return morning | afternoon


if __name__ == "__main__":
    morning = {"Ritesh", "Aditi", "Sahil", "Meena"}
    afternoon = {"Sahil", "Meena", "Karan", "Priya"}

    print(f"Morning: {morning}")
    print(f"Afternoon: {afternoon}")
    print(f"Both sessions: {both_sessions(morning, afternoon)}")
    print(f"Only morning: {only_morning(morning, afternoon)}")
    print(f"Only afternoon: {only_afternoon(morning, afternoon)}")
    print(f"At least one session: {at_least_one_session(morning, afternoon)}")
