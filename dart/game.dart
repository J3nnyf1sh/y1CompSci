import 'dart:io';
import 'dart:math';

void main() {
  game();
}

void game() {
  bool guessed = false;
  int number = Random().nextInt(100);
  int guesses = 0;

  while (!guessed) {
    print('Your guess: ');
    String? input = stdin.readLineSync();
    try {
      int guess = int.parse(input!);  
    } on FormatException {
      print('Input a number');
      continue;
    } catch (e) {
      print('Uknown error');
    }
  
    int guess = int.parse(input!);  
    guesses++;

    if (guess == number) { 
      guessed = true;
      print('You guessed correctly');
      print('Number of guesses: $guesses');
    }
    else if (guess < number) {
      print('Higher');
    }
    else if (guess > number) {
      print('Lower');
    }
  }
}