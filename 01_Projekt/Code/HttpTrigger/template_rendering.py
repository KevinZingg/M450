from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory='templates/')

def render_template(template_name, request, context=None):
    if context is None:
        context = {}
    context['request'] = request
    return templates.TemplateResponse(template_name, context)
