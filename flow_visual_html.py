def generate_flow_html(logs):

    html = "<html><body><h2>Serializer Flow</h2><ul>"

    for log in logs:
        html += f"<li><b>{log['step']}</b> - {log.get('status')}</li>"

    html += "</ul></body></html>"

    return html