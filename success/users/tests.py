from django.test import TestCase
#from todo.models import Todo

from users.models import User


class TestModel (TestCase):

    def test_should_create_user(self):
        user=User.objects.create_user(username='username', email='email@app.com')
        user.set_password('password12345')
        user.save()

        self.assertEqual(str(user), 'email@app.com')
    






