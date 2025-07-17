type One = string
type Two = string | number
type Three = 'hello'

// converter para menos ou mais especifico 
let a: One = 'hello'
let b = a as Two // menos especifico
let c = a as Three // mais especifico

let d = <One>'world'
let e = <string | number>'world'

const addOrConcat = (a: number, b: number, c:'add'|'concat'): number | string => {
    if(c === "add") return a+b;
    return '' + a + b 
}

let myVal: string = addOrConcat(2, 2, 'concat') as string

//Cuidado! TS não ve problema, mas aqui sera retornada uma string
let nextVal: number = addOrConcat(2, 2, 'concat') as number

//10 as string
(10 as unknown) as string

// DOM

const img = document.querySelector('img')!
const myImg = document.getElementById('#img') as HTMLImageElement
const nextImg = <HTMLImageElement>document.getElementById('#img')

img.src
myImg.src