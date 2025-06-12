// class 정의
class Dog {
  constructor() {
    this.eyes = 2;
    this.nose = 1;
    this.mouth = 1;
    this.ears = 2;
    this.kinds = "dog";
    console.log(`${this.kinds} initialized: Eyes=${this.eyes}, Nose =${this.nose}, Mouth = ${this.mouth}, Ears = ${this.ears}
    `);
  }

  Bark() {
    console.log("멍멍")
  }
}

class Poodle extends Dog {
  constructor() {
    super(); // 부모인 DOG 클래스 호출 오버라이딩
    this.kinds = "Poodle";
    console.log(`${this.kinds} initialized: Eyes=${this.eyes}, Nose = ${this.nose}, Mouth = ${this.mouth}, Ears = ${this.ears}
    `);
  }
  Bark() {
    console.log("멍멍")
  }
}

let a = new Dog();
a.Bark();

let b = new Poodle();
b.Bark();

function plus(a, b) {
  return a + b;
}