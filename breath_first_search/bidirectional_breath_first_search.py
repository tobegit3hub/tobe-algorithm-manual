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
    self.source_open_set = deque()
    self.destination_open_set = deque()

    # The source and destination nodes for this game
    self.source_node = 0
    self.destination_node = 7

    # The 8 array of boolean which means this node is visited
    self.source_is_visit_node_array = [False for i in range(self.node_number)]
    self.destination_is_visit_node_array = [
        False for i in range(self.node_number)
    ]

    # The 8 array of int which means this node's best parent node id
    self.source_best_parent_node_array = [-1 for i in range(self.node_number)]
    self.destination_best_parent_node_array = [
        -1 for i in range(self.node_number)
    ]

    # Record the step index of collision
    self.collision_step = 0
    self.collision_node = -1

    self.initialize_internal_variables()
    #print(self.graph)

    self.travel_and_update_variables()

    print("The output for the forward:")
    self.source_travel_desination_path(self.source_node, self.collision_node)
    print("Inverse the output for the backward:")
    self.destination_travel_desination_path(self.destination_node,
                                            self.collision_node)

  def initialize_internal_variables(self):
    # Update the graph with edges
    for i, j in self.edges:
      self.graph[i][j] = True
      self.graph[j][i] = True

    # Update the open set with the source nodes
    self.source_open_set.append(self.source_node)
    self.source_is_visit_node_array[self.source_node] = True
    self.source_best_parent_node_array[self.source_node] = self.source_node

    # Update the open set with the destination nodes
    self.destination_open_set.append(self.destination_node)
    self.destination_is_visit_node_array[self.destination_node] = True
    self.destination_best_parent_node_array[
        self.destination_node] = self.destination_node

  def travel_and_update_variables(self):

    is_collision = False

    # Travel if some nodes in open set
    while len(self.source_open_set) > 0 or len(self.destination_open_set) > 0:

      # Run forward
      if len(self.source_open_set) > 0:
        current_node = self.source_open_set.popleft()

        for other_node in range(self.node_number):

          # Check if these two nodes are connected
          if self.graph[current_node][other_node]:

            # Check if the other node is visited
            if self.source_is_visit_node_array[other_node] == False:

              # Update the open set and visited array
              self.source_open_set.append(other_node)
              self.source_best_parent_node_array[other_node] = current_node
              self.source_is_visit_node_array[other_node] = True

      # Run backward
      if len(self.destination_open_set) > 0:
        current_node = self.destination_open_set.popleft()

        for other_node in range(self.node_number):

          # Check if these two nodes are connected
          if self.graph[current_node][other_node]:

            # Check if the other node is visited
            if self.destination_is_visit_node_array[other_node] == False:

              # Update the open set and visited array
              self.destination_open_set.append(other_node)
              self.destination_best_parent_node_array[
                  other_node] = current_node
              self.destination_is_visit_node_array[other_node] = True

      # Check collision
      #print(self.source_is_visit_node_array)
      #print(self.destination_is_visit_node_array)
      self.collision_step += 1
      if is_collision:
        return
      else:
        for i in range(self.node_number):
          if self.source_is_visit_node_array[i] == True and self.destination_is_visit_node_array[i] == True:
            is_collision = True
            self.collision_node = i
            print("Collision step: {}, collision node: {}".format(
                self.collision_step, self.collision_node))
            return

  def source_travel_desination_path(self, source_node, destination_node):
    if destination_node == source_node:
      print(destination_node)
    elif destination_node == -1:
      print("Error, get node of -1 which is not updated")
    else:
      self.source_travel_desination_path(
          source_node, self.source_best_parent_node_array[destination_node])
      print(destination_node)

  def destination_travel_desination_path(self, source_node, destination_node):
    if destination_node == source_node:
      print(destination_node)
    elif destination_node == -1:
      print("Error, get node of -1 which is not updated")
    else:
      self.destination_travel_desination_path(
          source_node,
          self.destination_best_parent_node_array[destination_node])
      print(destination_node)


def main():
  print("Start bidirectional breath first search")

  game = BreathFirstSearchGame()


if __name__ == "__main__":
  main()
