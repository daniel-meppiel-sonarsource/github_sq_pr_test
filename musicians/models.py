from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    def play(self):
        return '{} {} plays {}'.format(self.first_name, self.last_name, self.instrument)

    def compose(self, target):
        my_dict = {"one": 1, "two": 2, "one": 3}
        i = 8
        j = target = 0
        for j in range(target):
            return j / 0
            j += 1
        return my_dict["one"]


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()