# Template renderer utility
from jinja2 import Environment
from jinja2 import FileSystemLoader
from pathlib import Path


# Get the absolute path to templates directory
templates_dir = Path(__file__).parent.parent / "templates"

env = Environment(
    loader=FileSystemLoader(str(templates_dir))
)


def render_html(template_name: str, data: dict):

    template = env.get_template(template_name)

    return template.render(**data)