from django.contrib.auth.models import User
user = User.objects.create_user('jorg', 'jorg@volg.com', 'mypassword').save()