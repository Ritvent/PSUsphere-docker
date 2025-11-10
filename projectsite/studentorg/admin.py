from django.contrib import admin


from .models import College, Program, Organization, Student, OrgMember

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "lastname", "firstname", "middlename", "program")

    search_fields = ("lastname", "firstname",)

@admin.register(OrgMember)
class OrgMemberAdmin(admin.ModelAdmin):
    list_display = ("student", "program", "organization", "date_joined",)

    search_fields = ("student__lastname", "student__firstname",)

    def program(self, obj):
        try:
            member = Student.objects.get(id=obj.student_id)
            return member.program
        except Student.DoesNotExist:
            return None
        
@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "college", "description")   

    search_fields = ("name", "description",)

    list_filter = ("college",)

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("prog_name", "college",)

    search_fields = ("prog_name", "college",)

    list_filter = ("college",)

@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ("college_name", "created_at", "updated_at",)

    search_fields = ("college_name",)

    list_filter = ("created_at",)

