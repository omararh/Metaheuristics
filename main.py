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
    print("result for initial solution ---> ", Validator.objectiveFunction(G))

    tabuSearch = TabuSearch(G, 1000, 100)
    tabuSearch.search()
    bestSolution = tabuSearch.getBestSolution()
    print("result for best solution ---> ", Validator.objectiveFunction(bestSolution))
