#!/bin/bash

# Script to clean up the gh-pages/branches directory
# This script removes all content from the branches directory to reduce repository size
# 
# WARNING: This script will permanently delete all files in the gh-pages/branches directory
# Make sure you have the necessary permissions and backups before running
#
# Issue: https://github.com/WorldHealthOrganization/smart-base/issues/150

set -e

echo "🧹 Starting cleanup of gh-pages/branches directory..."

# Check if we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "❌ Error: Not in a git repository"
    exit 1
fi

# Check if gh-pages branch exists
if ! git rev-parse --verify gh-pages > /dev/null 2>&1; then
    echo "❌ Error: gh-pages branch does not exist"
    exit 1
fi

# Get current branch for restoration later
ORIGINAL_BRANCH=$(git rev-parse --abbrev-ref HEAD)
echo "📍 Current branch: $ORIGINAL_BRANCH"

# Checkout gh-pages branch
echo "🔀 Switching to gh-pages branch..."
git checkout gh-pages

# Check if branches directory exists
if [ ! -d "branches" ]; then
    echo "❌ Error: branches directory does not exist in gh-pages branch"
    git checkout "$ORIGINAL_BRANCH"
    exit 1
fi

# Get size before cleanup
echo "📏 Measuring current size of branches directory..."
BEFORE_SIZE=$(du -sh branches 2>/dev/null | cut -f1 || echo "unknown")
BEFORE_COUNT=$(find branches -type f 2>/dev/null | wc -l || echo "unknown")
echo "📊 Before cleanup: $BEFORE_SIZE with $BEFORE_COUNT files"

# Remove all contents from branches directory
echo "🗑️  Removing all contents from branches directory..."
rm -rf branches/*

# Verify cleanup
AFTER_SIZE=$(du -sh branches 2>/dev/null | cut -f1 || echo "unknown")
AFTER_COUNT=$(find branches -type f 2>/dev/null | wc -l || echo "0")
echo "📊 After cleanup: $AFTER_SIZE with $AFTER_COUNT files"

# Stage all deletions
echo "📦 Staging all deletions..."
git add -A

# Check if there are changes to commit
if git diff --cached --quiet; then
    echo "ℹ️  No changes to commit (branches directory was already empty)"
    git checkout "$ORIGINAL_BRANCH"
    exit 0
fi

# Count changes
DELETED_FILES=$(git status --porcelain | grep "^D " | wc -l)
echo "🔢 Files to be deleted: $DELETED_FILES"

# Commit the cleanup
echo "💾 Creating commit for cleanup..."
git commit -m "Remove all content from gh-pages/branches directory

This commit removes $DELETED_FILES files from the branches directory
to reduce repository size. The branches directory contained historical
builds from various feature branches that are no longer needed and
were consuming significant repository space.

Before: $BEFORE_SIZE with $BEFORE_COUNT files
After: $AFTER_SIZE with $AFTER_COUNT files

Resolves #150"

# Show the commit
echo "✅ Cleanup commit created:"
git log --oneline -1

echo ""
echo "🚀 Next steps:"
echo "1. Review the changes with: git show --stat"
echo "2. Push to remote with: git push origin gh-pages"
echo "3. This will permanently remove the files from the remote repository"
echo ""
echo "⚠️  WARNING: Make sure you have necessary permissions before pushing!"

# Return to original branch
echo "🔀 Returning to original branch: $ORIGINAL_BRANCH"
git checkout "$ORIGINAL_BRANCH"

echo "✅ Cleanup script completed successfully!"