/* Algoritmos para agregar y eliminar filas de un formset

Recordar usar {{ nombreformset.management_form }} dentro de la tabla y antes de las filas
Tambien se necesita que los botones tengan la clase add-form-row.

Se pueden tener muchas tablas con su respectivo management_form y con los mismos
botones (misma clase)
*/


/*Recibe un elemento en lugar de un id, sirve para identificar un elemento
de un formset, pasando this.previousElementSibling o similar, se logra obtener
el id del elemento combobox relacionado al boton de popup*/


(function($) {
    
    function popitupElement(url,elem,size) {
        var newwindow=window.open(url,elem.id,size);
        window.callParent = function (func,args){
            window[func].apply(null,args);
        };
        if (window.focus) {newwindow.focus();}
        return false;
    }
    
    function updateElementIndex(el, prefix, ndx) {
        var id_regex = new RegExp('(' + prefix + '-\\d+)');
        var replacement = prefix + '-' + ndx;
        if ($(el).attr("for")) $(el).attr("for", $(el).attr("for").replace(id_regex, replacement));
        if (el.id) el.id = el.id.replace(id_regex, replacement);
        if (el.name) el.name = el.name.replace(id_regex, replacement);
    }
    function cloneMore(elem,add_form_row) {
        var table = $(elem).closest('table');
        table=table[0];
        var formset_mngnt = $("#"+table.id+" input[id*='TOTAL_FORMS']");
        var prefix = formset_mngnt[0].id.split('id_')[1].split('-TOTAL_FORMS')[0];
        var selector = '#'+table.id + ' tr:last';
        var newElement = $(selector).clone(true);
        var total = parseInt(formset_mngnt.val());//$('#id_' + prefix + '-TOTAL_FORMS').val();
        newElement.find(':input, a').each(function() {
            var name = $(this).attr('name');
            if (name){
                name = name.replace('-' + (total-1) + '-', '-' + total + '-');
                var id = 'id_' + name;
                $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
            }
        });
        total++;
        formset_mngnt.val(total);
        $(selector).after(newElement);
        var conditionRow = $('#'+table.id+' .formsetRow:not(:last)');
        conditionRow.find('.btn.'+add_form_row)
        .removeClass(add_form_row).addClass('remove-form-row')
        .html('<span class="deletelink" aria-hidden="true"></span>');
        return false;
    }
    function deleteForm(elem) {
        var table = elem.closest('table');
        var formset_mngnt = $("#"+table.id+" input[id*='TOTAL_FORMS']");
        var btn = $(elem);
        var total = parseInt(formset_mngnt.val());
        if (total > 1){
            btn.closest('.formsetRow').remove();
            var forms = $('#'+table.id+' .formsetRow');
            formset_mngnt.val(forms.length);
            var prefix = formset_mngnt[0].id.split('id_')[1].split('-TOTAL_FORMS')[0];
            for (var i=0, formCount=forms.length; i<formCount; i++) {
                $(forms.get(i)).find(':input').each(function() {
                    updateElementIndex(this, prefix, i);
                });
            }
        }
        return false;
    }
    $(document).on('click', '.add-form-row', function(e){
        e.preventDefault();
        cloneMore(this, 'add-form-row');
        return false;
    });
    $(document).on('click', '.remove-form-row', function(e){
        e.preventDefault();
        deleteForm(this);
        return false;
    });

})(django.jQuery);