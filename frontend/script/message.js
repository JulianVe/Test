document.addEventListener("DOMContentLoaded", async () => {
    try {
        const response = await fetch("{PLACEHOLDER_API_URL}}", {
            method: "GET",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
        });

        const data = await response.json();
        document.getElementById("message").textContent = `The saved string is ${data.text}`;
    } catch (error) {
        console.error("Error fetching message:", error);
        document.getElementById("message").textContent = "Failed to load message";
    }
});
