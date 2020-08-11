from django.contrib import admin

from .models import BuchiMdl


# Register your models here.

class BuchiMdlAdmin(admin.ModelAdmin):
    fields = [
        'fld_Char'
        ,'fld_Text'
        ,'fld_URL'
        ,'fld_Email'
        ,'fld_Slug'
        ,'fld_FilePath'
        ,'fld_GenericIPAddress'
        ,'fld_Integer'
        ,'fld_SmallInteger'
        ,'fld_PositiveInteger'
        ,'fld_PositiveSmallInteger'
        ,'fld_BigInteger'
        ,'fld_Decimal'
        ,'fld_Float'
        ,'fld_Date'
        ,'fld_DateTime'
        ,'fld_Time'
        ,'fld_Duration'
        #,'fld_Binary'
        ,'fld_File'
        ,'fld_Boolean'
        ,'fld_NullBoolean']


admin.site.register(BuchiMdl,BuchiMdlAdmin)
