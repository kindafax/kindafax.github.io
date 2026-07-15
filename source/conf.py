# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'KindaFax'
copyright = '&copy; 2026, itsdanjc'
author = 'itsdanjc'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
	"myst_parser",
    "sphinx_design",
    "sphinx_copybutton",
    "notfound.extension",
    "sphinx_sitemap",
    "sphinx_reredirects"
]

templates_path = ['_templates']
exclude_patterns = [
    "**/*.draft.rst",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "shibuya"
html_static_path = ['_static']
html_extra_path = ['robots.txt']
html_baseurl = "https://kindafax.itsdanjc.com/"
# html_logo = "/favicon.ico"

sitemap_show_lastmod = True
sitemap_url_scheme = "{link}"
sitemap_excludes = [
    "404.html",
]

notfound_urls_prefix = "/"

html_context = {
    "source_edit_template": "https://github.com/kindafax/kindafax.github.io/blob/main/source/{0}",
}

html_theme_options = {
    "page_layout": "default",
    "logo_target": "/",
    "accent_color": "blue",
    "globaltoc_expand_depth": 0,
    "toctree_includehidden": False,
    
    "show_ai_links": False,

    "github_url": "https://github.com/kindafax",
    "gitlab_url": "https://gitlab.com/kindafax",

    "nav_links": [
        {
	        "title": "Documentation",
            "url": "docs/index",
            "children": [
                {
                    "title": "Server",
                    "url": "docs/server/index",
                    "summary": "The main component of KindaFax. Learn how to host and maintain KindaFax, on your hardware."
                },
                {
                    "title": "Printer Client",
                    "url": "docs/printer/index",
                    "summary": "Use a receipt printer to receive messages."
                },
                {
                    "title": "Web Client",
                    "url": "docs/web/index",
                    "summary": "Connect to a KindaFax Server from anywhere."
                },
            ]
        },
        {
            "title": "About",
            "url": "https://itsdanjc.com",
        }
    ]
}

# -- Options for HTML redirects -------------------------------------------------
# https://documatt.com/sphinx-reredirects/usage/
#
# Redirects should be made when renaming pages, and to create shorter permanent
# urls, if the is a doc link in an error message.

redirects = {
    "./help/RECEIVER_NOT_FOUND.html":
        "/docs/server/developing-clients/websocket/status.html#receiver-not-found",

    "./help/SENDER_NOT_FOUND.html":
        "/docs/server/developing-clients/websocket/status.html#sender-not-found",

    "./help/INVALID_MESSAGE_SCHEMA.html":
        "/docs/server/developing-clients/websocket/status.html#invalid-message-schema",

    "./help/CLIENT_AUTH_REQUIRED.html":
        "/docs/server/developing-clients/websocket/status.html#client-auth-required",

    "./help/TOO_MANY_REQUESTS.html":
        "/docs/server/developing-clients/websocket/status.html#too-many-requests",

    "./help/SERVER_ERROR.html":
        "/docs/server/developing-clients/websocket/status.html#server-error",
        
}