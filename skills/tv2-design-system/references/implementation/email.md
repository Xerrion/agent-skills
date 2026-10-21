# Email rendering

Resolve token values before generating email HTML and place the resulting values inline.
This light-theme example uses `surface.primary`, `content.primary`, `content.link.default`, `size.24`, `size.16`, and `body.medium`.
Use a system font stack when the delivery environment cannot load the bundled TV2 font.
Replace `{{news_url}}` with the actual absolute HTTPS destination before sending, and escape dynamic text and attribute values.

```html
<!doctype html>
<html lang="da">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>TV 2 nyheder</title>
  </head>
  <body style="margin:0;background-color:#ffffff;color:#000523;">
    <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0">
      <tr>
        <td style="padding:24px;font-family:Arial,Helvetica,sans-serif;font-size:16px;font-weight:400;line-height:1.4;">
          <p style="margin:0 0 16px;">Få overblik over dagens nyheder.</p>
          <a href="{{news_url}}" style="color:#244dea;text-decoration:underline;">Læs nyhederne</a>
        </td>
      </tr>
    </table>
  </body>
</html>
```

For another theme, resolve its semantic values before inlining.
Check the generated email in the actual delivery environment; font loading and appearance depend on that environment.
