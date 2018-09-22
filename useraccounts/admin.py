from django.contrib import admin
from useraccounts.models import User, UserAccount, Trader, Funds
from store.models import Sensor_Post, Device
# Register your models here.

class UserAccountAdmin(admin.ModelAdmin):
    list_display = (["user",])

class TraderAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('fname',)}
    list_display = (["fname", "cell_leader", "fund_needed",])

class FundsAdmin(admin.ModelAdmin):
    list_display = (["trader", "amount",])

class Sensor_postAdmin(admin.ModelAdmin):
    list_display = (["device", "co_val", "ch4_val","aq_val", "h_val","sensor_time","created_at",])

class DeviceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = (["name", "location", "created_at",])

admin.site.register(UserAccount, UserAccountAdmin)
admin.site.register(Trader, TraderAdmin)
admin.site.register(Funds, FundsAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Sensor_Post, Sensor_postAdmin)