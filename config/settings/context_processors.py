from .base import REACT_CSS, REACT_JS


def react_files(request):
    return {
        "react_js": REACT_JS,
        "react_css": REACT_CSS
    }