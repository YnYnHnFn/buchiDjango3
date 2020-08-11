from django.db import models
from django.conf import settings

# Create your models here.

class BuchiMdl(models.Model):
	#fld_Auto                 = models.AutoField(  )
	#fld_BigAuto              = models.BigAutoField(  )
	#fld_SmallAuto            = models.SmallAutoField(  )
	#fld_UUID                 = models.UUIDField( 'Universally Unique Identifier' )

	fld_Char                 = models.CharField ( max_length=10 )
	fld_Text                 = models.TextField (  )
	fld_URL                  = models.URLField  ( max_length=200 )
	fld_Email                = models.EmailField( max_length=254 )
	fld_Slug                 = models.SlugField ( max_length=50 )
	fld_FilePath             = models.FilePathField( path=settings.LOCAL_FILE_DIR )
	fld_GenericIPAddress     = models.GenericIPAddressField( protocol='IPv4', unpack_ipv4=False ,null=True)

	fld_Integer              = models.IntegerField(  )
	fld_SmallInteger         = models.SmallIntegerField(  )
	fld_PositiveInteger      = models.PositiveIntegerField(  )
	fld_PositiveSmallInteger = models.PositiveSmallIntegerField(  )
	fld_BigInteger           = models.BigIntegerField( )
	fld_Decimal              = models.DecimalField( max_digits=6, decimal_places=3 )
	fld_Float                = models.FloatField(  )

	fld_Date                 = models.DateField    ( auto_now=False, auto_now_add=False )
	fld_DateTime             = models.DateTimeField( auto_now=False, auto_now_add=False )
	fld_Time                 = models.TimeField    ( auto_now=False, auto_now_add=False )
	fld_Duration             = models.DurationField( 'holds the time period',null=True )

	fld_Binary               = models.BinaryField( null=True )
	fld_File                 = models.FileField( 'File upload fields',null=True,upload_to=settings.LOCAL_FILE_DIR, max_length=100 )
	#fld_Image                = models.ImageField( 'Image upload fields',upload_to=settings.LOCAL_FILE_DIR, max_length=100 )

	fld_Boolean              = models.BooleanField(  )
	fld_NullBoolean          = models.NullBooleanField(  )

	def __str__(self):
		return self.fld_Char
