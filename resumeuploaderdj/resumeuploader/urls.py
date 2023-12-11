from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
from myapp.views import ResumeAnalysisView
from myapp.views import AboutUsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('aboutus/', AboutUsView.as_view(), name='aboutus'),
    path('resume-analysis/', ResumeAnalysisView.as_view(), name='resume_analysis'),
    path('<int:pk>', views.CandidateView.as_view(), name='candidate')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
