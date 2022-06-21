from odoo import models, fields

class student(models.Model):
    _name = 'student'

    name = fields.Char(string="Name")
    tanggal = fields.Date(string="Tanggal")
    status = fields.Selection([('draft','Draft'),('to_approve','To Approve'),('approved','Approved'),('done','Done')])