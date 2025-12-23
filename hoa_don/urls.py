from django.urls import path
from . import views

app_name = 'hoa_don'

urlpatterns = [
    path('<int:dat_phong_id>/', views.chi_tiet_hoa_don, name='chi_tiet'),
]
# hoa_don/urls.py ends here