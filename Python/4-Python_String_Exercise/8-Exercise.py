# Find all occurrences of a substring in a given string by ignoring the case
# Find all occurrences of a substring in a given string by ignoring the case

str1 = "Welcome to USA. usa awesome, isn't it?"

usa_count = "USA"

temp_str = str1.lower()

count = temp_str.count(usa_count.lower())
print("The USA count is:", count)
