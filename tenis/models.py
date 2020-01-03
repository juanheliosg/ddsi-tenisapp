from django.db import models

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

class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'

class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.PROTECT, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.PROTECT)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'

class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.PROTECT)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)

class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.PROTECT)
    permission = models.ForeignKey('AuthPermission', models.PROTECT)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.PROTECT)
    group = models.ForeignKey(AuthGroup, models.PROTECT)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.PROTECT)
    permission = models.ForeignKey(AuthPermission, models.PROTECT)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)
