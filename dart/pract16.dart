import 'dart:io';

import 'dart:math';

void main() {
  //maxNumbers(4, 3);

  //dayInMonth('March');
  //dayInMonth('February');
  //dayInMonth('September');

  //print(multiplyBy2(2));

  //heartMonitor(70, 160);
  //heartMonitor(20, 170);

  //basicCalculator(4, 2, 'divide');

  //bool prime = isPrime(3);
  //print(prime);

  //int gcd = calcGCD(210, 45);
  //print(gcd);

  //customisedGreeting('1200');
}

//1
void maxNumbers(a, b) {
  int max_number = max(a, b);
  print(max_number);
}

//2
void dayInMonth(month) {
  var thirty_one = [
    'january',
    'march',
    'may',
    'july',
    'august',
    'october',
    'december'
  ];
  var thirty = ['april', 'june', 'september', 'november'];

  if (thirty_one.contains(month.toLowerCase())) {
    print('$month has 31 days');
  } else if (thirty.contains(month.toLowerCase())) {
    print('$month has thirty days');
  } else if (month.toLowerCase() == 'february') {
    print('$month has twenty eight days');
  }
}

//3
double multiplyBy2(double number) => number * 2;

//4
void heartMonitor(int age, int bpm) {
  if (age <= 20 && bpm > 170) {
    print('High heart rate for 0-20!');
  } else if (age >= 21 && age <= 40 && bpm > 155) {
    print('High heart rate for 21-40!');
  } else if (age >= 41 && age <= 60 && bpm > 140) {
    print('High heart rate for 41-60!');
  } else if (age >= 61 && age <= 80 && bpm > 130) {
    print('High heart rate for 61-80!');
  } else if (age >= 81 && bpm > 100) {
    print('High heart rate for 81+!');
  } else {
    print('Healthy heart rate!');
  }
}

//5
void basicCalculator(double num1, double num2, String operand) {
  double result = 0;

  if (operand.toLowerCase() == 'add') {
    result = num1 + num2;
  } else if (operand.toLowerCase() == 'subtract') {
    result = num1 - num2;
  } else if (operand.toLowerCase() == 'multiply') {
    result = num1 * num2;
  } else if (operand.toLowerCase() == 'divide') {
    result = num1 / num2;
  }

  print('Result: $result');
}

//6
bool isPrime(int n) {
  bool prime = true;
  for (int i = 2; i < n; i++) {
    if (n % i == 0) {
      prime = false;
      break;
    }
  }
  return prime;
}

//7
int calcGCD(int a, int b) {
  if (b == 0) {
    return a;
  }
  return calcGCD(b, a % b);
}

//8
void customisedGreeting(time) {
  if (time is! int || time > 2400 || time < 0) {
    print('Need a time between 0000 and 2400');
  } else {
    if (time >= 500 && time < 1200) {
      print('Good Morning');
    } else if (time >= 1200 && time < 1800) {
      print('Good afternoon');
    } else if (time >= 1800 && time < 2100) {
      print('Good evening');
    } else if (time >= 2100 && time < 100) {
      print('Good Night');
    } else {
      print('Go to bed');
    }
  }
}
