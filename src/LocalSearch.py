from src.SolutionService import Solution


class LocalSearch:

    def __init__(self, G, nbMaxIt, nbNeighbors):
        self.currentSolution = None
        self.neighbors = []
        self.bestSolution = None
        self.parsedGraph = G
        self.nbNeighbors = nbNeighbors
        self.nbMaxIt = nbMaxIt

    def setInitialSolution(self):
        initialSolution = Solution.generateInitialSolution(self.parsedGraph)
        self.currentSolution = initialSolution
        self.bestSolution = initialSolution

    def generateNeighborhood(self):
        for i in range(self.nbNeighbors):
            n = Solution.generateNeighbor(self.currentSolution)
            self.neighbors.append(n)

    def cleanNeighborhood(self):
        self.neighbors.clear()

    def updateCurrentSolution(self):
        self.currentSolution = Solution.newCurrentSolution(self.currentSolution, self.neighbors)

    def updateBestSolution(self):
        self.bestSolution = Solution.newBestSolution(self.currentSolution, self.bestSolution)

    def getBestSolution(self):
        return self.bestSolution
