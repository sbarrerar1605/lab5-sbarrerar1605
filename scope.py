int_value = None
str_value = None


def set_globals(some_int, some_str):
    global int_value
    global str_value

    int_value = some_int
    str_value = some_str


def get_globals():
    return (int_value, str_value)