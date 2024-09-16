import re

# Define the regular expression pattern
pattern = re.compile(
    r"It's such a lovely day today\."  # Match "It's such a lovely day today."
    r"|Some weather we're having today, huh\?"  # Match "Some weather we're having today, huh?"
    r"|Maybe today's just not my day\."  # Match "Maybe today's just not my day."
)

# Create a regex object with the pattern
my_regex = pattern
