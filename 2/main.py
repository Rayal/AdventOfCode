
      
def parse_line(line: str) -> dict:
  retval = {}
  line = line.split(':')
  min_max = line[0][:-2].split('-')
  retval['min'] = int(min_max[0])
  retval['max'] = int(min_max[1])
  retval['char'] = line[0][-1]
  retval['data'] = line[1]
  
  return retval
  
  
def check_compliance(password: dict) -> bool:
  # n = password['data'].count(password['char'])
  # return password['min'] <= n <= password['max']
  interest = password['data'][password['min']] + password['data'][password['max']]
  print(password)
  print(interest)
  print('__________')
  return interest.count(password['char']) == 1
  
  
def parse_input(path: str) -> int:
  with open(path) as inp:
    compliance_list = [check_compliance(parse_line(line)) for line in inp]
    return sum(compliance_list)
    
input_path = "puzzle_input.py"
print(parse_input(input_path))
