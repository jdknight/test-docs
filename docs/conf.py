# -*- coding: utf-8 -*-

extensions = []

source_suffix = '.rst'

master_doc = 'contents'

project = u'test'
copyright = u'test'

version = '1.0'
release = '1.0'

exclude_patterns = ['_build']

html_theme = 'sphinx13b'
html_theme_path = ['_themes']
templates_path = ['_templates']

html_static_path = ['_static']
html_additional_pages = {'index': 'index.html'}
html_sidebars = {'index': ['indexsidebar.html', 'searchbox.html']}
