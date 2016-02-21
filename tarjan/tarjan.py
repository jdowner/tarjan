import collections


def strongly_connected(edges, nodes=None):
    """Returns a list of strongly-connected components

    This function uses Tarjan's algorithm to find all of the strongly-connected
    components in a directed graph. The components are returned as a list of
    lists, where each list contains the nodes that are a part of a
    strongly-connected component.

    This implementation was derived from the pseudo-code on wikipedia,

    https://en.wikipedia.org/wiki/Tarjan's_strongly_connected_components_algorithm


    Arguments:
        edges - A list of edges that are represented by tuple that contains the
                source node (the first element) and the target node (the second
                element)
        nodes - An optional list of nodes. If this list is not provided, the
                nodes are inferred from the list of edges

    Raises:
        A ValueError is raised if a node list is provided and it does not
        contain all of the nodes referenced by the edges. It is valid for the
        node list to contain more nodes than are contained in the edge list,
        but not fewer.

    Returns:
        A list of lists of nodes

    """
    # Determine the set of nodes from the edges
    if nodes is None:
        nodes = list({w for u, v in edges for w in (u, v)})

    # The nodes referenced by the edges should be a subset of the provided
    # list.
    else:
        induced = {w for u, v in edges for w in (u, v)}
        if not induced.issubset(nodes):
            msg = "An edge contains a node that is not in the node list"
            raise ValueError(msg)

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
