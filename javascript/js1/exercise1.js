// working with Variables and Data Types

const firstName = "jack";
const age = 26;
let isStudent = "true";
// Object string
const address = {city:'Nairobi', country:'Kenya'};
// array
let hobbies = ["coding","watching","rugby","gaming"];

// undefined
let undefinedVariable

let nullVariable = "null";


console.log(`My name is ${firstName} of type`,typeof firstName)
console.log(`I'm ${age} years old of type`, typeof age)


if (isStudent == "true"){
    console.log(isStudent)
}else{
    console.log("false")
}

console.log(address)
// priting a specific object
console.log(address.city)

// printing arrays
console.log(hobbies)

// printing specific array
console.log(hobbies[0])

console.log(undefinedVariable)

console.log(nullVariable)