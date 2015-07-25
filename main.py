#!/usr/bin/env python -u /home/user
__author__ = 'user'

titty="test"

from def_cpu import cpu_6502

import re

wat="poop"

class cpuGen:
    Symbol = str          # A Lisp Symbol is implemented as a Python str
    Command = str
    List   = list         # A Lisp List is implemented as a Python list
    Number = (int, float) # A Lisp Number is implemented as a Python int or float
    symbolTable = ()
    reMatchBin = re.compile("^0(b|B)(0|1)+$")
    reMatchHex = re.compile("^0(x|X)([A-F]|[a-f]|\d)+$")

    def __init__(self):
        print("-CPU STARTING-")
    def tokenize(self, code):
        return code.replace('(', ' ( ').replace(')', ' ) ').split()

    def parse(self, tokenList):
        return self.read_from_tokenList(tokenList)

    def prepro(self, code):
        pLevel = 0
        okExtras = "()-"
        ok=False
        curLoc=0
        newCode=""
        lineStart=0
        errorLine=""

        for i in code:
            if i == '(':
                pLevel+=1
                newCode+=i
            elif i == ')':
                if pLevel < 0:

                    raise SyntaxError('Unexpected closure at ' + str(curLoc))
                else:
                    pLevel-=1
                    newCode+=i
            elif i == '\n'

            elif i.isdigit():
                newCode+=i
            elif i.isalpha():
                newCode+=i
            elif okExtras.find(i) >= 0:
                newCode+=i

        if pLevel != 0: raise SyntaxError('Unmatched Parentheses')
        else: return newCode

    def read_from_tokenList(self, tokens):
        if len(tokens) == 0:
            raise SyntaxError('eof')
        token = tokens.pop(0)
        if '(' == token:
            L = []
            while tokens[0] != ')':
                L.append(self.read_from_tokenList(tokens))
            tokens.pop(0)
            return L
        elif ')' == token:
            raise SyntaxError('unexpected )')
        else:
            return self.typeify(token)

    def typeify(self, token):
        retVal=0
        if self.reMatchBin.match(token):
            try: return int(token[2:], 2)
            except ValueError:
                raise SyntaxError('Token %s is not a Bin' % token)
        if self.reMatchHex.match(token):
            try: return int(token[2:], 16)
            except ValueError:
                raise SyntaxError('Token %s is not a Hex' % token)

        try: return int(token)
        except ValueError:
            try: return int(token)
            except ValueError:
                return self.Symbol(token)


a = cpuGen()
#tokens = a.tokenize(cpu_6502)
#lists = a.parse(tokens)


