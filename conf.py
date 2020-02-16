import os
import datetime
from recommonmark.transform import AutoStructify

###############################################################################
# Project Configuration (Simple)
###############################################################################
project = 'Doc Template'
_abbreviation = 'doctemplate'
_description = 'Template für das Engineering Projekt'
_authors = [
  {'name': 'Fabian Hauser', 'email': 'fhauser@hsr.ch'},
  {'name': 'Farhad Mehta',  'email': 'fmehta@hsr.ch' },
]

language = 'de'

_documentation_gitlab_url = 'https://gitlab.dev.ifs.hsr.ch/fhauser/test-sphinx'  # No slash at the end!
_project_links = {
    'Task List': f'{_documentation_gitlab_url}/issues',
    'Code Repository': 'https://gitlab.dev.ifs.hsr.ch/fhauser/test-sphinx',
    'Continuous Integration': 'https://gitlab.dev.ifs.hsr.ch/fhauser/test-sphinx/pipelines',
}

###############################################################################
# Project Configuration (Details)
###############################################################################
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
#
# Note: This configuration assumes that there is a git repository and it 
# requires git to be available!
author = ', '.join(author['name'] for author in _authors)
copyright = f'{datetime.datetime.now().year} {author}'
release = os.popen('git describe --tags --long').read().strip()
version = os.popen('git describe --tags').read().strip()  # The short X.Y version.

###############################################################################
# Sphinx Configuration
###############################################################################

### General configuration #####################################################
# Keep Warnings in final document
keep_warnings = True

# Complain about really every missing reference
nitpicky = True

locale_dirs = ['_locales']

### Paths and Filenames #######################################################
# Name of the epub output file
epub_basename = project.lower().replace(' ', '')

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    '_locales',
    '_build',
    'Thumbs.db',
    '.DS_Store',
    '.env',
    'node_modules',
    'README.md',
]

###############################################################################
# Extensions
###############################################################################
# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'recommonmark',
    'sphinx_markdown_tables',
    'plantweb.directive',
    'plantweb.commonmark',
    'sphinxcontrib.rsvgconverter',
]

#### Spelling ################################################################
# NOTE: Currently, spellchecking is not well supported for the german language
#       (plurals, combined words etc. not supported).
#       As most documents are in german currently, spellchecking is not en-
#       abled by default.
if language == 'en':
    extensions.append('sphinxcontrib.spelling')
    spelling_lang = 'en_US'
    tokenizer_lang = 'en_US'  # Currently only tokenizer implemented by PyEnchant
    spelling_word_list_filename = 'dictionary.txt'
    spelling_show_suggestions = True

#### PlantUML #################################################################
plantweb_defaults = {
    'server': 'https://plantuml.dev.ifs.hsr.ch/'
}

###############################################################################
# Parsing, Rendering and HTML Output Configuration
###############################################################################
rst_epilog = f"""
.. |project| replace:: {project}
.. |project_abbreviation| replace:: {_abbreviation}
.. |project_description| replace:: {_description}
.. |author| replace:: {author}
.. |author_email| replace:: {', '.join(author['email'] for author in _authors)}
.. _author_email: mailto:{', '.join(author['email'] for author in _authors)}
"""

### HTML Theme ################################################################
# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'alabaster'
# Config options: https://alabaster.readthedocs.io/en/latest/customization.html

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_sidebars = {
    '**': [
        'about.html',
        'searchbox.html',
        'navigation.html',
        'relations.html',
        'alternative_formats.html',
        'version.html',
    ]
}

html_theme_options = {
    'description': _description,
    'page_width': '1200px',
    'sidebar_width': '300px',
    'sidebar_collapse': False,
    'fixed_sidebar': False,
    'show_powered_by': True,
    'extra_nav_links': _project_links,
}

### Theme extension ###########################################################

_tags = os.popen('git tag').read().strip().splitlines()
_branch = os.popen('git rev-parse --abbrev-ref HEAD').read().strip()
html_context = {
    'repository_url': f'{_documentation_gitlab_url}/tree/{_branch}',
    'tags': _tags,
    'tag_root_path': '_versions/',  # with trailing slash!
    'tag_root_path_relative_from_version': '../../_versions/',  # with trailing slash!
}

# We build features for all tags

if 'CI_JOB_NAME' in os.environ:
    # For the CI generated website, we manually move other formats in .gitlab-ci.yml
    html_context.update({
        'epub_url': f'_static/{epub_basename}.epub',
        'pdf_url': f'_static/{epub_basename}.pdf',
    })

###############################################################################
# Sphinx App Setup Hook
###############################################################################
def setup(app):
    app.add_config_value('recommonmark_config', {
        # 'enable_math': False,
        # 'enable_inline_math': False,
        'enable_eval_rst': True,
        # 'enable_auto_doc_ref': True,
    }, True)
    app.add_transform(AutoStructify)
