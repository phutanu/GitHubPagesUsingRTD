# At top on conf.py (with other import statements)
import recommonmark
from recommonmark.transform import AutoStructify

# -- Project information -----------------------------------------------------

project = 'niveristand-manual'
copyright = '2021, National Instruments'
author = 'National Instruments'

# The short X.Y version
version = '0.2'
# The full version, including alpha/beta/rc tags
release = '0.2.0 beta'

# source_suffix = ['.rst', '.md']
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown'
}

# The master toctree document.
master_doc = 'index'

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'sphinx_rtd_theme'
html_theme = 'press'

# We need MyST parser in Sphinx in order to parse .md files.
extensions = [
    'recommonmark'
             ]

# At the bottom of conf.py
def setup(app):
    app.add_config_value('recommonmark_config', {
            'url_resolver': lambda url: github_doc_root + url,
            'auto_toc_tree_section': 'Contents',
            }, True)
    app.add_transform(AutoStructify)
