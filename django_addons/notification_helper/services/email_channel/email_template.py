from django.template.loader import render_to_string
from django.utils.html import strip_tags


class EmailTemplateService:
    @staticmethod
    def render(template_path: str, context: dict):
        html_message = render_to_string(template_path, context)
        plain_message = strip_tags(html_message)

        return html_message, plain_message
