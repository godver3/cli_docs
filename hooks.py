"""
MkDocs build hook — fetches the latest pre-release version from GitHub
and injects it as a template variable so pages can use {{ version }}.
"""

import urllib.request
import json
import logging
import re

log = logging.getLogger("mkdocs.hooks")


def on_env(env, config, files, **kwargs):
    """Inject {{ version }} and {{ version_url }} into all page templates."""
    version = "latest"
    version_url = "https://github.com/godver3/clyde/releases"

    try:
        req = urllib.request.Request(
            "https://api.github.com/repos/godver3/clyde/releases",
            headers={"User-Agent": "mkdocs-cli_debrid-docs"},
        )
        with urllib.request.urlopen(req, timeout=5) as resp:
            releases = json.loads(resp.read().decode())
            # Find the latest pre-release first, fall back to latest release
            for release in releases:
                if release.get("prerelease"):
                    version = release["tag_name"]
                    version_url = release["html_url"]
                    break
            else:
                # No pre-release found — use latest release
                if releases:
                    version = releases[0]["tag_name"]
                    version_url = releases[0]["html_url"]
    except Exception as e:
        log.warning(f"cli_debrid docs: could not fetch release version: {e}")

    env.globals["cli_version"] = version
    env.globals["cli_version_url"] = version_url
    log.info(f"cli_debrid docs: version set to {version}")
    return env


def on_page_content(html, page, config, files, **kwargs):
    """Add target="_blank" rel="noopener" to all external links."""
    def replace_link(m):
        tag = m.group(0)
        href_match = re.search(r'href=["\']([^"\']*)["\']', tag)
        if not href_match:
            return tag
        href = href_match.group(1)
        if href.startswith("http://") or href.startswith("https://"):
            if 'target=' not in tag:
                tag = tag.rstrip(">").rstrip("/") + ' target="_blank" rel="noopener">'
        return tag

    return re.sub(r'<a [^>]+>', replace_link, html)
