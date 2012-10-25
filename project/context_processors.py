def ajax_template(request):
    if request.is_ajax():
        return {'base': 'ajax_base.yammy'}
    else:
        return {'base': 'base.yammy' }
