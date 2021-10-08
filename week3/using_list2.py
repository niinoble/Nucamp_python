
states = [ "Washington", "Oregon", "California"]

'''for state in states:
    state= state.lower()
    print(state)

print("Washington" in states)
print("Tennessee" in states)
print("Washington" not in states)
states2 = ["Arizona", "Ohio", "Louisianna"]
best_states = states + states2

print(best_states)
print(best_states[1:3])
print(best_states[:2])
print(best_states[4:])
'''



num = [0,1,2,3,4,5]
print(num[0:-1]) #prints elements from start to last element
print(num[:-1])
print(num[-7:-1]) #prints all elements starting from 1st element because there's no element beyond the provideded negative index
print(num[3:-1]) #prints all emelemnts between the 3 element and the last element(not inclusive)

