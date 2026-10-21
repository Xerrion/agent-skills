# Rendering basic icons

Basic SVGs retain their original fill attributes. An ordinary image element does not recolor them through CSS `color`. Use the bundled monochrome mask classes when the icon should follow a component's foreground color.

```html
<span class="tv2-icon tv2-icon--info-circle" aria-hidden="true"></span>
```

The [icon stylesheet](../../assets/web/tv2-icons.css) uses original local SVGs as masks and `background-color: currentColor`. Both `mask` and `-webkit-mask` are supplied. Its URLs resolve relative to the exported stylesheet. No request to Figma or an icon CDN is required.

Available baseline classes are `tv2-icon--arrow-right`, `tv2-icon--check-circle`, `tv2-icon--info-circle`, `tv2-icon--warning-triangle`, `tv2-icon--warning-circle`, `tv2-icon--play`, and `tv2-icon--x`. Keep an icon-only button's accessible name on the button itself.

For another basic icon, add a mask rule pointing to the exact bundled file and retain its aspect ratio. For a standalone meaningful icon, provide an accessible name on its surrounding element.
Multicolor logos, detailed icons, flags, and illustrations should keep their original colors. Use their original artwork files as images rather than applying a monochrome mask. See the [icon catalog](../artwork/icons.md) for the separate asset families.
