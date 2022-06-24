from odoo import models, fields

class jurusan_kuliah(models.Model):
    _name = 'jurusan.kuliah'

    name = fields.Char(string="Name")
    tanggal = fields.Date(string="Tanggal")
    status = fields.Selection([('draft','Draft'),('to_approve','To Approve'),('approved','Approved'),('done','Done')])