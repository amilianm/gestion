# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
# Generated by the Odoo plugin for Dia !
from openerp import api, fields, models

class ubc_continentes(models.Model):
    """Tabla de Ubicación de los Continentes"""
    _name = 'ubc_continentes'
    _rec_name = 'nombre'
    codigo = fields.Char('Código INE', size=12, required=True, help='Código INE')
    nombre = fields.Char('Nombre del Continente', size=120, required=True, help='Nombre del Continente')
    descripcion = fields.Char('Descripción del Continente', size=120, required=True, help='Descripción del Continente')
    _sql_constraints = [
        #('che_codigo', 'unique(codigo)', 'El Código del Continente ya se encuetra Registrado !'),
        #('che_nombre', 'unique(nombre)', 'El Nombre del Continente ya se encuetra Registrado !'),
    ]

class ubc_paises(models.Model):
    """Tabla Paises de Procedecia"""
    _name = 'ubc_paises'
    _rec_name = 'nombre'
    continente_id = fields.Many2one('ubc_continentes', 'Nombre del  Continente', required=True, help='Nombre del Continente')
    codigo = fields.Char('Código INE', size=12, required=True, help='Código INE')
    nombre = fields.Char('Nombre del País', size=120, required=True, help='Nombre del País')
    descripcion = fields.Char('Descripción', size=120, required=True, help='Descripción de su Ubicación según Continente')
    _sql_constraints = [
        #('che_codigo', 'unique(codigo)', 'El Código del País ya se encuetra Registrado !'),
        #('che_nombre', 'unique(nombre)', 'El Nombre del País ya se encuetra Registrado !'),
    ]

class ubc_estados(models.Model):
    """Tabla Estados"""
    _name = 'ubc_estados'
    _rec_name = 'nombre'
    pais_id = fields.Many2one('ubc_paises', 'Nombre del País', required=True, help='Nombre del País')
    nombre = fields.Char('Nombre del Estado', size=120, required=True, help='Nombre del Estado')
    abreviatura = fields.Char('Abreviatura', size=12, required=True, help='Abreviatura del Estado proporcionada por el INE')
    capital = fields.Char('Capital del Estado', size=120, required=True, help='Capital del Estado')
    poblacion = fields.Integer('Población', size=12, required=True, help='Estimación del la Población para 2016')
    latitud = fields.Char('Latitud', size=12, required=True, help='Coordenadas Geográficas Latitud')
    longitud = fields.Char('Longitud', size=12, required=True, help='Coordenadas Geográficas Longitud')
    horario = fields.Char('Zona Horaria', size=12, required=True, help='Zona Horaria')
    _sql_constraints = [
        #('che_abrevi', 'unique(abreviatura)', 'La Abreviatura del Estado ya se encuetra Registrada !'),
        #('che_nombre', 'unique(nombre)', 'El Nombre del Estado ya se encuetra Registrado !'),
    ]

class ubc_municipios(models.Model):
    """Tabla Municipios"""
    _name = 'ubc_municipios'
    _rec_name = 'nombre'
    estado_id = fields.Many2one('ubc_estados', 'Nombre del Estado', required=True, help='Nombre del Estado')
    codigo = fields.Char('Código INE', size=12, required=True, help='Código del Municipio proporcionado por INE')
    nombre = fields.Char('Nombre del Municipio', size=120, required=True, help='Nombre del Municipio')
    ciudad = fields.Char('Ciudad', size=120, required=True, help='Nombre de la Ciudad')
    _sql_constraints = [
        #('che_codigo', 'unique(codigo)', 'El Código del Municipio ya se encuetra Registrado !'),
        #('che_nombre', 'unique(nombre)', 'El Nombre del Municipio ya se encuetra Registrado !'),
    ]

class ubc_parroquias(models.Model):
    """Tabla Parroquias"""
    _name = 'ubc_parroquias'
    _rec_name = 'nombre'
    municipio_id = fields.Many2one('ubc_municipios', 'Nombre del Municipio', required=True, help='Nombre del Municipio')
    codigo = fields.Char('Código INE', size=12, required=True, help='Código de la Parroquia proporcionado por INE')
    nombre = fields.Char('Nombre de la Parroquia', size=120, required=True, help='Nombre de la Parroquia')
    ciudad = fields.Char('Ciudad', size=120, required=True, help='Nombre de la Ciudad')
    _sql_constraints = [
        #('che_codigo', 'unique(codigo)', 'El Código de la Parroquia ya se encuetra Registrado !'),
        #('che_nombre', 'unique(nombre)', 'El Nombre de la Parroquia ya se encuetra Registrado !'),
    ]