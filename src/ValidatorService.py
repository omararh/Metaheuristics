from src.GraphParserService import GraphParser


class Validator:
    @staticmethod
    def objectiveFunction(G):
        """
        Objective function
        :param G: Graph
        :return sum: int
        """
        coloring = GraphParser.getColoringFromGraph(G)
        return sum(coloring.values())

    @staticmethod
    def validate_coloring(G):
        """
        validate the coloring of the graph (No two adjacent nodes share the same color)
        :param G:
        :return:
        """
        for u, v in G.edges():
            if G.nodes[u]['color'] == G.nodes[v]['color']:
                print(f'\033[91mInvalid coloring: Nodes {u} and {v} have the same color {G.nodes[u]["color"]}.')
                return False
        print('\033[32mColoring is valid: No two adjacent nodes share the same color.')
        return True

