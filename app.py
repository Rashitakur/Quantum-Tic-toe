import streamlit as st
import numpy as np
import pandas as pd
import math
from PIL import Image

# Title and Header
st.title("Welcome to Quantum World")
st.header("Let's play the game!!")

# Function to get a random value for computer's move
def get_random_value():
    return '|0>'  # The computer's move is '|0>'

# Validate the game status: Check if anyone has won
def validate(arr):
    # Quantum game logic validation for a winner
    psi = '∣ψ⟩'
    zero_ket = '|0>'
    one_ket = '|1>'

    flag = True
    # Check for any winning condition for 'User' (|1>)
    if arr[0, 0] == one_ket and arr[1, 1] == one_ket and arr[2, 2] == one_ket:
        st.success('User has won!!')
        flag = False
    elif arr[0, 0] == one_ket and arr[1, 1] == zero_ket and arr[2, 2] == zero_ket:
        st.success('Computer wins!')
        flag = False
    elif arr[0, 2] == one_ket and arr[1, 1] == one_ket and arr[2, 0] == one_ket:
        st.success('User has won!!!')
        flag = False

    if flag:
        # Check rows for wins
        for index in [0, 1, 2]:
            if list(arr[index]) == [zero_ket, zero_ket, zero_ket]:
                st.success('Computer wins!')
                return 0
            if list(arr[index]) == [one_ket, one_ket, one_ket]:
                st.success('User wins!!')
                return 0

        # Check columns for wins
        for index in [0, 1, 2]:
            if list(arr[:, index]) == [one_ket, one_ket, one_ket]:
                st.success('User wins!!')
                return 0
            if list(arr[:, index]) == [zero_ket, zero_ket, zero_ket]:
                st.success('Computer wins!')
                return 0

        # Check diagonals for wins
        if list(np.diagonal(arr)) == [one_ket, one_ket, one_ket]:
            st.success('User wins!!')
            return 0
        if list(np.diagonal(arr)) == [zero_ket, zero_ket, zero_ket]:
            st.success('Computer wins!')
            return 0

        # If no winner, check for a draw (all squares filled)
        if np.all(arr != psi):
            st.write("It's a draw!!")
            return 0

    return 1  # Game continues
from PIL import Image
import streamlit as st

# Open the image
img = Image.open(r"C:\Users\HP\Downloads\quantum-computing-theme-vector.jpg")

# Ensure the image has an alpha channel (RGBA)
img = img.convert("RGBA")

# Get the image data
data = img.getdata()

# Create a new list for the modified image data
new_data = []

# Loop through each pixel and adjust the transparency
for item in data:
    # Change all white (also shades of whites) pixels to be transparent
    # You can adjust the condition below to be more specific if needed
    if item[0] in range(200, 256) and item[1] in range(200, 256) and item[2] in range(200, 256):
        new_data.append((item[0], item[1], item[2], 50))  # Adjust the alpha value here (0 is fully transparent, 255 is fully opaque)
    else:
        new_data.append(item)

# Update image data with new transparency
img.putdata(new_data)

# Resize the image
img_resized = img.resize((500, 300))

# Display the image in Streamlit
st.image(img_resized)



# Main function to run the game
def main():
    menu = ["Play", "Instructions", "About"]
    option = st.sidebar.selectbox("Menu", menu)

    if option == 'Play':
        st.write("This is play")
        st.write('computer --> |0>')
        st.write("User--> |1>")
        psi = '∣ψ⟩'

        if 'board' not in st.session_state:
            st.session_state.board = np.array([[psi, psi, psi], [psi, psi, psi], [psi, psi, psi]])
            st.session_state.available_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        # Display the board
        st.dataframe(st.session_state.board)

        # User selects a move
        moves = st.selectbox('Make a move!!', st.session_state.available_moves)

        # If a valid move is selected
        if moves:
            row, col = divmod(moves - 1, 3)  # Get the row and column from the move (1-9)

            # Check if the chosen spot is available
            if st.session_state.board[row, col] == psi:
                st.session_state.board[row, col] = '|1>'  # User's move (|1>)
                user_flag = validate(st.session_state.board)  # Validate game status after user move

                if not user_flag:
                    st.session_state.available_moves.clear()  # Game over, clear available moves

                # Computer's move (random choice from remaining available moves)
                if user_flag:  # Only let the computer play if the game is still ongoing
                    comp_square = np.random.choice(st.session_state.available_moves)
                    st.session_state.available_moves.remove(comp_square)  # Remove the computer's move from available moves
                    comp_row, comp_col = divmod(comp_square - 1, 3)
                    st.session_state.board[comp_row, comp_col] = get_random_value()  # Computer's move
                    validate(st.session_state.board)  # Validate game status after computer move

    elif option == 'Instructions':
        st.subheader('Instructions')
        st.write("""
        The above board represents the initial state of the game.
        ∣ψ⟩ represents the surprise state!
        Always, the user is given the chance to make the first move.
        |0> and |1> represent the pieces chosen by the computer and user respectively.
        However, unlike the classical Tic Tac Toe, there's not a 100% probability that
        when the computer makes its move, it will result in its respective move.
        This is the Quantum effect of Quantum Superposition in Quantum Tic Tac Toe!
        """)
        
        # Display the board numbering
        board_numbering = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        st.dataframe(board_numbering)

    elif option == 'About':
        st.subheader('About')
        

        # About description
        about = """
        Created by Rashita:
        Created using: Python, Streamlit, Qiskit
        The game is built to help beginners understand Quantum Superposition (QS).
        """
        st.write(about)
        st.markdown(r'$|\psi\rangle = \alpha |0\rangle + \beta |1\rangle$')

        # Display mathematical explanation of Quantum Superposition
        st.markdown(r'''
        $|\psi\rangle = \text{Superposition state}$

        $|0\rangle = \text{Zero ket} = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$

        $|1\rangle = \text{One ket} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$

        After a measurement, superposition collapses to either $|0\rangle$ or $|1\rangle$.

        Probability of $|\psi\rangle$ collapsing to $|0\rangle$ is $|\alpha|^2$.

        Probability of $|\psi\rangle$ collapsing to $|1\rangle$ is $|\beta|^2$.

        $|\alpha|^2 + |\beta|^2 = 1$
        ''')

# Call the main function to run the app
if __name__ == "__main__":
    condition=main()
    if condition==0:
        st.subheader('Game Over!')
