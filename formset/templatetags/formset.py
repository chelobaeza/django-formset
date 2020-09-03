from django import template


register = template.Library()


@register.inclusion_tag('formset/formset.html')
def formset(*args, **kwargs):
    base = {
        'static': True,
    }
    if args:
        kwargs['formset'] = args[0]
    base.update(kwargs)
    return base


@register.filter
def exclude_delete_field(form):
    DELETE_FIELD = 'DELETE'
    if DELETE_FIELD not in form.fields:
        return form
    else:
        fields = []
        for field in form:
            if field.name is not DELETE_FIELD:
                fields.append(field)
        return fields
