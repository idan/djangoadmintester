from django.db import models


class FieldTest(models.Model):
    m_CharField = models.CharField("CharField", max_length=50)
    m_BooleanField = models.BooleanField("BooleanField")
    m_NullBooleanField = models.NullBooleanField("NullBooleanField")
    m_TextField = models.TextField("TextField")
    m_TextField_Optional = models.TextField("TextField (Optional)", null=True, blank=True)
    m_EmailField = models.EmailField("EmailField")
    m_DecimalField = models.DecimalField("DecimalField", max_digits=10, decimal_places=2)
    m_FloatField = models.FloatField("FloatField")
    m_IntegerField = models.IntegerField("InteerField")
    m_PositiveIntegerField = models.PositiveIntegerField("PositiveIntegerField")
    m_PositiveSmallIntegerField = models.PositiveSmallIntegerField("PositiveSmallIntegerField")
    m_IPAddressField = models.IPAddressField("IPAddressField")
    m_URLField = models.URLField("URLField")
    m_DateField = models.DateField("DateField")
    m_TimeField = models.TimeField("TimeField")
    m_DateTime = models.DateTimeField("DateTime")

    def __unicode__(self):
        return self.m_CharField


class Manufacturer(models.Model):
    """ For testing FKs. """
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Car(models.Model):
    """ For testing FKs. """
    name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(Manufacturer, related_name='cars')

    def __unicode__(self):
        return self.name


class Pizza(models.Model):
    """ For testing m2m """

    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Topping(models.Model):
    """ For testing m2m """
    name = models.CharField(max_length=50)
    pizzas = models.ManyToManyField(Pizza, related_name='toppings')

    def __unicode__(self):
        return self.name


class Author(models.Model):
    """ For testing stacked inlines """
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, related_name='books')

    def __unicode__(self):
        return self.title


class Composer(models.Model):
    """ For testing tabular inliens """
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=50)
    composer = models.ForeignKey(Composer, related_name='songs')

    def __unicode__(self):
        return self.title
