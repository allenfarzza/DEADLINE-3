from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.karyawan)
admin.site.register(models.pembelian)
admin.site.register(models.penjualan)
admin.site.register(models.produk)
admin.site.register(models.detailpembelian)
admin.site.register(models.detailpenjualan)