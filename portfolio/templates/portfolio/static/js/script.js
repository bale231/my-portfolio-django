// Funzione per lo scroll fluido
document.querySelectorAll(".nav-links a").forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault(); // Previene il comportamento predefinito del link
    const targetId = this.getAttribute("href"); // Ottieni l'ID della sezione di destinazione
    const targetSection = document.querySelector(targetId); // Seleziona la sezione di destinazione

    if (targetSection) {
      // Animazione di scroll con GSAP e ScrollToPlugin
      gsap.to(window, {
        duration: 1.5,
        scrollTo: { y: targetSection, offsetY: 70 }, // Scroll alla sezione con un offset per il menu fisso
        ease: "power3.inOut",
      });
    }
  });
});

// Animazione iniziale del titolo e del pulsante
gsap.from(".hero h1", {
  duration: 1.5,
  opacity: 0,
  y: -50,
  ease: "power3.out",
  delay: 0.5,
});

gsap.from(".hero p", {
  duration: 1.5,
  opacity: 0,
  y: 50,
  ease: "power3.out",
  delay: 1,
});

gsap.from(".cta-button", {
  duration: 1,
  opacity: 0,
  y: 50,
  ease: "bounce.out",
  delay: 1.5,
});

// Animazioni al scroll con ScrollTrigger
gsap.from(".about-section", {
  scrollTrigger: {
    trigger: ".about-section",
    start: "top 80%",
  },
  opacity: 0,
  y: 50,
  duration: 1,
});

gsap.from(".gallery-item", {
  scrollTrigger: {
    trigger: ".gallery",
    start: "top 80%",
  },
  opacity: 0,
  y: 50,
  stagger: 0.3,
  duration: 1,
});

gsap.from(".card", {
  scrollTrigger: {
    trigger: ".services-section",
    start: "top 80%",
  },
  opacity: 0,
  y: 50,
  stagger: 0.3,
  duration: 1,
});

gsap.from(".contact-section form", {
  scrollTrigger: {
    trigger: ".contact-section",
    start: "top 80%",
  },
  opacity: 0,
  y: 50,
  duration: 1,
});
