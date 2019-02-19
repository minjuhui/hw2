from django.contrib import admin
from django.urls import path, include
import blog.views
import portfolio.views
import account.views
# media 사용
from django.conf import settings
from django.conf.urls.static import static 



# path를 추가했다고 해서 무조건 템플릿을 만들어야 하는 것은 아님 단지 함수실행
urlpatterns = [
    path('portfolio/',portfolio.views.portfolio, name='portfolio'),
    path('',blog.views.home, name='home'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('account/', include('account.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
