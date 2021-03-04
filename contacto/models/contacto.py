from odoo import models, fields, api
class contacto(models.Model):
	_name  = 'prueba_contacto'
	nombre = fields.Char('Nombre', required=True)
	correo  = fields.Char('Correo', required=True)