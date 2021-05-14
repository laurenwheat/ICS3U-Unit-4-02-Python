#!/usr/bin/env python3

# Created by: Lauren Wheatley
# Created on: May 2021
# This program determines the factorial of a number


def main():

    loop_counter = 1
    product_num = 1

    user_input = input("Enter a positive integer: ")
    print("")

    try:
        user_input_int = int(user_input)

        if user_input_int > 0:
            while loop_counter <= user_input_int:
                product_num = product_num * loop_counter
                loop_counter = loop_counter + 1
            print("Factorial of {0} = {1}".format(user_input_int, product_num))
        else:
            print("{} is not a positive integer!".format(user_input_int))
    except Exception:
        print("That is not a valid input!!!")
    finally:
        print("")
        print("Thanks for playing <3")


if __name__ == "__main__":
    main()
