/*
function predictPrice() {
    var bedrooms = parseFloat(document.getElementById("bedrooms").value);
    var bathrooms = parseFloat(document.getElementById("bathrooms").value);
    var houseSize = parseFloat(document.getElementById("houseSize").value);
    var acreLot = parseFloat(document.getElementById("acreLot").value);
    var zipCode = parseFloat(document.getElementById("zipCode").value);

    var input_data = [bedrooms, bathrooms, houseSize, acreLot, zipCode];

    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(input_data),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("predictedPrice").textContent = "Predicted Price: $" + data.predicted_price.toFixed(2);
    });
}
*/

async function trainModel() {
    var formData = new FormData();
    var fileInput = document.getElementById("csvFile");
    formData.append("csvFile", fileInput.files[0]);

    await fetch("/train", {
        method: "POST",
        body: formData,
    });
}


function predictPrice() {
    var bedrooms = parseFloat(document.getElementById("bedrooms").value);
    var bathrooms = parseFloat(document.getElementById("bathrooms").value);
    var houseSize = parseFloat(document.getElementById("houseSize").value);
    var acreLot = parseFloat(document.getElementById("acreLot").value);
    var zipCode = parseFloat(document.getElementById("zipCode").value);

    var input_data = [bedrooms, bathrooms, houseSize, acreLot, zipCode];

    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(input_data),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("predictedPrice").textContent = "Predicted Price: $" + data.predicted_price.toFixed(2);
    });
}