from django import forms
from .models import Post

class NewsForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'author',
            'category'
            ]

    # def clean(self):
    #     cleaned_data = super().clean()
    #     title = cleaned_data.get("title")
    #     text = cleaned_data.get("text")
    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)
        self.fields['author'].label = "Автор:"
        self.fields['category'].label = "Категория:"
        self.fields['title'].label = "Название публикации:"
        self.fields['text'].label = "Текст публикации:"