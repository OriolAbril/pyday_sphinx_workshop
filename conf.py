"""Sphinx configuration file"""

# General configuration ------------------------------
project = "Personal website"
author = "Oriol Abril Pla"
copyright = f"2023, {author}"

exclude_patterns = [
    ".DS_Store",
    "Thumbs.db",
    "README.md",
    "build",
    "gettext",
    "jupyter_execute",
    "**/.ipynb_checkpoints/*",
    ".virtual_documents/**",
    "*.html",
]

extensions = [
    "sphinx_togglebutton",
    "sphinx_copybutton",
    "myst_parser",
    "sphinx_design",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "notfound.extension",
]

# Extension configuration ----------------------------
## notfound extension -----------------
notfound_urls_prefix = ""

## Myst parser ------------------------
myst_enable_extensions = [
    "colon_fence",
    "dollarmath",
    "linkify",
]
myst_url_schemes = ["mailto", "http", "https"]

## Intersphinx ------------------------
intersphinx_mapping = {
    "numpy": ("https://numpy.org/doc/stable/", None),
    "python": ("https://docs.python.org/3/", None),
}

# HTML output configuration --------------------------
html_theme = "sphinx_book_theme"
html_logo = "images/portrait_placeholder.png"
html_title = f"{author}'s website"
html_theme_options = {
    "repository_url": "https://github.com/OriolAbril/pyday_sphinx_repo",
    "repository_branch": "main",
    "home_page_in_toc": True,
    "use_edit_page_button": False,
    "use_issues_button": False,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/OriolAbril", 
            "icon": "fa-brands fa-github",
            "type": "fontawesome",
        },
        {
            "name": "Mastodon",
            "url": "https://toot.cat/@oriolabril", 
            "icon": "fa-brands fa-mastodon",
            "type": "fontawesome",
            "attributes": {"rel": "me"},
        },
        {
            "name": "Orcid",
            "url": "https://orcid.org/0000-0002-1847-9481",
            "icon": "fa-brands fa-orcid",
            "type": "fontawesome",
        },
    ],
}
