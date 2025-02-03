def age_assignment(*args, **kwargs):

    people_ages = []

    for letter, ages in kwargs.items():

        for name in args:
            if name[0] == letter:
                people_ages.append(f"{name} is {ages} years old.")

    return '\n'.join(sorted(people_ages))


''' TESTS '''
# print(age_assignment("Peter", "George", G=26, P=19))
# print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
