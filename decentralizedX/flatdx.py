# -*- coding: utf-8 -*-
import time
import sys
import random
from decimal import *
from decimal import *

class FlatDx:
    def __init__(self):
        self.blocks = 100
        # self.rate = Decimal('0.07')     # maker/taker =  1/10
        self.blocktime = 0.01
        self.orders = []
        self.orders.append({'pair': 'GNTPAY', 'A': Decimal('10'), 'B': Decimal('0'), 'rate': Decimal('0.07'), 'ttl': 10})
        self.orders.append({'pair': 'GNTPAY', 'A': Decimal('0'), 'B': Decimal('600'), 'rate': Decimal('0.07'), 'ttl': 5})

    def run(self):
        randmaker = int(random.random() * 10)
        randtaker = randmaker + int(random.random() * 20)
        makerpresent = False

        for i in range(0, self.blocks):
            # every n block,
            n = 10 
            if int(random.random() * n) == 1:
                self.inject()

            if makerpresent is True:
                self.maker['ttl'] = self.maker['ttl'] - 1
                # Nach dem TTL vom Maker werden die B Token ausbezahlt und allfällige überzählige A Token an den Maker zurückgesendet
                if self.maker['ttl'] == 0:
                    self.returnToken()
                    makerpresent = False

            print('Block {}').format(i)

            time.sleep(self.blocktime)

            if i == randtaker:
                if makerpresent is True:
                    self.injectTaker()
                    self.swap()
                else:
                    print('ttl is up')

    def inject(self):
            print('inject')




    def runold(self):
        randmaker = int(random.random() * 10)
        randtaker = randmaker + int(random.random() * 20)
        makerpresent = False

        for i in range(0, self.blocks):
            if i == randmaker:
                makerpresent = True
                self.injectMaker()

            if makerpresent is True:
                self.maker['ttl'] = self.maker['ttl'] - 1
                # Nach dem TTL vom Maker werden die B Token ausbezahlt und allfällige überzählige A Token an den Maker zurückgesendet
                if self.maker['ttl'] == 0:
                    self.returnToken()
                    makerpresent = False

            print('Block {}').format(i)

            time.sleep(self.blocktime)

            if i == randtaker:
                if makerpresent is True:
                    self.injectTaker()
                    self.swap()
                else:
                    print('ttl is up')

    def injectMaker(self):
            print('injectMaker')
            self.maker = {'A': Decimal('10'), 'B': Decimal('0'), 'rate': Decimal('0.07'), 'ttl': 10}

    def injectTaker(self):
            print('injectTaker')
            self.taker = {'A': Decimal('0'), 'B': Decimal('600'), 'rate': Decimal('0.05'), 'ttl': 5}

    def returnToken(self):
            print('returnToken')
            del(self.maker)

    def swap(self):
        if self.maker['rate'] == self.taker['rate']:
            self.rate = self.maker['rate']
            if self.maker['A'] / self.rate <= self.taker['B']:
                A = self.maker['A']
                B = A / self.rate
            elif self.maker['A'] / self.rate > self.taker['B']:
                A = self.taker['B'] * self.rate
                B = A / self.rate
            else:
                sys.exit()
            print('Amount to Exchange in A: {}').format(A)
            print('Amount to Exchange in B: {}').format(B)

            self.maker['A'] = self.maker['A'] - A
            self.taker['A'] = self.taker['A'] + A

            self.maker['B'] = self.maker['B'] + B
            self.taker['B'] = self.taker['B'] - B

            print('Maker A: {} B: {}').format(self.maker['A'], self.maker['B'])
            print('Taker A: {} B: {}').format(self.taker['A'], self.taker['B'])
        else:
            print('rate not matching!')

    def withdraw(self):
        nothing

dx = FlatDx()
dx.run()