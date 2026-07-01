---
version: alpha
name: DualCam Ops UI
description: Dark-tech operational dashboard for multi-camera person detection and registration.
colors:
  primary: "#E8EDF2"
  secondary: "#9AA7B1"
  tertiary: "#39D98A"
  neutral: "#0F1115"
  surface: "#151A20"
  on-surface: "#E8EDF2"
  error: "#E05454"
  warning: "#F0B429"
  success: "#39D98A"
typography:
  headline-display:
    fontFamily: Plus Jakarta Sans
    fontSize: 40px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.5
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
  body-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
  label-lg:
    fontFamily: "IBM Plex Sans"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.08em
  label-md:
    fontFamily: "IBM Plex Sans"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.08em
  label-sm:
    fontFamily: "IBM Plex Sans"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1em
  mono:
    fontFamily: "JetBrains Mono"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
rounded:
  none: 0
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
  full: 9999px
spacing:
  base: 16px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  gutter: 20px
  margin: 28px
components:
  button-primary:
    backgroundColor: "{colors.tertiary}"
    textColor: "{colors.neutral}"
    rounded: "{rounded.md}"
    padding: 12px
  button-primary-hover:
    backgroundColor: "#2CC67A"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    rounded: "{rounded.md}"
    padding: 12px
  button-destructive:
    backgroundColor: "{colors.error}"
    textColor: "{colors.neutral}"
    rounded: "{rounded.md}"
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    rounded: "{rounded.md}"
    padding: 12px
  card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.lg}"
    padding: 16px
---

# DualCam Ops UI

## Overview
A precision-focused operations dashboard for running dual-camera person detection, registration, and model training. The UI is dark-tech and utilitarian to reduce glare, keep attention on live feeds, and surface dense telemetry without distraction.

**Design Dials:**
| Dial | Value | Rationale |
|------|-------|-----------|
| Design Variance | 4 | Functional, familiar dashboard patterns with a tailored visual signature. |
| Motion Intensity | 3 | Minimal motion to avoid distracting operators during monitoring. |
| Visual Density | 8 | High information density needed for feeds, detections, and system metrics. |

**Visual Direction:** Dark tech operations console
**Memorable Signature:** Dual-feed frame lines with neon-lime status accents and monochrome telemetry chips
**Anti-generic decisions:** Avoided purple gradients and soft card shadows; used crisp borders, matte surfaces, and a single neon accent for focus.

## Colors
The palette prioritizes legibility and alert-state clarity on dark surfaces.

- **Signal White ({colors.primary}):** Primary text and key data.
- **Slate Gray ({colors.secondary}):** Secondary text, borders, metadata.
- **Neon Mint ({colors.tertiary}):** Action and status highlights.
- **Carbon Black ({colors.neutral}):** App background.
- **Graphite Surface ({colors.surface}):** Panels, cards, control areas.

Contrast notes: Primary text on neutral and surface backgrounds maintains WCAG AA; accent is reserved for CTAs and active states.

## Typography
A crisp sans-serif hierarchy for readability and a monospace accent for telemetry.

- **Display/Headlines:** Plus Jakarta Sans — modern, technical, and compact.
- **Body:** Plus Jakarta Sans — steady legibility at smaller sizes.
- **Labels/Metadata:** IBM Plex Sans — structured for UI labeling.
- **Monospace:** JetBrains Mono — timestamps, IDs, model versions.

## Layout
Dense operational grid with predictable spacing for scanning.

- **Grid:** 12 columns, 20px gutter, max-width 1360px.
- **Spacing scale:** 4/8/16/24/40 with tight card padding.
- **Breakpoints:** mobile (0), tablet (768), desktop (1200), wide (1440).
- **Section rhythm:** 24–32px between major panels.

## Elevation & Depth
Depth is conveyed through tonal contrast and 1px borders. Shadows are minimal; focus states use accent glows and inset outlines.

## Shapes
Sharp, engineered corners with an 8–12px radius for cards and controls. Rounded only where touch targets need emphasis.

## Components

### Buttons
- **Primary:** Neon mint fill, dark text, compact height, hover darkens.
- **Secondary:** Transparent with 1px border, subtle hover fill.
- **Ghost/Text:** No border, hover underline or faint tint.
- **Destructive:** Solid red with dark text, reserved for deletions.

### Cards & Containers
Graphite surfaces with 1px slate borders; optional accent strip for status. No heavy shadowing.

### Inputs & Forms
Dark surface fields with clear focus ring; error state uses red border + helper text. Labels are uppercase, tight tracking.

### Navigation
- **Header:** 56px height with system status and quick actions.
- **Sidebar:** 220px wide, icon + label, active state uses neon mint bar.

### Data Display
Tables use zebra rows with subtle tints; badges for status (success/warn/error). Empty states show a single-line instruction and icon.

### Motion & Interaction
- **Default easing:** cubic-bezier(0.2, 0.8, 0.2, 1)
- **Duration scale:** fast 120ms, normal 200ms, slow 320ms
- **Hover states:** text brighten + 1px border highlight
- **Focus states:** 2px neon mint ring with 2px offset
- **Loading states:** subdued skeletons and compact spinners
- **Reduced motion:** animations disabled with `prefers-reduced-motion`

## Do's and Don'ts
- Do keep the accent color to one primary action per panel.
- Don't use soft gradients or glossy effects.
- Do maintain AA contrast for all telemetry text.
- Don't mix multiple border radii in a single screen.

## Screen Scope

| Screen | Route | Purpose |
|--------|-------|---------|
| Live Monitoring Dashboard | / | Dual camera feeds, detections, and system status |
| Registration & Capture | /register | Capture five images and register a person |
| People & Identity Management | /people | Manage registered people and anonymous IDs |
| Training & Model Control | /training | Train, deploy, and monitor model versions |
