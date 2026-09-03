# Represent the friends of two users using sets. Find:
# - Mutual friends
# - Friends unique to User 1
# - Friends unique to User 2
# - Total unique friends

def mutual_friends(user1, user2):
    return user1 & user2


def unique_to_user1(user1, user2):
    return user1 - user2


def unique_to_user2(user1, user2):
    return user2 - user1


def total_unique_friends(user1, user2):
    return user1 | user2


if __name__ == "__main__":
    user1_friends = {"Ritesh", "Aditi", "Sahil", "Meena"}
    user2_friends = {"Sahil", "Meena", "Karan", "Priya"}

    print(f"User 1 friends: {user1_friends}")
    print(f"User 2 friends: {user2_friends}")
    print(f"Mutual friends: {mutual_friends(user1_friends, user2_friends)}")
    print(f"Unique to User 1: {unique_to_user1(user1_friends, user2_friends)}")
    print(f"Unique to User 2: {unique_to_user2(user1_friends, user2_friends)}")
    print(f"Total unique friends: {total_unique_friends(user1_friends, user2_friends)}")
