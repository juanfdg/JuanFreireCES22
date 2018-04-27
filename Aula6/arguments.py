def select_keys_by_values(*args, **kwargs):
    result = []
    keys = sorted(kwargs.keys())
    for kw in keys:
        if kwargs[kw] in args:
            result.append(kw)
    return result


"""Selecting kids by age"""
dict = {'Joe': 7, 'Anne': 8, 'Jose': 9, 'Elisa':8, 'Ravi': 7, 'Kenny': 9}
ages = [8, 9]
print(select_keys_by_values(*ages, **dict))
