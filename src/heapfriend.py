#!/usr/bin/python

import sys
import re

MALLOC_PATTERN = r'^malloc\((\d+)\)\s+=\s+((?:0x|0X)?[a-fA-F0-9]+)$'
MALLOC_RE = re.compile(MALLOC_PATTERN)

FREE_PATTERN = r'^free\(((?:0x|0X)?[a-fA-F0-9]+)\)'
FREE_RE = re.compile(FREE_PATTERN)

CALLOC_PATTERN = r'^calloc\((\d+), (\d+)\)\s+=\s+((?:0x|0X)?[a-fA-F0-9]+)$'
CALLOC_RE = re.compile(CALLOC_PATTERN)

REALLOC_PATTERN = (r'^realloc\(((?:0x|0X)?[a-fA-F0-9]+), ' +
                   r'(\d+)\)\s+=\s+((?:0x|0X)?[a-fA-F0-9]+)$')
REALLOC_RE = re.compile(REALLOC_PATTERN)

class MallocOperation:

    def __init__(self, size, address):
        self.size = size
        self.address = address

    def __repr__(self):
        return "[MALLOC] (Size: %d, Address: 0x%x)" % (self.size, self.address)

class FreeOperation:

    def __init__(self, address):
        self.address = address

    def __repr__(self):
        return "[FREE] (Address: 0x%x)" % (self.address)

class CallocOperation:

    def __init__(self, fill, size, address):
        self.fill = fill
        self.size = size
        self.address = address

    def __repr__(self):
        return "[CALLOC] (Fill: %d, Size: %d, Address: 0x%x)" % (self.fill,
                self.size, self.address)

class ReallocOperation:

    def __init__(self, old_address, size, address):
        self.old_address = old_address
        self.size = size
        self.address = address

    def __repr__(self):
        return "[REALLOC] (Old Address: 0x%x, Size: %d, Address: 0x%x)" % (
                self.old_address, self.size, self.address)

class HeapState:

    mapping = []
    allocations = []

    def __init__(self):
        pass

    def parse_unit(self, l):
        m = MALLOC_RE.match(l)
        op = None
        if m:
            size, address = m.groups()
            mallocop = MallocOperation(int(size), int(address, 16))
            op = mallocop
        m = FREE_RE.match(l)
        if m:
            address = m.group(1)
            freeop = FreeOperation(int(address, 16))
            op = freeop
        m = CALLOC_RE.match(l)
        if m:
            fill, size, address = m.groups()
            callocop = CallocOperation(int(fill), int(size), int(address, 16))
            op = callocop
        m = REALLOC_RE.match(l)
        if m:
            old_address, size, address = m.groups()
            reallocop = ReallocOperation(int(old_address, 16), int(size),
                    int(address, 16))
            op = reallocop
        return op

    def process_unit(self, op):
        self.allocations.append(op)

    def parse_data(self, data):
        for i in data.split("\n"):
            result = self.parse_unit(i)
            if result:
                self.process_unit(result)

def main():
    heapstate = HeapState()
    if len(sys.argv) < 2:
        print "python heapfriend.py trace"
        return

    data = file(sys.argv[1]).read()
    heapstate.parse_data(data)

if __name__ == "__main__":
    main()
