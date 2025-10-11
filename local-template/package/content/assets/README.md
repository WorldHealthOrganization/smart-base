# BPMN Viewer Implementation

This directory contains the BPMN viewer implementation for WHO SMART Base Implementation Guides.

## Overview

The BPMN viewer provides interactive visualization of Business Process Model and Notation (BPMN) diagrams with automatic viewport scaling. This implementation addresses the viewport scaling issues identified in [litlfred/sgex#1082](https://github.com/litlfred/sgex/pull/1082).

## Features

### ✅ Implemented
- **240px preview height** - 50% taller than original (was 160px)
- **Compact single-line file info** - File name and action buttons in one row
- **requestAnimationFrame viewport scaling** - Replaces `setTimeout` for proper browser paint timing
- **Comprehensive diagnostic logging** - Shows container dimensions at every stage
- **Container dimension validation** - Waits for non-zero dimensions before zoom operations
- **Fallback recovery** - Attempts manual viewbox recovery if viewport transform fails

### Key Improvements

1. **requestAnimationFrame Instead of setTimeout**
   - Uses nested `requestAnimationFrame` calls to ensure browser has painted container
   - First RAF: Ensure layout is painted
   - Second RAF: Ensure dynamic content is ready
   - Waits up to 50 RAF cycles (~833ms at 60fps) for valid container dimensions

2. **Diagnostic Logging**
   - Logs all dimension properties: offsetWidth, offsetHeight, clientWidth, clientHeight
   - Shows boundingClientRect and computedStyle dimensions
   - Logs viewport transform matrix before and after zoom
   - Detects when viewport transform becomes all zeros (indicates failure)

3. **Container Dimension Validation**
   ```javascript
   function hasValidDimensions(container) {
     const rect = container.getBoundingClientRect();
     const width = rect.width || container.offsetWidth;
     const height = rect.height || container.offsetHeight;
     return width > 0 && height > 0;
   }
   ```

4. **Viewport Fitting with Recovery**
   ```javascript
   // Check if transform is all zeros (failure)
   if (transformAfter && transformAfter.includes('matrix(0 0 0 0 0 0)')) {
     // Attempt manual viewbox recovery
     canvas.viewbox({
       x: 0, y: 0,
       width: outer.width,
       height: outer.height
     });
   }
   ```

## Files

### CSS
- `bpmn.css` - Styles for BPMN preview containers
  - Light/dark mode support matching WHO template
  - 240px preview height
  - Compact file info header
  - Loading and error states

### JavaScript
- `bpmn-viewer.js` - BPMN viewer initialization and viewport handling
  - Loads bpmn-js library from CDN
  - Implements requestAnimationFrame-based viewport fitting
  - Comprehensive diagnostic logging
  - Container dimension validation

### HTML Template
- `test-bpmn-viewer.html` - Test page demonstrating the viewer
  - Example BPMN preview container
  - Documentation of expected console output
  - Implementation details

### Test Data
- `sample.bpmn` - Simple BPMN diagram for testing

## Usage

### In HTML Pages

```html
<!-- Include CSS and JS -->
<link href="assets/css/bpmn.css" rel="stylesheet"/>
<script src="assets/js/bpmn-viewer.js"></script>

<!-- BPMN Preview Container -->
<div class="bpmn-preview-container" data-bpmn-url="path/to/diagram.bpmn">
  <div class="bpmn-file-info">
    <span class="bpmn-file-name">My Process</span>
    <div class="bpmn-file-actions">
      <a href="path/to/diagram.svg" target="_blank">SVG</a>
      <a href="path/to/diagram.bpmn" target="_blank">BPMN</a>
    </div>
  </div>
  <div class="bpmn-canvas-container">
    <div class="bpmn-canvas"></div>
  </div>
</div>
```

### In Python Extractors

The `dd_extractor.py` automatically generates BPMN preview containers:

```python
code_definition['defintion'] += f"""<div class="bpmn-preview-container" data-bpmn-url="{link_bpmn}">
<div class="bpmn-file-info">
<span class="bpmn-file-name">{display}</span>
<div class="bpmn-file-actions">
<a href="{link_svg}" target="_blank">SVG</a>
<a href="{link_bpmn}" target="_blank">BPMN</a>
</div>
</div>
<div class="bpmn-canvas-container">
<div class="bpmn-canvas"></div>
</div>
</div>
"""
```

### In XSLT Templates

The `bpmn2fhirfsh.xsl` generates BPMN preview containers:

```xml
<xsl:text disable-output-escaping="yes">&lt;div class="bpmn-preview-container" data-bpmn-url="</xsl:text>
<xsl:value-of select="$bpmnUrl"/>
<xsl:text disable-output-escaping="yes">"&gt;
&lt;div class="bpmn-file-info"&gt;
&lt;span class="bpmn-file-name"&gt;</xsl:text>
<xsl:value-of select="@name"/>
<!-- ... rest of HTML structure ... -->
```

## Diagnostic Output

When DEBUG_MODE is enabled (default), the browser console shows:

```
[BPMN Viewer] Found 1 BPMN preview container(s)
[BPMN Viewer] Loading BpmnJS from CDN: https://unpkg.com/bpmn-js@17.2.1/...
[BPMN Viewer] BpmnJS library loaded successfully
[BPMN Viewer] Initializing viewer 1/1 {bpmnUrl: "diagram.bpmn"}
[BPMN Viewer] Initial container dimensions: {
  container.offsetWidth: 1160,
  container.offsetHeight: 240,
  canvas.offsetWidth: 1160,
  canvas.offsetHeight: 240
}
[BPMN Viewer] Container dimensions check: {
  offsetWidth: 1160,
  offsetHeight: 240,
  clientWidth: 1160,
  clientHeight: 240,
  boundingRect.width: 1160,
  boundingRect.height: 240,
  computedStyle.width: "1160px",
  computedStyle.height: "240px",
  hasValidDimensions: true
}
[BPMN Viewer] fitViewportWithRAF called
[BPMN Viewer] First RAF callback: layout should be painted
[BPMN Viewer] Container has valid dimensions, proceeding with callback
[BPMN Viewer] Second RAF callback: executing zoom
[BPMN Viewer] Pre-zoom state: {
  viewbox.x: 0,
  viewbox.y: 0,
  viewbox.width: 1160,
  viewbox.height: 240,
  viewbox.scale: 1,
  ...
}
[BPMN Viewer] Viewport transform before zoom: matrix(1 0 0 1 0 0)
[BPMN Viewer] Post-zoom state: {
  viewbox.scale: 0.85,
  ...
}
[BPMN Viewer] Viewport transform after zoom: matrix(0.85 0 0 0.85 100 50)
```

If the viewport transform is all zeros after zoom:

```
[BPMN Viewer] WARNING: Viewport transform is all zeros after zoom!
[BPMN Viewer] Attempting manual viewbox recovery {width: 500, height: 200}
```

## Testing

1. Open `test-bpmn-viewer.html` in a browser
2. Open Developer Console (F12)
3. Check for diagnostic output
4. Verify the BPMN preview container is 240px tall
5. Verify file info is on a single line
6. Check that viewport transform is not all zeros

## Browser Compatibility

- Modern browsers with ES6 support
- requestAnimationFrame support (all modern browsers)
- Fetch API support (all modern browsers)

## Dependencies

- **bpmn-js** (v17.2.1) - Loaded from CDN
- No other external dependencies required

## Related Issues

- [litlfred/sgex#1082](https://github.com/litlfred/sgex/pull/1082) - Original PR with initial work
- Issue description noted viewport scaling problems with `setTimeout` approach
- Container dimensions were 0 when zoom was called, resulting in `matrix(0 0 0 0 0 0)` transform

## License

This implementation is part of WHO SMART Base and follows the same license.
