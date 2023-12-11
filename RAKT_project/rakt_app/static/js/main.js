function findFoodTrucks() {
    const latitude = document.getElementById('latitude').value;
    const longitude = document.getElementById('longitude').value;

    fetch(`/api/foodtrucks/?latitude=${latitude}&longitude=${longitude}`)
        .then(response => response.json())
        .then(data => {
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '<h2>Nearby Food Trucks</h2>';

            data.forEach(truck => {
                resultDiv.innerHTML += `<p>${truck.name} - ${truck.description}</p>`;
            });
        })
        .catch(error => console.error('Error:', error));
}
