#Задано масив цілих чисел розмірності . 
#Здійснити циклічний зсув його від’ємних елементів на k позицій вправо. 
#Додатні елементи масиву записати в оберненому порядку. 
#Наприклад, -2 5 6 -3 -4 3 -1. k = 2 
#Результат: -4 3 6 -1 -2 5 -3.

from random import randint

class Negative(Exception):
    pass

class WrongListElement(Exception):
    pass

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(nodes[0])
            self.head = node
            for elem in range(1, len(nodes)):
                node.next = Node(nodes[elem])
                node = node.next

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def push_back(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = node

    def get_negative_node(self, param):
        current = self.head
        next1 = current.next
        answer = 0
        while next1:
            if current.data < 0:
                answer = current
                if param == "first":
                    return answer
            current = next1
            next1 = current.next
        if current.data < 0:
            answer = current
        return answer.data if answer != 0 else answer

    def negative_k_cycle(self, k):
        for i in range(k):
            k1 = 0
            t = 0
            last_node_data = self.get_negative_node("last")
            if last_node_data == 0:
                return self
            for node in self:
                if node.data < 0 and k1 == 0:
                    t_data = node.data
                    k1 += 1
                elif node.data < 0 and k1 > 0:
                    s_data = node.data
                    node.data = t_data
                    t_data = s_data
            first_node = self.get_negative_node("first")
            if first_node == 0:
                return
            first_node.data = last_node_data
        return self

    def reverse_positive(self):
        list_1 = LinkedList()
        for node1 in self:
            if node1.data >= 0:
                list_1.push_back(node1.data)
        prev = None
        current = list_1.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        list_1.head = prev
        current1 = list_1.head
        for node1 in self:
            if node1.data >= 0:
                node1.data = current1.data
                current1 = current1.next
        return self

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes = list(map(str, nodes))
        return " ".join(nodes)


def validation_input(parametr):
    while True:
        try:
            if parametr == "linked_list":
                param = LinkedList()
                print('Type STOP to exit')
                while True:
                    n = input('Element of linked list: ')
                    if n == 'STOP':
                        return param
                    elif str(abs(int(n))).isnumeric() is False:
                        raise WrongListElement
                    else:
                        param.push_back(int(n))
            elif parametr == "a" or parametr == "b":
                param = int(input('Input ' + parametr + ': '))
                if str(abs(param)).isnumeric() is False:
                    raise ValueError
            else:
                param = int(input('Input ' + parametr + ': '))
                if param < 0:
                    raise Negative
        except WrongListElement:
            print('Element of list should be number, try again')
            return
        except Negative:
            print(parametr + " should be positive")
        except ValueError:
            print("You typed not a number")
        else:
            return param


while True:
    print('''Choose option: 
    1. Input array and k 
    2. Input n, k but array will be generated
    3. Exit''')
    choice = validation_input("choice")
    if choice == 1:
        linked_list = validation_input("linked_list")
        k = validation_input("k")
    elif choice == 2:
        n = validation_input("n")
        print("You need to input a i b for range of elements: ")
        a = validation_input("a")
        b = validation_input("b")
        k = validation_input("k")
        if a > b:
            a, b = b, a
        linked_list = LinkedList([randint(a, b) for i in range(n)])
        print("Linked list:", linked_list)
    else:
        break
    print(linked_list)
    linked_list.negative_k_cycle(k)
    linked_list.reverse_positive()
    print("Result:", linked_list)