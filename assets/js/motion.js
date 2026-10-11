/* Observe selected sections once; never hide content while waiting for JS. */
(() => {
  const motion = matchMedia("(prefers-reduced-motion: reduce)");
  const animate = (element, className) => {
    if (motion.matches) return;
    element.classList.remove(className);
    // Restart safely when a visitor changes filters quickly.
    void element.offsetWidth;
    element.classList.add(className);
    element.addEventListener(
      "animationend",
      () => element.classList.remove(className),
      { once: true },
    );
  };
  window.revealGallery = (items) => {
    items.slice(0, 6).forEach((item) => animate(item, "filter-arriving"));
  };
  if (!("IntersectionObserver" in window)) return;
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach(({ target, isIntersecting }) => {
        if (!isIntersecting) return;
        animate(target, "is-arriving");
        observer.unobserve(target);
      });
    },
    { threshold: 0.12 },
  );
  document
    .querySelectorAll(
      ".home .section-heading, .about-introduction, .guide-visual, .contact-info",
    )
    .forEach((section) => observer.observe(section));
  motion.addEventListener("change", () => {
    if (motion.matches)
      document
        .querySelectorAll(".is-arriving, .filter-arriving")
        .forEach((element) =>
          element.classList.remove("is-arriving", "filter-arriving"),
        );
  });
})();
