from django.db import models
from django.contrib import admin

# Create your models here.



#class Item(models.Model):
#    name = models.CharField(max_length=60)
#    created = models.ForeignKey(DateTime)
#    priority = models.IntegerField(default=0)
#    difficulty = models.IntegerField(default=0)
#    done = models.BooleanField(default=False)


class PersonRole(models.Model):
    name = models.CharField(max_length=60)
    def __unicode__(self):
        return unicode(self.name)

class PersonRoleAdmin(admin.ModelAdmin):
    list_display = ["name"]


class Person(models.Model):
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)
    phone = models.CharField(max_length=10)
    work_phone = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    role = models.ForeignKey(PersonRole)
    
    def __unicode__(self):
        return unicode(self.name+" "+self.surname)


class PersonRoleInProject(models.Model):
     person = models.ForeignKey(Person)
     role = models.ForeignKey(PersonRole)

     def __unicode__(self):
        return unicode(self.person+", "+self.role)
class PersonAdmin(admin.ModelAdmin):
    list_display = ["name","surname","phone","work_phone","created"]
    search_fields = ["name","surname"]

class Location(models.Model):
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=60)
    building = models.CharField(max_length=60)
    lat = models.FloatField(default=0)
    lon = models.FloatField(default=0)

    def __unicode__(self):
        return unicode(self.street+", "+self.city+", "+self.country)

class LocationAdmin(admin.ModelAdmin):
    list_display = ["city","state","country","building","lat","lon"]
    search_fields = ["street"]

class Company(models.Model):
    name = models.CharField(max_length=60)
    location = models.ManyToManyField(Location, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    contact = models.ManyToManyField(Person, blank=True, null=True)

class CompanyAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]

class Project(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey(Company, blank=True, null=True)
    person_role =  models.ManyToManyField(PersonRoleInProject, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.title)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]

class ProjectNote(models.Model):
    text = models.CharField(max_length=600)
    #TODO: fitxers
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(blank=True, null=True)
    project = models.ForeignKey(Project)

class ProjectNoteAdmin(admin.ModelAdmin):
    list_display = ["created","text"]
    search_fields = ["created","text"]

admin.site.register(Project, ProjectAdmin)
admin.site.register(PersonRole, PersonRoleAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(ProjectNote, ProjectNoteAdmin)



