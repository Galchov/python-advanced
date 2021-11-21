def age_assignment(*args, **kwargs):
    people_dict = {}

    for key, value in kwargs.items():
        for name in args:
            if name.startswith(key):
                people_dict[name] = value

    return people_dict


print(age_assignment("Peter", "George", G=26, P=19))
