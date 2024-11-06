void main() {
  BowlingAlley alley = BowlingAlley();
  alley.showPins();
  alley.bowl([3, 5, 9]);
}

class BowlingAlley {
  List<List<String>> pins = [
    ['I', ' ', 'I', ' ', 'I', ' ', 'I'],
    [' ', 'I', ' ', 'I', ' ', 'I', ' '],
    [' ', ' ', 'I', ' ', 'I', ' ', ' '],
    [' ', ' ', ' ', 'I', ' ', ' ', ' ']
    ];
  
  void resetPins() {
    pins = [
      ['I', ' ', 'I', ' ', 'I', ' ', 'I'],
      [' ', 'I', ' ', 'I', ' ', 'I', ' '],
      [' ', ' ', 'I', ' ', 'I', ' ', ' '],
      [' ', ' ', ' ', 'I', ' ', ' ', ' ']
    ];
  }

  void showPins() {
    String displayingPins = '';
    for (List<String> row in pins) {
      displayingPins += row.join('') + '\n';
    }
    print(displayingPins);
  }

  void bowl(List<int> knocked) {
    Map<int, List<int>> map = {
      1:  [3, 3],
      2:  [2, 2],
      3:  [2, 4],
      4:  [1, 1],
      5:  [1, 3],
      6:  [1, 5],
      7:  [0, 0],
      8:  [0, 2],
      9:  [0, 4],
      10: [0, 6],
    };

    for (int knockedOver in knocked) {
      List<int> coordinates = map[knockedOver]!;
      int row = coordinates[0];
      int col = coordinates[1];
      pins[row][col] = ' ';
    }

    showPins();
  }
}

