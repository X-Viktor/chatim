from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    """Форма для авторизации."""

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        for field_name in ['username', 'password']:
            self.fields[field_name].widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ('username', 'password')
