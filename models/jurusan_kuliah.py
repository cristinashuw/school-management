from odoo import models, fields, _

class JurusanKuliah(models.Model):
    _name = 'jurusan.kuliah'

    name = fields.Char(string="Name")