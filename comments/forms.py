from django import forms
from .models import Comment, Reply


class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        label='comment', 
        widget=forms.Textarea(
            attrs={'rows':'1','cols':'70','placeholder': 'Write a Comment...', 'class':'comment-form-class'}
        )
    )
    class Meta:
        model = Comment
        exclude = ('likes_count', 'dislikes_count', 'content_type', 'object_id', 'content_object')


class ReplyForm(forms.ModelForm):

    """Author: Aly Yakan"""
    comment = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Reply
        exclude = ('likes_count', 'parent_comment')