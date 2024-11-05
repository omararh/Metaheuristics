import networkx as nx
import matplotlib.pyplot as plt


class GraphParser:
    @staticmethod
    def parseFile(file_path):
        try:
            G = nx.Graph()
            with open(file_path, 'r') as file:
                for line in file:
                    if line.startswith('e'):
                        _, u, v = line.strip().split()
                        G.add_edge(u, v)
            return G
        except Exception as e:
            print(f"Error when reading file : {e}")
            return None

    @staticmethod
    def drawGraph(G, coloring):
        pos = nx.spring_layout(G, k=0.1, iterations=20)
        node_colors = [coloring[node] for node in G.nodes()]

        nx.draw(G, pos,
                with_labels=True,
                node_color=node_colors,
                cmap=plt.get_cmap('Set3'),
                node_size=300,
                font_size=8,
                font_weight='bold')

        plt.title("Graph Coloring Visualization")
        plt.show()

    @staticmethod
    def getColoringFromGraph(G):
        """
        :param Graph G:
        :return dict coloring:
        """
        return nx.get_node_attributes(G, 'color')

    @staticmethod
    def getNbOfColorsUsed(G):
        """
        get the number of used colors
        :param G:
        :return int nb of colors:
        """
        coloring = GraphParser.getColoringFromGraph(G)
        unique_colors = set(coloring.values())
        return len(unique_colors)

    @staticmethod
    def convertColoringToResultFile(coloring):
        """
        after getting the best solution we want to store the coloring of the
        graph in a file named "coloring.txt" in the `utils/results/` folder
        :param dict coloring:
        :return:
        """
        try:
            output_path = "utils/result/coloring.txt"

            with open(output_path, 'w') as file:
                for vertex, color in sorted(coloring.items(), key=lambda x: int(x[0])):
                    file.write(f"vertex {vertex}: color {color}\n")

            print(f"\033[32mColoring result saved to {output_path}.")
        except Exception as e:
            print(f"\033[91mError writing to file: {e}")
