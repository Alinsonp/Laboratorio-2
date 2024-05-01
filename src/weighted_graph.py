import math
import numpy as np
from typing import List, Optional, Tuple
from Map import aristas, show_in_browser, conexion

class Node:

  # constructor de la clase Node recibe los parametros de la clase que se encuentra en manejo_data_set.py
  # y los nodos adyacentes
  def __init__(self, Source_Airport_Code: str, Source_Airport_Name: str,
               Source_Airport_City: str, Source_Airport_Country: str,
               Source_Airport_Latitude: float, Source_Airport_Longitude: float,
               ) -> None:
    self.Source_Airport_Code = Source_Airport_Code
    self.Source_Airport_Name = Source_Airport_Name
    self.Source_Airport_City = Source_Airport_City
    self.Source_Airport_Country = Source_Airport_Country
    self.Source_Airport_Latitude = Source_Airport_Latitude
    self.Source_Airport_Longitude = Source_Airport_Longitude
    self.edges: List[Tuple['Node', str]] = []

  # añadir los nodos adyacentes
  def add_edge(self, edge: Tuple['Node', str]) -> None:
    if edge not in self.edges:
      self.edges.append(edge)

  def __str__(self) -> str:
    return (f"Source_Airport_Code: {self.Source_Airport_Code}\n"
            f"Source_Airport_Name: {self.Source_Airport_Name}\n"
            f"Source_Airport_City: {self.Source_Airport_City}\n"
            f"Source_Airport_Country: {self.Source_Airport_Country}\n"
            f"Source_Airport_Latitude: {self.Source_Airport_Latitude}\n"
            f"Source_Airport_Longitude: {self.Source_Airport_Longitude}\n")


class WeightedGraph:
  INF = (1 << 31) - 1  # 2 ** 31 - 1

  # constructor de la clase WeightedGraph recibe el parametro n que es el numero de nodos
  def __init__(self, n: int) -> None:
    self.n = n
    self.nodes: List["Node"] = []
    self.aristas: List[Tuple[str, str, str]] = []

  # añadir los nodos
  def add_node(self, node: "Node") -> None:
    self.nodes.append(node)

  # añadir las aristas
  def add_edge(self, node1: "Node", node2: "Node") -> bool:
    weight = str(self.haversine(node1.Source_Airport_Latitude, node1.Source_Airport_Longitude,
                 node2.Source_Airport_Latitude, node2.Source_Airport_Longitude))
    if (node1.Source_Airport_Code, node2.Source_Airport_Code, weight) in self.aristas or (node2.Source_Airport_Code, node1.Source_Airport_Code, weight) in self.aristas:
      return False
    self.aristas.append((node1.Source_Airport_Code, node2.Source_Airport_Code, weight))
    node1.add_edge((node2, weight))
    node2.add_edge((node1, weight))
    return True

  # calcular la distancia
  def haversine(self, lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    R = 6372.8
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    a = math.sin(dLat / 2)**2 + math.cos(lat1) * \
        math.cos(lat2) * math.sin(dLon / 2)**2
    c = 2 * math.asin(math.sqrt(a))
    return R * c

  # buscar el nodo
  def search_node(self, source_airport_code: str) -> Optional["Node"]:
    for node in self.nodes:
      if node.Source_Airport_Code == source_airport_code:
        return node
    return None

  def __get_minimum(self, l):
    minor = ["", np.inf]
    index = -1
    for i in range(len(l)):
      if l[i][1] < minor[1]:
        minor = l[i].copy()
        index = i

    return (minor, index)

  # hallar las distancias minimas

  # hallar las 10 distancias minimas
  def tenmax(self, minimas, father):
    max_ordenadas = sorted(minimas.items(), key=lambda x: x[1], reverse=True)
    ten = max_ordenadas[:10]
    for i in range(len(ten)):
      print(self.search_node(ten[i][0]), "Distancia:", ten[i][1], "km")
      print()

    if ten[0][1] == 0:
      print("No hay conexiones con ese código o código inválido")
      print()
      return
  # hallar las aristas de las 10 distancias minimas (no sirve)
    for key in ten:
      l = key[0]
      if key[1] != 0:
        while father[l] != None:
            # crear una arista dada por nodo con el nombre del padre l y el nombre del nodo l
          aristas(self.search_node(l).Source_Airport_Latitude, self.search_node(l).Source_Airport_Longitude, self.search_node(
            father[l]).Source_Airport_Latitude, self.search_node(father[l]).Source_Airport_Longitude, l, father[l])
          l = father[l]
    show_in_browser()

  # hallar las distancias infinitas y volverlas 0
  def notinf(self, distance, father):
    for key in distance:
      if distance[key] == np.inf:
        distance[key] = 0
    self.tenmax(distance, father)
    return distance

  # source: nodo fuente
  def Dijkstra(self, source, progress, source2=None):
    task1 = progress.add_task("[cyan]Iniciando Dijkstra...", total=100)

    distance = dict()
    father = dict()
    visited = dict()

    print(self.search_node(source))
    progress.update(task1, advance=10)

    for u in self.nodes:
      distance[u.Source_Airport_Code] = np.inf
      father[u.Source_Airport_Code] = None
      visited[u.Source_Airport_Code] = False

    distance[source] = 0
    queue = [[source, distance[source]]]
    progress.update(task1, advance=20)
    while len(queue) != 0:
      t = self.__get_minimum(queue)
      u = t[0]
      u_name = u[0]
      queue.pop(t[1])
      visited[u_name] = True

      for v in self.aristas:
        v_name = None
        if v[0] == u_name:
          v_name, (v_weight) = v[1], float(v[2])
        elif v[1] == u_name:
          v_name, v_weight = v[0], float(v[2])
        if (v_name != None):
          if (not visited[v_name]):
            if (distance[v_name] > distance[u_name] + v_weight):
              distance[v_name] = distance[u_name] + v_weight
              father[v_name] = u_name
              queue.append([v_name, distance[v_name]])

    progress.update(task1, advance=30)

    if source2 != None:
      while father[source2] != None:
        print(self.search_node(source2), "Distancia:", distance[source2], "km")
        # crear una arista dada por nodo con el nombre del padre l y el nombre del nodo l
        aristas(self.search_node(source2).Source_Airport_Latitude, self.search_node(source2).Source_Airport_Longitude, self.search_node(
          father[source2]).Source_Airport_Latitude, self.search_node(father[source2]).Source_Airport_Longitude, source2, father[source2])
        source2 = father[source2]
      show_in_browser()
      return

    progress.update(task1, advance=40)
    return self.notinf(distance, father)
