class Milk: #! parent cls
    def __init__(m,colour,state):
        m.colour=colour
        m.state=state
    def form(f):
        return f'Milk is {f.colour} colour and {f.state} states'
    
class Ghee(Milk): #! child cls of Milk, parent cls of Butter
    def __init__(g,colour,state,converted):
        super().__init__(colour,state)
        g.colour=colour
        g.state=state
        g.converted=converted
    def form_ghee(fg):
        return f'Ghee is {fg.colour} colour and {fg.state} states and converted from {fg.converted} to Ghee'

class Butter(Ghee): #! child cls of Ghee cls
    def __init__(b,colour, state, converted, process):
        super().__init__(colour, state, converted)
        b.colour=colour
        b.state=state
        b.converted=converted
        b.process=process
    def form_butter(fb):
        return f'Butter is {fb.colour} colour and {fb.state} states and converted from {fb.converted} to Butter, {fb.process} step processes'
    
class Cow(Butter,Ghee,Milk):
    def __init__(c,colour,state,converted,process,breed):
        super().__init__(colour,state,converted,process)
        c.colour=colour
        c.breed=breed
    def Animal(a):
        return f'Cow is {a.colour} colour and {a.breed} breed animal' 
    
x=Milk('white','Liquid')
print(x.form())   
y=Ghee('yellow','solid-liquid','milk')
print(y.form_ghee())
z=Butter('white','soft-solid','ghee',2)
print(z.form_butter())
s=Cow('black-white combination','','','','sahiwal')
print(s.Animal())  

