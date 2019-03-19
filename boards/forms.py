from django import forms
from .models import Board

class BoardForm(forms.Form):
    title = forms.CharField(label='제목', max_length=10,
                            error_messages={'required' : '제목을 반드시 입력해주세요.'})
    content = forms.CharField(label='내용',
                            error_messages = {'required' : '내용을 반드시 입력해주세요.'},
                            widget=forms.Textarea(attrs={
                                    'placeholder' : '내용을 입력해줘~~',
                                    'class' : 'input-box'
                                    })
                            )
    