sample_path = 'day9_sample.txt';
input_path = 'day9_input.txt';

def file_to_instructions(path):
  file = open(path, 'r');
  rules = list(map(lambda n : int(n), file.read().split('\n')));
  file.close()
  return rules;

def contains_sum_pair(target, list):
  print('find sum of <{}> in <{}>'.format(target, list));
  dict = {};
  for n in list:
    if n in dict:
      return True;
    dict[target - n] = n;

  return False;

def find_first_nonsum(nums, preamble_size):
  start = 0;
  end = preamble_size;

  for i in range(end, len(nums)):
    if not contains_sum_pair(nums[end], nums[start:end]):
      return nums[end];
    start += 1;
    end += 1;

def find_contigous_sum_range(target, list):
  start = 0;
  end = 1;

  for i in range(len(list)):
    sum_range = list[start:end + 1];
    addition = sum(sum_range);

    print('<{}> sums to <{}>'.format(sum_range, addition));
    if addition == target:
      sum_range.sort();
      return sum_range[0] + sum_range[-1];
    if addition < target:
      end += 1;
    else:
      start += 1;
    

def stars(is_sample):
  
  path = sample_path if is_sample else input_path;
  preamble_size = 5 if is_sample else 25;
  nums = file_to_instructions(path);

  nonsum = find_first_nonsum(nums, preamble_size);
  print('star1: {}'.format(nonsum));
  print('star2: {}'.format(find_contigous_sum_range(nonsum, nums)));

stars(False);

