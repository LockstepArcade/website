#!/usr/bin/env python3
"""
Build script for Lockstep Arcade website.

Reads config.json and templates, generates static HTML files in docs/ directory.

Usage:
    python build.py
"""

import json
import os
import shutil
from pathlib import Path

# Directories
SCRIPT_DIR = Path(__file__).parent
TEMPLATES_DIR = SCRIPT_DIR / "templates"
PARTIALS_DIR = TEMPLATES_DIR / "partials"
DOCS_DIR = SCRIPT_DIR / "docs"
CONFIG_FILE = SCRIPT_DIR / "config.json"


def load_config():
    """Load configuration from config.json."""
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def load_template(name):
    """Load a template file."""
    template_path = TEMPLATES_DIR / name
    with open(template_path, "r", encoding="utf-8") as f:
        return f.read()


def load_partial(name):
    """Load a partial template file."""
    partial_path = PARTIALS_DIR / name
    with open(partial_path, "r", encoding="utf-8") as f:
        return f.read()


def build_changelog_html(releases):
    """Build the changelog HTML from releases data."""
    html_parts = []
    for release in releases:
        is_current = release.get("current", False)
        version = release["version"]
        changes = release["changes"]

        # Build class
        block_class = "version-block current-version" if is_current else "version-block"

        # Build header
        badge_html = '<span class="version-badge">Current</span>' if is_current else ""

        # Build changes list
        changes_html = "\n".join(f"                        <li>{change}</li>" for change in changes)

        block_html = f"""                <div class="{block_class}">
                    <div class="version-header">
                        <h3>Version {version}</h3>
                        {badge_html}
                    </div>
                    <ul class="changelog-list">
{changes_html}
                    </ul>
                </div>"""
        html_parts.append(block_html)

    return "\n\n".join(html_parts)


def build_whats_new_html(releases):
    """Build the 'What's New' list for the download page (current version only)."""
    current_release = next((r for r in releases if r.get("current", False)), releases[0])
    changes = current_release["changes"]
    return "\n".join(f"                    <li>{change}</li>" for change in changes)


def render_template(template_content, variables):
    """
    Render a template by replacing {variable} placeholders.

    Uses a simple approach: replace each known variable.
    Curly braces in CSS/JS are preserved because they won't match variable names.
    """
    result = template_content
    for key, value in variables.items():
        placeholder = "{" + key + "}"
        result = result.replace(placeholder, str(value))
    return result


def ensure_dir(path):
    """Ensure a directory exists."""
    path.mkdir(parents=True, exist_ok=True)


def build_install_script_mac(version):
    """Build the macOS install shell script."""
    return f"""#!/bin/bash
cd ~/Downloads

echo "Downloading Lockstep Arcade {version}..."
curl -LO https://locksteparcade.com/lockstep_arcade_{version}_mac.zip

echo "Extracting..."
unzip -o lockstep_arcade_{version}_mac.zip -d lockstep_arcade_{version}

echo "Cleaning up..."
rm lockstep_arcade_{version}_mac.zip

echo "Opening folder..."
open lockstep_arcade_{version}

echo "Done! Run LockstepArcade to play."
"""


def build_install_script_windows(version):
    """Build the Windows install PowerShell script."""
    return f"""$ProgressPreference = 'SilentlyContinue'
$downloadDir = "$env:USERPROFILE\\Downloads"
$zipFile = "$downloadDir\\lockstep_arcade_{version}.zip"
$extractDir = "$downloadDir\\lockstep_arcade_{version}"

Write-Host "Downloading Lockstep Arcade {version}..."
Invoke-WebRequest -Uri "https://locksteparcade.com/lockstep_arcade_{version}.zip" -OutFile $zipFile

Write-Host "Extracting..."
Expand-Archive -Path $zipFile -DestinationPath $extractDir -Force

Write-Host "Cleaning up..."
Remove-Item $zipFile

Write-Host "Opening folder..."
Start-Process explorer.exe $extractDir

Write-Host "Done! Run LockstepArcade.exe to play."
"""


def clean_generated_files():
    """Remove generated HTML files and subdirectories from docs/.

    Preserves assets: images, CSS, zip files, CNAME, etc.
    """
    if not DOCS_DIR.exists():
        return

    print("Cleaning generated files...")

    # Remove all generated files in docs/
    for pattern in ["*.html", "*.sh", "*.ps1"]:
        for generated_file in DOCS_DIR.glob(pattern):
            print(f"  Removing {generated_file.name}")
            generated_file.unlink()

    # Remove subdirectories (download/, signup/, changelog/, etc.)
    # These only contain generated index.html files
    for item in DOCS_DIR.iterdir():
        if item.is_dir():
            print(f"  Removing {item.name}/")
            shutil.rmtree(item)


def build_site():
    """Build the entire site."""
    clean_generated_files()

    print("Loading configuration...")
    config = load_config()

    # Extract config values
    version = config["version"]
    download_size_windows = config["download_size_windows"]
    download_size_mac = config["download_size_mac"]
    discord_url = config["discord_url"]
    web3forms_key = config["web3forms_key"]
    current_year = config["current_year"]
    releases = config["releases"]

    # Build generated HTML content
    changelog_html = build_changelog_html(releases)
    whats_new_html = build_whats_new_html(releases)

    # Load partials
    navbar_template = load_partial("navbar.html")
    footer_template = load_partial("footer.html")

    # Ensure docs directory exists
    ensure_dir(DOCS_DIR)
    ensure_dir(DOCS_DIR / "download")
    ensure_dir(DOCS_DIR / "signup")
    ensure_dir(DOCS_DIR / "changelog")

    # Common variables for all pages
    common_vars = {
        "version": version,
        "download_size_windows": download_size_windows,
        "download_size_mac": download_size_mac,
        "discord_url": discord_url,
        "web3forms_key": web3forms_key,
        "current_year": current_year,
        "changelog_html": changelog_html,
        "whats_new_html": whats_new_html,
    }

    # Pages to build: (template_name, output_path, path_prefix)
    pages = [
        ("index.html", DOCS_DIR / "index.html", ""),
        ("download.html", DOCS_DIR / "download" / "index.html", "../"),
        ("signup.html", DOCS_DIR / "signup" / "index.html", "../"),
        ("setup.html", DOCS_DIR / "setup.html", ""),
        ("changelog.html", DOCS_DIR / "changelog" / "index.html", "../"),
    ]

    for template_name, output_path, path_prefix in pages:
        print(f"Building {output_path.relative_to(DOCS_DIR)}...")

        # Load template
        template = load_template(template_name)

        # Render navbar and footer with path prefix
        navbar_vars = {**common_vars, "path_prefix": path_prefix}
        footer_vars = {**common_vars, "path_prefix": path_prefix}
        navbar = render_template(navbar_template, navbar_vars)
        footer = render_template(footer_template, footer_vars)

        # Build page variables
        page_vars = {
            **common_vars,
            "navbar": navbar,
            "footer": footer,
            "path_prefix": path_prefix,
        }

        # Render page
        output = render_template(template, page_vars)

        # Write output
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(output)

    # Generate install scripts
    print("Building install_mac.sh...")
    with open(DOCS_DIR / "install_mac.sh", "w", encoding="utf-8", newline="\n") as f:
        f.write(build_install_script_mac(version))

    print("Building install_windows.ps1...")
    with open(DOCS_DIR / "install_windows.ps1", "w", encoding="utf-8", newline="\n") as f:
        f.write(build_install_script_windows(version))

    print("\nBuild complete!")
    print(f"Output directory: {DOCS_DIR}")
    print("\nRemember to copy/move your assets to docs/:")
    print("  - styles.css")
    print("  - banner.jpg")
    print("  - screenshot1.png, screenshot2.png, screenshot3.png")
    print("  - lockstep_arcade_*.zip (game files)")
    print("  - CNAME")


if __name__ == "__main__":
    build_site()
