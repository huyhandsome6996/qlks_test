from django.shortcuts import render, get_object_or_404
from .models import HoaDon

def chi_tiet_hoa_don(request, dat_phong_id):
    hoa_don = get_object_or_404(HoaDon, dat_phong_id=dat_phong_id)
    return render(request, 'hoa_don/chi_tiet_hoa_don.html', {
        'hoa_don': hoa_don
    })
