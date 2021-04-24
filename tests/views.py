from django.forms import inlineformset_factory, modelformset_factory
from django.views.generic import CreateView

from formset.mixins import FormsetMixin, ModelFormsetMixin, InlineFormsetMixin
from tests.models import Brand, Car


class BrandInlineCreateView(InlineFormsetMixin, CreateView):
    model = Brand
    template_name = 'tests/brand_form.html'
    formset_class = inlineformset_factory(
        Brand,
        Car,
        fields='__all__',
        extra=1
    )
    fields = '__all__'


class BrandModelCreateView(ModelFormsetMixin, CreateView):
    model = Brand
    template_name = 'tests/brand_form.html'
    formset_class = modelformset_factory(
        Car,
        fields='__all__',
        extra=1
    )
    fields = '__all__'
