from django.db import models

#migrations serve para migrar seus objetos pythons para tabelas do BD SQL

class User(models.Model):
    # cria um campo autmatico com um valor numerico sequencial não duplicavel
    id_user = models.AutoField(primary_key=True) 
    name = models.TextField(max_length=255)
    age = models.IntegerField()

    #metodo temporiario, o certo seria filtrar dentro de views
    def save(self, *args, **kwargs):
        if User.objects.filter(name=self.name, age=self.age).exists():
            pass
        else:
            super(User, self).save(*args, **kwargs)
