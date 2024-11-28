document.addEventListener("click", addItem);
function addItem(){
    const InputValue=document.getElementById("input-text").value;
    console.log(InputValue);
    if(InputValue !== ""){

        const ListItem = document.createElement("li");
        ListItem.textContent = InputValue;
        const ListContainer = document.getElementById("list-container");
        ListContainer.appendChild(ListItem);
        document.getElementById("input-text").value = "";
    
    }

}

sessionStorage.setItem("Cat", JSON.stringify({name: "Chucky", age: 6}));
const myCat = JSON.parse(sessionStorage.getItem("Cat"));
console.log(myCat)