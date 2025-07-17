const echo = <T>(arg: T): T => arg

const isObj = <T>(arg: T): boolean => {
    return (typeof arg === "object" && !Array.isArray(arg) && arg !== null)
}

console.log("isObj")
console.log(isObj(true))
console.log(isObj('Jhon'))
console.log(isObj([1, 2, 3]))
console.log(isObj({name: 'jhon'}))
console.log(isObj(null))

interface BoolCheck<T> {
    value: T
    is: boolean
}

const isTrue = <T>(arg: T): BoolCheck<T> => {
    if(Array.isArray(arg) && !arg.length){
        return {value: arg, is: false}
    }
    if(isObj(arg) && !Object.keys(arg as keyof T).length){
        return {value: arg, is: false}
    }
    return {value: arg, is:!!arg}
}

console.log("isTrue")
console.log(isTrue(false))
console.log(isTrue(0))
console.log(isTrue(true))
console.log(isTrue(1))
console.log(isTrue('Dave'))
console.log(isTrue(''))
console.log(isTrue(null))
console.log(isTrue(undefined))
console.log(isTrue({}))
console.log(isTrue({name: 'Dave'}))
console.log(isTrue([]))
console.log(isTrue([1, 2, 3]))
console.log(isTrue(NaN))
console.log(isTrue(-0))


interface HasID {
    id: number
}

const processUser = <T extends HasID>(user: T): T => {
    //Processar o usuario 
    return user
}

console.log(processUser({id: 1, name: 'Dave'}))
//console.log(processUser({name: 'Dave'}))

const getUsersProperty = <T extends HasID, K extends keyof T>(users: T[], key: K): T[K][] => {
    return users.map(user => user[key])
    
}

const userrArray = [
    {
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz",
        "address": {
            "street": "Kulas Light",
            "suite": "Apt. 556",
            "city": "Gwenborough",
            "zipcode": "92998-3874",
            "geo": {
                "lat": "-37.3159",
                "lng": "81.1496"
            }
        },
        "phone": "1-770-736-8031 x56442",
        "website": "hildegard.org",
        "company": {
            "name": "Romaguera-Crona",
            "catchPhrase": "Multi-layered client-server neural-net",
            "bs": "harness real-time e-markets"
        }
    },
    {
        "id": 2,
        "name": "Ervin Howell",
        "username": "Antonette",
        "email": "Shanna@melissa.tv",
        "address": {
            "street": "Victor Plains",
            "suite": "Suite 879",
            "city": "Wisokyburgh",
            "zipcode": "90566-7771",
            "geo": {
                "lat": "-43.9509",
                "lng": "-34.4618"
            }
        },
        "phone": "010-692-6593 x09125",
        "website": "anastasia.net",
        "company": {
            "name": "Deckow-Crist",
            "catchPhrase": "Proactive didactic contingency",
            "bs": "synergize scalable supply-chains"
        }
    },
]

console.log(getUsersProperty(userrArray, "email"))
console.log(getUsersProperty(userrArray, "username"))

class StateObject<T> {
    private data: T

    constructor(value: T){
        this.data = value
    }

    get state() : T {
        return this.data
    }

    set state(value: T) {
        this.data = value
    }
}

const store = new StateObject("John")
//store.state = 12
console.log(store.state)

const myState = new StateObject<(string | number | boolean)[]>([15, 'jhon', true])

console.log(myState.state)
myState.state = ([...myState.state, 'AAAAA'])
console.log(myState.state)