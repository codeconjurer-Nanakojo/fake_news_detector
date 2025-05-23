document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("news-form");
    const loading = document.getElementById("loading");
    const clearBtn = document.getElementById("clear-btn");
    const textarea = document.getElementById("news");
    const copyBtn = document.getElementById("copy-btn");
    const resultText = document.querySelector(".result-text");

    // Show loading on submit
    form.addEventListener("submit", () => {
        loading.style.display = "block";
    });

    // Clear textarea
    clearBtn.addEventListener("click", () => {
        textarea.value = "";
    });

    // Copy prediction result
    if (copyBtn && resultText) {
        copyBtn.addEventListener("click", () => {
            navigator.clipboard.writeText(resultText.textContent.trim()).then(() => {
                copyBtn.textContent = "Copied!";
                setTimeout(() => {
                    copyBtn.textContent = "Copy Result";
                }, 2000);
            });
        });
    }
});
