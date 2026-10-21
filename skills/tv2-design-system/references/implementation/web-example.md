# Responsive panel example

Export the [web assets](web-assets.md) and copy the selected TV 2 logos before using this example.
The panel is an application composition. Its card structure, borders, and focus outline width are application choices.
Use the component's own [reference](../COMPONENTS.md) and the [web baseline](web-baseline.md) when adding design-system controls.

Save the following application CSS as `public/assets/tv2/panel.css`. It consumes the generated tokens without redefining them.

```css
:root { color-scheme: light; }
[data-tv2-theme="dark"] { color-scheme: dark; }

.tv2-page {
  margin: 0;
  padding: var(--tv2-size-24-step);
  background: var(--tv2-surface-primary);
  color: var(--tv2-content-primary);
}

.tv2-panel {
  padding: var(--tv2-size-24-step);
  border: 1px solid var(--tv2-stroke-input-default);
}

.tv2-panel h1 { margin: 0 0 var(--tv2-size-16); }
.tv2-panel p { margin: 0 0 var(--tv2-size-16); }
.tv2-panel a { color: var(--tv2-content-link-default); }
.tv2-panel a:hover { color: var(--tv2-content-link-default-hover); }
.tv2-panel a:focus-visible {
  outline: 2px solid var(--tv2-stroke-focus-outline);
  outline-offset: var(--tv2-size-8);
}

.tv2-logo {
  display: block;
  height: var(--tv2-size-44);
  width: auto;
  margin-bottom: var(--tv2-size-24);
}
```

Save this HTML at the application's public root alongside a local `nyheder.html` destination.

```html
<!doctype html>
<html lang="da" data-tv2-theme="light">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>TV 2 nyheder</title>
    <link rel="stylesheet" href="/assets/tv2/tv2-tokens.css">
    <link rel="stylesheet" href="/assets/tv2/tv2-components.css">
    <link rel="stylesheet" href="/assets/tv2/panel.css">
  </head>
  <body class="tv2-page tv2-type-body-medium">
    <main class="tv2-panel">
      <img class="tv2-logo" src="/assets/tv2/logos/dark/tv2_color.svg" alt="TV 2">
      <h1 class="tv2-type-heading-large">Seneste nyheder</h1>
      <p>Få overblik over dagens nyheder.</p>
      <a href="/nyheder.html">Læs nyhederne</a>
    </main>
  </body>
</html>
```

To select the dark theme, set `data-tv2-theme="dark"` on the HTML element and use `/assets/tv2/logos/light/tv2_color.svg` for the logo. Copy that [light logo variant](../../assets/logos/light/tv2_color.svg) to the matching public path first.

The generated stylesheet supplies `heading.large`, `body.medium`, and responsive `size.24.step` values. At wider desktop widths it keeps the `lg` type sizes.
Television requires the explicit platform selector described in the [web baseline](web-baseline.md).
