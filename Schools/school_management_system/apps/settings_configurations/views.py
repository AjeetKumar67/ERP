from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import SystemSetting

@login_required
def settings_dashboard(request):
    settings = SystemSetting.objects.all()
    return render(request, 'settings_configurations/dashboard.html', {'settings': settings})

@login_required
def update_setting(request, setting_id):
    setting = SystemSetting.objects.get(id=setting_id)
    if request.method == 'POST':
        setting.value = request.POST.get('value')
        setting.save()
        return redirect('settings_dashboard')
    return render(request, 'settings_configurations/update_setting.html', {'setting': setting})