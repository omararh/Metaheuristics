import networkx as nx
from src.ValidatorService import Validator
from src.GraphParserService import GraphParser
import random


class Solution:

    @staticmethod
    def assignColorsToGraph(G, coloring):
        """
        Given a networkx graph and a set of colors, assign colors to a graph.
        :param Graph G:
        :param dict coloring:
        :return Graph G:
        """
        nx.set_node_attributes(G, coloring, 'color')
        return G

    @staticmethod
    def generateInitialSolutionRandomly(G):
        """
        Generates an initial solution graph by assigning random colors to nodes
        while ensuring no two adjacent nodes have the same color.
        :param Graph G: The graph to color
        :return: Graph G with colors assigned randomly to nodes
        """
        coloring = {}
        # Generate a pool of possible colors
        colors = list(range(1, len(G.nodes()) + 1))

        for node in G.nodes():
            available_colors = set(colors)
            for neighbor in G.neighbors(node):
                if neighbor in coloring:
                    available_colors.discard(coloring[neighbor])
            chosen_color = random.choice(list(available_colors))
            coloring[node] = chosen_color

        Solution.assignColorsToGraph(G, coloring)
        return G

    @staticmethod
    def generateInitialSolution(G):
        """
        Generates an initial solution graph using a custom glouton coloring algorithm.
        :param Graph G:
        :return: Graph G with colors assigned to nodes
        """
        coloring = {}
        nodes = sorted(G.nodes(), key=lambda x: G.degree[x], reverse=True)
        for node in nodes:
            neighbor_colors = set()
            for neighbor in G.neighbors(node):
                if neighbor in coloring:
                    neighbor_colors.add(coloring[neighbor])
            color = 1
            while color in neighbor_colors:
                color += 1
            coloring[node] = color
        G = Solution.assignColorsToGraph(G, coloring)
        return G

    @staticmethod
    def findSmallestValidColorForNode(G, coloring, node):
        neighbor_colors = {coloring[neighbor] for neighbor in G.neighbors(node)}
        new_color = 1
        while new_color in neighbor_colors:
            new_color += 1
        return new_color

    @staticmethod
    def generateNeighbor(G):
        coloring = GraphParser.getColoringFromGraph(G)
        nodes = list(G.nodes())
        random.shuffle(nodes)
        randomlyChosenNode = nodes[0]
        new_color = Solution.findSmallestValidColorForNode(G, coloring, randomlyChosenNode)
        coloring[randomlyChosenNode] = new_color
        Solution.assignColorsToGraph(G, coloring)
        return G

    @staticmethod
    def newCurrentSolution(currentSolution, neighbors):
        """
        Arguments
        currentSolution : Graph
        neighbors : List<Graph>

        return
        currentSolution : Graph (improved)
        """
        current_objective = Validator.objectiveFunction(currentSolution)

        for neighbor in neighbors:
            neighbor_objective = Validator.objectiveFunction(neighbor)
            if neighbor_objective < current_objective:
                current_objective = neighbor_objective
                currentSolution = neighbor

        return currentSolution

    @staticmethod
    def newBestSolution(currentSolution, bestSolution):
        """
        Arguments
        currentSolution : Graph
        bestSolution : Graph

        return
        solution : Graph (improved)
        """
        current_objective = Validator.objectiveFunction(currentSolution)
        best_objective = Validator.objectiveFunction(bestSolution)
        if current_objective < best_objective:
            return currentSolution
        return bestSolution
