from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField


month_choices = (('January', 'January'), ('February', 'February'), ('March', 'March'),
    ('April', 'April'), ('May', 'May'), ('June', 'June'), 
    ('July', 'July'), ('August', 'August'), ('September', 'September'),
    ('October', 'October'), ('November', 'November'), ('December', 'December'))

day_choices = (('1','1'), ('2','2'), ('3','3'), ('4','4'), ('5','5'), ('6','6'),
    ('7','7'), ('8','8'), ('9','9'), ('10','10'), ('11','11'), ('12','12'), ('13','13'), ('14','14'),
    ('15','15'), ('16','16'), ('17','17'), ('18','18'), ('19','19'), ('20','20'),('21','21'),('22','22'),
    ('23','23'), ('24','24'),('25','25'),('26','26'),('27','27'),('28','28'),('29','29'),('30','30'),('31','31')
    )

year_choices = (('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025'), ('2026', '2026'),
    ('2027', '2027'), ('2028', '2028'), ('2029', '2029'), ('2030', '2030'), ('2031', '2031'))

class Customuser(AbstractUser):
    full_name = models.CharField(max_length = 35, blank= True)
    phone_number = models.CharField(max_length=11, blank=True)

    def __str__(self):
        return ('User: {} \n email: {}'.format(self.full_name, self.email))

class Devotional(models.Model):
    image = models.ImageField(blank = True, null=True, upload_to='devotional_img')
    title = models.CharField(max_length = 200, blank= True)
    date = models.DateField()
    scripture = models.TextField(max_length = 400, blank= True)
    body = RichTextField(blank=True, null=True)
    prayer = models.TextField(max_length = 500, blank= True)
    # day = models.CharField(max_length=2, choices= day_choices, null=True)
    # month = models.CharField(max_length=4, choices= month_choices, null=True)
    # year = models.CharField(max_length=4, choices= year_choices, null=True) 
    further_study = models.TextField(max_length = 1000, blank= True)



