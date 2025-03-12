gsap.from(".card", { opacity: 0, y: -50, duration: 1 });

$(document).ready(function () {
  $("#appointmentForm").submit(function (event) {
    event.preventDefault();
    const appointmentData = {
      nome_paziente: $("#nome_paziente").val(),
      eta: $("#eta").val(),
      tipologia_visita: $("#tipologia_visita").val(),
      diagnosi: $("#diagnosi").val(),
      orario: $("#orario").val(),
      numero_stanza: $("#numero_stanza").val(),
    };

    $.ajax({
      type: "POST",
      url: "/api/appointments/",
      contentType: "application/json",
      data: JSON.stringify(appointmentData),
      success: function (response) {
        alert("Appuntamento prenotato con successo!");
        $("#appointmentForm")[0].reset();
      },
      error: function (error) {
        alert("Errore nella prenotazione. Riprova.");
      },
    });
  });
});

document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".action-btn").forEach((button) => {
    button.addEventListener("click", function () {
      const row = this.closest("tr"); // Trova la riga
      const appointmentId = row.getAttribute("data-id"); // Ottiene l'ID dall'attributo data-id
      const action = this.classList.contains("approve") ? "approve" : "delete";

      if (action === "approve") {
        fetch(`/api/appointments/${appointmentId}/approve/`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCSRFToken(),
          },
        })
          .then((response) => response.json())
          .then((data) => {
            if (data.success) {
              row.style.backgroundColor = "#d4edda"; // Verde per indicare confermato
              alert("Appuntamento confermato!");
            } else {
              alert("Errore: " + data.error);
            }
          });
      } else if (action === "delete") {
        if (!confirm("Sei sicuro di voler eliminare questo appuntamento?"))
          return;

        fetch(`/api/appointments/${appointmentId}/delete/`, {
          method: "DELETE",
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCSRFToken(),
          },
        })
          .then((response) => response.json())
          .then((data) => {
            if (data.success) {
              row.remove(); // Rimuove la riga dalla tabella
              alert("Appuntamento eliminato!");
            } else {
              alert("Errore: " + data.error);
            }
          });
      }
    });
  });

  function getCSRFToken() {
    let csrfToken = null;
    document.cookie.split(";").forEach((cookie) => {
      let [name, value] = cookie.trim().split("=");
      if (name === "csrftoken") csrfToken = value;
    });
    return csrfToken;
  }
});
