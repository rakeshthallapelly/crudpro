from curdapp.models import Patient
from rest_framework.serializers import ModelSerializer

class PatientSerializer(ModelSerializer):
	class Meta:
		model=Patient
		fields="__all__"



 # gender = serializers.CharField(source='get_gender_display')

 