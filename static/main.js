document.querySelector("form").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent form submission

    // Get the input text
    var inputText = document.querySelector("textarea").value.trim(); // Trim leading/trailing whitespace

    // Only send the request if input text is not empty
    if (inputText !== "") {
        // Send the request to the server
        fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                "input-text": inputText
            })
        })
        .then(response => {
            if (response.ok) {
                // Redirect to the prediction page
                window.location.href = "/prediction";
            } else {
                throw new Error("Request failed");
            }
        })
        .catch(error => {
            console.error("Error:", error);
        });
    }
});
