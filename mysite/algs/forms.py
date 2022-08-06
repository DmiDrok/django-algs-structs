from django import forms

from algs.models import Note


class AddNoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget = forms.TextInput(attrs={'placeholder': 'О пользе алгоритма...'})
        self.fields['content'].widget = forms.Textarea(attrs={'cols': 30, 'rows': 10, 'placeholder': 'Содержимое заметки'})

    class Meta:
        model = Note
        fields = ['name', 'type', 'content']