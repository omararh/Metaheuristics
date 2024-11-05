from src.LocalSearch import LocalSearch
from src.ValidatorService import Validator


class TabuSearch(LocalSearch):

    def __init__(self, G, nbMaxIt, nbNeighbors):
        super().__init__(G, nbMaxIt, nbNeighbors)
        self.tabuList = []

    def rollBackOnSolutionUpdate(self, savedSolution):
        """
        roll back on current solution if needed, based on :
         - if the current solution is already tabuList
         - if the current solution is ameliorating the best solution
        :param Graph savedSolution:
        """
        if self.currentSolution not in self.tabuList:
            return
        bestSolutionObjective = Validator.objectiveFunction(self.bestSolution)
        currentSolutionObjective = Validator.objectiveFunction(self.currentSolution)
        if currentSolutionObjective < bestSolutionObjective:
            return
        self.currentSolution = savedSolution

    def search(self):
        """
        Tabu search implementation
        :return:
        """
        self.setInitialSolution()
        cp = 0
        max_tabu_size = max(1, self.nbNeighbors // 10)
        while cp < self.nbMaxIt:
            self.generateNeighborhood()
            savedCurrentSolution = self.currentSolution
            self.updateCurrentSolution()
            self.rollBackOnSolutionUpdate(savedCurrentSolution)

            self.tabuList.append(self.currentSolution)
            if len(self.tabuList) > max_tabu_size:
                self.tabuList.pop(0)

            self.updateBestSolution()
            self.cleanNeighborhood()
            cp += 1
