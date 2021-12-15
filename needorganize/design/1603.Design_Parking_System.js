class ParkingSystem {
  constructor(big, medium, small) {
    this.bigslot = big;
    this.mediumslot = medium;
    this.smallslot = small;
  }
  addCar(carType) {
    if (carType == 1) {
      //big car
      if (this.bigslot > 0) {
        this.bigslot -= 1;
        return true;
      } else return false;
    } else if (carType == 2) {
      //medium
      if (this.mediumslot > 0) {
        this.mediumslot -= 1;
        return true;
      } else return false;
    } else {
      //small
      if (this.smallslot > 0) {
        this.smallslot -= 1;
        return true;
      } else return false;
    }
  }
}
let parkingSystem = new ParkingSystem(1, 1, 0);
console.log(parkingSystem.addCar(1)); // return true because there is 1 available slot for a big car
console.log(parkingSystem.addCar(2)); // return true because there is 1 available slot for a medium car
console.log(parkingSystem.addCar(3)); // return false because there is no available slot for a small car
console.log(parkingSystem.addCar(1)); // return false because there is no available slot for a big car. It is already occupied.
