from django.shortcuts import render, redirect
from . import models

# Create your views here.
def dataproduk(request):
    allprodukobj = models.produk.objects.all()
    getprodukobj = models.produk.objects.get(idproduk=1)
    filterprodukobj = models.produk.objects.filter(namaproduk = 'Whiskas')

    return render (request, 'dataproduk.html' ,{
        'allprodukobj' : allprodukobj,
        'getprodukobj' : getprodukobj,
        'filterprodukobj' : filterprodukobj
    })

def createproduk(request):
    if request.method == "GET":
        return render(request, 'createproduk.html')
    else:
        jumlahstok = request.POST['jumlahstok']
        nama = request.POST['nama']
        satuan = request.POST['satuan']
        harga = request.POST['harga']
        kategori = request.POST['kategori']

        newproduk = models.produk(
            jumlahstok = jumlahstok,
            namaproduk = nama,
            satuanproduk = satuan,
            hargaproduk = harga,
            kategoriproduk = kategori
        )
        newproduk.save()
        return redirect('dataproduk')

def updateproduk(request, id):
    produkobj = models.produk.objects.get(idproduk = 1)
    if request.method == "GET":
        return render(request, 'updateproduk.html' ,{
            'allprodukobj' : produkobj
        })
    else:
        produkobj.jumlahstok = request.POST['jumlahstok']
        produkobj.namaproduk = request.POST['nama']
        produkobj.satuanproduk = request.POST['satuan']
        produkobj.hargaproduk = request.POST['harga']
        produkobj.kategoriproduk = request.POST['kategori']
        produkobj.save()
    
        return redirect('dataproduk')