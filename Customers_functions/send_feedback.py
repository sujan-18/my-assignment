# Send feedback
FEEDBACK_FILE="data/feedback.txt"
def send_feedback():
    feedback = input("Enter your feedback: ")
    with open(FEEDBACK_FILE, "a") as f:
        f.write(f"{feedback}\n")
    print("Feedback submitted successfully!")