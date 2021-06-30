from django.contrib import admin
from . models import indexregister,addcourse,contacts,allstudents,category,feedback,packagecreate,alladminuser,allinstructor,zoommeet
# Register your models here.
admin.site.register(indexregister)
admin.site.register(contacts)
admin.site.register(allstudents)
admin.site.register(zoommeet)
admin.site.register(category)
admin.site.register(packagecreate)
admin.site.register(alladminuser)
admin.site.register(allinstructor)
admin.site.register(addcourse)
admin.site.register(feedback)


