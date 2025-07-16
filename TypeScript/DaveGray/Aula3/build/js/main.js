"use strict";
let stringArr = ['one', 'hey', 'dave'];
let guitars = ['Strat', 'Les Paul', 5150];
let mixedData = ['EVH', 1984, true];
stringArr[0] = 'John';
stringArr.push('42');
guitars[0] = 1984;
guitars.unshift('Jim');
guitars = stringArr;
//guitars = mixedData - erro
mixedData = guitars;
let test = [];
let bands = [];
bands.push('Van Halen');
// Tupla
let myTuple = ['dave', 1234, false];
let mixed = ['Jhon', 1, false];
myTuple[1] = 42;
// Objetos
let myObj;
myObj = mixed;
console.log(typeof myObj);
console.log(myObj);
console.log(typeof mixed);
console.log(mixed);
console.log(typeof myTuple);
console.log(myTuple);
const exampleObj1 = {
    prop1: 'Dave',
    prop2: true
};
exampleObj1.prop2 = false;
let evh = {
    name: 'Eddie',
    active: false,
    albuns: [1984, 5150, 'OU812']
};
let jp = {
    name: 'Jimmy',
    active: false,
    albuns: ['I', 'II', 'IV'],
};
console.log(evh);
console.log(evh);
const greetGuitarist = (guitarist) => {
    if (guitarist.name) {
        return `Hello ${guitarist.name.toLocaleUpperCase()}!`;
    }
    return 'Hello';
};
console.log(greetGuitarist(evh));
// Enum
var Grade;
(function (Grade) {
    Grade[Grade["U"] = 1] = "U";
    Grade[Grade["D"] = 2] = "D";
    Grade[Grade["C"] = 3] = "C";
    Grade[Grade["A"] = 4] = "A";
    Grade[Grade["B"] = 5] = "B";
})(Grade || (Grade = {}));
console.log(Grade.B);
