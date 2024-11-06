import 'dart:io';
import 'dart:math';

void main() {
  //print('Email: ');
  //String? input = stdin.readLineSync();
  //String email = input!.toString();
  //bool validity = isValidEmail(email); 
  //print(validity);

  //List<double> temperatures = [10.0, 12.5, 14.0, 16.5, 15.0, 12.0];
  //weatherDifference(temperatures);

  //Set<String> foodNames = {'milkshake', 'yoghurt', 'burger', 'banana milk'};
  //removeMilk(foodNames);

  //capitalize('jENNy');

  //String sentence = 'Learning #Dart and #Flutter is fun';
  //extractHashtags(sentence);

  //capitalizeSentence('me and my girlies we gon party till its early');

  //snakeToCamel('is_valid_email');

  Map<String, List<int>> marksDetailed = {
    'Programming': [100, 80, 70, 64, 00, 52],
    'Networks': [90, 85, 95],
    'Core Computing': [64, 70]
  };
  capMarks('Networks', marksDetailed);
  capMarks('Programming', marksDetailed);
  print(marksDetailed);

  //Map<String, double> prices = {
    //'Tesco Finest Yogurt': 0.90,
    //'Robinson\'s orange squash': 2.00,
    //'Tesco Finest Macaroni Cheese': 4.25,
    //'Doritos Cool Original': 1.20,
    //'Milk': 1.20,
  //};
  //ogPriceRise(prices);
  //print('After price rises: $prices');

  //Map<String, double> newPrices = priceRise(prices);
  //print(newPrices);

}

bool isValidEmail(String email) {
  String username = email.split('@')[0];
  print(username);
  String domain = email.split('@')[1];
  print(domain);
  bool validity = true;
  if (username.startsWith('up') != true || username.length != 9 || domain != 'myport.ac.uk') {
    validity = false;
  }
  return validity;
}

bool checkExpenses(List<double> expenditures, double maximum) {
  double total = 0;
  for (double expenses in expenditures) {
    total += expenses;

    if (total > maximum) {
      print('Maximum reached');
      break;
    }
  }

  return true; 
} 

void weatherDifference(List<double> temperatures) {
  int numberOfTemps = temperatures.length;
  int lastIndex = numberOfTemps - 1;
  double difference = temperatures[lastIndex] - temperatures[0];
  print(difference);
}

void removeMilk(Set<String> foodNames) {
  Set<String> noMilk = {};
  for (String food in foodNames) {
    if (!food.contains('milk')){
      noMilk.add(food);
    }
  }
  print(noMilk);
}

void capMarks(String module, Map<String, List<int>> marks) {
  List<int> newMarks = [];
  for (int mark in marks[module]!) {
    if (mark > 40) {
      newMarks.add(40);
    }
    else {
      newMarks.add(mark);
    }
  }
  marks[module] = newMarks;//
}

void ogPriceRise(Map<String, double> productPrices) {
  if (productPrices.containsKey('Milk')) {
    print('Price of milk is £${productPrices['Milk']}');
    productPrices['Milk'] = productPrices['Milk']! + 0.20;
  }
}

Map<String, double> priceRise(Map<String, double> productPrices) {
  Map<String, double> newPrices = productPrices;
  for (String product in productPrices.keys) {
    newPrices[product] = newPrices[product]! * 1.10;
  }
  return newPrices;
}

String capitalize(String string){
  //int lastIndex = string.length;
  String lowerString =string.substring(1).toLowerCase();
  String capitalised = string[0].toUpperCase();
  String newString = capitalised + lowerString;
  return newString;
}

void extractHashtags(String sentence){
  Set<String> hashtags = {};
  List<String> split = sentence.split(' ');
  for (String word in split) {
    if (word.startsWith('#')) {
      hashtags.add(word);
    }
  }
  print(hashtags);
}

void capitalizeSentence(String sentence){
  List<String> newString = [];
  List<String> split = sentence.split(' ');
  
  for (String word in split) {
    String lowerString = word.substring(1).toLowerCase();
    String capitalised = word[0].toUpperCase();
    String capitalisedWord = capitalised + lowerString;
    
    newString.add(capitalisedWord);
  }

  String newSentence = newString.join(' ');
  print(newSentence);
}

void snakeToCamel(String snake) {
  String camelCase = '';
  List<String> sub = snake.split('_');
  for (var subString in sub) {
    if (subString == sub[0]) {
      String newString = subString.toLowerCase();
      camelCase += newString;
    }
    else {
      String newString = capitalize(subString);
      camelCase += newString;
    }
  }
  print(camelCase);
}

// void compress(int n, String string){
  
//}


