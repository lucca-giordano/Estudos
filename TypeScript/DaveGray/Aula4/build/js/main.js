"use strict";
let userId;
// interface PostId = stringOrNumber - ERRO, 
// Literal types - variaveis só podem receber alguns valores
let myName;
let username;
username = 'John';
// Function
const add = (a, b) => {
    return a + b;
};
const logMessage = (message) => {
    console.log(message);
};
logMessage('Hello');
logMessage(add(2, 3));
let subtract = function (c, d) {
    return c - d;
};
/*interface mathFunction {
    (a: number, b:number) : number
} */
let multiply = function (c, d) {
    return c * d;
};
logMessage(multiply(2, 2));
const addAll = (a, b, c) => {
    if (typeof c !== 'undefined') {
        return a + b + c;
    }
    return a + b;
};
const sumAll = (a = 10, b, c = 2) => {
    if (typeof c !== 'undefined') {
        return a + b + c;
    }
    return a + b;
};
logMessage(addAll(1, 2, 1));
logMessage(sumAll(3, 2));
logMessage(sumAll(undefined, 2));
// rest parameters
const total = (...nums) => {
    return nums.reduce((prev, curr) => prev + curr);
};
logMessage(total(1, 1, 1, 10));
const createError = (errMsg) => {
    throw new Error(errMsg);
};
const infinite = () => {
    let i = 1;
    while (true) {
        i++;
        logMessage(i);
        if (i > 100)
            break;
    }
};
// type guard
const isNumber = (value) => {
    return typeof value === 'number';
};
// uso do tipo never
const numberOrString = (value) => {
    if (typeof value === 'string')
        return 'string';
    if (isNumber(value))
        return 'number';
    return createError('This should never happen!');
};
logMessage(isNumber(true));
