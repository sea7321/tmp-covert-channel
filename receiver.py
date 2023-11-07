"""
Filename: receiver.py
Author: Savannah Alfaro, sea2985
"""
# Standard Imports
import os
import time


def main():
    message_filename = "/tmp/.message"
    sent_filename = "/tmp/.sent"
    binary_letter = ""
    decoded_message = ""

    # wait for the sender to send a digit
    while not os.path.exists(sent_filename):
        time.sleep(1)

    # read the length of the message
    with open(sent_filename, "r") as file:
        message_length = file.readline()

    # loop through each digit in the message
    for index in range(1, (int(message_length) * 7) + 1):
        # retrieve digit from sender
        if os.path.getsize(message_filename) == 0:
            binary_letter += "0"
        else:
            binary_letter += "1"
        print("Received: {}".format(binary_letter))

        # decode encoded letter
        if index % 7 == 0:
            # convert binary letter to character
            decoded_message += chr(int(binary_letter, 2))
            binary_letter = ""

        # delete sent file
        os.remove(sent_filename)

        # wait for sender if the end of message hasn't been reached
        if index != int(message_length) * 7:
            while not os.path.exists(sent_filename):
                time.sleep(1)

    print("\nDecoded message: {}".format(decoded_message))


if __name__ == "__main__":
    main()
