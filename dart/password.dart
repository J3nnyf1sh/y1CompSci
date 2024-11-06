import 'dart:io';
import 'dart:math';

void main(List<String> arguments) {
  int characters = int.parse(arguments[0]);
  String password = generatePassword(characters);
  print('Your password is $password');
}

String generatePassword(int characters) {
  var r = Random();
  return String.fromCharCodes(List.generate(characters, (index) => r.nextInt(33) + 89));
}