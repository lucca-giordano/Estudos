class Coder {

    secondLang!: string

    constructor(
        public readonly name: string,
        public music: string,
        private age: number,
        protected lang:string = 'TypeSCript'
    ) {
        this.name = name
        this.music = music
        this.age = age
        this.lang = lang
    }

    public getAge(){
        return `Ola, tenho ${this.age}`
    }
}

const Dave = new Coder("Dave", "Rock", 42, "ola!")

console.log(Dave.getAge())
//console.log((Dave.age))
//console.log(Dave.lang)

class WebDev extends Coder {
    constructor(
        public computer: string,
        name: string,
        music: string,
        age: number
    ) {
        super(name, music, age)
        this.computer = computer
    }

    public getLang() {
        return `I write ${this.lang}`
    }
}

const Sarah = new WebDev('Mac', 'Sara', 'Lofi', 25)
console.log(Sarah.getLang())
// console.log(Sarah.age)
// console.log(Sarah.lang)
//////////////////////////////////////////

// Implementing interface to class

interface Musician {
    name: string,
    instrument: string,
    play(action: string): string
}

class Guitarist implements Musician {
    name: string
    instrument: string
    constructor(name: string, instrument: string){
        this.name = name
        this.instrument = instrument
    }

    play(action: string) {
        return `${this.name} ${action} the ${this.instrument}`
    }
}

const Page = new Guitarist('Jimmy', 'guitar')

console.log(Page.play('strums'))

//////////////////////////////////////////////////

class Peeps{
    static count: number = 0 // Static - aplica a classe, e nao aos objetos instanciados
    static getCount(): number {
        return Peeps.count
    }
    
    public id: number
    constructor(public name:string){
        this.name = name
        this.id = ++Peeps.count
    }
}

const Jhon = new Peeps('Jhon')
const Steve = new Peeps('Steve')
const Amy = new Peeps('Amy')

console.log(Peeps.count)
console.log(Jhon.id)
console.log((Steve.id))
console.log(Amy.id)

//////////////////////////////////

class Bands {
    private dataState: string[]
    constructor(){
        this.dataState = []
    }

    public get data(): string[]{
        return this.dataState
    }

    public set data(value: string[]){
        if(Array.isArray(value) && value.every(el => typeof el === 'string')){
            this.dataState = value
            return
        } else throw new Error('Param is not in array of strings')
    }
}

const myBands = new Bands()
myBands.data = ['Neil Young', 'Led Zep']
console.log(myBands.data)
myBands.data = [...myBands.data, 'ZZ Top']
console.log(myBands.data)
myBands.data = ['Van Halen', '5150']
console.log(myBands.data)