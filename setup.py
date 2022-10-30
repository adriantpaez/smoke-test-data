import sys
from jinja2 import Template

if __name__ == "__main__":
    labels = sys.argv[1].split(',')
    ips = sys.argv[2].split(',')
    cl_consensus = sys.argv[3].split(',')

    with open('./prometheus.yml.j2') as f:
        tmpl:Template = Template(f.read())
    nodes_data = zip(labels, ips, cl_consensus)
    prometheus_config = tmpl.render(nodes_data=nodes_data)
    print(prometheus_config)
