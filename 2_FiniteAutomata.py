#FiniteAutomata
automat = {
    'q0': {'a': 'q1', 'b': 'q0'}, 
    'q1': {'a': 'q1', 'b': 'q2'},  
    'q2': {'a': 'q1', 'b': 'q0'}   
}

start_state = 'q0'
accept_states = {'q2'}

def finite_automat(input_string):
    state = start_state  
    for char in input_string:
        if char in automat[state]: 
            state = automat[state][char]  
        else:
            return False  
    
    return state in accept_states  

input_string = input("Enter a string of 'a' and 'b': ")
if finite_automat(input_string):
    print("Found")
else:
    print("Not found")

#aaabbab#