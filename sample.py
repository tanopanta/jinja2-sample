from jinja2 import Template
template = Template('Hello {{name}}')
result = template.render(name='Jinja2')
print(result) # 'Hello Jinja2'