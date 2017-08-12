# -*- coding:utf-8 -*-

from __future__ import unicode_literals
from django.contrib.auth.models import User

from datetime import datetime
from decimal import Decimal

from django.db import models



STATUS = [
    ('warnings', 'Urgent'),
    ('accept', 'Accepted'),
    ('active', 'Suspend'),
    ('decision', 'Customers decision'),
    ('wait', 'Waiting for spare parts'),
    ('info', 'In progress'),
    ('done', 'Done'),
    ('success', 'Customer informed'),
    ('closed', 'Closed'),
]

REPAIRS = [
    ('nochoice', 'doesnt choose'),
    ('warranty', 'Warranty'),
    ('laptop', 'Laptop'),
    ('monitor', 'Monitor'),
    ('tab', 'Tab'),
    ('phone', 'Phone'),
    ('other', 'Other'),
]

SENDING = [
    ('Not', 'No'),
    ('PHOTORVICE', 'PHOTORVICE'),
    ('PHOTORVICE_REPORT', 'PHOTORVICE_REPORT'),
    ('ASSISTANT', 'ASSISTANT'),
    ]

SOURCE = [
    ('Not', 'No'),
    ('NET', 'Internet'),
    ('TRANSPORT', 'Street advertising'),
    ('ADVISE', 'Advise'),
    ('SHOP', 'Partner'),
    ]

class Kvant(models.Model):
    class Meta(object):
        ordering = ['-date_now']
        verbose_name = u"Order"
        verbose_name_plural = u"Orders"


    status = models.CharField(
        max_length=256,
        choices=STATUS,
        default='accept',
        verbose_name=u"status")

    customer = models.ForeignKey('Customer',

                                 blank=True,
                                 null=True,
                                 verbose_name=u"Customer")

    date_now = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        blank=False,
        verbose_name=u"Date")

    date_close = models.DateTimeField(
        auto_now_add=False,
        blank=True,
        null=True,
        verbose_name=u"Closing date")


    is_warranty = models.BooleanField(
        default= False,
        choices=((True, 'warranty'), (False, 'no warranty')),
        verbose_name=u"warranty"
    )

    to_send = models.CharField(
        max_length=256,
        default='Not',
        blank=True,
        null=True,
        choices=SENDING,
        verbose_name=u"Shipping"
    )

    brand = models.CharField(
        max_length=256,
        blank=False,
        null=True,
        verbose_name=u"Brand")

    model_item = models.CharField(
        max_length=256,
        blank=True,
        null=True,
        verbose_name=u"Model")

    serial_number = models.CharField(
        max_length=256,
        blank=True,
        null=True,
        verbose_name=u"Serial number")

    reason = models.CharField(
        max_length=256,
        blank=True,
        null=True,
        verbose_name=u"Issue")

    look = models.CharField(
        max_length=256,
        blank=True,
        null=True,
        verbose_name=u"Appirience")

    warranty_start = models.DateField(
        auto_now=False,
        blank=True,
        null = True,
        verbose_name=u"Warranty start")


    additional = models.CharField(
        max_length=256,
        blank=True,
        null=True,
        verbose_name=u"Additional")


    source = models.CharField(
        max_length=256,
        blank=False,
        null=True,
        choices=SOURCE,
        verbose_name=u"Advertising"
    )

    engineer = models.ForeignKey('Engineer',blank=True, null=True, verbose_name=u"Engineer")

    cost_repair = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        default=0,
        blank=True,
        null=True,
        verbose_name=u"Repair cost")

    pay_engineer = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        default=0,
        blank=True,
        null=True,
        verbose_name=u"Engineer salary")


    is_paid = models.BooleanField(default=False,
                                  choices=((True, 'Yes'), (False, 'No')),
                                  verbose_name=u"Paid")


    notes = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=u"Notes")

    photo = models.ImageField(
        blank=True,
        verbose_name=u"Photo",
        null=True)

    def __unicode__(self):
        return u"%s %s" % (self.pk, self.customer)

    def close_order(self):
        self.date_close = datetime.now()
        self.status = 'closed'

    def send_order(self):
        self.status = 'wait'



class Customer(models.Model):
    class Meta(object):
        ordering = ['contact_name']
        verbose_name = u"Customer"
        verbose_name_plural = u"Customers"

    contact_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Name and surname")

    phone = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Phone number")

    email = models.EmailField(
        blank=True,
        verbose_name=u"E-mail")

    adress = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=u"Address")

    notes = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=u"Notes")

    def __unicode__(self):
        return u"%s %s" % (self.contact_name, self.phone)


class Engineer(models.Model):
    class Meta(object):
        verbose_name = u"Engineer"
        verbose_name_plural = u"Engineers"

    name = models.ForeignKey(User)

    nickname = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=u"Name")

    surname = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=u"Surname")

    def __unicode__(self):
        return u"%s %s" % (self.nickname, self.surname)


class Balance(models.Model):

    class Meta(object):
        verbose_name = u"Сashbox"
        verbose_name_plural = u"Сashboxes"

    name = models.CharField(
        default='Main',
        max_length=256,
        blank=True,
        verbose_name=u"Назва")

    current_balance = models.DecimalField(verbose_name=u"Сashbox", max_digits=9, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __unicode__(self):
        return u"%s %s" % (self.name, self.current_balance)

    def balance_credit(self, credit):

        if credit < 0:
            raise ValueError('Invalid amount')

        self.credit=-credit,
        self.current_balance -= credit
        self.save()

    def balance_debit(self, debit):

        if debit < 0:
            raise ValueError('Invalid amount')

        self.current_balance += debit
        self.save()

class Transaction(models.Model):

    class Meta(object):
        verbose_name = u"Transaction"
        verbose_name_plural = u"Transactions"
        ordering = ['-created_at']

    balance = models.ForeignKey(Balance, default='Main')
    debit = models.DecimalField(verbose_name=u"Entrance", max_digits=9, decimal_places=2, default=0, blank=True)
    credit = models.DecimalField(verbose_name=u"expenses", max_digits=9, decimal_places=2, default=0, blank=True)
    created_at = models.DateField(auto_now_add=True, null=True)
    order_number = models.ForeignKey(Kvant, verbose_name=u"Order", blank=True, null=True)
    agent = models.ForeignKey(Customer, verbose_name=u"Customer", blank=True, null=True)
    notes = models.CharField(verbose_name=u"Notes", max_length=256, blank=True)

    def __unicode__(self):
        return u"%s %s" % (self.id, self.created_at)


class KindRepair(models.Model):

    class Meta(object):
        verbose_name = u"Kind Repair"
        verbose_name_plural = u"Kind Repair"
        ordering = ['item']

    item = models.CharField(
        max_length=256,
        choices=REPAIRS,
        default='nochoice',
        verbose_name=u"technics")
    name = models.CharField(verbose_name=u"Name", max_length=256, blank=True)
    paid_customer = models.DecimalField(verbose_name=u"expansives jobs", max_digits=9, decimal_places=2, default=0, blank=True)
    paid_engineer = models.DecimalField(verbose_name=u"engineer paid", max_digits=9, decimal_places=2, default=0, blank=True)



    def __unicode__(self):
        return u"%s %s %s" % (self.get_item_display(), self.name, self.paid_customer)

class SalaryReport(models.Model):

    class Meta(object):
        verbose_name = u"engineer report"
        verbose_name_plural = u"engineer reports"

    item = models.ForeignKey(KindRepair, verbose_name=u"Kind Repair", blank=False)
    engineer = models.ForeignKey(Engineer, blank=False, verbose_name=u"engineer")
    repair = models.ForeignKey(Kvant, blank=False, verbose_name=u"Order")
    part = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=u"Spare part")
    is_paid = models.BooleanField(default=False,
                                  choices=((False, 'No'), (True, 'Yes')),
                                  verbose_name=u"Paid")
    repair_cost = models.DecimalField(verbose_name=u"expansives jobs", max_digits=9, decimal_places=2, default=0, blank=True)
    paid_engineer = models.DecimalField(verbose_name=u"engineer paid", max_digits=9, decimal_places=2, default=0,
                                        blank=True)
    paid_date = models.DateTimeField(
        auto_now_add=False,
        blank=True,
        null=True,
        verbose_name=u"Date paid")


    def __unicode__(self):
        return u"%s %s" % (self.repair, self.item)

