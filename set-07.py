# Create a set of programming languages and display each language using
# a for loop.

def display_languages(language_set):
    for language in language_set:
        print(language)


if __name__ == "__main__":
    languages = {"Python", "Java", "C++", "JavaScript", "Go"}
    display_languages(languages)
