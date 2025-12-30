from odoo import api, fields, models


class ActivityType(models.Model):
    _name = 'activity.type'
    _description = 'Tipos de actividad'

    name = fields.Char(string='Nombre de la actividad', required=True)

