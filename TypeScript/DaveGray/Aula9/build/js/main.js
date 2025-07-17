"use strict";
//Tipos utilitarios
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
const updateAssignment = (assign, propsToUpdate) => {
    return Object.assign(Object.assign({}, assign), propsToUpdate);
};
const assign1 = {
    studentId: 'compsci123',
    title: 'Final project',
    grade: 0
};
console.log(updateAssignment(assign1, { grade: 95 }));
const assignGraded = updateAssignment(assign1, { grade: 95 });
console.log(assign1);
console.log(assignGraded);
// Required - Torna todas as propriedades obrigatorias
// Readonly - Impede modificações
const recordAssignment = (assign) => {
    // lógica e etc
    return assign;
};
const assignVerified = Object.assign(Object.assign({}, assignGraded), { verified: true });
//assignVerified.grade = 88 - erro, readonly
recordAssignment(Object.assign(Object.assign({}, assignGraded), { verified: true }));
// Record - Cria um objeto mapeado com chaves e valores especificados
const hexColorMap = {
    red: 'FF00000',
    green: '00FF00',
    blue: '0000FF',
};
const finlGrades = {
    Sara: "B",
    Kelly: "F"
};
const gradeData = {
    Sara: { assign1: 10, assign2: 9 },
    Kelly: { assign1: 10, assign2: 7 }
};
const score = {
    studentId: 'k123',
    grade: 85
};
const preview = {
    studentId: 'k123',
    title: 'Final project'
};
// ReturnType - Extrai o tipo de retorno de uma função
//type newAssign = { title: string, points: number }
const createNewAssign = (title, points) => {
    return { title, points };
};
const tsAssign = createNewAssign("Utility Types", 100);
console.log(tsAssign);
const assignArgs = ["Generics", 100];
const tsAssign2 = createNewAssign(...assignArgs);
console.log(tsAssign2);
const fetchUsers = () => __awaiter(void 0, void 0, void 0, function* () {
    const data = yield fetch('https://jsonplaceholder.typicode.com/users').then(res => {
        return res.json();
    }).catch(err => {
        if (err instanceof Error)
            console.log(err.message);
    });
    return data;
});
fetchUsers().then(users => console.log(users));
