from django.core.exceptions import ImproperlyConfigured


class FormsetMixin:
    formset_class = None

    def get_context_data(self, **kwargs):
        if 'formset' not in kwargs:
            kwargs['formset'] = self.get_formset()
        return super().get_context_data(**kwargs)

    def get_formset(self, *args, **kwargs):
        formset_class = self.get_formset_class()
        formset = formset_class(
            *args,
            **kwargs,
            **self.get_formset_kwargs(),
            instance=self.object
        )
        return formset

    def get_formset_class(self):
        if not self.formset_class:
            raise ImproperlyConfigured(
                'formset_class attribute is missing.'
            )
        return self.formset_class

    def get_formset_kwargs(self):
        return {}

    def formset_invalid(self, formset):
        return self.render_to_response(self.get_context_data(formset=formset))

    def formset_valid(self, formset):
        self.objects = formset.save()

    def post(self, request, *args, **kwargs):
        response = super().post(request)
        formset = self.get_formset(request.POST)
        if formset.is_valid():
            self.formset_valid(formset)
            return response
        else:
            return self.formset_invalid(formset)
