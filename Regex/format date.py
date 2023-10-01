import re

def parse_date(date_str):
    date_pattern = re.compile(r'(?P<day>\d{2})[/,.](?P<month>\d{2})[/,.](?P<year>\d{4})$')
    date_match = date_pattern.match(date_str)
    if date_match:
        return_dict = {
            'd': date_match.group("day"),
            'm': date_match.group("month"),
            'y': date_match.group("year")
        }
    else:
        return_dict = None
    return return_dict

print(parse_date("01/22/1999"))
print(parse_date("12,04,2003"))
print(parse_date("12.11.2003"))
print(parse_date("12.11.200312"))
