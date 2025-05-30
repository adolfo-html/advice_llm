async function promptRequest(e) { // Declaring the function 
    // e is an event object. Naming it gives you a local variable with methods and properties you can use.
    e.preventDefault();

    // Getting textarea input
    const input = document.getElementById('user_input').value;

    // Disable submit button
    document.getElementById('submit_button').disabled = true;

    // Logging what's happening
    document.getElementById("submit_button").value = "Sending...";
    console.log("communicating with server ...");

    // SENDING the request
    const response = await fetch("http://localhost:5000/generate", { // Local testing for now!
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({input}) // Formats the query data into JSON. Compatible with Python web application APIs like Flask
    });

    // This script stops if fetch() returns an error, so getting to this point means the request went through!
    console.log("fetch response received");

    // Variable awaiting the response JSON!
    const data = await response.json();

    document.getElementById("responsebox").innerText = data.reply;
    document.getElementById('submit_button').disabled = false;
    document.getElementById('submit_button').value = "Send";
}

// Setting the event listener so that the function runs every time the form is submitted.
document.getElementById('form').addEventListener('submit', promptRequest)