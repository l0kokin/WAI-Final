from rest_framework import serializers
from .models import ContactInfo

class ContactInfoSerializer(serializers.ModelSerializer):
    PHONE_LABEL = 'Phone'
    EMAIL_LABEL = 'Email'
    ADDRESS_LABEL = 'Address'

    class Meta:
        model = ContactInfo
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'workingHours': instance.working_hours,
            'phone': {
                'label': self.PHONE_LABEL,
                'number': instance.phone
            },
            'email': {
                'label': self.EMAIL_LABEL,
                'address': instance.email
            },
            'address': {
                'label': self.ADDRESS_LABEL,
                'street': instance.address,
                'transportInfo': instance.transport_info
            }
        }