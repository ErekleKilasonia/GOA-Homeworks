def get_initials(full_name):

    names = full_name.split()

    first_initial = names[0][0]

    last_initial = names[-1][0]

    initials = first_initial + "." + last_initial
    return initials

full_name = input("Enter your first and last name: ")
print("Initials:", get_initials(full_name))

