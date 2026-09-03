# Create a dictionary of programming languages and their creators.
# Display each key and value using a loop.

def display_languages(language_dict):
    for language, creator in language_dict.items():
        print(f"{language} was created by {creator}")


if __name__ == "__main__":
    languages = {
        "Python": "Guido van Rossum",
        "Java": "James Gosling",
        "C++": "Bjarne Stroustrup",
    }
    display_languages(languages)
