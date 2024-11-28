//Conditional logical Practice
let number = 0;

if (number>0){
    console.log(`${number} is postive`)
}else if(number<0){
    console.log(`${number} is negative`)
}else{
    console.log(`${number} is zero`)
}


// Looping through numbers
for(let i=1; i<=10; i++){
    console.log(`in loop ${i}`)
}
console.log("loop finished")

// Basic Function creation
function sum(num1,num2){
    return num1 + num2;
}
let total = sum(5,8);
console.log(total)