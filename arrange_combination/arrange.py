#!/usr/bin/env python

def range(input_list, step):

  if step == 3:
    print(input_list)
    return

  for i in range(step, len(input_list)):
    input_list[step], input_list[i] = input_list[i], input_list[step]
    range(input_list, step+1)
    input_list[step], input_list[i] = input_list[i], input_list[step]


def main():
  import ipdb;ipdb.set_trace()
  input_list = ["a", "b", "c"]
  range(input_list, 0)

if __name__ == "__main__":
  main()
