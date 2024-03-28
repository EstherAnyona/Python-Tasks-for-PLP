import 'dart:io';

// Define an interface
abstract class Vehicle {
  void start();
  void stop();
}

// Implement the interface with a class
class Car implements Vehicle {
  @override
  void start() {
    print("Car started");
  }

  @override
  void stop() {
    print("Car stopped");
  }

  void accelerate() {
    print("Car is accelerating");
  }
}

// Create a subclass that inherits from Car and overrides a method
class ElectricCar extends Car {
  @override
  void accelerate() {
    print("Electric car is accelerating silently");
  }
}

// A class that represents data from a file
class CarData {
  String make;
  String model;
  int year;

  CarData(this.make, this.model, this.year);

  @override
  String toString() {
    return '$year $make $model';
  }
}

void main() {
  // Create an instance of ElectricCar
  var electricCar = ElectricCar();

  // Demonstrate method override
  electricCar.accelerate(); // Output: Electric car is accelerating silently

  // Demonstrate class initialization with data from a file
  var carData = readFileAndCreateCarData('car_data.txt');
  print(carData); // Output: 2022 Tesla Model S

  // Demonstrate the use of a loop
  for (var i = 0; i < 3; i++) {
    electricCar.accelerate();
  }
}

CarData readFileAndCreateCarData(String filePath) {
  var file = File(filePath);
  var lines = file.readAsLinesSync();
  var data = lines[0].split(' ');
  var make = data[0];
  var model = data[1];
  var year = int.parse(data[2]);
  return CarData(make, model, year);
}
