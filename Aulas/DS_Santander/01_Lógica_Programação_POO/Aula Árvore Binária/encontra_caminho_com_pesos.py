"""
Road Navigation

Road systems can be imagined as a graph of intersections connected by lines. The advantage of this is it makes it easier to find the shortest path between any two intersections.
Task

Write a function that takes as arguments:

    A string representing JSON graph of the road system
    The starting intersection (node)
    The ending intersection (node)

And returns a dictionary containing information about the shortest path.
"""

def find_shortest_path_weighted(graph, start, end, path=[], distance=0):
	path = path + [start]
	if start == end:
		return [path], [distance]
	#if not graph.has_key(start):
	#    return None
	distances = []
	paths = []
	for node_dist in graph[start]:
		node = node_dist[0]
		if node not in path:
			distance += node_dist[1]
			newpaths, newdistance = find_shortest_path_weighted(graph, node, end, path, distance)
			for newpath in newpaths:
				distances.append(newdistance)
				paths.append(newpath)            
	return paths, distances


def convert_json_to_linked_list(json_graph):
    nodes = json_graph['graph']['nodes']
    len_nodes = len(nodes)
    edges = json_graph['graph']['edges']
    len_edges = len(edges)
    list_graph = [[] for i in range(len_nodes)]
    print(edges)

    for edge in edges:
        source = edge['source']
        target = edge['target']
        distance = edge['metadata']['distance']
        list_graph[source].append([target, distance])
        list_graph[target].append([source, distance])
    return list_graph


        
graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['E','D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}


json_graph = {
  "graph": {
    "directed": 'false',
    "nodes": [
      { "id": 0 },
      { "id": 1 },
      { "id": 2 },
      { "id": 3 },
      { "id": 4 }
    ],
    "edges": [
      {
        "source": 0,
        "target": 1,
        "metadata": {
          "distance": 5
        }
      },
      {
        "source": 1,
        "target": 3,
        "metadata": {
          "distance": 9
        }
      },
      {
        "source": 3,
        "target": 2,
        "metadata": {
          "distance": 6
        }
      },
      {
        "source": 2,
        "target": 4,
        "metadata": {
          "distance": 3
        }
      },
      {
        "source": 4,
        "target": 3,
        "metadata": {
          "distance": 8
        },
      },
      {
       "source": 4,
       "target": 0,
       "metadata": {
         "distance": 2
       }
     }
    ]
  }
}


list_graph = convert_json_to_linked_list(json_graph)
print(list_graph)

print('find_shortest_path_weighted')
paths, distances = find_shortest_path_weighted(list_graph, 0, 2)
print(paths)
print(distances)