import re

post = "Loving the new #Python course! #LearnToCode #regex_rocks2026 Join us @ 5pm #AI"

hashtags = re.findall(r"#\w+", post)
print("Post:", post)
print("Hashtags:", hashtags)
