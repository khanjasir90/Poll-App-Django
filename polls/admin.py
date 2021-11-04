from django.contrib import admin
from polls.models import Register
from polls.models import Poll
from polls.models import CheckVote
# Register your models here.

admin.site.register(Register)
admin.site.register(Poll)
admin.site.register(CheckVote)