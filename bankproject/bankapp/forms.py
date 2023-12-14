from django import forms

class AccountForm(forms.Form):
    name = forms.CharField(label='Name', required=True)
    date_of_birth = forms.DateField(label='Date of Birth', required=True)
    age = forms.IntegerField(label='Age', required=True)
    gender = forms.CharField(label='Gender', required=True)
    phone_number = forms.IntegerField(label='Phone Number', required=True)
    email = forms.EmailField(label='Email', required=True)
    address = forms.CharField(label='Address', required=True)
    district = forms.ChoiceField(choices=[('Alappuzha', 'Alappuzha'), ('Ernakulam', 'Ernakulam'), ('Kollam', 'Kollam'),
                                         ('Kozhikode', 'Kozhikode'), ('Thiruvananthapuram', 'Thiruvananthapuram')],
                                label='District', required=True)
    city = forms.CharField(label='City', required=True)
    account_type = forms.ChoiceField(choices=[('savings', 'Savings Account'), ('current', 'Current Account'),
                                             ('credit', 'Credit Account')],
                                    label='Account Type', widget=forms.RadioSelect, required=True)
    materials_provide = forms.ChoiceField(choices=[('debit_card', 'Debit Card'), ('credit_card', 'Credit Card'),
                                                  ('cheque', 'Cheque')],
                                         label='Materials Provide', widget=forms.RadioSelect, required=True)
