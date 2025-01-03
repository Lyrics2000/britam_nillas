
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/",include("home.urls",namespace="home"))
    # path("api/v1/onboarding/",include("onboarding.urls",namespace="onboarding")),
    # path("api/v1/client/",include("client.urls",namespace="client")),
    # path("api/v1/invest/",include("invest.urls",namespace="invest")),
    # path("api/v1/switch/",include("switch.urls",namespace="switch")),
    # path("api/v1/utils/",include("utilss.urls",namespace="utilss")),
    # path("api/v1/withdrawal/",include("withdrawal.urls",namespace="withdrawal")),
]
