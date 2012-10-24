from markdown import markdown
from adminfiles.utils import render_uploads


def markup_filter(markup):
        return markdown(render_uploads(markup))
