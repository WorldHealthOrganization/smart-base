/**
 * Dark/Light mode theme toggle functionality
 * Handles theme switching and persistence across page loads
 */
(function() {
    'use strict';
    
    // Get current theme from localStorage or detect system preference
    function getCurrentTheme() {
        const savedTheme = localStorage.getItem('theme');
        if (savedTheme) {
            return savedTheme;
        }
        
        // Check system preference
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            return 'dark';
        }
        
        return 'light';
    }
    
    // Apply theme to the document
    function applyTheme(theme) {
        if (theme === 'dark') {
            document.documentElement.setAttribute('data-theme', 'dark');
        } else {
            document.documentElement.removeAttribute('data-theme');
        }
    }
    
    // Toggle between light and dark themes
    function toggleTheme() {
        const currentTheme = getCurrentTheme();
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        
        localStorage.setItem('theme', newTheme);
        applyTheme(newTheme);
        updateToggleButton();
    }
    
    // Update the toggle button text/icon
    function updateToggleButton() {
        const button = document.getElementById('theme-toggle');
        if (button) {
            const currentTheme = getCurrentTheme();
            button.textContent = currentTheme === 'dark' ? '☀️ Light' : '🌙 Dark';
            button.setAttribute('aria-label', `Switch to ${currentTheme === 'dark' ? 'light' : 'dark'} mode`);
        }
    }
    
    // Create and insert the theme toggle button
    function createToggleButton() {
        const button = document.createElement('button');
        button.id = 'theme-toggle';
        button.className = 'theme-toggle';
        button.type = 'button';
        button.addEventListener('click', toggleTheme);
        
        // Try to find a good location for the button (near language selector or in header)
        const possibleLocations = [
            '.navbar-nav',
            '.navbar',
            '#segment-header',
            '.segment-header',
            'header',
            '.container-fluid',
            'body'
        ];
        
        let inserted = false;
        for (const selector of possibleLocations) {
            const container = document.querySelector(selector);
            if (container && !inserted) {
                // If it's a nav container, append to it
                if (selector.includes('nav')) {
                    container.appendChild(button);
                } else {
                    // For other containers, create a wrapper div and position it appropriately
                    const wrapper = document.createElement('div');
                    wrapper.style.cssText = 'position: absolute; top: 10px; right: 10px; z-index: 1000;';
                    wrapper.appendChild(button);
                    
                    if (container.style.position === '' || container.style.position === 'static') {
                        container.style.position = 'relative';
                    }
                    container.appendChild(wrapper);
                }
                inserted = true;
                break;
            }
        }
        
        // Fallback: create a floating button if no suitable container found
        if (!inserted) {
            const wrapper = document.createElement('div');
            wrapper.style.cssText = 'position: fixed; top: 10px; right: 10px; z-index: 9999;';
            wrapper.appendChild(button);
            document.body.appendChild(wrapper);
        }
        
        return button;
    }
    
    // Initialize theme functionality
    function initTheme() {
        // Apply the current theme immediately
        const currentTheme = getCurrentTheme();
        applyTheme(currentTheme);
        
        // Create the toggle button when DOM is ready
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', function() {
                createToggleButton();
                updateToggleButton();
            });
        } else {
            createToggleButton();
            updateToggleButton();
        }
        
        // Listen for system theme changes
        if (window.matchMedia) {
            window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function(e) {
                // Only update if user hasn't explicitly set a theme
                if (!localStorage.getItem('theme')) {
                    applyTheme(e.matches ? 'dark' : 'light');
                    updateToggleButton();
                }
            });
        }
    }
    
    // Start initialization
    initTheme();
})();