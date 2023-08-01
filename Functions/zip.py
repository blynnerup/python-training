def interleave(string1, string2):
    return ''.join(''.join(x) for x in zip(string1, string2))

print(interleave('lzr','iad'))
