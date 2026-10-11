/* Progressive enhancement: links and content work without JavaScript. */
document.documentElement.classList.add("js");
const menuButton = document.querySelector(".menu-toggle");
const navigation = document.querySelector(".site-nav");
function closeMenu() {
  navigation?.classList.remove("is-open");
  menuButton?.setAttribute("aria-expanded", "false");
}
menuButton?.addEventListener("click", () => {
  const open = navigation.classList.toggle("is-open");
  menuButton.setAttribute("aria-expanded", String(open));
});
document.addEventListener("keydown", (event) => {
  if (
    event.key === "Escape" &&
    menuButton?.getAttribute("aria-expanded") === "true"
  ) {
    closeMenu();
    menuButton.focus();
  }
});
window.matchMedia("(min-width: 1200px)").addEventListener("change", closeMenu);
navigation
  ?.querySelectorAll("a")
  .forEach((link) => link.addEventListener("click", closeMenu));

const galleryItems = [...document.querySelectorAll("[data-category]")];
document.querySelectorAll(".gallery-filter").forEach((button) => {
  button.addEventListener("click", () => {
    const category = button.dataset.filter;
    document
      .querySelectorAll(".gallery-filter")
      .forEach((item) =>
        item.setAttribute("aria-pressed", String(item === button)),
      );
    galleryItems.forEach((item) => {
      item.hidden = category !== "all" && item.dataset.category !== category;
    });
    document.querySelector(".gallery-status").textContent =
      `${button.textContent.trim()} selected.`;
    window.revealGallery?.(galleryItems.filter((item) => !item.hidden));
  });
});

/* No backend: prepare an email or let the visitor copy their enquiry. */
const form = document.querySelector("#enquiry-form");
if (form) {
  const selectedTour = new URLSearchParams(window.location.search).get("tour");
  if (selectedTour) form.elements.subject.value = `Enquiry: ${selectedTour}`;
  const status = document.querySelector("#form-status");
  function enquiry() {
    const data = new FormData(form);
    return {
      subject: String(data.get("subject") || "Destination Pakistan enquiry"),
      body: `Name: ${data.get("name")}\nEmail: ${data.get("email")}\n\n${data.get("message")}`,
    };
  }
  form.addEventListener("input", () => {
    document.querySelector("#email-draft-link").hidden = true;
    status.textContent = "";
  });
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    if (!form.reportValidity()) return;
    const message = enquiry();
    status.textContent =
      "Your draft is ready. Open it in your email app, review it, and send it there. If no app opens, copy your enquiry instead.";
    const draftLink = document.querySelector("#email-draft-link");
    draftLink.href = `mailto:destinationpakistan@gmail.com?subject=${encodeURIComponent(message.subject)}&body=${encodeURIComponent(message.body)}`;
    draftLink.hidden = false;
  });
  document
    .querySelector("#copy-enquiry")
    ?.addEventListener("click", async () => {
      if (!form.reportValidity()) return;
      const message = enquiry();
      try {
        await navigator.clipboard.writeText(
          `${message.subject}\n\n${message.body}`,
        );
        status.textContent =
          "Enquiry copied. Paste it into an email to destinationpakistan@gmail.com. Nothing has been sent.";
      } catch {
        status.textContent =
          "Clipboard access is unavailable. Copy your message manually and email destinationpakistan@gmail.com.";
      }
    });
}
