# from django.contrib import admin
from django.urls import path
from board.views import board
from user.views import home, signin, signup, signout, returnvalue, rentalvalue, \
    rental, position, position1, sidebar, sidebar1
from django.conf import settings
from django.conf.urls.static import static

# views한테 보내는 역할
urlpatterns = [
    path("", home, name="home"),
    path("board/", board, name="board"), 
    path("user/signin", signin, name="signin"),
    path("user/signup", signup, name="signup"),
    path("user/signout", signout, name="signout"),
    path("user/returnvalue", returnvalue, name="returnvalue"),
    path("user/rentalvalue", rentalvalue, name="rentalvalue"),
    path("user/rental", rental, name="rental"),
    path("user/position", position, name="position"),
    path("user/position1", position1, name="position1"),
    path("user/sidebar", sidebar, name="sidebar"),
    path("user/sidebar1", sidebar1, name="sidebar1"),
    path("position/", position, name="position_direct"),
]

if settings.DEBUG:  
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)