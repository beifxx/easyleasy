from django import forms
from leasingapp.models import *


class Login_form(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'username_login'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password_login'}))


class Register_form(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'email_register'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'email_register'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password_register'}))
    repeat_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password_repeat_register'}))


class Support_form(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['topic'].label = "Запрос на поддержку"
        self.fields['name'].label = "Ваше имя"
        self.fields['phone_num'].label = "Номер телефона"

    topic = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'topic', 'placeholder': 'Тема запроса/продукт'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'name'}))
    phone_num = forms.CharField(widget=forms.TextInput(attrs={'class': 'phone_num'}))


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
    duration = forms.CharField(widget=forms.TextInput(attrs={'class': 'duration'}))
    rate = forms.CharField(widget=forms.TextInput(attrs={'class': 'rate'}))
    loan_amount = forms.CharField(widget=forms.TextInput(attrs={'class': 'loan_amount'}))
    regular_payment_size = forms.CharField(widget=forms.TextInput(attrs={'class': 'regular_payment_size'}))
