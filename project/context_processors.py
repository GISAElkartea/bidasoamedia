def ajax_template(request):
    if request.is_ajax():
        return {'base': 'ajax_base.html'}
    else:
        return {'base': 'base.html' }
