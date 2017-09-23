# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render

from ..forms import ContactForm
from studentsdb.settings import ADMIN_EMAIL


def contact_admin(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        # ADMIN_EMAIL = 'antongramenko@gmail.com'
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']

            try:
                send_mail(subject, message, from_email, [ADMIN_EMAIL])
            except Exception:
                message = u'Під час відправки листа виникла непередбачувана помилка. Спробуйте пізніше.'
            else:
                message = u'Повідомлення успішно надіслано!'
            return HttpResponseRedirect(u'%s?status_message=%s' % (reverse('students:contact_admin'), message))
    else:
        form = ContactForm()
    return render(request, 'students/contact_admin_form.html', locals())
