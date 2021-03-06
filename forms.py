from django import forms
from post.models import Comment,BlogPost

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['username','email','body']
        
class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title','images','created_on','published','content']
        

class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()