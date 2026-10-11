/* Reveal selected content once; never hide it while waiting for observation. */
(() => {
  const motion = matchMedia("(prefers-reduced-motion: reduce)");
  const animate = (element, className, delay = 0) => {
    if (motion.matches) return;
    element.style.setProperty("--entrance-delay", `${delay}ms`);
    element.classList.remove(className);
    void element.offsetWidth;
    element.classList.add(className);
    element.addEventListener(
      "animationend",
      () => element.classList.remove(className),
      { once: true },
    );
  };
  document
    .querySelectorAll(".hero h1, .hero p, .hero-actions")
    .forEach((element, index) => animate(element, "hero-enter", index * 90));
  window.captureGallery = () => {
    const grid = document.querySelector(".photo-gallery");
    return grid
      ? {
          height: grid.getBoundingClientRect().height,
          boxes: new Map(
            [...grid.querySelectorAll("figure:not([hidden])")].map((item) => [
              item,
              item.getBoundingClientRect(),
            ]),
          ),
        }
      : null;
  };
  window.revealGallery = (items, before) => {
    if (motion.matches) return;
    const grid = document.querySelector(".photo-gallery");
    grid.getAnimations().forEach((animation) => animation.cancel());
    items.forEach((item) =>
      item.getAnimations().forEach((animation) => animation.cancel()),
    );
    // Move remaining thumbnails and resize the grid smoothly after filtering.
    items.forEach((item) => {
      const old = before?.boxes.get(item);
      const next = item.getBoundingClientRect();
      if (old)
        item.animate(
          [
            {
              transform: `translate(${old.x - next.x}px, ${old.y - next.y}px)`,
            },
            { transform: "translate(0,0)" },
          ],
          { duration: 350, easing: "ease-out" },
        );
      else animate(item, "filter-arriving");
    });
    if (before)
      grid.animate(
        [
          { height: `${before.height}px` },
          { height: `${grid.getBoundingClientRect().height}px` },
        ],
        { duration: 350, easing: "ease-out" },
      );
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
      ".home .section-heading, .home .destination-card, .mini-gallery img, .destination-guide .page-heading h1, .article-copy > p:first-of-type, .article-copy > figure, .article-copy > h2, .package-page .card, .about-introduction, .team .card, .contact-form, .contact-info",
    )
    .forEach((element) => observer.observe(element));
  motion.addEventListener("change", () => {
    if (!motion.matches) return;
    document
      .querySelectorAll(".is-arriving, .filter-arriving, .hero-enter")
      .forEach((element) =>
        element.classList.remove(
          "is-arriving",
          "filter-arriving",
          "hero-enter",
        ),
      );
    document
      .querySelectorAll(".photo-gallery, .photo-gallery figure")
      .forEach((element) =>
        element.getAnimations().forEach((animation) => animation.cancel()),
      );
  });
})();
