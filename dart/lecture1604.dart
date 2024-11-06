import 'dart:io';
import 'dart:math';

void main() {
  double answer = equation1(4);
  String roundedAnswer = answer.toStringAsFixed(2);
  print(roundedAnswer);

  equation2();
}

//y = 3x + 2
double equation1(double x) => (3 * x)  + 2;

// - 10 to +10 increments of .5, and y in second column
void equation2() {
  print('-'.padRight(33, '-'));
  print('|' + 'x'.padRight(15, ' ') + '|' + 'y'.padRight(15, ' ') + '|');
  print('|'.padRight(32, '-') + '|');
  for (double x = -10; x <= 10; x += 0.5) {
    double y = equation1(x);
    String yString = y.toStringAsFixed(2);
    String xString = x.toStringAsFixed(2);

    print('|' + '${xString.padRight(15, ' ')}|${yString.padRight(15, ' ')}' + '|');
  }

  print('-'.padRight(33, '-'));
}   
