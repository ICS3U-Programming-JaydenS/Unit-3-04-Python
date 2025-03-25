#!/usr/bin/env python3
# Created By: Jayden Smith
# Date: March 25, 2025
# This program tells the user if a number is positive or negative


def main():
    user_num = int(input("What is your number?"))
    if user_num > 0:
        print("You have a positive number!")
    elif user_num < 0:
        print("You have a negative number!")
    else:
        print("Your number is 0!")


if __name__ == "__main__":
    main()
