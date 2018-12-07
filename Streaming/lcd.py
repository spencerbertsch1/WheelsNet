#!/usr/bin/env python
import LCD1602

class LCD:
    def __init__(self):
        LCD1602.init(0x27, 1)
        self.default_message()

    def default_message(self):
        self.clear()
        self.display_message("Hello!")
        self.display_message("I'm WheelsNet", row=1)

    def display_message(self, message, row=0):
        LCD1602.write(0, row, message)

    def clear(self):
        LCD1602.clear()

    def __del__(self):
        LCD1602.clear()
