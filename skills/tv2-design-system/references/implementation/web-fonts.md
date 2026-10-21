# Loading TV2 fonts on the web

The [web asset generator](web-assets.md) creates declarations for all [mapped font faces](../artwork/fonts.md). Use those declarations with the generated baseline.

When the application owns font loading through another asset pipeline, use the matching weights, styles, and URLs as follows.

Copy the required font files into the application's served assets.
The skill's local filesystem paths are not deployed web URLs.
For a stylesheet served beside the font files, these declarations load regular, bold, and regular italic faces:

```css
@font-face {
  font-family: "TV2";
  src: url("./TV2-Regular.ttf") format("truetype");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: "TV2";
  src: url("./TV2-Bold.ttf") format("truetype");
  font-weight: 700;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: "TV2";
  src: url("./TV2-RegularItalic.ttf") format("truetype");
  font-weight: 400;
  font-style: italic;
  font-display: swap;
}

body {
  font-family: "TV2", Arial, sans-serif;
}
```

Adjust the URLs to the deployed stylesheet location.
Add a separate declaration for each additional face that the selected styles need.
The fallback stack above is a temporary loading choice; check layout while TV2 loads, then verify that the mapped TV2 font actually renders.
Treat missing or failed font loading as a defect in product UIs.
For email clients that cannot load the font, use an available fallback font and verify the rendered result.

The [font catalog](../artwork/fonts.md) maps all ten faces to their recorded weights and styles.
