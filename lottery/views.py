from django.template.response import TemplateResponse


def main_page(request):
    return TemplateResponse(request, 'index.html', {})
