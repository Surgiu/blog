import os
import sys
sys.path.append(os.path.abspath('plugins'))
#import sphinx_rtd_theme

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Surgiu's Blog"
copyright = '2024, Surgiu Han'
author = 'Surgiu Han'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [

]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
#html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_theme_options = {
    'canonical_url': '',
    'analytics_id': 'G-EVD5Z6G6NH',
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'None',
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': -1,
}

html_static_path = ['_static']

myst_heading_anchors = 3
