from odoo import models, fields, _

class WaliMurid(models.Model):
    _name = 'wali.murid'

    name = fields.Char(string="Name")
    tanggal = fields.Date(string="Tanggal Masuk")
    status = fields.Selection([('komputer','Komputer'),('bisnis','Bisnis'),('seni','Seni')])