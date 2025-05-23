document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("news-form");
    const loading = document.getElementById("loading");
    const clearBtn = document.getElementById("clear-btn");
    const textarea = document.getElementById("news");
    const copyBtn = document.getElementById("copy-btn");
    const resultText = document.querySelector(".result-text");

    // Show loading during form submission
    if (form) {
        form.addEventListener("submit", () => {
            if (loading) loading.style.display = "block";
        });
    }

    // Clear the textarea
    if (clearBtn && textarea) {
        clearBtn.addEventListener("click", () => {
            textarea.value = "";
        });
    }

    // Copy the result to clipboard
    if (copyBtn && resultText) {
        copyBtn.addEventListener("click", () => {
            const text = resultText.textContent.trim();
            navigator.clipboard.writeText(text).then(() => {
                copyBtn.textContent = "✅ Copied!";
                setTimeout(() => {
                    copyBtn.textContent = "Copy Result";
                }, 2000);
            }).catch(() => {
                copyBtn.textContent = "❌ Failed to copy";
            });
        });
    }
});
