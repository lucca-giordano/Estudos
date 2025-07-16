let myName: string = 'Lucca';
let meaningOfLife: number;
let isLoading: boolean;
let album: string | number;

myName = 'Pedro';
meaningOfLife = 42;
isLoading = true;
album = 2;


const sum = (a:number, b:string) => {
    return a + b;
}

console.log(sum(1,'2'));

let postId: string | number;
let isActive: number | boolean;

let re:RegExp = /\w+/g