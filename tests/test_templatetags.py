from django.forms import inlineformset_factory, modelformset_factory
from django.template import Context, Template
from django.test import TestCase

from tests.models import Brand, Car
from formset.templatetags import formset as tags


class DefaultFormsetTestCase(TestCase):
    """
    Test the templatetag {% formset *args %} should render by default
    the formset passed as argument.
    """
    TEMPLATE = Template('{% load formset %}{% formset formset_object %}')

    def setUp(self):
        self.brand = Brand.objects.create(name='suzuki')
        Car.objects.create(name='swift', brand=self.brand)
        self.formset = inlineformset_factory(
            Brand,
            Car,
            fields='__all__',
            extra=1
        )

    def render_template(self, template=TEMPLATE):
        return template.render(Context({
            'formset_object': self.formset
        }))

    def test_render(self):
        html = self.render_template()
        self.assertTrue(isinstance(html, str))

    def test_has_no_table_element(self):
        html = self.render_template()
        self.assertNotIn('table', html)

    def test_load_static_javascript(self):
        html = self.render_template()
        self.assertIn('<script type="text/javascript"', html)


class FormsetWithTableTestCase(TestCase):
    """
    Test the templatetag {% formset formset_object auto_table=True table_id="cars" %} should render by default
    the formset passed as argument.
    """
    TEMPLATE = Template('{% load formset %}{% formset formset_object auto_table=True table_id="cars" %}')

    def setUp(self):
        self.brand = Brand.objects.create(name='suzuki')
        Car.objects.create(name='swift', brand=self.brand)
        self.formset = inlineformset_factory(
            Brand,
            Car,
            fields='__all__',
            extra=1
        )

    def render_template(self, template=TEMPLATE):
        return template.render(Context({
            'formset_object': self.formset
        }))

    def test_render(self):
        html = self.render_template()
        self.assertTrue(isinstance(html, str))

    def test_has_table_element(self):
        html = self.render_template()
        self.assertIn('table', html)

    def test_load_static_javascript(self):
        html = self.render_template()
        self.assertIn('<script type="text/javascript"', html)


class DefaultFormsetTestCase(TestCase):
    """
    Test the templatetag {% formset *args %} should render by default
    the formset passed as argument.
    """
    TEMPLATE = Template('{% load formset %}{% formset formset_object static=False %}')

    def setUp(self):
        self.brand = Brand.objects.create(name='suzuki')
        Car.objects.create(name='swift', brand=self.brand)
        self.formset = inlineformset_factory(
            Brand,
            Car,
            fields='__all__',
            extra=1
        )

    def render_template(self, template=TEMPLATE):
        return template.render(Context({
            'formset_object': self.formset
        }))

    def test_render(self):
        html = self.render_template()
        self.assertTrue(isinstance(html, str))

    def test_has_no_table_element(self):
        html = self.render_template()
        self.assertNotIn('table', html)

    def test_load_static_javascript(self):
        html = self.render_template()
        self.assertNotIn('<script type="text/javascript"', html)