from src.GraphParserService import GraphParser
from src.SolutionService import Solution
from src.SolutionService import Validator
from src.TabuSearch import TabuSearch
import networkx as nx

if __name__ == "__main__":
    #print("give the graph filename (without extension)")
    #graphFileName = str(input("graph filename: "))
    #file_path = "Utils/Graphs/" + graphFileName + ".col"
    file_path = "Utils/Graphs/dsjc500.1.col"

    G = GraphParser.parseFile(file_path)
    G = Solution.generateInitialSolution(G)
    print("res = ", Validator.objectiveFunction(G))
    ''''
    graph_edges = list(G.edges())
    print("graph_edges =", graph_edges)

    tabuSearch = TabuSearch(G, 1000, 100)
    tabuSearch.search()
    bestSolution = tabuSearch.getBestSolution()
    #Validator.validate_coloring(bestSolution)
    print("res = ", Validator.objectiveFunction(bestSolution))
    '''
    '''
    s = Solution.generateInitialSolution(G)
    for node, data in s.nodes(data=True):
        print(f"vertex {node}: color {data['color']}")

    Solution.generateNeighbor(s)
    coloring = nx.get_node_attributes(s, 'color')
    print(type(coloring))
    '''
