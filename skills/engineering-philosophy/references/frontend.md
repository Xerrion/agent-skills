# Frontend Philosophy

Design an interface that supports the user's task and fits its product.

Use deliberate visual choices without making novelty a requirement. A familiar component or restrained layout can be the correct design.

Respect an existing design system unless the task calls for changing it.

This reference guides design and inspection. It does not grant browser, execution, or editing permissions.

## 1. Typography and Hierarchy

Make the primary content and action easy to identify.

Choose typography for readability, content density, product character, and the target environment.

Existing fonts, system fonts, and established component defaults are valid choices. A distinctive font is not inherently better.

Use a coherent type scale and meaningful grouping. Do not make every heading, label, and control compete for attention.

Provide usable fallback rendering while fonts load or fail.

Keep long text, translated text, zoom, and user font settings in mind.

## 2. Coherent Color and Theme

Use semantic tokens for recurring colors, spacing, typography, and component states.

Apply the product's visual language consistently. Do not introduce a new palette for each component.

Use color to support hierarchy and communicate state. Do not rely on color alone for errors, selection, or required information.

Check text, controls, focus indicators, and disabled states against the project's accessibility requirements.

When supporting multiple themes, verify each theme's actual surfaces and states. Do not assume that inversion produces a usable dark theme.

Visual effects must serve the design. Gradients, textures, shadows, and depth are optional.

## 3. Purposeful Interaction and Motion

Prefer native semantic controls before custom substitutes.

Provide accessible names, keyboard operation, visible focus, and understandable feedback.

Preserve focus and interaction order when content changes. Associate errors with the controls they concern.

Use motion to clarify a transition, relationship, or response. Do not animate merely to make the interface feel designed.

Respect reduced-motion preferences and avoid unnecessary blocking transitions.

Use existing platform and project primitives when sufficient. Add an animation dependency only for a justified capability.

## 4. Responsive Composition

Choose layout and density according to content, task, and available space.

Use the existing spacing system deliberately. Token reuse is consistency, not a design failure.

Let content constraints guide responsive changes. Do not assume that stacking everything vertically solves every narrow layout.

Check overflow, long labels, tables, navigation, dialogs, and touch interaction where relevant.

Preserve reading order and action priority across layouts.

Do not fix one viewport by hiding information needed to complete the task.

## 5. Complete and Verified States

Consider the states the component can actually reach: initial, loading, empty, success, partial, error, disabled, and offline where applicable.

Explain what happened and what the user can do next. Preserve entered data when recovery permits it.

Do not show success before the underlying operation establishes it.

Distinguish client-side feedback from server-side authorization and validation.

Inspect relevant rendering and interaction in a browser when tools and environment permit.

Record the viewport, state, and interaction checked. A screenshot does not prove keyboard behaviour or a working submission.

When inspection cannot run, name the missing coverage. Do not report visual or accessibility checks as passed from source inspection alone.

## Application

Match verification to the changed surface.

Do not redesign unrelated components or replace established styling merely to satisfy a personal aesthetic.

Evaluate the result by task completion, clarity, consistency, accessibility, and observed behaviour.
