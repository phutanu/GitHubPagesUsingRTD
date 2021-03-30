# -- Project information -----------------------------------------------------

project = 'niveristand-manual'
copyright = '2021, National Instruments'
author = 'National Instruments'

# The short X.Y version
version = '0.1'
# The full version, including alpha/beta/rc tags
release = '0.1.0 beta'

# source_suffix = ['.rst', '.md']
source_suffix = ['.md']

# The master toctree document.
master_doc = 'index'

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'sphinx_rtd_theme'

# We need MyST parser in Sphinx in order to parse .md files.
extensions = ['recommonmark']
