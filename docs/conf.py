# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'hyperspy-bundle'
copyright = '2022, HyperSpy Community'
author = 'HyperSpy Developers'

# The full version, including alpha/beta/rc tags
release = ''


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.githubpages',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = '_static/hyperspy_logo.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = '_static/hyperspy.ico'

html_theme_options = {
    "github_url": "https://github.com/hyperspy/hyperspy-bundle",
    "icon_links": [
        {
            # Label for this link
            "name": "HyperSpy",
            # URL where the link will redirect
            "url": "https://hyperspy.org",  # required
            # Icon class (if "type": "fontawesome"), or path to local image (if "type": "local")
            "icon": "_static/hyperspy.ico",
            # The type of image to be used (see below for details)
            "type": "local",
        },
        {
            "name": "Gitter",
            "url": "https://gitter.im/hyperspy/hyperspy",
            "icon": "fab fa-gitter",
        },
        {
            # Label for this link
            "name": "Release",
            # URL where the link will redirect
            "url": "https://github.com/hyperspy/hyperspy-bundle/releases",  # required
            # Icon class (if "type": "fontawesome"), or path to local image (if "type": "local")
            "icon": "https://img.shields.io/github/v/release/hyperspy/hyperspy-bundle",
            # The type of image to be used (see below for details)
            "type": "url",
        },
    ],
    "logo": {
        "text": "HyperSpy-bundle",
    },
    "show_toc_level": 2,
    "show_nav_level": 2,
}

# If you’re hosting your documentation on ReadTheDocs, you should consider
# adding an explicit placement for their ethical advertisements. These are
# non-tracking advertisements from ethical companies, and they help
# ReadTheDocs sustain themselves and their free service.
#
# Ethical advertisements are added to your sidebar by default. To ensure
# they are there if you manually update your sidebar, ensure that the
# sidebar-ethical-ads.html template is added to your list. For example:

html_sidebars = {
    "**": ["search-field.html", "sidebar-nav-bs.html", "sidebar-ethical-ads.html"]
}

linkcheck_ignore = [
    "https://github.com/conda-forge/miniforge#Install",  # Anchor on github.com not supported
]

def setup(app):
    app.add_css_file("custom-styles.css")
