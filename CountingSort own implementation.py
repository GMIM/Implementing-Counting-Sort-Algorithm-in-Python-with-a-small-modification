from random import *

# probably not sorted list L
L = []
# amin and amax (maximum and minimum elements)
aMin = 0
aMax = 0
# pointers
p_1 = 0
p_2 = 0
# Working on List
A_1 = []
# Final sorted list
A_2 = []
# temporary list used for reversing
A_3 = []


# class for numbers
class number:
    value = 0
    frequency = 0

    def __init__(self):
        value = 0
        frequency = 0

    def __repr__(self):
        return str(str(self.value) + " " + str(self.frequency))


size = int(input("Enter the number of elements: "))
for i in range(size):
    # choose randomly.
    #element = randint(0, 1000)
    element = int(input())
    if i == 0:
        aMin = element
        aMax = element

    else:
        if element > aMax:
            aMax = element
        if element < aMin:
            aMin = element
    L.append(element)
print("Before Sorting...")
print(L)
# allocate all elements between interval aMin to aMax
for i in range(aMin, aMax + 1):
    n_i = number()
    A_1.append(n_i)
for i in range(size):
    A_1.__getitem__(L.__getitem__(i) - aMin).frequency += 1
    A_1.__getitem__(L.__getitem__(i) - aMin).value = L.__getitem__(i)

# two conditions will stop either both pointers are == so that it is a list of odd size or size of sorted list  is = to original one.
p_2 = aMax
p_1 = aMin
while True:
    if p_1 == p_2:
        v = A_1.__getitem__(p_1 - aMin).value
        j = A_1.__getitem__(p_1 - aMin).frequency
        for i in range(j):
            A_2.append(v)
        break
    v = A_1.__getitem__(p_1 - aMin).value
    j = A_1.__getitem__(p_1 - aMin).frequency
    vv = A_1.__getitem__(p_2 - aMin).value
    jj = A_1.__getitem__(p_2 - aMin).frequency
    for i in range(j):
        A_2.append(v)
    for i in range(jj):
        A_3.append(vv)
    if len(A_2) + len(A_3) == size:
        break;
    p_1 += 1
    p_2 -= 1

# last step is reversing A_3
for i in reversed(A_3):
    A_2.append(i)
print("After Sorting...")
print(A_2)
