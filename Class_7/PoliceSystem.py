class Node(object):
    def __init__(self, val):
        # val will be (id, priority, type)
        self.val = val
        self.next = None


class pQueue(object):
    def __init__(self):
        self.head = None
        self.size = 0
        self.med = 0
        self.traffic = 0
        self.crime = 0

    def add(self, val):
        id = int(val[1])
        priority = int(val[2])
        type = val[3]

        if type == "medical":
            self.med += 1
        if type == "traffic":
            self.traffic += 1
        if type == "crime":
            self.crime += 1

        insertNode = Node([id, priority, type])

        if self.size == 0:
            self.head = insertNode
        elif priority > self.head.val[1]:
            insertNode.next = self.head
            self.head = insertNode
        else:
            curr = self.head
            while curr.next and curr.val[1] > priority:
                curr = curr.next

            insertNode.next = curr.next
            curr.next = insertNode

        self.size += 1
        print("Adding job " + str(id) + " to the queue. " + str(priority) +
        " is the priority of the call." " Job " + str(id)  + " is of type " + type)

    def respond(self):
        if self.size == 0:
            print("No current emergencies – time for a coffee break!")
        else:
            print("Responding to job " + str(self.head.val[0]))

    def show(self):
        print("Number of jobs in the queue: " + str(self.size))
        avgPrior = 0
        curr = self.head
        while curr:
            avgPrior = avgPrior + curr.val[1]
            curr = curr.next

        if self.size == 0:
            print("Average Priority is: 0")
        else:
            print("Average Priority is: " + str(avgPrior/self.size))

    def modify(self, cmd):
        curr = self.head
        next = curr.next

        while next:
            if curr.val[0] == int(cmd[1]):
                curr.val[1] = int(cmd[2])

            if curr.val[1] < next.val[1]:
                curr.val, next.val = next.val, curr.val

            curr = curr.next
            next = next.next

    def remove(self, cmd):
        prev = None
        curr = self.head

        if self.head.val[0] == int(cmd[1]):
            if self.head.val[2] == "medical":
                self.med -= 1
            if self.head.val[2] == "traffic":
                self.traffic -= 1
            if self.head.val[2] == "crime":
                self.crime -= 1

            self.head = self.head.next
        else:
            while curr:
                if curr.val[0] == int(cmd[1]):
                    # Found node with given ID
                    prev.next = curr.next
                    if curr.val[2] == "medical":
                        self.med -= 1
                    if curr.val[2] == "traffic":
                        self.traffic -= 1
                    if curr.val[2] == "crime":
                        self.crime -= 1

                prev = curr
                curr = curr.next

        self.size -= 1

    def details(self, cmd):
        curr = self.head

        while curr:
            if curr.val[0] == cmd[1]:
                # Found node with given ID
                print("ID: " + str(curr.val[0]))
                print("Priority: " + str(curr.val[1]))
                print("Type: " + str(curr.val[2]))

            curr = curr.next

    def stats(self):
        print("Amount of Medical Jobs: " + str(self.med))
        print("Amount of Traffic Jobs: " + str(self.traffic))
        print("Amount of Crime Jobs: " + str(self.crime))

    def printQueue(self):
        curr = self.head
        for i in range(self.size):
            print(curr.val)
            curr = curr.next

def main():
    commandFile = open("emergencies.txt", "r")
    cmdList = []
    for line in commandFile:
       job = line.split()
       cmdList.append(job)

    PoliceSystem = pQueue()

    for cmd in cmdList:
        if cmd[0] == "received":
            PoliceSystem.add(cmd)
        if cmd[0] == "respond":
            PoliceSystem.respond()
        if cmd[0] == "show":
            PoliceSystem.show()
        if cmd[0] == "modify":
            PoliceSystem.modify(cmd)
        if cmd[0] == "remove":
            PoliceSystem.remove(cmd)
        if cmd[0] == "details":
            PoliceSystem.details(cmd)
        if cmd[0] == "statistics":
            PoliceSystem.stats()

    PoliceSystem.printQueue()

if __name__ == "__main__":
    main()
