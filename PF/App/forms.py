from django import forms
from .models import Video, Viewer, Streamer
from django.forms.widgets import DateInput
 
class ViewerForm(forms.ModelForm):
    class Meta:
        model = Viewer
        fields = ('realname', 'surname', 'mail', 'img')


class StreamerForm(forms.ModelForm):
    class Meta:
        model = Streamer
        fields = ('username', 'mail', 'desc', 'link', 'img')

class VideoForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput(format='%d/%m/%Y'))
    class Meta:
        model = Video
        fields = ('title', 'author', 'mins', 'sec', 'date', 'link', 'gif')

