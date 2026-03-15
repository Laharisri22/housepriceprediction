function predict() {

    const data = {
        medinc: parseFloat(document.getElementById("medinc").value),
        houseage: parseFloat(document.getElementById("houseage").value),
        averooms: parseFloat(document.getElementById("averooms").value),
        avebedrms: parseFloat(document.getElementById("avebedrms").value),
        population: parseFloat(document.getElementById("population").value),
        aveoccup: parseFloat(document.getElementById("aveoccup").value),
        latitude: parseFloat(document.getElementById("latitude").value),
        longitude: parseFloat(document.getElementById("longitude").value)
    };

    console.log("Sending data:", data); // DEBUG

    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(result => {
        console.log("Result:", result); // DEBUG
        document.getElementById("result").innerHTML =
            "💰 Predicted Price: ₹ " + result.price;
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("result").innerHTML =
            "❌ Error predicting price";
    });
}
