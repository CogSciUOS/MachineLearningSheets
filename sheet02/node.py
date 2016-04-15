from collections import namedtuple
"""
This module provides a Tree structure to be built from Nodes.
"""

class Node(namedtuple('Node', 'label children')):
    """
    This is a simple Node representation. It allows for arbitrary Trees
    and comes with a horizontal __str__ representation.
    """
    
    indentation = 4

    def __str__(self, level=0):
        """
        Returns a string representation of a Tree.
        The Node is traversed pre_order-wise (that means root first, then the
        children in order first to last (assuming the children inside lists)).
        For each level below the root level an indentation of Node.indentation * level 
        as spaces is added. 

        The Node Node('root', [Node('child1', ['child1.1', 'child1.2']), Node('child2', None)])
        will thus result in:

        root
            child1
                child1.1
                child1.2
            child2

        Or, if Node.indentation = 8 is set:

        root
                child1
                        child1.1
                        child1.2
                child2
        
        For the leaves and the data the repr() method is used. An exception is the case
        where the children are a single Node (e.g. Node('root', Node()) ), as this
        might mean there are more nodes coming.

        Note that this function call does no checking for cycles in the Node and might thus
        end up in infinite recursion depths.
        """
        indent = '|' + (' ' * Node.indentation)[:-1]

        if isinstance(self.children, str):
            children_str = '{}L: {!s}\n'.format(indent * (level + 1), self.children)
        else:
            children_strings = []
            try:
                for child in self.children:
                    if isinstance(child, Node):
                        children_strings.append(child.__str__(level + 1))
                    elif isinstance(child, str):
                        children_strings.append('{}L: {!s}\n'.format(indent * (level + 1), child))
                    elif child is not None:
                        children_strings.append('{}L: {!s}\n'.format(indent * (level + 1), child))
            except TypeError:
                if isinstance(self.children, Node):
                    children_strings.append(self.children.__str__(level + 1))
                elif self.children is not None:
                    children_strings.append(repr(self.children))
            children_str = ''.join(children_strings)
        
        if isinstance(self.label, str):
            return '{}L: {!s}\n{}'.format(indent * level, self.label, children_str)
        return '{}L: {!s}\n{}'.format(indent * level, self.label, children_str)

if __name__ == '__main__':
    n1 = Node('n1', None)
    print('n1 (root node only):')
    print(n1)

    n2 = Node('n2', n1)
    print('T2 (child):')
    print(n2)

    n3 = Node('n3', [n1, n2])
    print('n3 (more nesting):')
    print(n3)

    Node.indentation = 8
    print('n3 (more indentation):')
    print(n3)
    Node.indentation = 4

    n4 = Node('n4', 'string child')
    print('n4 (string child):')
    print(n4)

    doc_Node = Node('root', [Node('child1', ['child1.1', 'child1.2']), Node('child2', None)])
    print('DocNode:')
    print(doc_Node)

