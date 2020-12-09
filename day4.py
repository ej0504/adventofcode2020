import re;

path = "day4_input.txt";
pattern_format = '{}:(#)*(\w+)';
keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'];

def file_to_list():
  file1 = open(path, 'r');
  list = file1.readlines();
  list2= [];

  temp_line = '';
  for line in list:
    if line == '\n':
      list2.append(temp_line);
      temp_line = '';
    else:
      temp_line += line;
  list2.append(temp_line);
  file1.close();
  return list2;

def extract(key, line):
  pattern = pattern_format.format(key);
  match = re.search(pattern, line);
  #print('k:{} p:{} '.format(key, pattern));
  if match:
    return True;
  #print('No match! k:{} p:{} '.format(key, pattern));
  return False;


def all_present(line):
  count = 0;
  for key in keys:
    if extract(key, line):
      count += 1;
  #print(count);
  return count == len(keys);


list2 = file_to_list();

count = 0;
for line in list2:
  #print(line);
  if all_present(line):
    count += 1;


print(count);