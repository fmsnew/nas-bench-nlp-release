import pygraphviz as pgv
from IPython.display import Image
import matplotlib.pyplot as plt


def plot_recepie(recepie, dpi=100):
    graph = pgv.AGraph(directed=True, strict=True,
                       fontname='Helvetica', arrowtype='open')

    node_color = {'x':'forestgreen', 
                  'h_prev_0':'orange',
                  'h_new_0':'orange',
                  'h_prev_1':'cyan',
                  'h_new_1':'cyan',
                  'h_prev_2':'purple',
                  'h_new_2':'purple'}
    
    blend_i_to_color = {1:'blue3', 
                        2:'brown3'}
    
    nodes_dict = {}
    for k in recepie.keys():
        if k not in nodes_dict:
            graph.add_node(len(nodes_dict), label=recepie[k]['op'] + ':\n' + k, 
                           fillcolor=node_color.get(k, 'white'), style='filled')
            nodes_dict[k] = len(nodes_dict)
    for k in recepie.keys():
        for i, n in enumerate(recepie[k]['input']):
            if n not in nodes_dict:
                graph.add_node(len(nodes_dict), label=n, 
                               fillcolor=node_color.get(n, 'white'), style='filled')
                nodes_dict[n] = len(nodes_dict)
            #print(nodes_dict[k], nodes_dict[n])
            if recepie[k]['op'] != 'blend':
                graph.add_edge(nodes_dict[n], nodes_dict[k])
            else:
                if i == 0:
                    graph.add_edge(nodes_dict[n], nodes_dict[k], style='dashed')
                else:
                    graph.add_edge(nodes_dict[n], nodes_dict[k], color=blend_i_to_color[i])    

    return Image(graph.draw(format='png', prog='dot', args=f'-Gdpi={dpi} -Nfontsize=8'))