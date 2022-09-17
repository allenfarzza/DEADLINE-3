from django.db import models

# Create your models here.

class produk(models.Model):
    idproduk = models.CharField(max_length=10, primary_key=True)
    jumlahstok = models.IntegerField()
    namaproduk = models.CharField(max_length=100)
    satuanproduk = models.CharField(max_length=10)
    hargaproduk = models.IntegerField()
    kategoriproduk = models.CharField(max_length=100)

    def __str__ (self):
        return str(self.namaproduk)

class karyawan(models.Model):
    idkaryawan = models.CharField(max_length=10, primary_key=True)
    namakaryawan = models.CharField(max_length=100)
    kontakkaryawan = models.IntegerField()
    jobdesk = models.CharField(max_length=100)

    def __str__ (self):
        return str(self.idkaryawan)

class pembelian(models.Model):
    idpembelian = models.CharField(max_length=10, primary_key=True)
    idkaryawan = models.ForeignKey(karyawan, on_delete=models.CASCADE)
    tanggaltransaksi = models.DateField()
    namasupplier = models.CharField(max_length=100)

    def __str__ (self):
        return str(self.namasupplier)

class penjualan(models.Model):
    idpenjualan = models.CharField(max_length=10, primary_key=True)
    idkaryawan = models.ForeignKey(karyawan, on_delete=models.CASCADE)
    tanggalpenjualan = models.DateField()
    namapelanggan = models.CharField(max_length=100)

    def __str__ (self):
        return str(self.namapelanggan)

class detailpembelian(models.Model):
    iddetailpembelian = models.CharField(max_length=10, primary_key=True)
    idpembelian = models.ForeignKey(pembelian, on_delete=models.CASCADE)
    idproduk = models.ForeignKey(produk, on_delete=models.CASCADE)
    kuantitasproduk = models.IntegerField()

    def __str__ (self):
        return str(self.iddetailpembelian)

class detailpenjualan (models.Model):
    iddetailpenjualan = models.CharField(max_length=10, primary_key=True)
    idpenjualan = models.ForeignKey(penjualan, on_delete=models.CASCADE)
    idproduk = models.ForeignKey(produk, on_delete=models.CASCADE)
    kuantitasproduk = models.IntegerField()

    def __str__ (self):
        return str(self.iddetailpenjualan)