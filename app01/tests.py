import re

from django.test import TestCase

# Create your tests here.


start = '2022-03-23'
end = '2033-03-24'

print(re.search(r'-\d{1,2}-', start))
