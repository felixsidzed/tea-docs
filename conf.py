# Configuration file for the Sphinx documentation builder.
#
from pygments.token import *
from pygments.lexer import RegexLexer
from sphinx.highlighting import lexers

class TeaLexer(RegexLexer):
	name = "Tea"
	aliases = ["tea"]
	filenames = ["*.tea"]

	tokens = {
		"root": [
			(r"(using|private|public|func|var|return|while|for|do|end|if|else|elseif|const|int|float|double|char|string|void|bool)", Keyword),
			(r"\/\*.*?\*\/|\/\/.*$", Comment),
			(r"([+-/*=<>!&]|\|\|)", Operator),
			(r"(-?[0-9]+|[0-9]+\.[0-9]*f?)", Number),
			(r"\b[A-Za-z_][A-Za-z0-9_]*\b", Name),
			(r"'\\?.'", String),
			(r"\".*?(?<!\\)(\\\\)*?\"", String),
			(r"\s+", Whitespace),
			(r"\S+", Text),
		],
	}

lexers["tea"] = TeaLexer()
highlight_language = "tea"

# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Tea"
copyright = "2025, felixsidzed"
author = "felixsidzed"
release = "1.0.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

extensions = ["sphinx_rtd_dark_mode"]
html_theme = "sphinx-rtd-dark-mode"
html_static_path = ["_static"]
default_dark_mode = True
