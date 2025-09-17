# gh-pages/branches Directory Cleanup

## Issue Summary

The `gh-pages/branches` directory has grown to **8.4GB** containing **1,578 items** (93,719+ files total). This directory contains historical builds from various feature branches and is consuming significant repository space, impacting clone and fetch performance.

**Issue Link**: [#150 - Depopulate gh-pages/branches](https://github.com/WorldHealthOrganization/smart-base/issues/150)

## Analysis Results

### Current State (Before Cleanup)
- **Directory Size**: 8.4GB
- **Number of Items**: 1,578 directories
- **Total Files**: 93,719+ files
- **Content**: Historical builds from branches like:
  - `fix-58-2`, `fix-54`, `v1`, `Persona`, `R5`, `updatescript`, `wfw`
  - Each containing complete IG builds with HTML, JSON, XML, TTL files
  - Duplicate content across multiple branch builds

### Target State (After Cleanup)
- **Directory Size**: 92KB (empty directory)
- **Number of Items**: 0
- **Total Files**: 0
- **Space Saved**: ~8.3GB

## Solution Implemented

### GitHub Workflow: "Prune Deployed Branches"

A secure GitHub Actions workflow has been created: `.github/workflows/prune-deployed-branches.yml`

**Features:**
- ✅ Manual dispatch from GitHub UI (workflow_dispatch)
- ✅ Comprehensive safety checks and validation
- ✅ Dry run mode for safe testing
- ✅ Confirmation requirement to prevent accidental execution
- ✅ Automatic size measurement and reporting
- ✅ Detailed commit documentation with statistics
- ✅ Secure execution with proper permissions

**Safety Features:**
- Requires explicit "CONFIRM" input to proceed
- Validates execution on correct gh-pages branch
- Verifies branches directory exists before proceeding
- Dry run mode shows what would be deleted without making changes
- Comprehensive logging and status reporting

## Execution Instructions

### Using GitHub Actions Workflow (Recommended)

1. **Navigate to GitHub Actions**:
   - Go to the repository on GitHub
   - Click on "Actions" tab
   - Find "Prune Deployed Branches" workflow

2. **Run the workflow**:
   - Click "Run workflow" button
   - **For testing**: Leave "dry_run" as `true` to see what would be deleted
   - **For actual cleanup**: Set "dry_run" to `false`
   - Type "CONFIRM" in the confirmation field
   - Click "Run workflow"

3. **Monitor execution**:
   - Watch the workflow run in real-time
   - Review logs for detailed progress and results
   - Verify success in the workflow summary

### Dry Run Process (Recommended First Step)

1. Run workflow with `dry_run: true`
2. Review the analysis output to see:
   - Current size and file count
   - Directories that would be removed
   - Expected impact of cleanup
3. If satisfied, run again with `dry_run: false`

## Impact Assessment

### Repository Benefits
- **Significant size reduction**: ~8.3GB space saved
- **Improved performance**: Faster clones, fetches, and operations
- **Cleaner history**: Removes unnecessary historical artifacts
- **Better maintenance**: Easier to manage gh-pages content

### Risk Assessment
- **Low Risk**: Only removes old build artifacts from branches
- **No functional impact**: Current main/production content unaffected
- **Reversible**: Branches can be rebuilt if needed through CI/CD
- **Backup available**: Git history preserves pre-cleanup state

## Technical Details

### GitHub Workflow Details
The workflow (`prune-deployed-branches.yml`) includes:
- **Trigger**: Manual dispatch only (workflow_dispatch)
- **Inputs**: 
  - `confirm_cleanup`: Requires "CONFIRM" to proceed
  - `dry_run`: Boolean to enable safe testing mode
- **Safety checks**: Branch validation, directory existence, proper permissions
- **Execution**: Automated cleanup with comprehensive logging

### Files Removed
The cleanup removes build artifacts including:
- HTML documentation files
- JSON/XML/TTL resource files  
- CSS/JS/image assets
- Excel/CSV export files
- PNG icon files
- Various metadata files

### Directories Cleaned
- `branches/fix-*` (various fix branches)
- `branches/v1` (version builds)
- `branches/Persona` (feature branch builds)
- `branches/R5` (FHIR R5 builds)
- `branches/updatescript` (script builds)
- `branches/wfw` (workflow builds)

## Verification Steps

After workflow execution:

1. **Check workflow logs**:
   - Review GitHub Actions run logs
   - Verify successful completion
   - Check size reduction statistics

2. **Verify results**:
   - Navigate to gh-pages branch on GitHub
   - Confirm branches directory is empty
   - Check repository size improvements

3. **Monitor performance**:
   - Test clone speed improvements
   - Verify GitHub Pages functionality

## Conclusion

This GitHub Actions workflow provides a secure, auditable way to clean up the gh-pages/branches directory. The workflow dramatically improves repository performance by removing 8.3GB of unnecessary historical build artifacts while maintaining safety through comprehensive checks and dry-run capabilities.

The solution is accessible through the GitHub UI, provides detailed logging, and ensures proper authorization and confirmation before making any changes.