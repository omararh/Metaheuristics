from src.GraphParserService import GraphParser
from src.SimulatedAnnealingSearch import SimulatedAnnealing
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
    G = Solution.greedyAlgoSolution(G)
    print("result for greedyAlgo solution ---> ", Validator.objectiveFunction(G))
    print("number of used colors ---> ", GraphParser.getNbOfColorsUsed(G))

    T0 = 100  # Température initiale
    Tf = 0.01  # Température finale
    alpha = 0.95  # Facteur de refroidissement
    nbMaxIt = 1000  # Nombre maximal d'itérations
    nbNeighbors = 50  # Nombre de voisins par itération

    # to try : 10 000 it, 50
    tabuSearch = TabuSearch(G, nbMaxIt, nbNeighbors)
    tabuSearch.search()
    bestSolution = tabuSearch.getBestSolution()
    print("result for best solution N1 ---> ", Validator.objectiveFunction(bestSolution))
    print("number of used colors ---> ", GraphParser.getNbOfColorsUsed(bestSolution))

    simulatedAnnealing = SimulatedAnnealing(G, T0, Tf, alpha, nbMaxIt, nbNeighbors)
    simulatedAnnealing.search()
    bestSolution = simulatedAnnealing.getBestSolution()
    print("result for best solution N2 ---> ", Validator.objectiveFunction(bestSolution))
    print("number of used colors ---> ", GraphParser.getNbOfColorsUsed(bestSolution))

