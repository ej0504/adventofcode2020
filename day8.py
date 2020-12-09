path = 'day8_sample.txt';

def file_to_instructions():
  file = open(path, 'r');
  rules = file.read().split('\n');
  file.close()
  return rules;

def find_accumulator_at_infinite_loop(instructions):

  #for inst in instructions:
    #print(inst);

  i = 0;
  accumulator = 0;
  prev_instructions = [];
  
  while True:
    if i in prev_instructions:
      return (-1, accumulator);
    
    prev_instructions.append(i);
    inst = instructions[i];
    operator, operand = inst.split();

    if operator == 'acc':
      accumulator += int(operand);
    if operator == 'jmp':
      i += int(operand)
    else:
      i += 1;

    print('<{}> <{}>. acc={}.'.format(operator, operand, accumulator));

    if i == len(instructions):
      return (1, accumulator);
    
    inst = instructions[i];
  return (1, accumulator);

def correct_corrupted_operator(instructions):
  result, acc = find_accumulator_at_infinite_loop(instructions);

  if result > 0:
    return acc;

  for i in range(len(instructions)):
    operator, operand = instructions[i].split();
    instructions_attempt = instructions[:];

    if operator == 'jmp':
      instructions_attempt[i] = '{} {}'.format('nop', operand);
    elif operator == 'nop':
      instructions_attempt[i] = '{} {}'.format('jmp', operand);
    else:
      print('No corrections for ' + instructions[i]);
      pass;

    print('Another attempt after changing ' + instructions[i]);
    result, acc = find_accumulator_at_infinite_loop(instructions_attempt);

    if result > 0:
      return acc;


instructions = file_to_instructions();
print('star1: {}'.format(find_accumulator_at_infinite_loop(instructions)));
print('star2: {}'.format(correct_corrupted_operator(instructions)));