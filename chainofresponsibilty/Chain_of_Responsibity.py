""" ATM Machine Dispenser"""
from abc import ABCMeta, abstractmethod


class IDispenser(metaclass=ABCMeta):

    @abstractmethod
    def next_successor(successor):
        """Set the next handler in the chain"""

    @abstractmethod
    def handle(amount):
        """Handle the event"""


class Dispenser2000(IDispenser):
    # Dispenses Rs 2000 notes if applicable, otherwise continues to next successor

    def __init__(self):
        self._successor = None

    def next_successor(self, successor):
        # Set the next successor
        self._successor = successor

    def handle(self, amount):
        # Handle the dispensing of notes
        if amount >= 2000:
            num = amount // 2000
            remainder = amount % 2000
            print(f"Dispensing {num} Rs 2000 note")
            if remainder != 0:
                self._successor.handle(remainder)
        else:
            self._successor.handle(amount)


class Dispenser500(IDispenser):
    # Dispenses Rs 500 notes if applicable, otherwise continues to next successor

    def __init__(self):
        self._successor = None

    def next_successor(self, successor):
        # Set the next successor
        self._successor = successor

    def handle(self, amount):
        # Handle the dispensing of notes
        if amount >= 500:
            num = amount // 500
            remainder = amount % 500
            print(f"Dispensing {num} Rs 500 note")
            if remainder != 0:
                self._successor.handle(remainder)
        else:
            self._successor.handle(amount)


class Dispenser200(IDispenser):
    # Dispenses Rs 200 notes if applicable, otherwise continues to next successor

    def __init__(self):
        self._successor = None

    def next_successor(self, successor):
        # Set the next successor
        self._successor = successor

    def handle(self, amount):
        # Handle the dispensing of notes
        if amount >= 200:
            num = amount // 200
            remainder = amount % 200
            print(f"Dispensing {num} Rs 200 note")
            if remainder != 0:
                self._successor.handle(remainder)
        else:
            self._successor.handle(amount)


class Dispenser100(IDispenser):
    # Dispenses Rs 100 notes if applicable, otherwise continues to next successor

    def __init__(self):
        self._successor = None

    def next_successor(self, successor):
        # Set the next successor
        self._successor = successor

    def handle(self, amount):
        # Handle the dispensing of notes
        if amount >= 100:
            num = amount // 100
            remainder = amount % 100
            print(f"Dispensing {num} Rs 100 note")
            if remainder != 0:
                self._successor.handle(remainder)
        else:
            self._successor.handle(amount)


class ATMDispenserChain:
    # The Chain Client

    def __init__(self):
        # initializing the successors chain
        self.chain1 = Dispenser2000()
        self.chain2 = Dispenser500()
        self.chain3 = Dispenser200()
        self.chain4 = Dispenser100()

        # The successor chain will be recalculated dynamically at runtime.
        self.chain1.next_successor(self.chain2)
        self.chain2.next_successor(self.chain3)
        self.chain3.next_successor(self.chain4)


ATM = ATMDispenserChain()
AMOUNT = int(input("Enter an amount to withdraw : "))
if AMOUNT < 100 or AMOUNT % 100 != 0:
    print("Amount should in multiple of 100s.")
    exit()

# process the request
ATM.chain1.handle(AMOUNT)
print("Your withdrawal is successful!!!")
