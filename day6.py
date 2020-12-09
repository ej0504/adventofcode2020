import re;

path = "day6_sample.txt";

def file_to_list():
  file1 = open(path, 'r');
  list = file1.readlines();
  list2= [];

  temp_line = '';
  for line in list:
    if line.isspace():
      list2.append(temp_line);
      temp_line = '';
    else:
      temp_line += line;
  list2.append(temp_line);
  file1.close();
  return [line.strip() for line in list2];

def count_distinct_questions(group):
  distinct = set("".join(group.split()));
  return len(distinct);

def sum_group_distinct_questions():
  groups = file_to_list();
  print(sum([count_distinct_questions(group) for group in groups]));

def count_agreed_questions(group):
  peeps = group.split();
  peep_count = len(peeps);
  questions = "".join(peeps);
  
  question_count = {};
  for question in questions:
    if question in question_count:
      question_count[question] += 1;
    else:
      question_count[question] = 1;
  
  agreed_questions = len([filter(lambda count: count == peep_count, question_count.values())]);
  #agreed_questions = sum(1 for count in question_count.values() if count == peep_count);
  # print('{} gives {} from {}'.format(group, agreed_questions, question_count));
  return agreed_questions;

def sum_group_agreed_questions():
  groups = file_to_list();
  print(sum([count_agreed_questions(group) for group in groups]));

sum_group_agreed_questions();