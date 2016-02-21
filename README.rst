==================================================
TARJAN
==================================================

.. image:: https://travis-ci.org/jdowner/tarjan.svg?branch=master
    :target: https://travis-ci.org/jdowner/tarjan


Summary
--------------------------------------------------

Tarjan's algorithm is an efficient way of find all of the strongly-connected
components in a graph. In a directed graph, a strongly-connected component is a
set of nodes where there is a path from each node to every other node in the
set. Note, this implies that there is a cycle in the component, if there is not
than one node in the component, and cycle detection is one of the main usages
for Tarjan's algorithm.


From wikipedia_,

::

The basic idea of the algorithm is this: a depth-first search begins from an
arbitrary start node (and subsequent depth-first searches are conducted on any
nodes that have not yet been found). As usual with depth-first search, the
search visits every node of the graph exactly once, declining to revisit any
node that has already been explored. Thus, the collection of search trees is a
spanning forest of the graph. The strongly connected components will be
recovered as certain subtrees of this forest. The roots of these subtrees are
called the "roots" of the strongly connected components. Any node of a strongly
connected component might serve as the root, if it happens to be the first node
of the component that is discovered by the search.


References
--------------------------------------------------

.. _wikipedia: https://en.wikipedia.org/wiki/Tarjan's_strongly_connected_components_algorithm
