class MetaDict(dict):
  def __getitem__(self, key):
    if key[0] != '_' and key not in self:
      print(f'pretending to have key: {key!r}')
      return key # avoid the NameError

    return super().__getitem__(key)


class Meta(type):
  def __prepare__(name, bases):
    return MetaDict()


class Real(metaclass=Meta):
  Hello, world
