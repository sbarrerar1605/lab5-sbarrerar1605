global_int = None
global_str = None


def set_globals(x, y):
    global global_int
    global global_str
    global_int = x
    global_str = y


def get_globals():
    return (global_int, global_str)