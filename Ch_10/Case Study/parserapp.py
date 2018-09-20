"""
File: parserapp.py
Project 10.9

Completes the parser with expression trees.

View for the infix expression parser.
Handles user interaction.
"""

from parsers import Parser

class ParserView(object):

    def run(self):
        parser = Parser()
        while True:
            sourceStr = input("Enter an infix expression: ")
            if sourceStr == "": break
            try:
                tree = parser.parse(sourceStr)
                print("Prefix:", tree.prefix())
                print("Infix:", tree.infix())
                print("Postfix:", tree.postfix())
                print("Value:", tree.value())
            except Exception as e:
                print("Error:")
                print(e)

ParserView().run()
