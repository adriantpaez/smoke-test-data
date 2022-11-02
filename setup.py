import sys
import os
from jinja2 import Template

def prometheus_config(out, nodes_data):
    generate("./prometheus/prometheus.yml.j2",nodes_data,f"{out}/prometheus/prometheus.yml")

def grafana_datasources(out, nodes_data):
    generate("./grafana/datasources/loki.yml.j2", nodes_data, f"{out}/grafana/datasources/loki.yml")

def generate(template_path, data, out):
    with open(template_path) as f:
        tmpl:Template = Template(f.read())
    render = tmpl.render(data)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as out:
        out.write(render)

if __name__ == "__main__":
    out = sys.argv[1]
    labels = sys.argv[2].split(',')
    ips = sys.argv[3].split(',')
    execution_clients = sys.argv[4].split(',')
    beacon_clients = sys.argv[5].split(',')

    nodes_data = list(zip(labels, ips, execution_clients, beacon_clients))
    prometheus_config(out,{'nodes_data': nodes_data})
    grafana_datasources(out,{'nodes_data': nodes_data})
