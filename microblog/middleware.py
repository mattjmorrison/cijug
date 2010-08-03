from django.db import connection
from django.template import Template, Context

TEMPLATE = Template(
"""
<br /><br /><hr />
<table>
{% for q in queries %}
<tr>
    <td>{{ q.time }}</td>
    <td>{{ q.sql }}</td>
</tr>
{% endfor %}
</table>
"""
)

class SqlLoggingMiddleware(object):

    def process_response(self, request, response):
        queries = [{'sql':q['sql'], 'time':q['time']} for q in connection.queries]
        response.write(TEMPLATE.render(Context({'queries':queries})))
        return response