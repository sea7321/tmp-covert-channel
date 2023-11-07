"""
Filename: sender.py
Author: Savannah Alfaro, sea2985
"""
# Standard Imports
import os
import time


def main():
    message = input("Enter the message to encode: ")
    message_filename = "/tmp/.message"
    sent_filename = "/tmp/.sent"
    
    # delete files
    if os.path.exists(message_filename):
        os.remove(message_filename)

    if os.path.exists(sent_filename):
        os.remove(sent_filename)

    # loop through each letter in the message
    for character in message:
        # convert letter to binary form
        binary_letter = format(ord(character), '07b')
        count = 0

        # loop through each digit in binary_letter
        for digit in binary_letter:
            # send encoded letter
            if digit == "1":
                with open(message_filename, "w") as file:
                    file.writelines(" ")
            elif digit == "0":
                with open(message_filename, "w"):
                    pass

            # send sent file
            with open(sent_filename, "w") as file:
                file.writelines(str(len(message)))
            print("Sent: {}".format(binary_letter[0:count + 1]))
    
            # check to see if receiver read digit
            while os.path.exists(sent_filename):
                time.sleep(1)

            # delete message file
            os.remove(message_filename)
            count += 1


if __name__ == "__main__":
    main()
