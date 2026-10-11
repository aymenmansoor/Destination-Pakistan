/* Native dialog keeps large photographs keyboard accessible without a library. */
(() => {
  const dialog = document.querySelector("#photo-dialog");
  if (!dialog || typeof dialog.showModal !== "function") return;
  const image = dialog.querySelector("img");
  const caption = dialog.querySelector("figcaption");
  let items = [];
  let index = 0;
  let opener = null;

  function show(position) {
    index = (position + items.length) % items.length;
    const source = items[index].querySelector("img");
    image.src = source.src;
    image.alt = source.alt;
    caption.textContent = source.alt;
  }
  document.querySelectorAll(".gallery-open").forEach((link) => {
    link.addEventListener("click", (event) => {
      event.preventDefault();
      opener = link;
      items = [
        ...document.querySelectorAll(
          ".photo-gallery figure:not([hidden]) .gallery-open",
        ),
      ];
      show(items.indexOf(link));
      dialog.showModal();
      document.body.classList.add("photo-open");
      dialog.querySelector(".photo-close").focus();
    });
  });
  dialog
    .querySelector(".photo-close")
    .addEventListener("click", () => dialog.close());
  dialog
    .querySelector(".photo-prev")
    .addEventListener("click", () => show(index - 1));
  dialog
    .querySelector(".photo-next")
    .addEventListener("click", () => show(index + 1));
  dialog.addEventListener("keydown", (event) => {
    if (event.key === "Tab") {
      const controls = [...dialog.querySelectorAll("button")];
      const first = controls[0],
        last = controls[controls.length - 1];
      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
    }
    if (event.key === "ArrowLeft" || event.key === "ArrowRight") {
      event.preventDefault();
      show(index + (event.key === "ArrowRight" ? 1 : -1));
    }
  });
  dialog.addEventListener("click", (event) => {
    if (event.target === dialog) dialog.close();
  });
  dialog.addEventListener("close", () => {
    document.body.classList.remove("photo-open");
    opener?.focus();
  });
})();
