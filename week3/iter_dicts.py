state_capitals = {"Washington": "Olympia", "Oregon": "Salem", "California":"Sacremento"}

for state in state_capitals:
    print(state)

""" for state in state_capitals.values():
    print(state) """

""" for state in state_capitals:
    print(state_capitals[state],"is the capital of", state)  """

for state,city in state_capitals.items():
    print(city,"is the capital of", state) 