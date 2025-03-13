// Funzione per la comparsa fluida tramite gsap
document.addEventListener("DOMContentLoaded", function () {
  gsap.to(".login-container", {
    opacity: 1,
    y: 0,
    duration: 1,
    ease: "power2.out",
  });

  gsap.from("h2", {
    opacity: 1,
    y: -20,
    delay: 0.5,
    duration: 1,
  });

  gsap.from("input, button", {
    opacity: 1,
    y: 20,
    delay: 0.8,
    duration: 1,
    stagger: 0.2,
  });

  gsap.to("body", {
    backgroundPosition: "center",
    duration: 1.5,
    ease: "power1.inOut",
  });
});




// Funzione per la validazione del form
document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("form");
  const usernameInput = document.querySelector("input[name='username']");
  const passwordInput = document.querySelector("input[name='password']");
  const messageBoxes = document.querySelectorAll(".message-box");

  form.addEventListener("submit", function (event) {
    let errors = false;

    // Rimuove i messaggi di errore precedenti
    messageBoxes.forEach((msg) => (msg.style.display = "none"));

    // Controlla il campo username
    if (usernameInput.value.trim() === "") {
      displayError(usernameInput, "Il campo username è obbligatorio.");
      errors = true;
    }

    // Controlla il campo password
    if (passwordInput.value.trim() === "") {
      displayError(passwordInput, "Il campo password è obbligatorio.");
      errors = true;
    }

    if (errors) {
      event.preventDefault(); // Blocca l'invio del form se ci sono errori
    }
  });

  function displayError(input, message) {
    let messageBox = input.nextElementSibling;
    if (messageBox && messageBox.classList.contains("message-box")) {
      messageBox.textContent = message;
      messageBox.style.display = "block";
    }
  }
});
