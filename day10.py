sample_path = 'day10_sample_1.txt';
input_path = 'day10_input.txt';

def file_to_instructions(path):
  file = open(path, 'r');
  rules = list(map(lambda n : int(n), file.read().split('\n')));
  file.close()
  return rules;

def print_lines(lines):
  for line in lines:
    print(line);

def search_for_valid_perm(nums, ans, jolt_rating):
  #print('<{}>, <{}>'.format(jolt_rating, ans));
  if not nums:
    return ans;

  for i in range(len(nums)):
    if nums[i] <= jolt_rating + 3:
      new_ans = ans[:];
      new_ans.append(nums[i]);
      result = search_for_valid_perm(nums[i + 1:], new_ans, nums[i]);
      if result:
        return result;
  return None;

def count_valid_perms(nums, index, jolt_rating, target, dict):
  if jolt_rating == target:
    return 1;

  count = 0;
  for i in range(index, len(nums)):
    if nums[i] <= jolt_rating + 3:
      if i in dict:
        count += dict[i];
      else:
        i_count = count_valid_perms(nums, i + 1, nums[i], target, dict);
        dict[i] = i_count;
        count += i_count;

    else:
      return count;
  return count;

def find_diffs(perm):
  diff_1 = 0;
  diff_3 = 1; #  built in adapter always +3
  for i in range(1, len(perm)):
    
    diff = perm[i] - perm[i - 1];
    if diff == 3:
      diff_3 += 1;
    if diff == 1:
      diff_1 += 1;

  return (diff_1, diff_3);

def find_jolt_difference_product(nums):
  nums.sort();

  perm = search_for_valid_perm(nums, [0], 0);
  diff_1, diff_3 = find_diffs(perm);
  
  final = diff_3 * diff_1;
  return final;

def count_perms(nums):
  dict = {};
  counts = count_valid_perms(nums, 0, 0, nums[-1], dict);
  return counts;


def stars(is_sample):
  path = sample_path if is_sample else input_path;
  nums = file_to_instructions(path);

  print('star1: {}'.format(find_jolt_difference_product(nums)));
  print('star2: {}'.format(count_perms(nums)));

stars(False);

