def main():
    # partA()
    # partB()
    partC()


def partA():
    mylist = [1, 7, 14, 'abcd', [4, 12, 29], 6]

    for j in range(len(mylist[4])):
        print(mylist[4][j])

    short = mylist[:3]
    short.append(25)
    print(short)

    print(mylist[3][-1])

    name = "Duke the Wonder Cat"
    print("I love", name[0:4])

    s = ""
    for i in range(-1, -4, -1):
        s = s + name[i]
    print(s)

    print("W" in name)

    name += "rocks"
    print(name)


def partB():
    nums = [1, 2, 3, 4]
    print(nums)
    swapPairs(nums)
    print(nums)
    print(recurse(9))


def swapPairs(inputList):
    for i in range(0, len(inputList) - 2, 2):
        temp = inputList[i + 1]
        inputList[i + 1] = inputList[i]
        inputList[i] = temp

    return inputList


def recurse(n):
    if n < 4:
        return n
    else:
        print("Start", n)
        x = recurse(n//2)
        print("x", n, x)
        y = recurse(n-2)
        print("y", n, y)
        return x+y


def partC():
    a = Node(15)
    b = Node(12, a)
    c = Node(1, b)

    printList(c)
    printList(reduceList(c, 12))


def reduceList(root, minVal):
    head = root
    while root != None:
        if root.value < minVal:
            temp = root
            root = root.next
            head = root
            temp.next = None
            del temp
        else:
            root = root.next

    return head


def printList(root):
    while root != None:
        print(root.value)
        root = root.next


class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def next(self):
        return self.next

    def value(self):
        return self.value


if __name__ == "__main__":
    main()
