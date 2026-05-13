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
# html_logo = "/favicon.ico"

html_theme_options = {
    "page_layout": "default",
    "logo_target": "/",
    "accent_color": "blue",
    "globaltoc_expand_depth": 1,

    "github_url": "https://github.com/itsdanjc/kindafax",
    "gitlab_url": "https://gitlab.com/itsdanjc/kindafax",

    "nav_links": [
        {
            "title": "About",
            "url": "/index"
        },
        # {
	    #     "title": "Docs",
        #     "url": "/docs/index",
        #     "children": [
        #         {
        #             "title": "Client",
        #             "url": "client/index",
        #             "summary": "Documentation for the KindaFax client software"
        #         },
        #         {
        #             "title": "Server",
        #             "url": "server/index",
        #             "summary": "Documentation for the KindaFax server software"
        #         },
        #         {
        #             "title": "Common Library",
        #             "url": "common/index",
        #             "summary": "Documentation for the KindaFax common library"
        #         },
        #     ]
        # },
        # {
        #     "title": "About",
        #     "url": "/index"
        # },
    ]
}
