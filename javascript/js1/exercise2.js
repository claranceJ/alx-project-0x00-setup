// Calculating year of  birth

rName = prompt("Enter your name: ")

let userAge = Number(prompt("Enter your age: "))

let currentYear = new Date().getFullYear();

let yearOfBirth = currentYear - userAge

alert(`Hey ${rName},Your year of birth is: ${yearOfBirth}`);