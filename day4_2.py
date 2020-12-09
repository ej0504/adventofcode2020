import re;
import functools;

path = "day4_input.txt";

def val_byr(year):
  return 1920 <= int(year) <= 2002;

def val_iyr(year):
  return 2010 <= int(year) <= 2020;

def val_eyr(year):
  return 2020 <= int(year) <= 2030;

def val_hgt(height):
  match = re.search('(\d+)cm', height);
  if match:
    return 150 <= int(match.group(1)) <= 193;

  match = re.search('(\d+)in', height);
  if match:
    return 59 <= int(match.group(1)) <= 76;

  return False;

def passfn(x):
  return True;

validations = {
  'byr': ['(^\d{4}$)', val_byr],
  'iyr': ['(^\d{4}$)', val_iyr],
  'eyr': ['(^\d{4}$)', val_eyr],
  'hgt': ['(^(\d+)(cm|in)$)', val_hgt],
  'hcl': ['#([0-9a-f]{6})', passfn],
  'ecl': ['^(amb|blu|brn|gry|grn|hzl|oth)$', passfn],
  'pid': ['(^\d{9}$)', passfn]
  };

def file_to_list():
  file = open(path, 'r');
  passports = file.read().split('\n\n');
  file.close()
  return passports;

def field_valid(pattern, method, line):
  match = re.match(pattern, line);
  if match:
    return method(match.group(1));
  return False;


def passport_fields_valid(passport):
  valid_count = 0;

  for field in passport.split():
    key, value = field.split(':');
    if key in validations and field_valid(validations[key][0], validations[key][1], value):
      valid_count += 1;

  return valid_count == 7;

def attempt2():
  final_count = 0;
  passports = file_to_list();
  for passport in passports:
    if passport_fields_valid(passport):
      final_count += 1;

  print(final_count);

attempt2();
