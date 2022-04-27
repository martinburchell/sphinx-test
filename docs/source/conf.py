from typing import Any

from sphinx.application import Sphinx
from sphinx.ext.autodoc import Options

extensions = [
    "sphinx.ext.autodoc",
]

source_suffix = ".rst"
master_doc = "index"


def skip(
    app: Sphinx,
    what: str,
    name: str,
    obj: Any,
    would_skip: bool,
    options: Options,
) -> bool:
    # Called by sphinx.ext.autodoc.Documenter.filter_members (q.v.).
    if name == "__init__":
        return False
    return would_skip


def setup(app: Sphinx) -> None:
    # Don't skip __init__
    app.connect("autodoc-skip-member", skip)
