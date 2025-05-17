document.addEventListener("DOMContentLoaded", async () => {
    try {
        const response = await fetch("/api/v1/message");
        const data = await response.json();

        document.getElementById("message").textContent = `The saved string is ${data.text}`;
    } catch (error) {
        console.error("Error fetching message:", error);
        document.getElementById("message").textContent = "Failed to load message";
    }
});
