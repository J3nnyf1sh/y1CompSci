void main() {
  Phone phone1 = Phone(34343, "This is my first phone");
  Phone phone2 = Phone(6, "This is my second phone");

  print(phone1.toString());
  print(phone2.toString());

  Network EE = Network();
  EE.addPhone(phone1);
  EE.addPhone(phone2);

  EE.broadcastMessage('The end of the world');
  print(EE.toString());
}

class Phone {
  int ID;
  String message;

  Phone(this.ID, this.message); //constructor

  String sendMessage(){
    return this.message;
  }
  
  void receiveMessage(String newMessage){
    this.message = newMessage;
  }

  @override
  String toString(){
    return 'Phone ID: ${this.ID} Message: ${this.message}';
  }
}

class Network{
  List<Phone> phones = [];

  void addPhone(Phone phone){
    phones.add(phone);
  }

  void broadcastMessage(String message){
    for (Phone phone in phones) {
      phone.receiveMessage(message);
    }
  }

  @override 
  String toString(){
    String string = '';
    for (Phone phone in phones) {
      string += 'Phone ID: ${phone.ID} Message: ${phone.message}\n';
    }
    return string;
  }
}