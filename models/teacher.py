from odoo import models, fields, _

class Teacher(models.Model):
    _name = 'teacher.teacher'

    name = fields.Char(string="Name")
    tanggal = fields.Date(string="Tanggal Masuk")
    status = fields.Selection([('komputer','Komputer'),('bisnis','Bisnis'),('seni','Seni')])