// script.js
function submitData() {
    const inputData = document.getElementById('data').value;

    // Send data to the backend (using Fetch API)
    fetch('https://replit.com/@404andrewtaylor/mainpy#main.py', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `data=${encodeURIComponent(inputData)}`,
    })
    .then(response => response.blob())
    .then(imgBlob => {
        const imgUrl = URL.createObjectURL(imgBlob);
        document.getElementById('result').innerHTML = `<img src="${imgUrl}" alt="Generated Graph">`;
    });
}
