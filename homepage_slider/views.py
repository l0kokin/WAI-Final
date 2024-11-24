from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Slider


class SliderAPIView(APIView):
    def get(self, request):
        sliders = Slider.objects.all()
        slider_data = [
            {
                "main_heading": slider.main_heading,
                "secondary_heading": slider.secondary_heading,
                "background_image": slider.background_image,
                "logo": slider.logo,
                "overlay_text": slider.overlay_text,
            }
            for slider in sliders
        ]
        return Response(slider_data)
