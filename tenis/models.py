from django.db import models,connection

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
        
class Tenista(models.Model):
    idtenista = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30, blank=True, null=True)
    telefono = models.CharField(unique=True, max_length=12)
    mail = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'tenista'

class Arbitro(models.Model):
    idarbitro = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30, blank=True, null=True)
    telefono = models.CharField(unique=True, max_length=12)
    mail = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'arbitro'

class Trabajador(models.Model):
    idtrabajador = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30, blank=True, null=True)
    telefono = models.CharField(unique=True, max_length=12)
    mail = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'trabajador'

class Edicion(models.Model):
    idedicion = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    fecha = models.DateField()

    class Meta:
        managed = False
        db_table = 'edicion'

class Pista(models.Model):
    idpista = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    capacidad = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'pista'

class Trabaja(models.Model):
    id = models.BigIntegerField(primary_key=True)
    idtrabajador = models.ForeignKey('Trabajador', models.PROTECT, db_column='idtrabajador', blank=True, null=True)
    idedicion = models.ForeignKey(Edicion, models.PROTECT, db_column='idedicion', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trabaja'
        unique_together = (('idtrabajador', 'idedicion'),)

class Asignado(models.Model):
    id = models.BigIntegerField(primary_key=True)
    idtrabajador = models.ForeignKey('Trabaja', models.PROTECT, db_column='idtrabajador', blank=True, null=True, related_name='trabajadores')
    idedicion = models.ForeignKey('Trabaja', models.PROTECT, db_column='idedicion', blank=True, null=True, related_name='ediciones')
    fechafin = models.DateField()
    fechaini = models.DateField()
    idpista = models.ForeignKey('Pista', models.PROTECT, db_column='idpista', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asignado'
        unique_together = (('idtrabajador', 'idedicion', 'fechafin', 'fechaini', 'idpista'),)
    
    def save(self, *args, **kwargs):
        """
        This is a complete disaster. We needed to overrided this method in order to avoid a hardcore Oracle error in the
        Database
        """
        if (self.pk is None):
            with connection.cursor() as cursor: 
                query =  "INSERT into Asignado (ID, IDTrabajador, IDEdicion, FechaFin, FechaIni, IDPista) values ({},{},{},TO_DATE(\'{}\',\'mm/dd/yyyy\'), TO_DATE(\'{}\',\'mm/dd/yyyy\'),{});".format(self.id, self.idtrabajador_id, self.idedicion_id,self.fechafin.strftime('%m/%d/%Y'),self.fechaini.strftime('%m/%d/%Y'), self.idpista.idpista); 
                cursor.execute(query)

            cursor.close()



class Tenistaedicionentrenador(models.Model):
    id = models.BigIntegerField(primary_key=True)
    idedicion = models.ForeignKey(Edicion, models.PROTECT, db_column='idedicion', blank=True, null=True)
    idtenista = models.ForeignKey(Tenista, models.PROTECT, db_column='idtenista', blank=True, null=True)
    identrenador = models.ForeignKey(Entrenador, models.PROTECT, db_column='identrenador', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tenistaedicionentrenador'
        unique_together = (('idedicion', 'idtenista'),)

            
class Partido(models.Model):
    id = models.BigIntegerField(primary_key=True)
    idpista = models.ForeignKey('Pista', models.PROTECT, db_column='idpista', blank=True, null=True)
    fecha = models.DateField()
    idarbitro = models.ForeignKey(Arbitro, models.PROTECT, db_column='idarbitro', blank=True, null=True)
    resultado = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'partido'
        unique_together = (('idpista', 'fecha'),)
    def save(self, *args, **kwargs):
        """
        This is a complete disaster. We needed to overrided this method in order to avoid a hardcore Oracle error in the
        Database
        """
        p = Partido.objects.filter(id = self.id)
        if (not p):
            with connection.cursor() as cursor: 
                query =  "INSERT into Partido (ID, Fecha, Resultado, IDPista, IDArbitro) values ({},TO_DATE(\'{}\',\'mm/dd/yyyy\'), {},{},{});".format(self.id,self.fecha.strftime('%m/%d/%Y'), self.resultado, self.idpista_id,self.idarbitro_id) 
                cursor.execute(query)
                cursor.close() 
       
        def update(self, *args, **kwargs):
            with connection.cursor() as cursor: 
                query =  "UPDATE Partido SET ID = {}, Fecha = TO_DATE(\'{}\',\'mm/dd/yyyy\'), Resultado = {}, IDPista = {}, IDArbitro = {};".format(self.id,self.fecha.strftime('%m/%d/%Y'),self.resultado, self.idpista_id,self.idarbitro_id) 
                
                cursor.execute(query)
            cursor.close()



   

            





class Compite(models.Model):
    id = models.BigIntegerField(primary_key=True)
    idpista = models.ForeignKey('Partido', models.PROTECT, db_column='idpista', blank=True, null=True, related_name='pistas')
    fecha = models.ForeignKey('Partido', models.PROTECT, db_column='fecha', related_name='fechas')
    idedicion = models.ForeignKey('Tenistaedicionentrenador', models.PROTECT, db_column='idedicion', blank=True, null=True, related_name='ediciones')
    idtenista = models.ForeignKey('Tenistaedicionentrenador', models.PROTECT, db_column='idtenista', blank=True, null=True, related_name='tenistas')

    class Meta:
        managed = False
        db_table = 'compite'
        unique_together = (('idpista', 'fecha', 'idedicion', 'idtenista'),)


class Compra(models.Model):
    idcompra = models.BigIntegerField(primary_key=True)
    idedicion = models.ForeignKey('Edicion', models.PROTECT, db_column='idedicion', blank=True, null=True)
    fecha_inicio = models.DateField()
    idusuario = models.ForeignKey('Usuario', models.PROTECT, db_column='idusuario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compra'

class Comprafinalizada(models.Model):
    idcompra = models.OneToOneField(Compra, models.PROTECT, db_column='idcompra', primary_key=True)
    idcomprafin = models.BigIntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'comprafinalizada'

class Tipodeentrada(models.Model):
    idtipo = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    precio = models.FloatField()

    class Meta:
        managed = False
        db_table = 'tipodeentrada'

class Compraentrada(models.Model):
    id = models.BigIntegerField(primary_key=True)
    idtipo = models.ForeignKey('Tipodeentrada', models.PROTECT, db_column='idtipo', blank=True, null=True)
    idcompra = models.ForeignKey(Compra, models.PROTECT, db_column='idcompra', blank=True, null=True)
    cantidad = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compraentrada'
        unique_together = (('idtipo', 'idcompra'),)


class Comprapagada(models.Model):
    idcompra = models.OneToOneField(Comprafinalizada, models.PROTECT, db_column='idcompra', primary_key=True)
    numeroticket = models.BigIntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'comprapagada'


