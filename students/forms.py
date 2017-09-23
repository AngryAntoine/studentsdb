# -*- coding: utf-8 -*-

from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(label=u'Ваша Е-мейл адреса')
    subject = forms.CharField(max_length=128, label=u'Заголовок листа')
    message = forms.CharField(max_length=2560, widget=forms.Textarea, label=u'Текст повідомлення')

    def __unicode__(self):
        return '%s' % self.from_email
