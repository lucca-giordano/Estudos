"use strict";
/* Problema
const year = document.getElementById("year")
const thisYear = new Date().getFullYear()
year.setAttribute("datetime", thisYear)
year.textContent = thisYear
*/
// Minha solução
/*
const year = document.getElementById("year")!
const thisYearNum = new Date().getFullYear()
const thisYear = thisYearNum.toString()
year.setAttribute("datetime", thisYear)
year.textContent = thisYear */
// Primeira solução
/*
let year:HTMLElement | null
year = document.getElementById("year")
let thisYear:string
thisYear = new Date().getFullYear().toString()
if (year){
    year.setAttribute("datetime", thisYear)
    year.textContent = thisYear
} */
// Segunda solução
const year = document.getElementById("year");
const thisYear = new Date().getFullYear().toString();
year.setAttribute("datetime", thisYear);
year.textContent = thisYear;
