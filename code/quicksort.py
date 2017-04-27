#!/usr/bin/env python

def main():
  print("Start")

  a = [2, 9, 1, 19, 16]
  print("Original array: {}".format(a))

  first = a[0]
  left = [i for i in a[1:] if i < first]
  right = [i for i in a[1:] if i > first]
  print("Left array: {}".format(left))
  print("Right array: {}".format(right))

  result = quick_sort(a)
  print("Quick sorted array: {}".format(result))

  print("End")

def quick_sort(a):
  if len(a) <= 1:
    return a
  else:
    first = a[0]
    left = [i for i in a[1:] if i < first]
    right = [i for i in a[1:] if i > first]
    return quick_sort(left) + [first] + quick_sort(right)

if __name__ == "__main__":
  main()
