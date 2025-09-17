#!/bin/bash

# Script to check the current status of the gh-pages/branches directory
# This can be used to verify the current state before or after cleanup

set -e

echo "🔍 Checking gh-pages/branches directory status..."

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
git checkout gh-pages > /dev/null 2>&1

# Check if branches directory exists
if [ ! -d "branches" ]; then
    echo "❌ branches directory does not exist in gh-pages branch"
    git checkout "$ORIGINAL_BRANCH" > /dev/null 2>&1
    exit 1
fi

echo ""
echo "📊 BRANCHES DIRECTORY STATUS:"
echo "================================"

# Get detailed statistics
SIZE=$(du -sh branches 2>/dev/null | cut -f1 || echo "unknown")
echo "📏 Total size: $SIZE"

FILE_COUNT=$(find branches -type f 2>/dev/null | wc -l || echo "0")
echo "📄 Total files: $FILE_COUNT"

DIR_COUNT=$(find branches -maxdepth 1 -type d 2>/dev/null | grep -v "^branches$" | wc -l || echo "0")
echo "📁 Subdirectories: $DIR_COUNT"

echo ""
echo "📁 SUBDIRECTORIES (first 20):"
echo "============================="
find branches -maxdepth 1 -type d 2>/dev/null | grep -v "^branches$" | head -20 | sed 's/^branches\//  /'

if [ "$DIR_COUNT" -gt 20 ]; then
    REMAINING=$((DIR_COUNT - 20))
    echo "  ... and $REMAINING more directories"
fi

echo ""
echo "💾 RECENT GH-PAGES COMMITS:"
echo "=========================="
git log --oneline -5

echo ""
echo "🔢 REPOSITORY SIZE STATS:"
echo "======================="
git count-objects -vH | grep -E "(size-pack|size)"

# Return to original branch
git checkout "$ORIGINAL_BRANCH" > /dev/null 2>&1

echo ""
echo "✅ Status check completed!"
echo ""

# Provide recommendations based on status
if [ "$FILE_COUNT" -gt 10000 ]; then
    echo "⚠️  RECOMMENDATION: Consider running cleanup-gh-pages-branches.sh"
    echo "   The branches directory contains $FILE_COUNT files ($SIZE)"
    echo "   This may be impacting repository performance."
elif [ "$FILE_COUNT" -eq 0 ]; then
    echo "✅ GOOD: branches directory is empty - no cleanup needed"
else
    echo "ℹ️  INFO: branches directory contains $FILE_COUNT files ($SIZE)"
    echo "   Cleanup may not be necessary unless size is concerning."
fi