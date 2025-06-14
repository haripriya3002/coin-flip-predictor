
import streamlit as st
from predictor import CoinFlipPredictor
from flip_history import get_history_display

# Initialize session state
if 'predictor' not in st.session_state:
    st.session_state.predictor = CoinFlipPredictor()

st.title("🪙 Coin Flip Predictor")

st.write("Predicts the next coin flip (Heads or Tails) based on the previous flip.")

# Show history
st.subheader("Flip History")
st.info(get_history_display(st.session_state.predictor.get_history()))

# Predict next outcome
if st.button("Predict Next Flip"):
    prediction = st.session_state.predictor.predict_next()
    st.success(f"Predicted: **{prediction}**")

# Flip coin
if st.button("Flip the Coin"):
    actual = st.session_state.predictor.flip_coin()
    st.warning(f"Actual Flip Result: **{actual}**")

# Reset
if st.button("Reset History"):
    st.session_state.predictor = CoinFlipPredictor()
    st.success("History cleared.")
