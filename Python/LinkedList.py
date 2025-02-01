# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List
class LinkedList:
    def __init__(self):
        self.head = None


    ###
    ### gENERIC mETHODS
    ###

    # Prints the List
    def print_list(self):
        temp = self.head
        while(temp):   # This will stop execution as the last node's head is always NULL in a SinglyLinkedList
            print(temp.data)
            temp = temp.next

    # Length of the list
    def size(self):
        current = self.head
        count = 0 
        while current:
            count += 1
            current = current.next

        return count
    
    # Returns the index of the first occurance of the specified value in the list
    def find(self, value):
        current = self.head

        index = 0

        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        
        print("Value doesn't exist in the List!")
        return -1
    
    ###
    ### Push methods
    ###ront

    # Adding a Value to the front of the list
    def push_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    # Addinga Value to the end of the list
    def push_back(self, value):
        new_node = Node(value)

        # if it's an empty list
        if self.head is None:
            self.head = new_node
            return
        
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    ###
    ### Pop Methods
    ###

    # Remove an element from the head end of the list
    def pop_front(self):
        if self.head is None:
            print("List is empty. Cannot pop !")
            return None
        
        popped_node = self.head
        self.head = self.head.next
        popped_node.next = None

        return popped_node.data # returns the popped element
    
    # Removes an element from the tail end of the list
    def pop_back(self):
        if self.head is None:
            print("List is empty. Cannot pop!")
            return None
        
        # If the list has a single element
        if self.head.next is None:
            popped_node = self.head
            self.head = None
            return popped_node.data
        
    ####
    ### Update and Remove methods
    ####

    # Removes the first occurance of a node with the given value
    def remove(self, value):
        current  = self.head
        if current and current.data == value:
            self.head = current.next
            current.next = None
            return
        
        prev = None
        while current and current.data != value:
            prev = current
            current = current.next

        if current is None:
            print(f"Node with data {value} not found.")
            return
        
        prev.next = current.next
        current.next = None

    # Removes the node at the given index
    def remove_at(self, index):
        # Empty List
        if self.head is None:
            print("List is empty.")
            return
        
        # Head as the index
        if index == 0:
            temp = self.head
            self.head = temp.next # self.head.next
            temp.next = None
            return
        
        
        current = self.head
        for i in range(index - 1):
            if current is None:
                print("Index out of bounds.")
                return
            
            current = current.next

        if current is None or current.next is None:
            print("Index out of bounds")
            return
        
        temp = current.next
        current.next = temp.next
        temp.next = None

    # Update the first occurance of old_value to new_value
    def update(self, old_value, new_value):
        current = self.head
        while current:
            if current.data == old_value:
                current.data = new_value
                return
            current = current.next

        print(f"Node with data {old_value} not found.")


    # Reverse the linked list
    # Reverse the linked list (reverse)
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_temp = current.next  # Save next node
            current.next = prev       # Reverse the pointer
            prev = current            # Move prev one step forward
            current = next_temp       # Move current one step forward
        self.head = prev


if __name__ == '__main__':
    ll = LinkedList()
    
    # Using push_back to add nodes 1, 2, 3
    ll.push_back(1)
    ll.push_back(2)
    ll.push_back(3)
    print("Initial list:")
    ll.print_list()

    # Using push_front to add 0 at the beginning
    ll.push_front(0)
    print("After push_front(0):")
    ll.print_list()

    # Remove a node with value 2
    ll.remove(2)
    print("After remove(2):")
    ll.print_list()

    # Remove a node at index 3
    ll.remove_at(3)
    print("After remove_at(3):")
    ll.print_list()

    # Update node value: change 3 to 33
    ll.update(3, 33)
    print("After update(3, 33):")
    ll.print_list()

    # Pop from the front
    popped_front = ll.pop_front()
    print(f"After pop_front(), popped value: {popped_front}")
    ll.print_list()

    # Pop from the back
    popped_back = ll.pop_back()
    print(f"After pop_back(), popped value: {popped_back}")
    ll.print_list()

    # Find the node with value 1.5
    pos = ll.find(1.5)
    print(f"Node with value 1.5 found at index: {pos}")

    # Print the size of the list
    print(f"Size of list: {ll.size()}")

    # Reverse the list
    ll.reverse()
    print("After reverse():")
    ll.print_list()