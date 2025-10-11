/**
 * BPMN Viewer Initialization for SMART Guidelines
 * 
 * This script provides interactive BPMN diagram viewing capabilities using bpmn-js.
 * Features:
 * - Automatic viewport scaling with requestAnimationFrame
 * - Diagnostic logging for container dimensions
 * - Graceful error handling
 * - Ensures container has non-zero dimensions before zoom operations
 * 
 * Based on requirements from: https://github.com/litlfred/sgex/pull/1082
 */

(function() {
  'use strict';

  // Configuration
  const BPMN_CDN = 'https://unpkg.com/bpmn-js@17.2.1/dist/bpmn-viewer.production.min.js';
  const DEBUG_MODE = true; // Enable diagnostic logging
  
  /**
   * Log diagnostic information to console
   */
  function logDiagnostic(message, data) {
    if (DEBUG_MODE) {
      console.log(`[BPMN Viewer] ${message}`, data || '');
    }
  }

  /**
   * Check if container has non-zero dimensions
   */
  function hasValidDimensions(container) {
    const rect = container.getBoundingClientRect();
    const computed = window.getComputedStyle(container);
    const width = rect.width || container.offsetWidth;
    const height = rect.height || container.offsetHeight;
    
    logDiagnostic('Container dimensions check:', {
      'offsetWidth': container.offsetWidth,
      'offsetHeight': container.offsetHeight,
      'clientWidth': container.clientWidth,
      'clientHeight': container.clientHeight,
      'boundingRect.width': rect.width,
      'boundingRect.height': rect.height,
      'computedStyle.width': computed.width,
      'computedStyle.height': computed.height,
      'hasValidDimensions': width > 0 && height > 0
    });
    
    return width > 0 && height > 0;
  }

  /**
   * Wait for container to have valid dimensions using requestAnimationFrame
   */
  function waitForValidDimensions(container, callback, maxAttempts = 50, attempt = 0) {
    if (hasValidDimensions(container)) {
      logDiagnostic('Container has valid dimensions, proceeding with callback');
      callback();
      return;
    }
    
    if (attempt >= maxAttempts) {
      logDiagnostic('Max attempts reached waiting for valid dimensions', {
        attempt: attempt,
        maxAttempts: maxAttempts
      });
      // Try callback anyway as fallback
      callback();
      return;
    }
    
    logDiagnostic(`Waiting for valid dimensions (attempt ${attempt + 1}/${maxAttempts})`);
    
    requestAnimationFrame(() => {
      waitForValidDimensions(container, callback, maxAttempts, attempt + 1);
    });
  }

  /**
   * Fit viewport to diagram with proper timing using requestAnimationFrame
   */
  function fitViewportWithRAF(viewer, canvas) {
    logDiagnostic('fitViewportWithRAF called');
    
    // First requestAnimationFrame: ensure layout is painted
    requestAnimationFrame(() => {
      logDiagnostic('First RAF callback: layout should be painted');
      
      // Check container dimensions at time of first RAF
      const container = canvas.parentElement;
      if (!hasValidDimensions(container)) {
        logDiagnostic('Container still has zero dimensions in first RAF, waiting...');
        
        // Wait for valid dimensions before proceeding
        waitForValidDimensions(container, () => {
          executeViewportFit(viewer, canvas);
        });
      } else {
        // Container has valid dimensions, proceed
        executeViewportFit(viewer, canvas);
      }
    });
  }

  /**
   * Execute the viewport fit operation
   */
  function executeViewportFit(viewer, canvas) {
    // Second requestAnimationFrame: ensure any dynamic content is ready
    requestAnimationFrame(() => {
      logDiagnostic('Second RAF callback: executing zoom');
      
      try {
        const zoomScroll = canvas.get('zoomScroll');
        const viewbox = canvas.viewbox();
        
        logDiagnostic('Pre-zoom state:', {
          'viewbox.x': viewbox.x,
          'viewbox.y': viewbox.y,
          'viewbox.width': viewbox.width,
          'viewbox.height': viewbox.height,
          'viewbox.scale': viewbox.scale,
          'viewbox.inner': viewbox.inner,
          'viewbox.outer': viewbox.outer
        });
        
        // Get SVG viewport transform before zoom
        const svg = canvas._svg;
        const viewport = svg.querySelector('.viewport');
        if (viewport) {
          const transformBefore = viewport.getAttribute('transform');
          logDiagnostic('Viewport transform before zoom:', transformBefore);
        }
        
        // Execute fit-viewport with center
        canvas.zoom('fit-viewport', 'auto');
        
        // Log state after zoom using RAF to ensure it's applied
        requestAnimationFrame(() => {
          const viewboxAfter = canvas.viewbox();
          logDiagnostic('Post-zoom state:', {
            'viewbox.x': viewboxAfter.x,
            'viewbox.y': viewboxAfter.y,
            'viewbox.width': viewboxAfter.width,
            'viewbox.height': viewboxAfter.height,
            'viewbox.scale': viewboxAfter.scale,
            'viewbox.inner': viewboxAfter.inner,
            'viewbox.outer': viewboxAfter.outer
          });
          
          if (viewport) {
            const transformAfter = viewport.getAttribute('transform');
            logDiagnostic('Viewport transform after zoom:', transformAfter);
            
            // Check if transform is still all zeros (indicates failure)
            if (transformAfter && transformAfter.includes('matrix(0 0 0 0 0 0)')) {
              logDiagnostic('WARNING: Viewport transform is all zeros after zoom!');
              
              // Attempt recovery by manually setting a reasonable viewbox
              try {
                const outer = viewboxAfter.outer;
                if (outer && outer.width > 0 && outer.height > 0) {
                  logDiagnostic('Attempting manual viewbox recovery', outer);
                  canvas.viewbox({
                    x: 0,
                    y: 0,
                    width: outer.width,
                    height: outer.height
                  });
                }
              } catch (err) {
                logDiagnostic('Manual viewbox recovery failed:', err);
              }
            }
          }
        });
        
      } catch (error) {
        logDiagnostic('Error during zoom operation:', error);
      }
    });
  }

  /**
   * Initialize a BPMN viewer for a given container
   */
  function initializeBpmnViewer(container, bpmnUrl) {
    logDiagnostic('Initializing BPMN viewer', { bpmnUrl: bpmnUrl });
    
    // Check if BpmnJS is available
    if (typeof window.BpmnJS === 'undefined') {
      const errorMsg = 'BpmnJS library not loaded. Please include bpmn-js script.';
      logDiagnostic('ERROR: ' + errorMsg);
      showError(container, errorMsg);
      return;
    }

    const canvas = container.querySelector('.bpmn-canvas');
    if (!canvas) {
      logDiagnostic('ERROR: No canvas element found in container');
      return;
    }

    // Show loading indicator
    const loadingDiv = document.createElement('div');
    loadingDiv.className = 'bpmn-loading';
    loadingDiv.textContent = 'Loading BPMN diagram...';
    container.querySelector('.bpmn-canvas-container').appendChild(loadingDiv);

    // Log initial container dimensions
    logDiagnostic('Initial container dimensions:', {
      'container.offsetWidth': container.offsetWidth,
      'container.offsetHeight': container.offsetHeight,
      'canvas.offsetWidth': canvas.offsetWidth,
      'canvas.offsetHeight': canvas.offsetHeight
    });

    // Create viewer instance
    const viewer = new window.BpmnJS({
      container: canvas,
      height: 240
    });

    // Fetch and display BPMN diagram
    fetch(bpmnUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        }
        return response.text();
      })
      .then(bpmnXml => {
        logDiagnostic('BPMN XML fetched successfully', { 
          length: bpmnXml.length,
          url: bpmnUrl 
        });
        
        return viewer.importXML(bpmnXml);
      })
      .then(() => {
        logDiagnostic('BPMN diagram imported successfully');
        
        // Remove loading indicator
        if (loadingDiv && loadingDiv.parentElement) {
          loadingDiv.remove();
        }

        // Get canvas for zoom operations
        const bpmnCanvas = viewer.get('canvas');
        
        // Log canvas dimensions after import
        logDiagnostic('Canvas dimensions after import:', {
          'canvas.offsetWidth': canvas.offsetWidth,
          'canvas.offsetHeight': canvas.offsetHeight,
          'container.offsetWidth': container.offsetWidth,
          'container.offsetHeight': container.offsetHeight
        });

        // Use requestAnimationFrame for viewport fitting
        fitViewportWithRAF(viewer, bpmnCanvas);
      })
      .catch(error => {
        logDiagnostic('Error loading BPMN diagram:', error);
        
        // Remove loading indicator
        if (loadingDiv && loadingDiv.parentElement) {
          loadingDiv.remove();
        }
        
        showError(container, `Failed to load BPMN diagram: ${error.message}`);
      });
  }

  /**
   * Show error message in container
   */
  function showError(container, message) {
    const errorDiv = document.createElement('div');
    errorDiv.className = 'bpmn-error';
    errorDiv.textContent = message;
    
    const canvasContainer = container.querySelector('.bpmn-canvas-container');
    if (canvasContainer) {
      // Remove loading indicator if present
      const loading = canvasContainer.querySelector('.bpmn-loading');
      if (loading) {
        loading.remove();
      }
      
      canvasContainer.appendChild(errorDiv);
    }
  }

  /**
   * Load bpmn-js library from CDN
   */
  function loadBpmnJsLibrary(callback) {
    // Check if already loaded
    if (typeof window.BpmnJS !== 'undefined') {
      logDiagnostic('BpmnJS already loaded');
      callback();
      return;
    }

    logDiagnostic('Loading BpmnJS from CDN:', BPMN_CDN);
    
    const script = document.createElement('script');
    script.src = BPMN_CDN;
    script.onload = () => {
      logDiagnostic('BpmnJS library loaded successfully');
      callback();
    };
    script.onerror = () => {
      logDiagnostic('ERROR: Failed to load BpmnJS library from CDN');
    };
    
    document.head.appendChild(script);
  }

  /**
   * Initialize all BPMN viewers on the page
   */
  function initializeAllViewers() {
    const containers = document.querySelectorAll('.bpmn-preview-container');
    
    if (containers.length === 0) {
      logDiagnostic('No BPMN preview containers found on page');
      return;
    }

    logDiagnostic(`Found ${containers.length} BPMN preview container(s)`);

    // Load bpmn-js library first
    loadBpmnJsLibrary(() => {
      containers.forEach((container, index) => {
        const bpmnUrl = container.getAttribute('data-bpmn-url');
        
        if (!bpmnUrl) {
          logDiagnostic(`Container ${index} missing data-bpmn-url attribute`);
          showError(container, 'BPMN file URL not specified');
          return;
        }

        logDiagnostic(`Initializing viewer ${index + 1}/${containers.length}`);
        initializeBpmnViewer(container, bpmnUrl);
      });
    });
  }

  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializeAllViewers);
  } else {
    // DOM already loaded
    initializeAllViewers();
  }

  // Also expose initialization function globally for manual use
  window.initializeBpmnViewers = initializeAllViewers;

})();
