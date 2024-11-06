import 'dart:io';

void main() {
  print('How mcuh money can you spend on burger?');
  String? money_input = stdin.readLineSync();
  double money = double.parse(money_input!);
  print('How much does one burger cost?');
  String? burger_price_input = stdin.readLineSync();
  double burger_price = double.parse(burger_price_input!);
  burgerOrder(money, burger_price);
}

void burgerOrder(double money, double burger_price) {
  int burgers = money ~/ burger_price;
  double total_price = burger_price * burgers;
  String yas = 'Your order: ';
  for (int i = 1; i <= burgers; i++) {
    yas += '🍔';
  }
  print(yas);
  print('Total: £${total_price.toStringAsFixed(2)}');
}

