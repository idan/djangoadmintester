from django.contrib import admin
from .models import (FieldTest, Manufacturer, Car, Pizza, Topping, Author, Book,
                     Composer, Song)

admin.site.register(FieldTest, admin.ModelAdmin)
admin.site.register(Manufacturer, admin.ModelAdmin)
admin.site.register(Car, admin.ModelAdmin)
admin.site.register(Pizza, admin.ModelAdmin)
admin.site.register(Topping, admin.ModelAdmin)


class BookInline(admin.TabularInline):
    model = Book


class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInline]
admin.site.register(Author, AuthorAdmin)


class SongInline(admin.StackedInline):
    model = Song


class ComposerAdmin(admin.ModelAdmin):
    inlines = [SongInline]
admin.site.register(Composer, ComposerAdmin)
