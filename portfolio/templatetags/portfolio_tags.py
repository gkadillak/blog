from django.template import Template, Context
from django import template
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

register = template.Library()


def do_highlight(parser, token):
    nodelist = parser.parse(('endhighlight',))
    parser.delete_first_token()
    return HighlightNode(nodelist)


class HighlightNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        output = self.nodelist.render(context)

        formatter = HtmlFormatter(linenos=True)
        results = highlight(output, PythonLexer(stripall=True), formatter)
        return results


class RenderCustom(template.Node):

    @classmethod
    def handle_token(cls, parser, token):
        tokens = token.split_contents()
        field = tokens[1]

        return cls(parser.compile_filter(field))

    def __init__(self, field):
        self.field = field

    def render(self, context):
        render_field = self.field.resolve(context)

        render_template = Template(render_field)

        rendered = render_template.render(Context())
        return rendered

# Register the tags
register.tag('highlight', do_highlight)


@register.tag
def render_this(parser, token):
    return RenderCustom.handle_token(parser, token)
