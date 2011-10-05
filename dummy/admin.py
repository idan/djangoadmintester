from django.contrib import admin
from .models import (FieldTest, FKParent, FKChild, M2MParent, M2MChild,
                     StackedInlineTest, StackedInlineChild,
                     TabularInlineTest, TabularInlineChild)

admin.site.register(FieldTest, admin.ModelAdmin)
admin.site.register(FKParent, admin.ModelAdmin)
admin.site.register(FKChild, admin.ModelAdmin)
admin.site.register(M2MParent, admin.ModelAdmin)
admin.site.register(M2MChild, admin.ModelAdmin)


class StackedChild(admin.StackedInline):
    model = StackedInlineChild


class StackedAdmin(admin.ModelAdmin):
    inlines = [StackedChild]
admin.site.register(StackedInlineTest, StackedAdmin)


class TabularChild(admin.TabularInline):
    model = TabularInlineChild


class TabularAdmin(admin.ModelAdmin):
    inlines = [TabularChild]
admin.site.register(TabularInlineTest, TabularAdmin)
