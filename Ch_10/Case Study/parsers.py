"""
File: parsers.py
Defines Parser
"""

from tokens import Token
from scanner import Scanner
from expressiontree import LeafNode, InteriorNode

class Parser(object):

    def parse(self, sourceStr):
        self._completionMessage = "No errors"
        self._parseSuccessful = True
        self._scanner = Scanner(sourceStr)
        tree = self._expression()
        self._accept(self._scanner.get(), Token.EOE,
                     "symbol after end of expression")
        return tree
   
    def parseStatus(self):
        return self._completionMessage
    
    def _accept(self, token, expected, errorMessage):
        if token.getType() != expected:
            self._fatalError(token, errorMessage)

    def _fatalError(self, token, errorMessage):
        self._parseSuccessful = False
        self._completionMessage = "Parsing error -- " + \
                                  errorMessage + \
                                  "\nExpression so far = " + \
                                  self._scanner.stringUpToCurrentToken()
        raise Exception(self._completionMessage)

    def _expression(self):
        tree = self._term()
        token = self._scanner.get()
        while token.getType() in (Token.PLUS, Token.MINUS):
            op = str(token)
            self._scanner.next()
            tree = InteriorNode(op, tree, self._term())
            token = self._scanner.get()
        return tree

    def _term(self):
        tree = self._factor()
        token = self._scanner.get()
        while token.getType() in (Token.MUL, Token.DIV):
            op = str(token)
            self._scanner.next()
            tree = InteriorNode(op, tree, self._factor())
            token = self._scanner.get()
        return tree

    def _factor(self):
        token = self._scanner.get()
        if token.getType() == Token.INT:
            tree = LeafNode(token.getValue())
            self._scanner.next()
        elif token.getType() == Token.L_PAR:
            self._scanner.next()
            tree = self._expression()
            self._accept(self._scanner.get(),
                         Token.R_PAR,
                         "')' expected")
            self._scanner.next()
        else:
            tree = None
            self._fatalError(token, "bad factor")
        return tree

