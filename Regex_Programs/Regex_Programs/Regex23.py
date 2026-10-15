import re

source_lines = [
    'x = 10  # initial value',
    '# full-line comment',
    'url = "http://example.com/#section"  # real comment after a string',
    "msg = 'Use # to start a comment'",
    "text = '''first line # inside a multiline string",
    "second line'''",
]

# 1. Naive pattern: everything from '#' to the end of the line
naive = r"#.*"

# 2. Slightly better: skip over simple single-line string literals first
string_literal = r'"(?:\\.|[^"\\\n])*"' + "|" + r"'(?:\\.|[^'\\\n])*'"
better = re.compile("(" + string_literal + ")|(#.*)")

print("--- Naive regex ---")
for line in source_lines:
    m = re.search(naive, line)
    print(f"{line!r:75} -> {m.group() if m else None}")

print()
print("--- Regex that skips simple string literals ---")
for line in source_lines:
    comments = [m.group(2) for m in better.finditer(line) if m.group(2)]
    print(f"{line!r:75} -> {comments}")

print('''
Why regular expressions alone are not enough:
 1. A '#' inside a string literal is not a comment. The naive pattern
    reports false comments for lines 3 and 4.
 2. Multiline (triple-quoted) strings span several lines. A regex applied
    line by line cannot know that line 5 starts a string that continues on
    line 6, so '# inside a multiline string' is wrongly reported.
 3. Escaped quotes, raw strings, f-strings with nested quotes, and
    implicit string concatenation make the pattern grow complicated and fragile.
 4. Regular expressions cannot track nesting/state across the whole file.

Better approach: use Python's tokenize module, which understands the
language grammar and returns real COMMENT tokens.
''')

import io
import tokenize

code = chr(10).join(source_lines)
print("--- Using the tokenize module ---")
for tok in tokenize.generate_tokens(io.StringIO(code).readline):
    if tok.type == tokenize.COMMENT:
        print(f"Line {tok.start[0]}: {tok.string}")
