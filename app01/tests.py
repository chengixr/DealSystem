import datetime
import re
import time
from time import localtime
from django.test import TestCase

# Create your tests here.
from django.utils import timezone

start = '2022-03-23'
end = '2033-03-24'

print(re.search(r'-\d{1,2}-', start))

i = 1
print(type(time.localtime()))
