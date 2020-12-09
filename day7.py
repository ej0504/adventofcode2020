import re;
path = 'day7_sample.txt';

def file_to_rules():
  file = open(path, 'r');
  rules = file.read().split('\n');
  file.close()
  return rules;

def find_num_idx(item):
  for i in range(len(item)):
    if not item[i].isdigit():
      return i;



def rule_into_structs(index, rule, idx, grid, first_pass):
  key, list_str = rule.split(' bags contain ');

  if first_pass:
    idx[key] = index;

  else:
    list = [map.replace(' bags', '').replace(' bag', '').strip() for map in list_str[:-1].split(',')];
    # strip out number.
    for item in list:
      non_num_i = find_num_idx(item);
      if non_num_i > 0:
        num = int(item[:non_num_i]);
        final_item = item[non_num_i:].strip();
        grid[idx[key]][idx[final_item]] = num;

def grid_2d(length):
  grid = [0] * length;
  for i in range(length):
    grid[i] = [0] * length;
  return grid;

def print_grid(grid):
  for x in grid:
    print(x);

def set_bags_containing(grid, starting_bag_index, containing_bags):

  for x in range(len(grid)):
    quantity = grid[x][starting_bag_index];
    if quantity != 0:
      containing_bags.add(x);
      set_bags_containing(grid, x, containing_bags);

def count_bags_inside(grid, starting_bag_index):

  count = 0;
  for y in range(len(grid)):
    quantity = grid[starting_bag_index][y];
    if quantity != 0:
      count += count_bags_inside(grid, y) * quantity + quantity;
  return count;


def day7():
  rules = file_to_rules();

  index_map = {};

  length = len(rules);
  grid = grid_2d(length);

  for count, rule in enumerate(rules):
    rule_into_structs(count, rule, index_map, grid, True);

  #print(index_map);

  for count, rule in enumerate(rules):
    rule_into_structs(count, rule, index_map, grid, False);

  #print_grid(grid);

  containing_bags = set();
  set_bags_containing(grid, index_map['shiny gold'], containing_bags);

  print('star 1:{}'.format(len(containing_bags)));
  print('star 2:{}'.format(count_bags_inside(grid, index_map['shiny gold'])));

day7();

