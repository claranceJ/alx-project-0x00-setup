
// document.addEventListener("click", submited);

// function submited(){
//     document.getElementById("#submit-answer").innerHTML = "Submited";
// }




// Create a program that only accepts an Array of numbers and filters out Odd numbers.

// function filter(numbers){
//     const result = [];
//     for ( number of numbers){
//         if (number%2 != 0){
//             result.push(number);
//         }
//     }
//     return result;
// }
// const numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15];
// console.log(filter(numbers));


//Fetching and logging a Random Activity from Bored API

function getBoredActivty() {
    fetch('https://www.boredapi.com/api/activity')// api for the get request
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ');
            }
            return response.json();
        })
        .then(data => console.log(data.));
    }

getBoredActivty()


//Fetching using async/awai syntax

function logActivity(activity) {
    console.log('Random Activity:', activity);
  }
  // Modify the getBoredActivity function to use async/await syntax
  async function getBoredActivity(callback) {
    try {
      // Await the fetch operation
      const response = await fetch('https://www.boredapi.com/api/activity');
      // Check if the response is okay
      if (!response.ok) {
        throw new Error('Network response was not ok ' + response.statusText);
      }     
      // Await the response JSON parsing
      const data = await response.json();   
      // Invoke the callback function with the received activity
      callback(data.activity);
    } 
    catch (error) {
      console.error('There was a problem with the fetch operation:', error);
    }
  }
  // Call the getBoredActivity function, passing the logActivity function as the callback
  getBoredActivity(logActivity);
