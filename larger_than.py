# !/user/bin/env python3

# Created by Trent Hodgins
# Created on 09/30/2021
# This is the Larger Than program
# The user enters in twp numbers
# The program tells the user which number is larger


def main():
    # this function checks what number is larger

    # input
    first_number = input("Enter in a integer: ")
    second_number = input("Enter in a second integer: ")
    print("")

    # process and output
    try:
        first_number_as_integer = int(first_number)
        second_number_as_integer = int(second_number)
        if first_number_as_integer > second_number_as_integer:
            print("{0} is larger than {1}".format(first_number, second_number))
        elif first_number_as_integer < second_number_as_integer:
            print("{0} is larger than {1}".format(second_number, first_number))
        elif first_number_as_integer == second_number_as_integer:
            print("Both numbers are equal")

    except Exception:
        print("You didn’t enter in an integer.")

    print("\nDone")


if __name__ == "__main__":
    main()
