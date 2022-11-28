from django import forms
from django.utils.safestring import mark_safe

from leasingapp.models import *


class Login_form(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'username_login', 'placeholder': 'Имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password_login', 'placeholder': 'Пароль'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = ""
        self.fields['password'].label = ""


class Register_form(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'username', 'placeholder': 'Имя пользователя'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'email', 'placeholder': 'Электронная почта'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password', 'placeholder': 'Пароль'}))
    repeat_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password', 'placeholder': 'Повтор пароля'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = ""
        self.fields['password'].label = ""
        self.fields['email'].label = ""
        self.fields['repeat_password'].label = ""

class Support_form(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['topic'].label = ""
        self.fields['name'].label = ""
        self.fields['phone_num'].label = ""

    topic = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'topic', 'placeholder': 'Тема запроса/продукт'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'name', 'placeholder': 'Ваше имя'}))
    phone_num = forms.CharField(widget=forms.TextInput(attrs={'class': 'phone_num', 'placeholder': 'Номер телефонаl'}))


class Change_my_username_form(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Новое имя пользователя"
        self.fields['username'].required = False

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'username'}))


class Change_my_password_form(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].label = "Новый пароль"
        self.fields['password'].required = False

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password'}))


class New_request_phys_form(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['income'].label = "Справка с места работы о доходе за последние 6 месяцев"
        self.fields['passport'].label = "Копия паспорта - страница с фото, стр. 31, 32, страницы с браком, пропиской и детьми"
        self.fields['existing_credits'].label = "Справка о текущих крединтых обязательствах"
        self.fields['leasing_object'].label = "Документ об объекте лизинга"
        self.fields['application'].label = "Заявление на заключение договора лизинга"
        self.fields['credit_report_agreement'].label = "Согласие на предоставление кредитного отчета"
        self.fields['name'].label = "Имя контакта"
        self.fields['last_name'].label = "Фамилия контакта"
        self.fields['phone_number'].label = "Номер телефона для связи"
        self.fields['work_record_book'].label = "Копия трудовой книжки"

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'last_name'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'phone_number'}))

    income = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'income', 'accept': 'application/pdf'}))
    existing_credits = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'existing_credits', 'accept': 'application/pdf'}))
    leasing_object = forms.forms.FileField(
        widget=forms.FileInput(attrs={'class': 'leasing_object', 'accept': 'application/pdf'}))

    application = forms.forms.FileField(
        widget=forms.FileInput(attrs={'class': 'application', 'accept': 'application/pdf'}))

    credit_report_agreement = forms.forms.FileField(
        widget=forms.FileInput(attrs={'class': 'credit_report_agreement', 'accept': 'application/pdf'}))

    passport = forms.forms.FileField(
        widget=forms.FileInput(attrs={'class': 'passport', 'accept': 'application/pdf'}))

    work_record_book = forms.forms.FileField(
        widget=forms.FileInput(attrs={'class': 'work_record_book', 'accept': 'application/pdf'}))

class New_request_jur_form(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['annual_financial_reporting'].label = "Годовая Финансовая отчетность, с отметкой ИМНС, за последние два (2) года"
        self.fields['bank_extract'].label = "Справка банка, в котором обслуживается Клиент"
        self.fields['leasing_object'].label = "Детальная информация об объекте лизинга"
        self.fields['application'].label = "Заявление на заключение договора лизинга"
        self.fields['chief_officer_assignment'].label = "Копия документов, подтверждающая факт назначения и полномочия генерального директора"
        self.fields['chief_officer_id'].label = "Копия паспорта генерального директора/руководителя (включая страницы с пропиской, семейным положением)"
        self.fields['debit_credit_debt'].label = "Расшифровка задолженности по кредитам, займам, лизинговым договорам на последнюю отчетную дату с указанием сроков погашения"
        self.fields['creditor_debitor_debt'].label = "Расшифровка дебиторской и кредиторской задолженности на последнюю отчетную дату в разрезе сроков образования"
        self.fields['entity_statute'].label = "Копия Устава со всеми изменениями и дополнениями"
        self.fields['equipment_list'].label = "Опись основных средств с указанием остаточной балансовой стоимости на последнюю отчетную дату"
        self.fields['interim_financial_reporting'].label = "Промежуточная Финансовая отчетность за последний отчетный период"
        self.fields['existing_credits'].label = "Копии действующих кредитных, факторинговых и лизинговых договоров"
        self.fields['license'].label = "Имеющиеся лицензии"
        self.fields['object_usage'].label = "Общая информация о компании и об использовании объекта лизинга"
        self.fields['registration'].label = "Копия свидетельства о регистрации"
        self.fields['shareholder_registration'].label = "Выписка из реестра акционеров (при наличии)"
        self.fields['tax_statement'].label = "Копия свидетельства о постановке на налоговый учет в ИМНС"
        self.fields['name'].label = "Имя контакта"
        self.fields['last_name'].label = "Фамилия контакта"
        self.fields['phone_number'].label = "Номер телефона для связи"

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'last_name'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'phone_number'}))

    annual_financial_reporting = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'annual_financial_reporting', 'accept': 'application/pdf'}))
    bank_extract = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'bank_extract', 'accept': 'application/pdf'}))
    leasing_object = forms.forms.FileField(
        widget=forms.FileInput(attrs={'class': 'leasing_object', 'accept': 'application/pdf'}))

    application = forms.forms.FileField(
        widget=forms.FileInput(attrs={'class': 'application', 'accept': 'application/pdf'}))

    chief_officer_assignment = forms.forms.FileField(
        widget=forms.FileInput(attrs={'class': 'chief_officer_assignment', 'accept': 'application/pdf'}))

    chief_officer_id = forms.forms.FileField(
        widget=forms.FileInput(attrs={'class': 'chief_officer_id', 'accept': 'application/pdf'}))

    debit_credit_debt = forms.forms.FileField(
        widget=forms.FileInput(attrs={'class': 'debit_credit_debt', 'accept': 'application/pdf'}))

    creditor_debitor_debt = forms.forms.FileField(
        widget=forms.FileInput(attrs={'class': 'creditor_debitor_debt', 'accept': 'application/pdf'}))

    entity_statute = forms.forms.FileField(
        widget=forms.FileInput(attrs={'class': 'entity_statute', 'accept': 'application/pdf'}))

    equipment_list = forms.forms.FileField(
        widget=forms.FileInput(attrs={'class': 'equipment_list', 'accept': 'application/pdf'}))

    interim_financial_reporting = forms.forms.FileField(
        widget=forms.FileInput(attrs={'class': 'interim_financial_reporting', 'accept': 'application/pdf'}))

    existing_credits = forms.forms.FileField(
        widget=forms.FileInput(attrs={'class': 'existing_credits', 'accept': 'application/pdf'}))

    license = forms.forms.FileField(
        widget=forms.FileInput(attrs={'class': 'license', 'accept': 'application/pdf'}))

    object_usage = forms.forms.FileField(
        widget=forms.FileInput(attrs={'class': 'object_usage', 'accept': 'application/pdf'}))

    registration = forms.forms.FileField(
        widget=forms.FileInput(attrs={'class': 'registration', 'accept': 'application/pdf'}))

    shareholder_registration = forms.forms.FileField(
        widget=forms.FileInput(attrs={'class': 'shareholder_registration', 'accept': 'application/pdf'}))

    tax_statement = forms.forms.FileField(
        widget=forms.FileInput(attrs={'class': 'tax_statement', 'accept': 'application/pdf'}))

class Admin_application_form(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['duration'].required = False
        self.fields['rate'].required = False
        self.fields['loan_amount'].required = False
        self.fields['regular_payment_size'].required = False
        self.fields['duration'].label = mark_safe('Срок  ')
        self.fields['rate'].label = mark_safe('<br /><br />Процентная ставка')
        self.fields['loan_amount'].label = mark_safe('<br /><br />Размер лизинга')
        self.fields['regular_payment_size'].label = mark_safe('<br /><br />Размер ежемесячного платежа')
    duration = forms.CharField(widget=forms.TextInput(attrs={'class': 'duration'}))
    rate = forms.CharField(widget=forms.TextInput(attrs={'class': 'rate'}))
    loan_amount = forms.CharField(widget=forms.TextInput(attrs={'class': 'loan_amount'}))
    regular_payment_size = forms.CharField(widget=forms.TextInput(attrs={'class': 'regular_payment_size'}))

class Admin_deed_form(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['duration'].required = False
        self.fields['rate'].required = False
        self.fields['loan_amount'].required = False
        self.fields['regular_payment_size'].required = False
        self.fields['date_signed'].required = False
        self.fields['contract'].required = False
        self.fields['duration'].label = mark_safe('Срок')
        self.fields['rate'].label = mark_safe('<br /><br />Процентная ставка')
        self.fields['loan_amount'].label = mark_safe('<br /><br />Размер лизинга')
        self.fields['regular_payment_size'].label = mark_safe('<br /><br />Размер ежемесячного платежа')
        self.fields['date_signed'].label = mark_safe('<br /><br />Дата подписания')
        self.fields['contract'].label = mark_safe('<br /><br />Документ контракта')
    duration = forms.CharField(widget=forms.TextInput(attrs={'class': 'duration'}))
    rate = forms.CharField(widget=forms.TextInput(attrs={'class': 'rate'}))
    loan_amount = forms.CharField(widget=forms.TextInput(attrs={'class': 'loan_amount'}))
    regular_payment_size = forms.CharField(widget=forms.TextInput(attrs={'class': 'regular_payment_size'}))
    contract = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'contract', 'accept': 'application/pdf'}))
    date_signed = forms.DateField(widget=forms.DateInput(attrs={'type':'date','class': 'date_signed'}))

class Best_offer_form(forms.Form):
    desired_amount = forms.CharField(widget=forms.TextInput(attrs={'class': 'desired_amount'}))
    desired_duration = forms.CharField(widget=forms.TextInput(attrs={'class': 'desired_duration'}))
