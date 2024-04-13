def get_pair(dict, key):
    x = dict.get(key)
    if x is not None:
        x = (x["id"], x["name"])
        return x
    return None


def get_nested_value(dict, arg1, arg2) -> any:
    x = dict.get(arg1)
    if x is not None:
        return x.get(arg2)
    return None


def get_nested_value2(dict, arg1, arg2, arg3):
    x = dict.get(arg1)
    if x is not None:
        x = x.get(arg2)
        if x is not None:
            return x.get(arg3)
    return None


def generate_array_str(arr) -> str:
    temp = str(arr)
    return '{' + temp[1:-1] + '}'
