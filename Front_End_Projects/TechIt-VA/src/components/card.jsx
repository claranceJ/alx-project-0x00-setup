import React from "react";

const Card = () =>{
    return (
        <div className="bg-gray-100 rouded-lg shadow-md p-6 container mx-auto mt-20">
            <h2 className="text-xl font-semibold mb-2">Jacktone</h2>
            <p className="text-gray-700 mb-4">
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Exercitationem magni asperiores, soluta ipsum blanditiis voluptate, tempore iure est cumque quam libero eos odio a eligendi animi molestiae ducimus at ullam.
            </p>
            <button className="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 focus:outline-none rounded">
                Button
            </button>

        </div>
    )
}

export default Card;