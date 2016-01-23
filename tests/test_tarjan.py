import collections
import unittest

import tarjan


Edge = collections.namedtuple('Edge', 'src dst')

class TestTarjen(unittest.TestCase):
    def test_linear_graph(self):
        edges = [
                Edge('a', 'b'),
                Edge('b', 'c'),
                Edge('c', 'd'),
                ]

        scc = tarjan.strongly_connected(edges)

        # There should be 4 distinct components
        self.assertEqual(4, len(scc))

        # Each component should contain one node
        for component in scc:
            self.assertEqual(1, len(component))

    def test_redundant_graph(self):
        # If the graph contains no nodes, there should be no strongly-connected
        # components
        scc = tarjan.strongly_connected([])
        self.assertEqual(0, len(scc))

    def test_3_cycle(self):
        # Create a 3-cycle graph. The result should be a single component
        # containing 3 nodes.
        edges = [
                Edge('a', 'b'),
                Edge('b', 'c'),
                Edge('c', 'a'),
                ]

        scc = tarjan.strongly_connected(edges)

        self.assertEqual(1, len(scc))
        self.assertEqual(3, len(scc[0]))

    def test_4_cycle(self):
        # Create a 4-cycle graph. The result should be a single component
        # containing 4 nodes.
        edges = [
                Edge('a', 'b'),
                Edge('b', 'c'),
                Edge('c', 'd'),
                Edge('d', 'a'),
                ]

        scc = tarjan.strongly_connected(edges)

        self.assertEqual(1, len(scc))
        self.assertEqual(4, len(scc[0]))

    def test_3_cycle_4_cycle(self):
        # Create a graph that contains a 3-cycle and a 4-cycle.

        edges = [
                # The 3-cycle
                Edge('a', 'b'),
                Edge('b', 'c'),
                Edge('c', 'a'),

                # The 4-cycle
                Edge('s', 't'),
                Edge('t', 'u'),
                Edge('u', 'v'),
                Edge('v', 's'),

                # An edge connecting the cycles
                Edge('s', 'a'),
                ]

        scc = tarjan.strongly_connected(edges)

        # There are 2 components corresponding to the 2 different cycles.
        self.assertEqual(2, len(scc))
        self.assertEqual([3,4], sorted(len(c) for c in scc))

    def test_funnel(self):
        edges = [
                # The first group
                Edge('p', 'q'),

                Edge('q', 'a'),
                Edge('q', 'b'),
                Edge('q', 'c'),

                Edge('a', 's'),
                Edge('b', 's'),
                Edge('c', 's'),

                # The second group
                Edge('s', 't'),

                Edge('t', 'x'),
                Edge('t', 'y'),
                Edge('t', 'z'),

                Edge('x', 'p'),
                Edge('y', 'p'),
                Edge('z', 'p'),
                ]

        scc = tarjan.strongly_connected(edges)

        self.assertEqual(1, len(scc))
        self.assertEqual(10, len(scc[0]))

    def test_node_list(self):
        edges = [
                Edge('d', 'a'),
                Edge('d', 'b'),
                Edge('d', 'c'),
                ]

        nodes = ['a', 'b', 'c', 'd', 'e']

        scc = tarjan.strongly_connected(edges, nodes=nodes)

        self.assertEqual(5, len(scc))
        for component in scc:
            self.assertEqual(1, len(component))

    def test_invalid_node_list(self):
        edges = [
                Edge('d', 'a'),
                Edge('d', 'b'),
                Edge('d', 'c'),
                ]

        nodes = ['a', 'b', 'c']

        with self.assertRaises(ValueError):
            tarjan.strongly_connected(edges, nodes=nodes)
