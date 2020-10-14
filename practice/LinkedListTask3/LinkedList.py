class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List implementation
class LinkedList:
    def __init__(self, lst=None):
        self.__head = None
        self.__length = 0
        if (lst is not None):
            for elem in lst: self.append(elem)

    def __len__(self):
        return self.__length

    def __str__(self):
        listStr = '[ '
        currentNode = self.__head
        while currentNode is not None:
            listStr += str(currentNode.data)+' '
            currentNode = currentNode.next
        return listStr + ']'

    # getitem + getslice implementation
    def __getitem__(self, key):
        #getslice
        if (isinstance(key, slice)):
            begin, end, step = key.indices(len(self))
            self.__checkIndex(begin)

            subList = LinkedList()
            currentNode, i = self.__head, 0    
            while currentNode is not None:
                if (i in range(begin, end, step)): 
                    subList.append(currentNode.data)
                currentNode = currentNode.next
                i += 1
            return subList

        self.__checkIndex(key)
        currentNode, i = self.__head, 0
        while currentNode is not None:
            if (i == key): return currentNode.data
            currentNode = currentNode.next
            i += 1

    # setitem + setslice implementation
    def __setitem__(self, key, value):
        # setslice
        if (isinstance(key, slice)):
            begin, end, step = key.indices(len(self))
            self.__checkIndex(begin)

            if (isinstance(value, (LinkedList, list))):
                i = j = 0
                currentNode = self.__head  
                while currentNode is not None:
                    if (i in range(begin, end, step)): 
                        currentNode.data = value[j]
                        j += 1
                    currentNode = currentNode.next
                    i += 1
            else: 
                currentNode, i = self.__head, 0    
                while currentNode is not None:
                    if (i in range(begin, end, step)): 
                        currentNode.data = value
                    currentNode = currentNode.next
                    i += 1
                
            return   

        self.__checkIndex(key)
        currentNode, i = self.__head, 0
        while currentNode is not None:
            if (i == key): currentNode.data = value
            currentNode = currentNode.next
            i += 1
    
    # Private method to check whether the key is out of List range
    def __checkIndex(self, key):
        if (key >= self.__length): 
            raise IndexError('LinkedList index out of range')

    def append(self, data):
        if (self.__head is None):
            self.__head = Node(data)
        else:
            currentNode = self.__head
            while currentNode.next is not None:
                currentNode = currentNode.next
            currentNode.next = Node(data)
        self.__length += 1

    def copy(self):
        copy = LinkedList()
        currentNode = self.__head
        while currentNode is not None:
            copy.append(currentNode.data)
            currentNode = currentNode.next

        return copy
