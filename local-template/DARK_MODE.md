# Dark Mode Implementation

This document describes the dark/light mode toggle feature implemented for the SMART Guidelines base template.

## Features

- **Automatic Detection**: Respects user's system preference (`prefers-color-scheme`)
- **Manual Toggle**: Button in the top-right corner to manually switch themes
- **Persistence**: Theme choice is saved in localStorage and persists across page reloads
- **WHO Color Palette**: Maintains WHO branding while providing optimal contrast for dark mode
- **Transparent Image Handling**: Automatically adds white background to images in dark mode for better visibility

## Implementation

### CSS Custom Properties

The implementation uses CSS custom properties (variables) to create a flexible theming system:

```css
:root {
  /* Light mode colors (default) */
  --bg-color: #ffffff;
  --text-color: #222222;
  --who-blue: #0093d0;
  /* ... more variables */
}

[data-theme="dark"] {
  /* Dark mode colors */
  --bg-color: #1a1a1a;
  --text-color: #e0e0e0;
  /* ... dark mode overrides */
}
```

### JavaScript Toggle

The theme toggle is implemented with vanilla JavaScript that:

1. Detects system preference on page load
2. Applies saved theme from localStorage if available
3. Creates and positions the toggle button dynamically
4. Handles theme switching and persistence

### Template Integration

The feature is integrated into the FHIR IG template system via:

- `_append.fragment-css.html`: Includes the dark mode CSS
- `_append.fragment-script.html`: Includes the theme toggle JavaScript
- CSS files in multiple locations for compatibility:
  - `local-template/package/content/assets/css/dmn.css`
  - `input/includes/dmn.css`
  - `input/scripts/includes/dmn.css`

## Usage

The dark mode toggle appears automatically in the top-right corner of pages. Users can:

1. Click the toggle button to switch between light and dark modes
2. The system will remember their choice
3. If no choice is made, the system preference is used

## Customization

To customize colors, modify the CSS custom properties in the `:root` and `[data-theme="dark"]` selectors in the CSS files.

## Browser Support

- Modern browsers with CSS custom properties support
- Graceful fallback to light mode for older browsers
- LocalStorage support for theme persistence