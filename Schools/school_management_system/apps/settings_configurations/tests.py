from django.test import TestCase
from .models import SystemSetting

class SystemSettingModelTest(TestCase):
    def setUp(self):
        SystemSetting.objects.create(key='site_name', value='My School')
        SystemSetting.objects.create(key='site_email', value='info@myschool.com')

    def test_system_setting_creation(self):
        setting = SystemSetting.objects.get(key='site_name')
        self.assertEqual(setting.value, 'My School')

    def test_system_setting_update(self):
        setting = SystemSetting.objects.get(key='site_email')
        setting.value = 'contact@myschool.com'
        setting.save()
        updated_setting = SystemSetting.objects.get(key='site_email')
        self.assertEqual(updated_setting.value, 'contact@myschool.com')

    def test_system_setting_deletion(self):
        setting = SystemSetting.objects.get(key='site_name')
        setting.delete()
        with self.assertRaises(SystemSetting.DoesNotExist):
            SystemSetting.objects.get(key='site_name')