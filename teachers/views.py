from django.shortcuts import render
from django.core.files.storage import default_storage
from .models import Teacher

def teacher_profile_page(request):
   id = int(request.GET.get('id'))
   teacher = Teacher.objects.get(id=id)

   check_image = default_storage.exists(str(teacher.profile_picture))
   if check_image == False:
      teacher.profile_picture = 'no-image.png'
   
   context = {'teacher': teacher}
   return render(request, 'teachers/profile_page.html', context)
