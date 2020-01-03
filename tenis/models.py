# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Arbitro(models.Model):
    idarbitro = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30, blank=True, null=True)
    telefono = models.CharField(unique=True, max_length=12)
    mail = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'arbitro'


class Asignado(models.Model):
    id = models.BigIntegerField(models.DO_NOTHING, db_column='ID', primary_key=True)
    idtrabajador = models.ForeignKey('Trabaja', models.DO_NOTHING, db_column='idtrabajador')
    idedicion = models.ForeignKey('Trabaja', models.DO_NOTHING, db_column='idedicion',related_name='edicion')
    fechafin = models.DateField()
    fechaini = models.DateField()
    idpista = models.ForeignKey('Pista', models.DO_NOTHING, db_column='idpista')

    class Meta:
        managed = False
        db_table = 'asignado'
        unique_together = (('idtrabajador', 'idedicion', 'fechafin', 'fechaini', 'idpista'),)


class Compite(models.Model):
    id = models.BigIntegerField(models.DO_NOTHING, db_column='ID', primary_key=True)
    idpista = models.OneToOneField('Partido', models.DO_NOTHING, db_column='idpista')
    fecha = models.ForeignKey('Partido', models.DO_NOTHING, db_column='fecha', related_name='fecha_compite')
    idedicion = models.ForeignKey('Tenistaedicionentrenador', models.DO_NOTHING,
    db_column='idedicion',related_name='edicion_compite')
    idtenista = models.ForeignKey('Tenistaedicionentrenador', models.DO_NOTHING, db_column='idtenista')

    class Meta:
        managed = False
        db_table = 'compite'
        unique_together = (('idpista', 'fecha', 'idedicion', 'idtenista'),)


class Compra(models.Model):
    idcompra = models.BigIntegerField(primary_key=True)
    idedicion = models.ForeignKey('Edicion', models.DO_NOTHING, db_column='idedicion', blank=True, null=True)
    fecha_inicio = models.DateField()
    idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='idusuario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compra'


class Compraentrada(models.Model):
    id = models.BigIntegerField(models.DO_NOTHING, db_column='ID', primary_key=True)
    idtipo = models.OneToOneField('Tipodeentrada', models.DO_NOTHING, db_column='idtipo')
    idcompra = models.ForeignKey(Compra, models.DO_NOTHING, db_column='idcompra')
    cantidad = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compraentrada'
        unique_together = (('idtipo', 'idcompra'),)


class Comprafinalizada(models.Model):
    idcompra = models.OneToOneField(Compra, models.DO_NOTHING, db_column='idcompra', primary_key=True)
    idcomprafin = models.BigIntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'comprafinalizada'


class Comprapagada(models.Model):
    idcompra = models.OneToOneField(Comprafinalizada, models.DO_NOTHING, db_column='idcompra', primary_key=True)
    numeroticket = models.BigIntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'comprapagada'


class Edicion(models.Model):
    idedicion = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    fecha = models.DateField()

    class Meta:
        managed = False
        db_table = 'edicion'


class Entrenador(models.Model):
    identrenador = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30, blank=True, null=True)
    telefono = models.CharField(unique=True, max_length=12)
    mail = models.CharField(unique=True, max_length=255)
    notificaciones = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entrenador'


class Partido(models.Model):
    id = models.BigIntegerField(models.DO_NOTHING, db_column='ID', primary_key=True)
    idpista = models.OneToOneField('Pista', models.DO_NOTHING, db_column='idpista')
    fecha = models.DateField()
    idarbitro = models.ForeignKey(Arbitro, models.DO_NOTHING, db_column='idarbitro', blank=True, null=True)
    resultado = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'partido'
        unique_together = (('idpista', 'fecha'),)


class Pista(models.Model):
    idpista = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    capacidad = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'pista'


class Tenista(models.Model):
    idtenista = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30, blank=True, null=True)
    telefono = models.CharField(unique=True, max_length=12)
    mail = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'tenista'


class Tenistaedicionentrenador(models.Model):
    id = models.BigIntegerField(models.DO_NOTHING, db_column='ID', primary_key=True)
    idedicion = models.OneToOneField(Edicion, models.DO_NOTHING, db_column='idedicion')
    idtenista = models.ForeignKey(Tenista, models.DO_NOTHING, db_column='idtenista')
    identrenador = models.ForeignKey(Entrenador, models.DO_NOTHING, db_column='identrenador', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tenistaedicionentrenador'
        unique_together = (('idedicion', 'idtenista'),)


class Tipodeentrada(models.Model):
    idtipo = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    precio = models.FloatField()

    class Meta:
        managed = False
        db_table = 'tipodeentrada'


class Trabaja(models.Model):
    id = models.AutoField(models.DO_NOTHING, db_column='ID', primary_key=True)
    idtrabajador = models.OneToOneField('Trabajador', models.DO_NOTHING, db_column='idtrabajador')
    idedicion = models.ForeignKey(Edicion, models.DO_NOTHING, db_column='idedicion')

    class Meta:
        managed = False
        db_table = 'trabaja'
        unique_together = (('idtrabajador', 'idedicion'),)


class Trabajador(models.Model):
    idtrabajador = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30, blank=True, null=True)
    telefono = models.CharField(unique=True, max_length=12)
    mail = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'trabajador'


class Usuario(models.Model):
    idusuario = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30, blank=True, null=True)
    mail = models.CharField(unique=True, max_length=50)
    contrasena = models.CharField(max_length=30)
    notificaciones = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'
