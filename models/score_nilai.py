from odoo import models, fields, _

class ScoreNilai(models.Model):
    _name = 'score.nilai'

    name = fields.Char(string="Name")
    tanggal = fields.Date(string="Tanggal Masuk")
    status = fields.Selection([('komputer','Komputer'),('bisnis','Bisnis'),('seni','Seni')])