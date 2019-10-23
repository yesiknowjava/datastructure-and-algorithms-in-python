'''
How can I organize my code to make it easier to change the base class?
'''

class Base:
    def mymethod(self):
        print('This is base')

BaseAlias = Base

class Derived(BaseAlias):
    def mymethod(self):
        print('This is derived')
