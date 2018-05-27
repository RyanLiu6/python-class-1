def length(root):
    count = 0
    curr = root

    while curr != None:
        count += 1
        curr = curr.next

    return count


def countOdd(root):
    count = 0
    curr = root

    while curr != None:
        if curr.value % 2 == 1:
            count += 1

        curr = curr.next

    return count


def addOneToEven(root):
    curr = root

    while curr != None:
        if curr.value % 2 == 0:
            curr.value = curr.value + 1
            # curr.value += 1

        curr = curr.next


def getNode(root, pos):
    # Assuming position is 0-based
    count = 0
    curr = root

    while curr != None:
        if count == pos:
            print(curr.value)
            return

        count += 1
        curr = curr.next


class Node:
    self.value = 0
    self.next = None
