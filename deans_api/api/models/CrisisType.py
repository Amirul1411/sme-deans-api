from django.db.models import Model, CharField
from django_mysql.models import ListCharField
    
class CrisisType (Model):
	name=ListCharField(
			base_field=CharField(max_length=30),
			default=None,
			size=10,
			max_length=(10*30))
	
	def __str__(self):
		return self.name

	class Meta:
		pass