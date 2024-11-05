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
    G = Solution.generateInitialSolution(G)
    print("result for initial solution ---> ", Validator.objectiveFunction(G))
    '''
    # to try : 10 000 it, 50 
    tabuSearch = TabuSearch(G, 1000, 100)
    tabuSearch.search()
    bestSolution = tabuSearch.getBestSolution()
    print("result for best solution ---> ", Validator.objectiveFunction(bestSolution))
    '''

    T0 = 100  # Température initiale
    Tf = 0.01  # Température finale
    alpha = 0.95  # Facteur de refroidissement
    nbMaxIt = 10000000  # Nombre maximal d'itérations
    nbNeighbors = 500  # Nombre de voisins par itération

    simulatedAnnealing = SimulatedAnnealing(G, T0, Tf, alpha, nbMaxIt, nbNeighbors)
    simulatedAnnealing.search()
    bestSolution = simulatedAnnealing.getBestSolution()
    print("result for best solution ---> ", Validator.objectiveFunction(bestSolution))