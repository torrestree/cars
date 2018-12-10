from odoo import api, fields, models

class Car(models.Model):
    _name='cars.car'
    _description='车辆信息'
    
    name=fields.Char(string='车辆名称')