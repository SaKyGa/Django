from django import forms
from posts.models import Category, Post, Tag

class PostForm(forms.ModelForm):
    image = forms.ImageField()
    title = forms.CharField()
    content = forms.CharField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")
        if (title and content) and (title.lower() == content.lower()):
            raise forms.ValidationError("title and content don't should be same!")
        return cleaned_data
    
    def clean_title(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        if title and title.lower() == "python":
            raise forms.ValidationError("title should not be python")
        return title



class PostForm2(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["image", "title", "content", "category", "tags"]



class SearchForm(forms.Form):
    search_q = forms.CharField(required=False)
    category_id = forms.ModelChoiceField(
        queryset=Category.objects.all(), required=False
    )
    orderings = (
        ("title", "По названию"),
        ("-title", "По названию (обратный)"),
        ("created_at", "По дате создания"),
        ("-created_at", "По дате создания (обратный)"),
        ("rate", "По рейтингу"),
        ("-rate", "По рейтингу (обратный)"),
        ("updated_at", "По дате обновления"),
        ("-updated_at", "По дате обновления (обратный)"),
        (None, None),
    )
    ordering = forms.ChoiceField(
        choices=orderings,
        required=False,
    )