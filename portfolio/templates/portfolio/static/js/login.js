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
