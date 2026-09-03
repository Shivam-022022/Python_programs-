# Create two sets representing technical skills of two employees. Find:
# - Common skills
# - Skills unique to Employee 1
# - Skills unique to Employee 2
# - All available skills

def common_skills(emp1, emp2):
    return emp1 & emp2


def unique_to_emp1(emp1, emp2):
    return emp1 - emp2


def unique_to_emp2(emp1, emp2):
    return emp2 - emp1


def all_skills(emp1, emp2):
    return emp1 | emp2


if __name__ == "__main__":
    employee1_skills = {"Python", "SQL", "Django", "Git"}
    employee2_skills = {"Python", "Java", "Git", "AWS"}

    print(f"Employee 1: {employee1_skills}")
    print(f"Employee 2: {employee2_skills}")
    print(f"Common skills: {common_skills(employee1_skills, employee2_skills)}")
    print(f"Unique to Employee 1: {unique_to_emp1(employee1_skills, employee2_skills)}")
    print(f"Unique to Employee 2: {unique_to_emp2(employee1_skills, employee2_skills)}")
    print(f"All skills: {all_skills(employee1_skills, employee2_skills)}")
