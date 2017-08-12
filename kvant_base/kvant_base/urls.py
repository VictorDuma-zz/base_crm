# -*- coding:utf-8 -*-


from django.conf.urls import patterns
from django.contrib import admin
from .settings import MEDIA_ROOT, DEBUG
from kvant_crm.views import AddCustomer, AddOrder, EditOrder, ListCustomers, PaidEngineer, ListPaid, AddSalaryReport, EditCustomer, EditSalaryReport, DeleteSalaryReport
from django.conf import settings
from django.conf.urls import include, url


urlpatterns = [

    
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^$', 'kvant_crm.views.kvant_base', name='kvant_base'),
    url(r'^assistant$', 'kvant_crm.views.assistant', name='assistant'),
    url(r'^assistant_doc$', 'kvant_crm.views.assistant_doc', name='assistant_doc'),
    url(r'^assistant_done$', 'kvant_crm.views.assistant_done', name='assistant_done'),
    url(r'^krok$', 'kvant_crm.views.krok', name='krok'),
    url(r'^krok_doc$', 'kvant_crm.views.krok_doc', name='krok_doc'),
    url(r'^photoservice$', 'kvant_crm.views.photoservice', name='photoservice'),
    url(r'^photoservice_done$', 'kvant_crm.views.photoservice_done', name='photoservice_done'),
    url(r'^photoservice_doc$', 'kvant_crm.views.photoservice_doc', name='photoservice_doc'),
    url(r'^photoservice_report$', 'kvant_crm.views.photoservice_report', name='photoservice_report'),
    url(r'^photoservice_report_doc$', 'kvant_crm.views.photoservice_report_doc', name='photoservice_report_doc'),
    url(r'^photoservice_report_done$', 'kvant_crm.views.photoservice_report_done', name='photoservice_report_done'),
    url(r'^finance$', 'kvant_crm.views.finance', name='finance'),
    url(r'^search/$', 'kvant_crm.views.search', name='search'),
    url(r'^search_customer/$', 'kvant_crm.views.search_customer',  name='search_customer'),
    url(r'^(?P<pk>\d+)/paid_engineer/$', PaidEngineer.as_view(), name='paid_engineer'),
    url(r'^(?P<pk>\d+)/copy_order/$', 'kvant_crm.views.copy_order', name='copy_order'),
    url(r'^(?P<pk>\d+)/paid_engineer_report/$', 'kvant_crm.views.paid_engineer_report', name='paid_engineer_report'),
    url(r'^paid_list/$', ListPaid.as_view(), name='paid_list'),
    url(r'^history/$', 'kvant_crm.views.history', name='history'),
    url(r'^add_order/$', AddOrder.as_view(), name='add_order'),
    url(r'^(?P<pk>\d+)/salary_report/$', AddSalaryReport.as_view(), name='salary_report'),
    url(r'^(?P<pk>\d+)/edit_salary_report/$', EditSalaryReport.as_view(), name='edit_salary_report'),
    url(r'^(?P<pk>\d+)/salary_confirm_delete/$', DeleteSalaryReport.as_view(), name='salary_confirm_delete'),
    url(r'^customer_list/$', ListCustomers.as_view(), name='customer_list'),
    url(r'^add_customer/$', AddCustomer.as_view(), name='add_customer'),
    url(r'^(?P<pk>\d+)/edit_order/$', EditOrder.as_view(), name='edit_order'),
    url(r'^(?P<pk>\d+)/edit_customer/$', EditCustomer.as_view(), name='edit_customer'),
    url(r'^finance/(?P<pk>\d+)/edit_debit/$', 'kvant_crm.views.edit_debit', name='edit_debit'),
    url(r'^finance/(?P<pk>\d+)/edit_credit/$', 'kvant_crm.views.edit_credit', name='edit_credit'),
    url(r'^finance/debit/$', 'kvant_crm.views.add_debit', name='debit'),
    url(r'^finance/credit/$', 'kvant_crm.views.add_credit', name='credit'),
    url(r'^(?P<pk>\d+)/close_order/$', 'kvant_crm.views.close_order', name='close_order'),
    url(r'^(?P<pk>\d+)/order_doc/$', 'kvant_crm.views.order_doc', name='order_doc'),
    url(r'^(?P<pk>\d+)/sticker/$', 'kvant_crm.views.sticker', name='sticker'),
    url(r'^(?P<pk>\d+)/hand_in/$', 'kvant_crm.views.hand_in', name='hand_in'),
    url(r'^finance/(?P<pk>\d+)/check_doc/$', 'kvant_crm.views.check_doc', name='check_doc'),
    url(r'^admin/', admin.site.urls),

]

if DEBUG:

    urlpatterns += patterns('',
                            url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                                'document_root': MEDIA_ROOT}))


