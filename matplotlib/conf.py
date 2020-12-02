project = 'Python: Matplotlib'
author = 'Matt Harasymczuk'
email = 'book-python@astronaut.center'

language = 'en'
html_theme = 'sphinx_rtd_theme'
html_baseurl = 'https://python.astrotech.io'

todo_emit_warnings = False
todo_include_todos = True

extensions = [
    # 'sphinx.ext.autosectionlabel',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.extlinks',
    # 'sphinx.ext.graphviz',
    'sphinx.ext.mathjax',
    'sphinx.ext.todo',
    # 'sphinx.ext.viewcode',
    'sphinxcontrib.bibtex',
]

suppress_warnings = [
    # 'app.add_node',
    # 'app.add_directive',
    # 'app.add_role',
    # 'app.add_generic_role',
    # 'app.add_source_parser',
    # 'download.not_readable',
    # 'image.not_readable',
    # 'ref.term',
    # 'ref.ref',
    # 'ref.numref',
    # 'ref.keyword',
    # 'ref.option',
    # 'ref.citation',
    # 'ref.footnote',
    # 'ref.doc',
    # 'ref.python',
    # 'misc.highlighting_failure',
    # 'toc.circular',
    'toc.secnum',
    # 'epub.unknown_project_files',
    'autosectionlabel.*',
]

html_static_path = [
    '_static',
    '_data/csv',
    '_data/json',
    '_data/sas',
    '_data/sqlite3',
    '_data/xml',
    '_data/xlsx',
]

# article - For articles in scientific journals, presentations, short reports,
#           Program documentation, invitations, etc
# proc    - A class for proceedings based on the article class.
# minimal - Is as small as it can get. It only sets a page size and a base font.
#           It is mainly used for debugging purposes.
# report  - For longer reports containing several chapters, small books, thesis, etc
# book    - For real books
# slides  - For slides. The class uses big sans serif letters.
# memoir  - For changing sensibly the output of the document.
#           It is based on the book class, but you can create
#           any kind of document with it (1)
# letter  - For writing letters.
# beamer  - For writing presentations (see LaTeX/Presentations).
latex_documentclass = 'report'


# -- Standard book config -----------------------------------------------------

import os
import re
import subprocess
import sys
from datetime import date

needs_sphinx = '3.0'

imgmath_image_format = 'png'
imgmath_latex = 'latex'

# mathjax_path = '_static/mathjax.js'
mathjax_path = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js'
mathjax_config = {
    'extensions': ['tex2jax.js'],
    'jax': ['input/TeX', 'output/HTML-CSS'],
}

exclude_patterns = [
    '.*',
    'venv*',
    'virtualenv*',
    '.venv*',
    '.virtualenv*',
    '_build',
    '_extensions',
    '_img',
    '_slides',
    '_i18n',
    '_static',
    '_themes',
    '_tmp',
    '**/contrib/*',
    '**/assignments/*',
    '**/solutions/*',
    '**/_template.rst',
    '**.ipynb_checkpoints',
    'README.rst',
    'TODO.rst',
    '**/_TODO.rst',
    'Thumbs.db',
    '.DS_Store',
]

master_doc = 'index'
templates_path = ['_templates']
highlight_language = 'python3'
pygments_style = 'stata-dark'
autodoc_typehints = "description"
autosectionlabel_maxdepth = 4

sys.path.insert(0, os.path.abspath('_extensions'))

extlinks = {'isbn': ('https://e-isbn.pl/IsbnWeb/start/search.html?szukaj_fraza=%s', 'ISBN: ')}

# 0 - sequence number of image in whole document
# 1 - sequence number of image in header level 1 (only if :numbered: option is present at toctree directive)
# 2 - sequence number of image in header level 2
#       will use x.1, x.2, … if located directly under a header level 1,
#       will use 1, 2, … if at the document level
numfig_secnum_depth = 1
numfig = True
smartquotes = False
numfig_format = {
    'section': 'Section %s.',
    'figure': 'Figure %s.',
    'table': 'Table %s.',
    'code-block': 'Listing %s.'}

project_slug = re.sub(r'[\W]+', '', project)
sha1 = subprocess.run('git log -1 --format="%h"', stdout=subprocess.PIPE, shell=True, encoding='utf-8').stdout.strip()
year = date.today().year
today = date.today().strftime('%Y-%m-%d')

version = f'#{sha1}, {today}'
release = f'#{sha1}, {today}'
copyright = f'{year}, CC-BY-SA-4.0, {author} <{email}>, last update: {today}'

html_show_sphinx = False
html_use_smartypants = False
html_search_language = language
html_add_permalinks = '¶'
html_theme_path = ['_themes']
html_secnumber_suffix = '. '
html_title = project
html_favicon = '_static/favicon.png'
html_context = {}
html_copy_source = False

if html_theme == 'sphinx_rtd_theme':
    html_context.update({
        'css_files': ['_static/dark.css', '_static/print.css'],
        'script_files': ['_static/jquery.min.js', '_static/onload.js', mathjax_path]})

if html_theme == 'thesis':
    html_context.update({
        'css_files': ['_static/theme-overrides.css'],
        'script_files': [mathjax_path]})

latex_documents = [('index', f'{project_slug}.tex', project, author, latex_documentclass)]
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    'figure_align': 'H',  # 'htbp',

    # Fix for: LaTeX Backend Fails with Citations In Figure Captions
    'preamble': r"""
        \usepackage{float}
        \usepackage{etoolbox}
        \AtBeginEnvironment{figure}{\renewcommand{\phantomsection}{}}
    """}

epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright
epub_exclude_files = ['search.html']

man_pages = [
    (master_doc, project_slug, project, [author], 1)
]

texinfo_documents = [
  (master_doc, project_slug, project, author, project, '', 'Miscellaneous'),
]
