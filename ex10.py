tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
#\t制表符，\n换行，\\转义，单个可用来区分单引号和双引号
#单引号、双引号要看具体情境
#format + escape sequences
formatter = "{} {} {} {}"
print(formatter.format('''\"Try your",
"Own text here",
"Or a song about fear")''')
#上述error,how?
