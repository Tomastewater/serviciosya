from django.db import models

class Provincia(models.Model):
    """
    Modelo que representa una provincia de Argentina.

    Atributos:
        PROVINCIAS (list): Lista de tuplas con los códigos y nombres de las provincias.
        nombre (IntegerField): Código de la provincia, seleccionado de las opciones disponibles.
    """
    PROVINCIAS = [
        (1, 'Buenos Aires'),
        (2, 'Ciudad Autónoma de Buenos Aires'),
        (3, 'Catamarca'),
        (4, 'Chaco'),
        (5, 'Chubut'),
        (6, 'Córdoba'),
        (7, 'Corrientes'),
        (8, 'Entre Ríos'),
        (9, 'Formosa'),
        (10, 'Jujuy'),
        (11, 'La Pampa'),
        (12, 'La Rioja'),
        (13, 'Mendoza'),
        (14, 'Misiones'),
        (15, 'Neuquén'),
        (16, 'Río Negro'),
        (17, 'Salta'),
        (18, 'San Juan'),
        (19, 'San Luis'),
        (20, 'Santa Cruz'),
        (21, 'Santa Fe'),
        (22, 'Santiago del Estero'),
        (23, 'Tierra del Fuego, Antártida e Islas del Atlántico Sur'),
        (24, 'Tucumán'),
    ]

    nombre = models.IntegerField(choices=PROVINCIAS)

    def __str__(self):
        """
        Retorna el nombre legible de la provincia.
        """
        provincia_nombre = dict(self.PROVINCIAS).get(self.nombre)
        return provincia_nombre

class Localidad(models.Model):
    """
    Modelo que representa una localidad dentro de una provincia.

    Atributos:
        nombre (CharField): Nombre de la localidad.
        provincia (ForeignKey): Provincia a la que pertenece la localidad.
    """
    nombre = models.CharField(max_length=100)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)

    def __str__(self):
        """
        Retorna el nombre completo de la localidad junto con la provincia.
        """
        return f'{self.nombre}, {self.provincia.__str__()}'
    
    def localidad_completa(self):
        """
        Retorna una representación completa de la localidad y provincia.
        """
        return f'| {self.nombre} | {self.provincia.nombre} |'
    

class Direccion(models.Model):
    """
    Modelo que representa una dirección postal.

    Atributos:
        calle (TextField): Nombre de la calle.
        altura (TextField): Altura de la calle.
        departamento (CharField): Departamento o unidad (opcional).
        codigo_postal (CharField): Código postal de la dirección.
        barrio (CharField): Barrio de la dirección (opcional).
        localidad (ForeignKey): Localidad asociada a la dirección.
        usuario (ForeignKey): Usuario al que pertenece la dirección.
    """
    calle = models.TextField(max_length=200)
    altura = models.TextField(max_length=200)
    departamento = models.CharField(max_length=100, null=True, blank=True)
    codigo_postal = models.CharField(max_length=100)
    barrio = models.CharField(max_length=200, blank=True, null=True, default=None)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE, default=None)
    usuario = models.ForeignKey("usuario.Usuario", on_delete=models.CASCADE, default=None)

    def __str__(self):
        """
        Retorna una representación legible de la dirección, incluyendo calle, altura, departamento, barrio y código postal.
        """
        departamento_str = f', Departamento: {self.departamento}' if self.departamento else ''
        barrio_str = f', Barrio: {self.barrio}' if self.barrio else ''
        return f"""{self.calle} {self.altura}{departamento_str},
        {barrio_str}, CP: {self.codigo_postal}"""
    
    def direccionCompleta(self):
        """
        Retorna una representación completa de la dirección, incluyendo localidad, calle, altura y departamento.
        """
        return f"| Localidad: {self.localidad} | Calle: {self.calle} | Altura: {self.altura} | Departamento: {self.departamento} | "
