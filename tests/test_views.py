from django.forms import inlineformset_factory, modelformset_factory
from django.test import TestCase, RequestFactory

from tests.models import Brand, Car
from tests.views import BrandInlineCreateView, BrandModelCreateView


class FormsetMixinTestCase(TestCase):

    def setUp(self):
        self.brand = Brand.objects.create(name='suzuki')
        Car.objects.create(name='swift', brand=self.brand)

    def setup_view(self, view):
        view.object = self.brand
        request = RequestFactory().get('/')
        view.setup(request)
        return view

    def test_get_inline_formset(self):
        view = BrandInlineCreateView()
        self.setup_view(view)
        context = view.get_context_data()
        self.assertIn('formset', context)

    def test_get_model_formset(self):
        view = BrandModelCreateView()
        self.setup_view(view)
        context = view.get_context_data()
        self.assertIn('formset', context)
