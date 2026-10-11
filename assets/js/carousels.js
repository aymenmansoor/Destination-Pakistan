/* One timer per slideshow. Bootstrap owns transitions, arrows, keys and swipes. */
(() => {
  if (!window.bootstrap) return;
  const motion = window.matchMedia("(prefers-reduced-motion: reduce)");
  const controllers = [];

  document.querySelectorAll(".carousel").forEach((element) => {
    if (element.dataset.carouselEnhanced === "true") return;
    element.dataset.carouselEnhanced = "true";
    const slides = element.querySelectorAll(".carousel-item");
    if (slides.length < 2) {
      element
        .querySelectorAll(
          ".carousel-indicators, .carousel-control-prev, .carousel-control-next",
        )
        .forEach((control) => {
          control.hidden = true;
        });
      return;
    }
    // Disable Bootstrap's interval and hover timer so there is only one clock.
    const carousel = bootstrap.Carousel.getOrCreateInstance(element, {
      interval: false,
      ride: false,
      pause: false,
      keyboard: true,
      touch: true,
    });
    const reasons = new Set();
    const inner = element.querySelector(".carousel-inner");
    const delay = Number(element.dataset.autoplay) || 5000;
    let timer = null;
    let sliding = false;

    function stop() {
      window.clearTimeout(timer);
      timer = null;
    }
    function reconcile() {
      stop();
      const paused = motion.matches || document.hidden || reasons.size > 0;
      if (inner) inner.setAttribute("aria-live", paused ? "polite" : "off");
      if (!paused && !sliding) {
        timer = window.setTimeout(() => {
          timer = null;
          carousel.next();
        }, delay);
      }
    }
    function pause(reason) {
      reasons.add(reason);
      reconcile();
    }
    function resume(reason) {
      reasons.delete(reason);
      reconcile();
    }

    element.addEventListener("slide.bs.carousel", () => {
      sliding = true;
      stop();
    });
    element.addEventListener("slid.bs.carousel", () => {
      sliding = false;
      reconcile();
    });
    element.addEventListener("mouseenter", () => pause("hover"));
    element.addEventListener("mouseleave", () => resume("hover"));
    element.addEventListener("focusin", () => pause("focus"));
    element.addEventListener("focusout", (event) => {
      if (!element.contains(event.relatedTarget)) resume("focus");
    });
    element.addEventListener("pointerdown", () => pause("pointer"));
    // A drag can finish outside the image: clear only an active pointer pause.
    const release = () => {
      if (reasons.has("pointer")) resume("pointer");
    };
    document.addEventListener("pointerup", release);
    document.addEventListener("pointercancel", release);
    controllers.push(reconcile);
    reconcile();
  });

  if (controllers.length) {
  document.addEventListener("visibilitychange", () =>
    controllers.forEach((update) => update()),
  );
  motion.addEventListener("change", () =>
    controllers.forEach((update) => update()),
  );
  }
})();
