import streamlit as st
import random

# Constants
NUM_DIGITS = 3
MAX_GUESSES = 10


def get_secret_num():
    """Returns a string of NUM_DIGITS unique random digits."""
    numbers = list("0123456789")
    random.shuffle(numbers)
    return "".join(numbers[:NUM_DIGITS])


def get_clues(guess, secret_num):
    """Returns clues for a guess."""
    if guess == secret_num:
        return "🎉 You got it!"

    clues = []
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append("Fermi")
        elif guess[i] in secret_num:
            clues.append("Pico")

    if not clues:
        return "Bagels"
    else:
        clues.sort()
        return " ".join(clues)


# Streamlit UI
st.title("🥯 Bagels - A Deductive Logic Game")

# Session state to store game variables
if "secret_num" not in st.session_state:
    st.session_state.secret_num = get_secret_num()
    st.session_state.num_guesses = 1
    st.session_state.game_over = False
    st.session_state.messages = []

st.write(f"I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.")
st.write(f"You have {MAX_GUESSES} guesses to get it.")

# Input box
if not st.session_state.game_over:
    guess = st.text_input(
        f"Guess #{st.session_state.num_guesses}:",
        max_chars=NUM_DIGITS,
        key=f"guess_{st.session_state.num_guesses}"
    )

    if st.button("Submit Guess"):
        if len(guess) == NUM_DIGITS and guess.isdecimal():
            clue = get_clues(guess, st.session_state.secret_num)
            st.session_state.messages.append(f"Your guess {guess} → {clue}")

            if guess == st.session_state.secret_num:
                st.success("🎉 You got it! The number was " + st.session_state.secret_num)
                st.session_state.game_over = True
            else:
                st.session_state.num_guesses += 1
                if st.session_state.num_guesses > MAX_GUESSES:
                    st.error("❌ You ran out of guesses! The number was " + st.session_state.secret_num)
                    st.session_state.game_over = True
        else:
            st.warning(f"Please enter exactly {NUM_DIGITS} digits.")

# Show previous messages
for msg in st.session_state.messages:
    st.write(msg)

# Play again
if st.session_state.game_over:
    if st.button("Play Again"):
        st.session_state.secret_num = get_secret_num()
        st.session_state.num_guesses = 1
        st.session_state.game_over = False
        st.session_state.messages = []
