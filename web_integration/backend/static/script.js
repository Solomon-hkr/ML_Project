document.getElementById("prediction-form").addEventListener("submit", async function (event) {
    event.preventDefault();

    const data = {
        attack_type: parseFloat(document.getElementById("attack_type").value),
        target_system: parseFloat(document.getElementById("target_system").value),
        data_compromised_GB: parseFloat(document.getElementById("data_compromised_GB").value),
        attack_duration_min: parseFloat(document.getElementById("attack_duration_min").value),
        security_tools_used: parseFloat(document.getElementById("security_tools_used").value),
        attack_severity: parseFloat(document.getElementById("attack_severity").value),
        industry: parseFloat(document.getElementById("industry").value),
        response_time_min: parseFloat(document.getElementById("response_time_min").value),
        year: parseInt(document.getElementById("year").value),
        month: parseInt(document.getElementById("month").value),
        day: parseInt(document.getElementById("day").value),
        hour: parseInt(document.getElementById("hour").value)
    };

    try {
        const response = await fetch("/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
        });

        const result = await response.json();
        const resultDiv = document.getElementById("prediction-result");
        resultDiv.style.display = "block";
        resultDiv.textContent = `Prediction: ${result.result || result.error}`;
    } catch (error) {
        console.error("Error:", error);
    }
});

document.getElementById("clear-button").addEventListener("click", function () {
    document.getElementById("prediction-form").reset();
    document.getElementById("prediction-result").style.display = "none";
});



