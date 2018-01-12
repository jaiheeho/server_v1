import sys
import django

from django.conf import settings

settings.configure(
	DEBUG=True,
	SECRET_KEY ='thisisthesecretkey',
	ROOT_URLCONF=__name__,
	MIDDLEWARE_CLASSES=(
		'django.middleware.common.CommonMiddleware',
		'django.middleware.csrf.CsrfViewMiddleware',
		'django.middleware.clickjacking.XFameOptionsMiddleware',
		),
	)


from django.http import HttpResponse
from django.conf.urls import url

def index(request):
	return HttpResponse("Hello Gazua!")


urlpatterns = {
	url(r'^$', index),
}

if __name__ == "__main__":
	from django.core.management import execute_from_command_line
	
	execute_from_command_line(sys.argv);

