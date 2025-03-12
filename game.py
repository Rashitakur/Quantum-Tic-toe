import streamlit as st
from qiskit import QuantumCircuit
from qiskit_aer import Aer
import numpy as np


def quantum_superposition():
    circuit=QuantumCircuit(1,1)
    circuit.h(0)
    circuit.measure(0,0)
    simulator=Aer.get_backend('aer_simulator')
    result=simulator.run(circuit).result().get_counts()
    return result


def get_random_value():
    res=quantum_superposition()

    value=list(res.values())
    keys=list(res.keys())
    print(value)
    print(keys)
    random_value='|' + str(keys[np.argmax(value)]) +'>'
    print(f'this is the maximum one: {random_value}')
    random_value='|' + str(keys[np.argmin(value)]) +'>'
    print(f'this is the minimum one: {random_value}')
    return random_value



def validate(arr):
    """ 
    The Method checks if the game is finished!
    Parameters:
    arr (numpy array): The array that serves as a board.
    
    Returns:
    int: returns 0 if any of the winning conditions are satisfied by any of the players.
         Else returns 1 if the game is ongoing or a draw.
    """
    
    # Boolean value to track if a winner is found
    flag = True
    
    # Define the states for '0' and '1' (Computer and User respectively)
    zero_ket = '|0>'
    one_ket = '|1>'

    # Check diagonals for a win
    if (arr[0, 0] == one_ket and arr[1, 1] == one_ket and arr[2, 2] == one_ket):
        st.success('User has won!!')
        flag = False
    elif (arr[0, 0] == zero_ket and arr[1, 1] == zero_ket and arr[2, 2] == zero_ket):
        st.success('Computer wins')
        flag = False
    elif (arr[0, 2] == one_ket and arr[1, 1] == one_ket and arr[2, 0] == one_ket):
        st.success('User has won!!!')
        flag = False
    elif (arr[0, 2] == zero_ket and arr[1, 1] == zero_ket and arr[2, 0] == zero_ket):
        st.success('Computer wins')
        flag = False

    # Check rows for a win
    if flag:
        for index in range(3):
            if list(arr[index]) == [zero_ket, zero_ket, zero_ket]:
                st.success('Computer wins')
                return 0
            elif list(arr[index]) == [one_ket, one_ket, one_ket]:
                st.success('User has won!')
                return 0

    # Check columns for a win
    if flag:
        for index in range(3):
            if list(arr[:, index]) == [zero_ket, zero_ket, zero_ket]:
                st.success('Computer wins')
                return 0
            elif list(arr[:, index]) == [one_ket, one_ket, one_ket]:
                st.success('User has won!')
                return 0

    # Check for a draw (if there are no empty spaces)
    if np.all((arr != '∣ψ⟩')):
        st.write('It\'s a draw!')
        return 0

    # If no winner and the board is not full, the game continues
    return 1
