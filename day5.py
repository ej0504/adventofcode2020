path = 'day5_input.txt'

def file_to_list():
  file1 = open(path, 'r');
  list = file1.readlines();
  file1.close;
  return list;

def partition_search(input, low, high):
  lower = 0;
  upper = 2 ** len(input) - 1;
  
  for n in input:
    midway = ((upper + 1) + lower) / 2;
    if n == high:
      upper = midway - 1;
    elif n == low:
      lower = midway; 
  return lower;

def board_id(input):
  row = partition_search(input[:7], 'B', 'F');
  seat = partition_search(input[7:], 'R', 'L');
  return row * 8 + seat;

def highest_board_id():
  inputs = file_to_list();

  highest_id = 0;
  for input in inputs:
    id = board_id(input.strip());
    if id > highest_id:
      highest_id = id;

  return highest_id;

def missing_id():
  inputs = file_to_list();
  ids = [board_id(input.strip()) for input in inputs];
  ids.sort();

  for i in range(1, len(ids)):
    if (ids[i] - ids[i - 1]) == 2:
      print('{} {} gives {}'.format(ids[i - 1], ids[i], ids[i] - 1));

print(highest_board_id());

missing_id();
