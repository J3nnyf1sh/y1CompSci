void main() {
  Car myCar = Car('red', 10.0);
  print(myCar.colour);
  print(myCar.speed);
  myCar.colour = 'blue';
  print(myCar.colour);

  myCar.accelerate(10);
  print(myCar.speed);
  myCar.brake();
  print(myCar.speed);
  print(myCar);

  Ingredient pasta = Ingredient('Pasta', 200);
  Ingredient sauce = Ingredient('Sauce', 100);
  Recipe pastaRecipe = Recipe('Pasta');
  pastaRecipe.addIngredient(pasta);
  pastaRecipe.addIngredient(sauce);
  print(pastaRecipe.ingredients);
  print(pastaRecipe.totalCalories());
  print(pastaRecipe);

  KidsMeal happyMeal = KidsMeal('Cheeseburger', 'Slimer');
  happyMeal.toy = 'Ectomobile';
  print(happyMeal.toy); // Ectomobile
  Meal meal = Meal('Big Mac');
  print(meal); // Big Mac, chips and drink
  print(happyMeal); // Cheeseburger, chips and drink plus a Ectomobile

  Person alice = Person('Alice', 20);
  Student alice2 = Student('Alice', 20, '+ 44 0740129134', 4);
  alice.age = 21;
  print('Alice is ${alice.age} years old');

  print('Next year, Alice will be ${alice.ageNextYear()} years old');
  print('Alice has a valid name: ${alice.hasValidName()}');

  print(alice);
  print(alice.runtimeType);

  print(alice2);


}

class Car {
  String colour;
  double speed;

  Car(this.colour, this.speed);

  void accelerate(double inc) {
    speed += inc;
  }

  // Q1 -----------------------------
  double distanceTravelled(double hours) {
    double distance = speed * hours;
    return distance;
  }
  // Q1 -----------------------------

  void brake() {
    speed = 0;
  }

  String toString() {
    return 'Car(colour: $colour, speed: $speed)';
  }
}

class BankAccount {
  String owner;
  double _balance = 0.0;

  BankAccount(this.owner);

  void deposit(double amount) => _balance += amount;

  void withdraw(double amount) {
    if (_balance - amount >= 0) {
      _balance -= amount;
    }
  }

  // Not needed anymore as we have balance getter and setter below
  // double getBalance() => _balance;

  // double get balance {
  //   return _balance;
  // }

  // Getter using arrow syntax
  double get balance => _balance;

  void set balance(double amount) {
    if (amount >= 0) {
      _balance = amount;
    }
  }
}

class Ingredient {
  String name;
  int calories;

  Ingredient(this.name, this.calories);

  String toString() => '$name ($calories calories)';
}

class Recipe {
  String name;
  Set<Ingredient> ingredients = {};

  Recipe(this.name);

  // String toString() => '$name: $ingredients';

  String toString() {
    String result = '$name\n';
    for (Ingredient ingredient in ingredients) {
      result += '  $ingredient\n';
    }
    result += 'Total calories: ${totalCalories()}';
    return result;
  }

  void addIngredient(Ingredient ingredient) {
    ingredients.add(ingredient);
  }

  int totalCalories() {
    int total = 0;
    for (Ingredient ingredient in ingredients) {
      total += ingredient.calories;
    }
    return total;
  }
}

class Meal {
  String burger;

  Meal(this.burger);

  String toString() {
    return '$burger, chips and drink';
  }
}

class KidsMeal extends Meal {
  String toy = 'unknown';

  // KidsMeal(String burger, this.toy) : super(burger);

  KidsMeal(String burger, String toy) : super(burger) {
    this.toy = toy;
  }

  String toString() {
    return '${super.toString()} plus a $toy';
  }
}

class Person {
  String name = 'unknown';
  int age = 0;

  Person(String name, int age) {
    this.name = name;
    this.age = age;
  }

  // Q2 -----------------------------
  bool isAdult() {
    if (age >= 18) {
      return true;
    }
    else {
      return false;
    }
  }
  // Q2 -----------------------------

  int ageNextYear() {
    return age + 1;
  }

  bool hasValidName() {
    if (name.length > 2 && name.length < 100) {
      return true;
    } else {
      return false;
    }
  }

  String toString() {
    return 'Person(name: $name, age: $age, isAdult: ${isAdult()})';
  }
}

// Q4 ----------------------------
class Student extends Person {
  int level = 4;
  String? _phoneNumber;

  Student(String name, int age, this._phoneNumber, this.level): super(name, age);

  void graduate() {
    level++;
  }

  String greet() => 'Hello, $name!';

  String get phoneNumber {
    String lastFourDigits = _phoneNumber!.substring(6);
    return '***-***-$lastFourDigits';
  }

  void set phoneNumber(String phoneNumber) {
    if (phoneNumber.length == 10) {
      _phoneNumber = phoneNumber;
    }
  }

  @override
  String toString() {
    return 'Student(name: $name, age: $age, level: $level, isAdult: ${isAdult()})';
  }
}
// Q4 ----------------------------

class Module {
  String name;
  int credits;

  Module(this.name, {this.credits = 20});
}

class Course {
  String name;
  List<Module> modules = [];
  int totalCredits = 0;
  int _maxCredits = 120;

  Course(this.name);

  void addModule(Module module) {
    if (totalCredits + module.credits <= maxCredits) {
      modules.add(module);
      totalCredits += module.credits;
    }
  }

  int get maxCredits => _maxCredits;

  String toString() {
    String output = 'Course name: $name, Modules:\n';
    for (Module module in modules) {
      output += '  ${module.name} (${module.credits} credits)\n';
    }
    output += 'Total credits: $totalCredits';
    return output;
  }
}

class Shape {
  double x = 0.0;
  double y = 0.0;

  Shape(this.x, this.y);

  void move(double dx, double dy) {
    x += dx;
    y += dy;
  }

  String toString() => 'x: $x, y: $y';
}

class Circle extends Shape {
  double radius = 0.0;

  // Circle(double x, double y, double radius) : super(x, y) {
  //   this.radius = radius;
  // }

  Circle(double x, double y, this.radius) : super(x, y);

  String toString() => '${super.toString()}, radius: $radius';
}

// Q3 -----------------------------
class Rectangle extends Shape {
  double width = 0.0;
  double height = 0.0;

  Rectangle(double x, double y, this.width, this.height) : super(x, y);

  double getArea() {
    double area = width * height;
    return area;
  }
  
  double getPerimeter() {
    double perimeter = 2 * (width + height);
    return perimeter;
  }
}
// Q3 -----------------------------

// Q5 ----------------------------
class Product {
  String name = 'unknown';
  int age = 0;

  Person(String name, int age) {
    this.name = name;
    this.age = age;
  }
}
// Q5 ----------------------------