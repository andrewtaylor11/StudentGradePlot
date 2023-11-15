// script.js
function submitData() {
    const inputData = document.getElementById('data').value;

    // Send data to the backend (using Fetch API)
    fetch('https://your-replit-app-name.repl.co/process_data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `data=${encodeURIComponent(inputData)}`,
    })
    .then(response => response.text())
    .then(result => {
        document.getElementById('result').innerText = result;
    });
}
