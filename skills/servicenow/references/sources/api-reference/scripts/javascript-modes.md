# JavaScript modes

JavaScript mode is a design and runtime setting for custom applications and scripts. To support existing server-side scripts and new scripts developed to the ECMAScript 2021 standard, the JavaScript engine has three modes: ECMAScript 2021 (ES12), ES5 Standards, and Compatibility.

The JavaScript mode controls which JavaScript features you have access to in an application or script. The default mode for new scoped applications is ECMAScript 2021 (ES12) and for new global applications, it’s ES5 Standards. You can also turn on ECMAScript 2021 (ES12) mode for individual scripts in applications that use ES5 Standards or Compatibility mode.

For more information about features supported by the ECMAScript 2021 (ES12) and ES5 Standards modes, see [JavaScript engine feature support](javascript-engine-feature-support.md).

## ECMAScript 2021 (ES12) mode

ECMAScript 2021 (ES12) mode is the default mode when you create new scoped applications. It isn't supported for global applications but can be turned on for individual global scripts.

When you create new scripts, ECMAScript 2021 (ES12) mode is turned on by default regardless of the JavaScript mode configured for the application. Do not assume that scripts depending on legacy engine behavior will behave identically in ECMAScript 2021 mode.

ECMAScript 2021 (ES12) mode supports a subset of ECMAScript 2021 (ES12) and ECMAScript 2022 (ES13) syntax and features, including the following features:

- Default function parameters
- Rest parameters
- For-of loops
- Template literals
- Destructuring
  - Declarations
  - Assignment
  - Parameters
- Const declaration
- Let declaration
- Arrow functions
- Class declarations
- Map set
- Optional chaining operator `(?.)`

To learn about specific ECMAScript 2021 (ES12) features, see the [Let's Learn ECMAScript 2021](https://www.youtube.com/playlist?list=PL3rNcyAiDYK1fUOYO83KOfF-NriBRAERV) videos on the ServiceNow Dev Program YouTube channel.

## ES5 Standards mode

ES5 Standards mode is the default mode for new global applications and is an option for scoped applications. Do not assume that scripts depending on legacy engine behavior will behave identically in ES5 Standards mode.

ES5 standards mode supports ECMAScript5 syntax and features, including the following features:

- The "use strict" declaration
- Control over extensibility of objects
- Get and set properties on objects (accessors)
- Control over writability, configurability, and enumerability of object properties
- New Array and Date methods
- Native JSON support
- Support for modern third-party libraries such as lodash.js and moment.js

## Compatibility mode

Compatibility mode is used for all scripts developed prior to the addition of ES5 Standards mode. Compatibility mode has some differences from the previous JavaScript engine.

JSON support changes:

- JSON.stringify() and JSON.parse() are implemented using the ES5 Native JSON object.
- The new JSON().encode() and new JSON().decode() are still supported, but should only be used when the legacy behavior is required.

The use of third-party JavaScript libraries isn’t supported in Compatibility mode.

- **Considerations for switching JavaScript modes**

  Switching the JavaScript mode for an application or script might change the behavior of existing scripts. Review some examples of behavior changes before switching JavaScript modes or to troubleshoot any issues that you experience after switching.

- **Set the JavaScript mode for an application**

  Configure which ECMAScript features can be used in an application by selecting the JavaScript mode.

- **Turn on ECMAScript 2021 (ES12) mode for a script**

  Use the latest JavaScript features supported with ECMAScript 2021 (ES12) mode in server-side scripts in applications that use ES5 Standards mode or Compatibility mode.
