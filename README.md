# MetaHeuristicProject

Metaheuristics are advanced optimization algorithms designed to solve complex computational problems by efficiently searching through large solution spaces where traditional methods fail. They employ high-level problem-independent strategies that balance exploration of the search space with exploitation of promising areas, making them particularly effective for NP-hard problems like graph coloring, traveling salesman, and scheduling problems.

# Graph Coloring with Metaheuristics

## Project Overview
This project explores the application of metaheuristic algorithms to solve the graph coloring problem, a well-known NP-hard optimization problem in computer science. Specifically, we implement and compare the performance of Simulated Annealing (SA) and Tabu Search (TS) algorithms on various graph instances.

## The Graph Coloring Problem
The graph coloring problem involves assigning colors to the vertices of a graph such that no adjacent vertices share the same color, while minimizing the total number of colors used. This problem has numerous real-world applications including:
- Scheduling problems
- Register allocation in compilers
- Frequency assignment in wireless networks
- Map coloring

## Implemented Metaheuristics

### Simulated Annealing
Simulated Annealing is a probabilistic technique inspired by the annealing process in metallurgy. Our implementation includes:
- A temperature cooling schedule with configurable parameters
- Neighborhood exploration through random vertex color reassignments
- Acceptance probability function based on solution quality and current temperature
- Configurable stopping criteria (maximum iterations, target solution quality)

### Tabu Search
Tabu Search is a local search algorithm that uses memory structures (tabu lists) to avoid cycling and getting trapped in local optima. Our implementation features:
- Short-term memory (tabu list) to prevent recently visited solutions
- Aspiration criteria to override tabu status for promising solutions
- Neighborhood exploration strategies focusing on conflicting vertices
- Diversification mechanisms to explore different regions of the search space

# To run the project : 
`pip install networkx`  
`python main.py`
