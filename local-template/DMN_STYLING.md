# Decision Table Enhancements for SMART Guidelines

This local template enhancement provides **decision table specific styling** that complements the WHO FHIR IG template's dark/light mode functionality. 

## Integration with WHO Template

The WHO FHIR IG template (smart-ig-template) now includes comprehensive dark/light mode theming with:
- Theme toggle button in the navbar
- System preference detection
- Theme persistence
- General template theming

This enhancement focuses specifically on **DMN decision table styling** with WHO color palette integration.

## Features

### 🎨 WHO Color Palette for Decision Tables
- **Input columns**: Light blue (`#e5f4fa` / `#2c5282`)
- **Output columns**: Light green (`#dff7ea` / `#2f855a`) 
- **Annotation columns**: Light yellow (`#fffbe5` / `#744210`)
- **Header rows**: WHO blue (`#0093d0`)
- **Border colors**: WHO blue tones

### 🌓 Automatic Theme Integration
- Respects the WHO template's theme system
- Uses `[data-theme="dark"]` selector for consistency
- Supports system preference via `@media (prefers-color-scheme: dark)`

### 📊 Decision Table Enhancement
- Enhanced styling for `.decision` tables
- Color-coded columns for better readability
- Proper contrast ratios in both themes
- WHO branding compliance

## Usage

The enhancement automatically applies to decision tables when using these CSS classes:

```html
<table class="decision">
  <tr class="decision-header">
    <th class="row-label">Rule</th>
    <th class="input">Input 1</th>
    <th class="output">Output</th>
    <th class="annotation">Notes</th>
  </tr>
  <tr class="rule">
    <td class="row-label">1</td>
    <td class="inputEntry">Condition</td>
    <td class="outputEntry">Action</td>
    <td class="annotationEntry">Comment</td>
  </tr>
</table>
```

## Implementation

The enhancement is implemented through:
- `local-template/package/content/assets/css/dmn.css` - Decision table specific styling
- `local-template/package/includes/_append.fragment-css.html` - CSS inclusion

No JavaScript is included as theme functionality is provided by the WHO template.

## Relationship to WHO Template

This enhancement is designed to work seamlessly with the WHO template's dark mode implementation. When the WHO template is updated with dark mode support, this enhancement will automatically integrate without conflicts.

**Note**: Once the WHO template includes comprehensive dark mode support, only the decision table specific enhancements in this local template will be necessary.