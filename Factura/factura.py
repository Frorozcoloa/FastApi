import pdfkit 
from jinja2 import Environment, FileSystemLoader
from uuid import uuid4 as uuid

env = Environment(loader=FileSystemLoader("template"))
template = env.get_template('factura.html')

def create_pdf(datos):
    global template
    id = str(uuid())
    datos['id'] = id
    html = template.render(datos)
    config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
    pdfkit.from_string(html, f'facturas/{id}.pdf', configuration=config)


if __name__ == '__main__':
    datos = {'placa':'YCP39E', 'fecha_in':'2013', 'fecha_out':'2014', 'total':'1000000'}
    create_pdf(datos)
