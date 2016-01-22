import collections


def strongly_connected(edges):
    """Returns a list of strongly-connected components

    This function uses Tarjan's algorithm to find all of the strongly-connected
    components in a directed graph. The components are returned as a list of
    lists, where each list contains the nodes that are a part of a
    strongly-connected component.


    Arguments:
        edges - a list of edges that are represented by tuple that contains the
                source node (the first element) and the target node (the second
                element)

    Returns:
        A list of lists of nodes

    """
    # Determine the set of nodes from the edges
    nodes = list({w for u, v in edges for w in (u, v)})

    # Create a lookup table for the children of each node
    children = collections.defaultdict(list)
    for src, dst in edges:
        children[src].append(dst)

    # Define the working structures used by the algorithm
    low_index = dict()
    index = dict()
    stack = list()
    scc = list()

    # Use a class variable to share the index with closures so that this code
    # works for both python2 and python3
    class current(object):
        index = 0

    def traversal(node):
        """Depth-first traversal over the nodes"""

        # Define the index of this node
        index[node] = current.index
        low_index[node] = current.index

        # Update the shared index
        current.index += 1

        stack.append(node)

        # Iterate over each of the nodes children and determine the low index
        for child in children[node]:
            if child not in index:
                traversal(child)
                low_index[node] = min(low_index[node], low_index[child])

            elif child in stack:
                low_index[node] = min(low_index[node], index[child])

        # If this node is a root node, create a new strongly-connected
        # component using the nodes on the stack
        if low_index[node] == index[node]:
            component = list()

            while stack:
                w = stack.pop()
                component.append(w)

                if w == node:
                    break

            scc.append(component)

    # Iterate over all of the nodes to ensure that every node is included in a
    # strongly-connected component
    for node in nodes:
        if node not in index:
            traversal(node)

    return scc
