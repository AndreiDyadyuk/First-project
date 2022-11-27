from django import forms



class Comment(forms.Form) :

    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class":"size-form-name"}))
    comment = forms.CharField(widget=forms.TextInput(attrs={"class":"size-form"}))
    required_css_class = 'required'
