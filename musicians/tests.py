from django.test import TestCase
from musicians.models import Musician

class MusicianTestCase(TestCase):
    def setUp(self):
        Musician.objects.create(first_name="Amadeus", last_name="Mozart", instrument="Violin")
        Musician.objects.create(first_name="Ludwig", last_name="van Beethoven", instrument="Piano")

    def test_musicians_can_play(self):
        """Musicians that can play are correctly identified"""
        amadeus = Musician.objects.get(first_name="Amadeus")
        ludwig = Musician.objects.get(first_name="Ludwig")
        self.assertEqual(amadeus.play(), 'Amadeus Mozart plays Violin')
        self.assertEqual(ludwig.play(), 'Ludwig van Beethoven plays Piano')