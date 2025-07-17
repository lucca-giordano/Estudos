"use strict";
// converter para menos ou mais especifico 
let a = 'hello';
let b = a; // menos especifico
let c = a; // mais especifico
let d = 'world';
let e = 'world';
const addOrConcat = (a, b, c) => {
    if (c === "add")
        return a + b;
    return '' + a + b;
};
let myVal = addOrConcat(2, 2, 'concat');
//Cuidado! TS não ve problema, mas aqui sera retornada uma string
let nextVal = addOrConcat(2, 2, 'concat');
//10 as string
10;
// DOM
const img = document.querySelector('img');
const myImg = document.getElementById('#img');
const nextImg = document.getElementById('#img');
img.src;
myImg.src;
