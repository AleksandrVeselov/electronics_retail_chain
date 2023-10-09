from django.contrib import admin

from retail_chain.models import Link, Product, Contacts

# регистрация моделей в админ-панели
admin.site.register(Link)
admin.site.register(Product)
admin.site.register(Contacts)
