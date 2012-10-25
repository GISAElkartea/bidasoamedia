from markdown import markdown
from adminfiles.utils import render_uploads


def markup_filter(markup, **kwargs):
    return markdown(render_uploads(markup), **kwargs)


class AjaxMixin(object):
    def get_context_data(self, *args, **kwargs):
        context = super(AjaxMixin, self).get_context_data(*args, **kwargs)
        if self.request.is_ajax():
            context['base'] = 'ajax_base.yammy'
        else:
            context['base'] = 'base.yammy'
        return context
