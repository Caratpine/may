from config import DevConfig
from pprint import pprint
from flask.views import View
from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object(DevConfig)


def count_substring(string, sub):
    return string.count(sub)

app.jinja_env.filters['count_substring'] = count_substring


class GenericView(View):
    methods = ['GET', 'POST']

    def __init__(self, template):
        self.template = template

    def dispatch_request(self):
        return render_template(self.template)


app.add_url_rule(
    '/test', view_func=GenericView.as_view(
        'test', template='test.html'
        )
    )


if __name__ == '__main__':
    pprint(res)
