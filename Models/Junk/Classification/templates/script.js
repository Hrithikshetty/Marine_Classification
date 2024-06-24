document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault(); 
    var formData = new FormData(this);

    fetch('/predict', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('predictionResult').innerText = 'Prediction: ' + data.message;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});