import re
import random
import string
import streamlit as st

def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(characters) for _ in range(length))

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Blacklist Common Passwords
    common_passwords = {"password", "123456", "123456789", "qwerty", "password123", "admin", "letmein"}
    if password.lower() in common_passwords:
        return "❌ Weak Password - Too common. Choose a more unique password."
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    # Strength Rating
    if score == 4:
        return "✅ Strong Password!", None
    elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features.", None
    else:
        return "\n".join(["❌ Weak Password - Improve it using the suggestions below:"] + feedback), generate_strong_password()

# Streamlit UI Styling
st.markdown(
    """
    <style>
        body {
            background-color: #f4f4f4;
            color: #333;
            font-family: Arial, sans-serif;
        }
        
        .header {
            background-color: #343a40;
            color: white;
            padding: 20px;
            text-align: center;
            font-size: 32px;
            font-weight: bold;
            border-radius: 10px 10px 0 0;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
            margin-bottom: 20px;
        }
        .footer {
            position: fixed;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 100%;
            text-align: center;
            background-color: #343a40;
            color: white;
            padding: 10px;
            font-size: 14px;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit UI
st.markdown('<div class="header">✅🔐 GIAIC - Password Strength Meter</div>', unsafe_allow_html=True)
password = st.text_input("Enter your password:", type="password")


if st.button("Check Password Strength"):
    result, suggested_password = check_password_strength(password)
    st.write(result)
    if suggested_password:
        st.write(f"🔑 Suggested Strong Password: `{suggested_password}`")

# Footer
st.markdown(
    """
    <div class="footer">
        &copy; 2025 Khawaja Naqeeb Uddin | Student of GIAIC | All Rights Reserved.
    </div>
    """,
    unsafe_allow_html=True
)
