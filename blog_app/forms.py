from django import forms

class CommentForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"id": "username","type":"username", "class": "from-control input-lg", "required": "required", "tabindex": "1"}), max_length=50, error_messages={"required": "username required",})
    email = forms.EmailField(widget=forms.TextInput(attrs={"id": "email", "type": "email", "class": "from-control input-lg", "tabindex": "2"}),max_length=50, required=False)
    url = forms.URLField(widget=forms.TextInput(attrs={"id": "url", "type": "url", "class": "from-control input-lg", "tabindex": "3"}),max_length=100, required=False)
    comment = forms.CharField(widget=forms.Textarea(attrs={"id": "comment", "type":"comment", "class": "from-control input-lg","rows":"6","required": "required", "tabindex": "4"}),error_messages={"required": "comment required",})
    article = forms.CharField(widget=forms.HiddenInput())
