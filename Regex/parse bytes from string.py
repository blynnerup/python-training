import re

def parse_bytes(input_str):
    byte_pattern = re.compile(r'\b[0,1]{8}\b')
    match = byte_pattern.findall(input_str)
    return match
    
print(parse_bytes("11010101 101 323"))
print(parse_bytes("my data is: 10101010 11100010"))
print(parse_bytes("asdsa"))
