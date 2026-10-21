/* Optional behavior. The host can restore focus in response to tv2:dismiss. */
document.addEventListener("click", (event) => {
  const trigger = event.target instanceof Element
    ? event.target.closest("[data-tv2-dismiss]")
    : null;
  const component = trigger?.closest(".tv2-notice, .tv2-snackbar");
  if (!component) return;
  component.hidden = true;
  const returnTarget = trigger.getAttribute("data-tv2-return-focus");
  if (returnTarget) document.getElementById(returnTarget)?.focus();
  component.dispatchEvent(new CustomEvent("tv2:dismiss", { bubbles: true }));
});
