# csp

domain = ['Red','Blue','Green']

variables = ['WA','NT','SA','Q','NSW','V','T']

neighbours = {
    'WA' : ['NT','SA'],
    'NT' : ['WA','Q','SA'],
    'SA' : ['WA','NT','Q','NSW','V'],
    'Q' : ['NT','SA','NSW'],
    'NSW' : ['Q','SA','V'],
    'V' : ['NSW','SA'],
    'T' : []
    }

color_state = {}

def promising(state,color):
    for neighbour in neighbours.get(state):
        color_neighbour = color_state.get(neighbour)
        if color_neighbour == color:
            return False
    return True

def get_color(state):
    for color in domain:
        if promising(state,color):
            return color

def main():
    for state in variables:
        color_state[state] = get_color(state)
    print(color_state)

main()
        
