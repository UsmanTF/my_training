calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    tuple_ = len(string), string.upper(), string.lower()
    return tuple_
def is_contains(string, list_to_search):
    count_calls()
    if string.lower() in map(str.lower, list_to_search):
        return True
    else:
        return False