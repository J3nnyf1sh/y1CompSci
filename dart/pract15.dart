//void main(){
//print('Hello, world!');
//}

import 'dart:ffi';
import 'dart:io';
import 'dart:math';

void main() {
  //int result = multiplyBy2(5);
  //print('Result: $result');

  //int distance = 100;
  //double time = 9.58;
  //speedCalculator(distance, time);

  //askForStudentNumber();

  //eurosToPounds(20.0);

  //double area = areaOfCircle();
  //print('The area is: $area');

  //print('How many burgers?');
  //String? burger_input = stdin.readLineSync();
  //int burgers = int.parse(burger_input!);
  //print('What is the price?');
  //String? price_input = stdin.readLineSync();
  //double price = double.parse(price_input!);
  //displayBurgerOrder(burgers, price);

  //print('How much money do you have?');
  //String? wallet = stdin.readLineSync();
  //double wallet_amount = double.parse(wallet!);
  //print('What is the price?');
  //String? burger_price = stdin.readLineSync();
  //double price = double.parse(burger_price!);
  //howManyBurgers(price, wallet_amount);

  print('Side 1:');
  String? a_input = stdin.readLineSync();
  double a = double.parse(a_input!);
  print('Side 2:');
  String? b_input = stdin.readLineSync();
  double b = double.parse(b_input!);
  pythagoras(a, b);
}

int multiplyBy2(int number) {
  return number * 2;
}

void speedCalculator(int distance, double time){
  double speed = distance/time;
  print('Speed: $speed');
}

void askForStudentNumber(){
  print('What is your student number?');
  String? input = stdin.readLineSync(); // ? tells complier that input could be null
  int studentNumber = int.parse(input!); // ! promises complier that the user will enter a number
  print('Your student number is $studentNumber');
}

void sayName(){
  print('My name is Jenny');
}

void studentDetails(){
  sayName();
  print('My student number is 2192054');
  print('My email address is: up2192054@myport.ac.uk');
}

double eurosToPounds(double euros){
  double pounds = euros * 0.86;
  print('Euros: $euros Pounds: $pounds');

  return pounds;
}

double farenheitToCelsius(double farenheit){
  double celsius = (farenheit-32)  * 5/9;

  return celsius;
}

double areaOfCircle(){
  print('Radius:');
  String? input = stdin.readLineSync();
  int radius = int.parse(input!);

  double area = pow(radius, 2) * pi;
  return area;
}

void circleInfo(){
  print('Radus:');
  String? input = stdin.readLineSync();
  int radius = int.parse(input!);

  double area = pow(radius, 2) * pi;
  double circumference = radius * 2 * pi;

  print('Area: $area, Circumference: $circumference');
}


void displayBurgerOrder(int burgers, double price){
  String yas = 'Your order: ';
  for (int i = 1; i <= burgers; i++) {
    yas += '🍔';
  }
  double order_total = price * burgers;
  print(yas);
  print('Total: £${order_total.toStringAsFixed(2)}'); //round to 2 decimal places
}


void howManyBurgers(double burger_price, double wallet_amount) {
  int burgers = wallet_amount ~/ burger_price;
  print('You can buy $burgers burgers.');
}

void pythagoras(a, b){
  double c = sqrt(pow(a, 2) + pow(b, 2));
  print('Hypotenuse: ${c.toStringAsFixed(2)}');
}

double pythagoras2(a, b) => sqrt(pow(a, 2) + pow(b, 2));



