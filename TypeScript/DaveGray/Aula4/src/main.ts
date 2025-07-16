// Type 
type stringOrNumber = string | number;

type stringOrNumberArray = (string | number)[]

type Guitarist = {
    name?: string,
    active: boolean,
    albuns: stringOrNumberArray
};

type userId = stringOrNumber;

let userId: userId;

// interface PostId = stringOrNumber - ERRO, 

// Literal types - variaveis só podem receber alguns valores
let myName: 'Dave'

let username: 'Dave' | 'John' | 'Amy'

username = 'John';

// Function

const add = (a: number, b: number) => {
    return a + b
}

const logMessage = (message: any): void => {
    console.log(message);
}

logMessage('Hello')
logMessage(add(2, 3))

let subtract = function(c: number, d:number): number {
    return c - d
}

type mathFunction = (a: number, b:number) => number

/*interface mathFunction { 
    (a: number, b:number) : number
} */

let multiply:mathFunction = function(c, d) {
    return c * d
}

logMessage(multiply(2, 2))

const addAll = (a: number, b: number, c?: number): number => {
    if (typeof c !== 'undefined'){
        return a + b + c
    }
    return a + b
}

const sumAll = (a: number = 10, b: number, c: number = 2): number => {
    if (typeof c !== 'undefined'){
        return a + b + c
    }
    return a + b
}

logMessage(addAll(1, 2, 1))
logMessage(sumAll(3, 2))
logMessage(sumAll(undefined, 2))

// rest parameters
const total = (...nums: number[]): number => {
    return nums.reduce((prev, curr) => prev + curr)
}

logMessage(total(1, 1, 1, 10))

const createError = (errMsg: string) => {
    throw new Error(errMsg)
}

const infinite = () => {
    let i: number = 1;
    while(true){
        i++;
        logMessage(i)
        if (i>100) break
    }
}

// type guard
const isNumber = (value: any): boolean => {
    return typeof value === 'number' 
}

// uso do tipo never
const numberOrString = (value: number | string): string => {
    if(typeof value === 'string') return 'string';
    if(isNumber(value)) return 'number';
    return createError('This should never happen!')
}

logMessage(isNumber(true))