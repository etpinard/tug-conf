"""Tools to style a talk."""

from IPython.display import HTML, display, YouTubeVideo, Image


def prefix(url):
    prefix = '' if url.startswith('http') else 'http://'
    return prefix + url


def simple_link(url, name=None):
    name = url if name is None else name
    url = prefix(url)
    return '<a href="%s" target="_blank">%s</a>' % (url, name)


def html_link(url, name=None):
    return HTML(simple_link(url, name))


# Utility functions
def website(url, name=None, width="800px", height="550px"):
    html = []
    if name:
        html.extend(['<div class="nb_link">',
                     simple_link(url, name),
                     '</div>'] )

    html.append('<iframe src="%s"  width="%s" height="%s">'
                % (prefix(url), width, height))
    return HTML('\n'.join(html))

# Load and publish CSS
style = HTML(open('style.css').read())

display(style)
