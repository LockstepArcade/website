# Lockstep Arcade Website

Static website for Lockstep Arcade, a multiplayer gaming platform.

## Build System

The site uses a pure Python build system (no dependencies) with simple template substitution.

### Key Files

- `config.json` - All release data: version, changelog, download sizes
- `build.py` - Generates HTML from templates into `docs/`
- `templates/` - Source templates with `{variable}` placeholders
- `templates/partials/` - Shared components (navbar, footer)
- `docs/` - Generated output served by GitHub Pages

### Building

```bash
python build.py
```

This regenerates all HTML files in `docs/` from templates.

## New Release Workflow

1. Add new game zip files to `docs/` (both Windows and Mac builds)
2. Edit `config.json`:
   - Update `"version"`
   - Update `"download_size_windows"` and `"download_size_mac"` if changed
   - Add new release entry at top of `"releases"` array with `"current": true`
   - Remove `"current": true` from the previous version
3. Run `python build.py`
4. Commit and push

## Template Variables

Templates use `{variable}` syntax. Available variables:
- `{version}` - Current version number
- `{download_size_windows}`, `{download_size_mac}` - File sizes
- `{discord_url}`, `{web3forms_key}`, `{current_year}`
- `{navbar}`, `{footer}` - Injected partials
- `{path_prefix}` - `../` for subdirectory pages, empty for root
- `{changelog_html}`, `{whats_new_html}` - Generated from releases data

## Deployment

GitHub Pages serves from the `docs/` directory. Assets (images, zip files, styles.css, CNAME) live directly in `docs/`.

## URL Structure

These URLs must remain stable (linked from the game):
- `/download` → `docs/download/index.html`
- `/signup` → `docs/signup/index.html`
- `/gettingstarted` → `docs/gettingstarted/index.html`

## CSS Components

Key reusable classes in `docs/styles.css`:

- `.content-box` - White card with shadow. Add `--bordered` for header border.
- `.info-box` - Colored callout. Variants: `--warning` (yellow), `--cta` (purple gradient)
- `.step-badge` - Numbered circle. Add `--small` for compact version.
- `.step-section` - Horizontal step with badge + content
- `.code-block` - Light code block. Use `--dark` for terminal commands.
- `.card-grid` - Responsive grid for cards
- `.resource-card` - Clickable link card
- `.content-wrapper` - Centers content at max-width 900px
