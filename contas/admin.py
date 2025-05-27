from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    model = User
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    
    
    list_display = ('username', 'email', 'data_de_nascimento', 'contato', 'is_staff') 
    
    list_display_links = ['email']
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)
    
    
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Informações Pessoais', {
            'fields': (
                'first_name',
                'last_name',
                'data_de_nascimento',
                'descricao_pessoal', 
                'cnpj',              
                'contato',           
            )
        }),
        ('Redes Sociais', { 
            'fields': (
                'insta',     
                'whats',    
                'linkedin',  
            )
        }),
        ('Permissões', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
    )
    
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'email',
                'password1',
                'password2',
                'data_de_nascimento',
                'descricao_pessoal', 
                'cnpj',              
                'contato',           
                'insta',             
                'whats',             
                'linkedin',          
            ),
        }),
    )

admin.site.register(User, CustomUserAdmin)