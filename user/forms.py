from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label="Kullanıcı Adı")
    password = forms.CharField(
        max_length=20, label="Parola", widget=forms.PasswordInput)
    confirm = forms.CharField(
        max_length=20, label="Parola Doğrula", widget=forms.PasswordInput)

    def clean(self):  # override ediyoruz form içindeki clean fonksiyonunu
        # formdan gelen username değerini alıyoruz
        username = self.cleaned_data.get("username")
        # formdan gelen password değerini alıyoruz
        password = self.cleaned_data.get("password")
        # formdan gelen confirm değerini alıyoruz
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError(
                "Parolalar Eşleşmiyor!")  # hata mesajı veriyoruz

            values = {
                "username": username,
                "password": password
            }
            return values


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label="Kullanıcı Adı")
    password = forms.CharField(
        max_length=20, label="Parola", widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if not username:
            raise forms.ValidationError("Kullanıcı Adı Boş Geçilemez!")

        if not password:
            raise forms.ValidationError("Parola Boş Geçilemez!")

        values = {
            "username": username,
            "password": password
        }
        return values
