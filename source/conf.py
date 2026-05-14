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
    "sphinx-sitemap"
]

templates_path = ['_templates']
exclude_patterns = []

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "shibuya"
html_static_path = ['_static']
html_baseurl = "https://kindafax.itsdanjc.com/"
# html_logo = "/favicon.ico"

sitemap_show_lastmod = True

notfound_urls_prefix = "/"

html_context = {
    "source_type": "github",
    "source_user": "kindafax",
    "source_repo": "server",
    "source_edit_template": "https://github.com/kindafax/kindafax.github.io/blob/main/source/{0}",
}

html_theme_options = {
    "page_layout": "default",
    "logo_target": "/",
    "accent_color": "blue",
    "globaltoc_expand_depth": 1,
    
    "show_ai_links": False,

    "github_url": "https://github.com/kindafax",
    "gitlab_url": "https://gitlab.com/kindafax",

    "nav_links": [
        {
            "title": "About",
            "url": "https://itsdanjc.com"
        },
        {
            "title": "Server",
            "url": "server/index"
        },
        {
	        "title": "Clients",
            "children": [
                {
                    "title": "Recept Printer",
                    "url": "docs/client/printer/index",
                    "summary": "Use a receipt printer to receive messages."
                },
                {
                    "title": "Web Client",
                    "url": "docs/client/web/index",
                    "summary": "Connect to a KindaFax Server from anywhere."
                },
            ]
        },
        # {
        #     "title": "Open Web Client",
        #     "url": "/web/",
        #     "external": True
        # },
    ]
}
