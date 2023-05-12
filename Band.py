import pytest

class Musician:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f'My name is {self.name} and I play {self.get_instrument()}'
    
    def __repr__(self):
        return f'{self.__class__.__name__} instance. Name = {self.name}'

    def get_instrument(self):
        pass
    
    def play_solo(self):
        pass


class Guitarist(Musician):
    def get_instrument(self):
        return 'guitar'
    
    def play_solo(self):
        return 'face melting guitar solo'


class Bassist(Musician):
    def get_instrument(self):
        return 'bass'
    
    def play_solo(self):
        return 'bom bom buh bom'


class Drummer(Musician):
    def get_instrument(self):
        return 'drums'
    
    def play_solo(self):
        return 'rattle boom crash'


class Band:
    instances = []

    def __init__(self, name, members=[]):
        self.name = name
        self.members = members if members is not [] else []
        self.__class__.instances.append(self)

    def play_solos(self):
        solos = []
        for member in self.members:
            print(f'Hello {member},Are you want to play a Solo?')
            solos.append(member.play_solo())
        return solos

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Band instance. Name = {self.name}'

    @classmethod
    def to_list(cls):
        return cls.instances
