#!/usr/bin/env python

class Node(object):
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class Queue(object):
  def __init__(self):
    # Left is head and right is tail, enqueue to tail and dequeue from head
    self.left = None
    self.right = None

  def is_empty(self):
    if self.left == None:
      return True
    else:
      return False

  def enqueue(self, data):
    node = Node(data)
    if self.left == None:
      self.left = node
      self.right = node 
    else:
      self.right.next = node
      self.right = node

  def dequeue(self):
    if self.left == None:
      print("No item to dequeue, exit")
      exit(1)
    elif self.left == self.right:
      return_node = self.left
      self.left = None
      self.right = None
      return return_node
    else:
      return_node = self.left
      self.left = return_node.next
      return return_node

  def display(self):
    if self.left == None:
      print("[ ]")
    else:
      node = self.left
      result = "[ "
      while node != self.right:
        result += self.left.data
        node = node.next
      result += self.right.data
      result += " ]"
      print(result)

def main():
  queue = Queue()
  queue.enqueue("node1")
  queue.display()
  queue.enqueue("node2")
  queue.display()
  queue.enqueue("node3")
  queue.display()

  queue.dequeue()
  queue.display()
  queue.dequeue()
  queue.display()

  queue.enqueue("node4")
  queue.display()

  queue.dequeue()
  queue.display()
  queue.dequeue()
  queue.display()

if __name__ == "__main__":
  main()


















