#!/usr/bin/env python

from collections import deque


class BreathFirstSearchGame(object):
  def __init__(self):
    # The node index are from 0 to 7, such as 0, 1, 2, 3, 4
    self.node_number = 8

    # The edges to connect each node
    self.edges = [(0, 1), (0, 3), (1, 2), (1, 5), (2, 7), (3, 4), (3, 6),
                  (4, 5), (5, 7)]

    # The 8 * 8 matrix of boolean values, only updated by the edges
    self.graph = [[False for j in range(self.node_number)]
                  for i in range(self.node_number)]
    #print(self.graph)

    # The queue of open set, which is an array
    self.open_set = deque()

    # The source and destination nodes for this game
    self.source_node = 0
    self.destination_node = 7

    # The 8 array of boolean which means this node is visited
    self.is_visit_node_array = [False for i in range(self.node_number)]

    # The 8 array of int which means this node's best parent node id
    self.best_parent_node_array = [-1 for i in range(self.node_number)]

    self.initialize_internal_variables()
    #print(self.graph)

    self.travel_and_update_variables()

    self.travel_desination_path(self.destination_node)

  def initialize_internal_variables(self):
    # Update the graph with edges
    for i, j in self.edges:
      self.graph[i][j] = True
      self.graph[j][i] = True

    # Update the open set with the source nodes
    self.open_set.append(self.source_node)
    self.is_visit_node_array[self.source_node] = True
    self.best_parent_node_array[self.source_node] = self.source_node

  def travel_and_update_variables(self):
    # Travel if some nodes in open set
    while len(self.open_set) > 0:

      current_node = self.open_set.popleft()

      for other_node in range(self.node_number):

        #import ipdb;ipdb.set_trace()
        # Check if these two nodes are connected
        if self.graph[current_node][other_node]:

          # Check if the other node is visited
          if self.is_visit_node_array[other_node] == False:

            # Update the open set and visited array
            self.open_set.append(other_node)
            self.best_parent_node_array[other_node] = current_node
            self.is_visit_node_array[other_node] = True

  def travel_desination_path(self, destination_node):

    if destination_node == self.source_node:
      print(destination_node)

    else:
      self.travel_desination_path(
          self.best_parent_node_array[destination_node])
      print(destination_node)


def main():
  print("Start breath first search")

  game = BreathFirstSearchGame()


if __name__ == "__main__":
  main()
