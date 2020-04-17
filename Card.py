
'''
class Card:
    def __init__(self,id,surface):
        self.id = id
        self.surf = surface
        self.surf_rect = surface.get_rect()
        self.power = 10
        self.movement = 25

    def clicked(self,pos):
        x1 = pos[0]
        y1 = pos[1]

        if self.surf_rect.left <= x1 <= self.surf_rect.right and self.surf_rect.top <= y1 <= self.surf_rect.bottom:
            return True
        else:
            return False
'''

class Card:
    def __init__(self,id,surface,name,Atk,Sil,Dos,Dry,Def,For):
        self.id = id
        self.surf = surface
        self.surf_rect = surface.get_rect()
        self.power = 10
        self.movement = 25
        self.name = name
        self.Atk = Atk;
        self.Sil = Sil;
        self.Dos = Dos;
        self.Dry = Dry;
        self.Def = Def;
        self.For = For;

    def clicked(self, pos):
        x1 = pos[0]
        y1 = pos[1]

        if self.surf_rect.left <= x1 <= self.surf_rect.right and self.surf_rect.top <= y1 <= self.surf_rect.bottom:
            return True
        else:
            return False

    def get_card_id(self):
        return self.id
