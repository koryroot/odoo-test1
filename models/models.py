# -*- coding: utf-8 -*-

from typing import Text
from odoo import fields,models

class TestModel(models.Model):
    _name = "test.model"
    _description = "Test Model"

    name = fields.Char()
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float()
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    # garden_orientation = fields.selection(
    #     # string = 'Type',
    #     selection = [('norte','Norte'),('sur','Sur'),('este','Este'),('oeste','Oeste')]
    #     # help = "Is used to choose a region"##
    # )


class wendry_module(models.Model):
    _name = 'wendry_module.wendry_module'
    _description = 'wendry_module.wendry_module'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
