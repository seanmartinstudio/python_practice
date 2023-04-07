
sean_age = 39
ashley_age = 39
    
def add_age(age_1, age_2):
    print("Age =", age_1 + age_2)

def conditional(age_1, age_2):
    if age_1 > age_2:
        print("Sean Greater")
    elif age_1 < age_2:
        print("Ashley Greater")
    else:
        print("Ages Equal!!!")


def main():
    add_age(sean_age, ashley_age)
    conditional(sean_age, ashley_age)

if __name__ == "__main__":
    main()