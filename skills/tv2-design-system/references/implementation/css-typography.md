# Mapping type styles to CSS

The [web asset generator](web-assets.md) writes all complete [type styles](../foundations/typography.md) into `tv2-tokens.css`.
A style named `heading.large` becomes the class `.tv2-type-heading-large`.
Each generated class includes its size, weight, font style, and line height.

At the `sm` breakpoint, `heading.large` uses TV2 Bold at 24 px with a unitless line height of 1.1.
Across `sm`, `md`, `lg`, and `tv`, its sizes are 24, 28, 32, and 42 px.
`body.medium` uses TV2 Regular at 16, 16, 16, and 32 px with a unitless line height of 1.4.
The default Medium Button's recorded type style is `utility.large.medium`: TV2 Medium at 18 px with a 22 px line height on non-TV layouts, and 36 px with a 44 px line height on TV.

Add `px` to absolute line heights. Relative line heights remain unitless.
Utility styles use `value` and `tvvalue` for size, and `absolute` and `tvabsolute` for line height.
Load the [font face](../artwork/fonts.md) matching the selected style's `fontType`.

Use `sm`, `md`, and `lg` values for responsive web. Keep `lg` at `xl` and `2xl` unless the application explicitly defines another mapping.
Select television typography through the explicit layout option described in the [web baseline](web-baseline.md).
