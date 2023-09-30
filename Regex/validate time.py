import re

def is_valid_time(time_string):
    time_pattern = re.compile(r'\d{1,2}:\d{2}')
    match = time_pattern.fullmatch(time_string)
    if match:
        return True
    return False

print(is_valid_time("11:22"))
print(is_valid_time("asd"))
print(is_valid_time("123:45"))
print(is_valid_time("11.32"))
print(is_valid_time("88:99"))
