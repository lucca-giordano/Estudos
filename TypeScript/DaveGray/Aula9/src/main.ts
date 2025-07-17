//Tipos utilitarios

// Partial - torna todas as propriedades opicionais

interface Assignment {
    studentId: string,
    title: string,
    grade: number,
    verified?: boolean,
}

const updateAssignment = (assign: Assignment, propsToUpdate: Partial<Assignment>): Assignment => {
    return { ...assign, ...propsToUpdate }
}

const assign1: Assignment = {
    studentId: 'compsci123',
    title: 'Final project',
    grade: 0
}

console.log(updateAssignment(assign1, {grade: 95}))
const assignGraded: Assignment = updateAssignment(assign1, {grade: 95})
console.log(assign1)
console.log(assignGraded)

// Required - Torna todas as propriedades obrigatorias
// Readonly - Impede modificações

const recordAssignment = (assign: Required<Assignment>): Assignment => {
    // lógica e etc
    return assign
}

const assignVerified: Readonly<Assignment> = {
    ...assignGraded, verified: true
}

//assignVerified.grade = 88 - erro, readonly
recordAssignment({...assignGraded, verified: true})

// Record - Cria um objeto mapeado com chaves e valores especificados

const hexColorMap: Record<string, string> = {
    red: 'FF00000',
    green: '00FF00',
    blue: '0000FF',
}

type Students = 'Sara' | 'Kelly'
type LetterGrades = 'A' | 'B' | 'C' | 'D' | 'F'

const finlGrades: Record<Students, LetterGrades> = {
    Sara: "B",
    Kelly: "F"
}

interface Grades {
    assign1: number,
    assign2: number
}

const gradeData: Record<Students, Grades> = {
    Sara: { assign1: 10, assign2: 9 },
    Kelly: { assign1: 10, assign2: 7 }
}

// Pick - Cria um novo tipo selecionando um conjunto de propriedades
// Omit - Cria um novo tipo removendo um conjunto de propriedades

type AssignResult = Pick<Assignment, 'studentId' | 'grade'>
const score: AssignResult = {
    studentId: 'k123',
    grade: 85
}

type AssignPreview = Omit<Assignment, 'grade' | 'verified'>

const preview: AssignPreview = {
    studentId: 'k123',
    title: 'Final project'
}

// Exclude - Remove tipos de um conjunto
// Extract - Extrai tipos de um conjunto

type adjustedGrade = Exclude<LetterGrades, "F">
type highGrades = Extract<LetterGrades, "A" | "B">

//NonNullable - Remove null e undefined de um tipo

type AllPossibleGrades = 'Dave' | 'John' | null | undefined

type NamesOnly = NonNullable<AllPossibleGrades>

// ReturnType - Extrai o tipo de retorno de uma função

//type newAssign = { title: string, points: number }

const createNewAssign = (title: string, points: number) => {
    return {title, points}
}

type NewAssign = ReturnType<typeof createNewAssign>

const tsAssign: NewAssign = createNewAssign("Utility Types", 100)
console.log(tsAssign)

// Parameters - Extrai os parâmetros de uma função como uma tupla

type AssignParams = Parameters<typeof createNewAssign>

const assignArgs: AssignParams = ["Generics", 100]

const tsAssign2: NewAssign = createNewAssign(...assignArgs)
console.log(tsAssign2)

// Awaited - Extrai o tipo resolvido de uma Promise

interface User {
    id: number,
    name: string,
    username: string,
    email: string,
}

const fetchUsers = async ():Promise<User[]> => {
    const data = await fetch(
        'https://jsonplaceholder.typicode.com/users'
    ).then(res => {
        return res.json()
    }).catch(err => {
        if(err instanceof Error) console.log(err.message)
    })
    return data
}

type FetchUsersReturnType = Awaited<ReturnType<typeof fetchUsers>>

fetchUsers().then(users => console.log(users))