import attr
import random
import string

@attr.s
class Roll:
  int_min = attr.ib(default=0)
  int_max = attr.ib(default=255)
  chars = attr.ib(default=string.ascii_letters)
  strlen = attr.ib(default=8)

  def __int__(self):
    return random.randint(self.int_min, self.int_max)

  def __float__(self):
    return random.random()

  def __bool__(self):
    return random.randint(0, 1) == 1

  def __str__(self):
    return ''.join(random.choice(self.chars) for _ in range(self.strlen))
