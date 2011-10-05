from django.db import models


class AllFields(models.Model):
    m_CharField = models.CharField("CharField", max_length=50)
    m_BooleanField = models.BooleanField("BooleanField")
    m_NullBooleanField = models.NullBooleanField("NullBooleanField")
    m_TextField = models.TextField("TextField")
    m_TextField_Optional = models.TextField("TextField (Optional)", null=True, blank=True)
    m_EmailField = models.EmailField("EmailField")
    m_DecimalField = models.DecimalField("DecimalField", max_digits=10, decimal_places=2)
    m_FloatField = models.FloatField("FloatField")
    m_IntegerField = models.IntegerField("IntegerField")
    m_PositiveIntegerField = models.PositiveIntegerField("PositiveIntegerField")
    m_PositiveSmallIntegerField = models.PositiveSmallIntegerField("PositiveSmallIntegerField")
    m_IPAddressField = models.IPAddressField("IPAddressField")
    m_URLField = models.URLField("URLField")
    m_DateField = models.DateField("DateField")
    m_TimeField = models.TimeField("TimeField")
    m_DateTime = models.DateTimeField("DateTime")

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.m_CharField


class FieldTest(AllFields):
    pass


class FKParent(models.Model):
    """ For testing FKs. """
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'FK Parent'
        verbose_name_plural = 'FK Parents'

    def __unicode__(self):
        return self.name


class FKChild(models.Model):
    """ For testing FKs. """
    name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(FKParent, related_name='children')

    class Meta:
        verbose_name = 'FK Child'
        verbose_name_plural = 'FK Children'

    def __unicode__(self):
        return self.name


class M2MParent(models.Model):
    """ For testing m2m """

    class Meta:
        verbose_name = 'M2M Parent'
        verbose_name_plural = 'M2M Parents'

    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class M2MChild(models.Model):
    """ For testing m2m """
    name = models.CharField(max_length=50)
    parents = models.ManyToManyField(M2MParent, related_name='children')

    class Meta:
        verbose_name = 'M2M Child'
        verbose_name_plural = 'M2M Children'

    def __unicode__(self):
        return self.name


class StackedInlineTest(models.Model):
    """ For testing stacked inlines """
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Stacked Inline Test'
        verbose_name_plural = 'Stacked Inline Tests'

    def __unicode__(self):
        return self.name


class StackedInlineChild(AllFields):
    parent = models.ForeignKey(StackedInlineTest, related_name='inlines')

    class Meta:
        verbose_name = 'Stacked Inline Child'
        verbose_name_plural = 'Stacked Inline Children'

    def __unicode__(self):
        return self.title


class TabularInlineTest(models.Model):
    """ For testing stacked inlines """
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Tabular Inline Test'
        verbose_name_plural = 'Tabular Inline Tests'

    def __unicode__(self):
        return self.name


class TabularInlineChild(AllFields):
    parent = models.ForeignKey(TabularInlineTest, related_name='inlines')

    class Meta:
        verbose_name = 'Tabular Inline Child'
        verbose_name_plural = 'Tabular Inline Children'

    def __unicode__(self):
        return self.title
