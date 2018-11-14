def solution(number):
  sum = 0;
  for number in range(0, number):
      if number % 3 == 0 or number % 5 == 0:
          print(number)
          sum += number;

  return sum        
