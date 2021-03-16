from django.forms.widgets import ClearableFileInput


class CustomClearableFileInput(ClearableFileInput):

    clear_checkbox_label = ("Remove")
    initial_text = ("Current Item Image")
    input_text = ("")
    template_name = "stock/widget_template/custom_file_input.html"
