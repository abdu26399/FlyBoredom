from testimonials.models import Testimonial

class testimonialForm(form.ModelForm):
    class Meta:
        model = Testimonial
        fields = '__all__'