def count_smileys(arr):
    return len(list(filter(lambda x: re.compile(r'[:;][-~]?[D\)]').match(x), arr)))
