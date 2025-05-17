# Configuration file for the Sphinx documentation builder.
#
from pygments.token import *
from pygments.lexer import RegexLexer, bygroups
from sphinx.highlighting import lexers


class TeaLexer(RegexLexer):
	name = "Tea"
	aliases = ["tea"]
	filenames = ["*.tea"]

	tokens = {
		"root": [
			(r"\b(using|private|public|func|var|return|while|for|do|end|if|else|elseif|const|int|float|double|char|string|void|long|bool|import|macro|__cdecl|__fastcall|__stdcall)\b", Keyword),
			(r"\/\/.*?$", Comment.Single),
			(r"\/\*.*?\*\/", Comment.Multiline),
			(r'"(?:\\.|[^"\\])*"', String.Double),
			(r"'\\?.'", String.Char),
			(r"([+\-*/=<>!&]|\|\|)", Operator),
			(r"-?[0-9]+\.[0-9]*f?", Number.Float),
			(r"-?[0-9]+", Number.Integer),
			(r"\b([A-Za-z_][A-Za-z0-9_]*)\s*(\()", bygroups(Name.Function, Punctuation)),
			(r"\b[A-Za-z_][A-Za-z0-9_]*\b", Name),
			(r"::", Operator),
			(r"[\(\)\{\}\[\]\,\;\.]", Punctuation),
			(r"\s+", Whitespace),
			(r".", Text),
		],
	}


lexers["tea"] = TeaLexer()

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

extensions = ["sphinx_book_theme", "sphinx_design"]
html_theme = "sphinx_book_theme"
html_static_path = ["_static"]
