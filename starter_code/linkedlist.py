#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        self.len = 0
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Running time: O(n) because you have to iterate though all items of the list. """
        # TODO: Loop through all nodes and count one for each
        return self.len

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Running time: O(1) each of the operations are constant time, ther are no loops."""
        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists
        if self.tail is not None:
            item = Node(item)
            self.tail.next = item
            self.tail = item
        else:
            item = Node(item)
            self.head = item
            self.tail = item
        self.len += 1

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Running time: O(n) each of the operations are constant time, ther are no loops."""
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists
        if self.head is not None:
            item = Node(item)
            item.next = self.head
            self.head = item
        else:
            item = Node(item)
            self.head = item
            self.tail = item
        self.len += 1

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(1) there are no items in the list
        TODO: Worst case running time: O(n) the item that we are looking for does not exist."""
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
        node = self.head
        if node is None:
            return None
        while True:
            if quality(node.data):
                return node.data
            elif node.next is None:
                return None
            node = node.next

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(1) there are no items in the list
        TODO: Worst case running time: O(n) the item that we are looking to delete does not exist."""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        if self.head is not None:
            node = self.head
        else:
            raise ValueError('Item not found: {}'.format(item))
        last_node = None
        while True:
            if node.data == item:
                if node == self.head and node == self.tail:
                    self.head = None
                    self.tail = None
                elif node == self.head:
                    if node.next is not None:
                        self.head = node.next
                    else:
                        self.head = None
                elif node == self.tail:
                    last_node.next = None
                    self.tail = last_node
                else:
                    last_node.next = node.next
                self.len -= 1
                break
            elif node.next is None:
                raise ValueError('Item not found: {}'.format(item))
            last_node = node
            node = node.next


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
