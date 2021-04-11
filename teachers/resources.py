from import_export import resources
from import_export.fields import Field
from import_export.widgets import ManyToManyWidget
from .models import Teacher,Subject

class TeacherResource(resources.ModelResource):
    first_name = Field(attribute='first_name', column_name='First Name')
    last_name = Field(attribute='last_name', column_name='Last Name')
    profile_picture = Field(attribute='profile_picture', column_name='Profile picture')
    email_address = Field(attribute='email_address', column_name='Email Address')
    phone_number = Field(attribute='phone_number', column_name='Phone Number')
    room_number = Field(attribute='room_number', column_name='Room Number')
    subjects = Field(attribute='subjects', column_name='Subjects taught', widget=ManyToManyWidget(Subject, field='name'))

    def before_import_row(self, row, **kwargs):
        new_subjects = ''
        splitted = row['Subjects taught'].split(',')

        if row['Profile picture'] != '':
            row['Profile picture'] = row['Profile picture'].upper()
        
        for s in splitted:
            subject = s.strip().capitalize()

            if subject != '':
                if subject == 'Maths':
                    subject = 'Mathematics'
                num_results = Subject.objects.filter(name= subject).count()
                if num_results < 1:
                    sub = Subject(name=subject)
                    sub.save()
            

            new_subjects += subject + ', '
    
        new_subjects = new_subjects.rstrip(',')
        row['Subjects taught'] = new_subjects


    def skip_row(self, instance, original):
        if instance.first_name  == '':
            return True
            
        return super(TeacherResource, self).skip_row(instance, original)

    class Meta:
        model = Teacher
        skip_unchanged = True
        report_skipped = True
        raise_errors = False
        import_id_fields = ('email_address',)