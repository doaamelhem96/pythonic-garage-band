class Musician:
    
    """
        A class representing a musician.
    """
    def __init__(self, name):#Initializes a new Musician instance. Args:name (str): The name of the musician.

        self.name = name
    
    def __str__(self):#  Returns a string representation of the Musician instance.
       
       

    
        return f'My name is {self.name} and I play {self.get_instrument()}' #str: A string describing the musician's name and instrument they play.
    
    def __repr__(self):#Returns a string representation of the Musician instance.string representing the class name and the musician's name.
        
        return f'{self.__class__.__name__} instance. Name = {self.name}'

    def get_instrument(self):#Gets the instrument played by the musician.
       
        pass
    
    def play_solo(self):#This method should be implemented by subclasses to define the specific solo performance.
        
        pass
        
         


class Guitarist(Musician):
    '''A class representing a guitarist, inheriting from the Musician class.
    '''

    def get_instrument(self):#Gets the instrument played by the guitarist.
  
        return 'guitar'
    
    def play_solo(self):#  Plays a solo performance on the guitar.
        
        return 'face melting guitar solo'



class Bassist(Musician):
    '''
     A class representing a bassist, inheriting from the Musician class.
    '''

    def get_instrument(self):#Gets the instrument played by the bassist.
    
        return 'bass'
    
    def play_solo(self):# Plays a solo performance on the bass.
        
        return 'bom bom buh bom'



class Drummer(Musician):
    ''' A class representing a drummer, inheriting from the Musician class.
    '''

    def get_instrument(self):#  Gets the instrument played by the drummer.
  
        return 'drums'
    
    def play_solo(self): #Plays a solo performance on the drums.
        
       
        return 'rattle boom crash'


class Band: 
    '''
    A class representing a band.
    '''
    
    instances = []

    def __init__(self, name, members=[]):# Initializes a new Band instance.
        
       

 
        self.name = name
        self.members = members if members is not [] else []
        self.__class__.instances.append(self)

    def play_solos(self):# Plays solos for each member of the band.
        
        solos = []
        for member in self.members:
            print(f'Hello {member},Are you want to play a Solo?')
            solos.append(member.play_solo())
        return solos

    def __str__(self):#Returns a string representation of the Band instance.
        
        return self.name

    def __repr__(self):#Returns a string representation of the Band instance.
   
        return f'Band instance. Name = {self.name}'
    

    """
     Returns a list of all Band instances.

    Returns:
            list: A list containing all Band instances.
    """
   
    def to_list(cls):
        return cls.instances
