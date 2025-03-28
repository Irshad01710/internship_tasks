import random
import datetime
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = {
    "greeting": ["Hello! How can I assist you today?", "Hi there! How can I help?", "Hey! What can I do for you?"],
    "goodbye": ["Goodbye! Have a great day!", "Bye! Feel free to reach out again!", "Take care!"],
    "thanks": ["You're welcome!", "Happy to help!", "Anytime!"]
}

faq_data = {
    "Can you edit or delete appointments or reminders ?": " Yes, just ask for it.",
    "What are your services?": "I can schedule appointment and set reminders for you.",
    "How do I contact customer support?": "You can contact our support via email at support@bot.com or call 123-456-7890.",
    "What are your working hours?": "I can schedule your appointments from 9:00 A.M to 6:00 P.M.",
}

df= pd.DataFrame(list(faq_data.items()), columns=["Question", "Answer"])
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(faq_df["Question"].values)

appointments = {}
reminders = {}

def schedule_appointment(user):
    print("Chatbot: Please enter the appointment date (YYYY-MM-DD):")
    date = input("You: ")
    print("Chatbot: Please enter the appointment time (HH:MM, 24-hour format):")
    time = input("You: ")
    print("Chatbot: Please enter purpose:")
    purpose = input("You: ")

    try:
        appointment_datetime = datetime.datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
        current_datetime = datetime.datetime.now()

        if appointment_datetime <= current_datetime:
            return "Appointment date and time must be in the future."

        appointment_hour = appointment_datetime.hour
        if appointment_hour < 9 or appointment_hour >= 18:
            return "Appointments can only be scheduled between 9:00 A.M and 6:00 P.M."

        if user not in appointments:
            appointments[user] = []
        appointments[user].append((purpose, date, time))
        return f"Your appointment is scheduled on {date} at {time}."
    except ValueError:
        return "Invalid date or time format. Please try again."

def show_appointments():
    if not appointments:
        return "No appointments scheduled."
    appointment_list = []
    for user, user_appointments in appointments.items():
        for purpose, date, time in user_appointments:
            appointment_list.append(f"{user}: {purpose} appointment on {date} at {time}")
    return "Scheduled Appointments:\n" + "\n".join(appointment_list)
def edit_appointment(user):
    if user not in appointments or not appointments[user]:
        return "No appointments found to edit."
    print("Chatbot: Your scheduled appointments:")
    for i, (purpose, date, time) in enumerate(appointments[user]):
        print(f"{i+1}. {purpose} on {date} at {time}")
    print("Chatbot: Enter the number of the appointment you want to edit:")
    try:
        choice = int(input("You: ")) - 1
        if choice < 0 or choice >= len(appointments[user]):
            return "Invalid choice."
        print("Chatbot: Enter the new date (YYYY-MM-DD):")
        new_date = input("You: ")
        print("Chatbot: Enter the new time (HH:MM, 24-hour format):")
        new_time = input("You: ")
        print("Chatbot: Enter the new purpose:")
        new_purpose = input("You: ")
        appointments[user][choice] = (new_purpose, new_date, new_time)
        return "Appointment updated successfully."
    except ValueError:
        return "Invalid input."

def delete_appointment(user):
    if user not in appointments or not appointments[user]:
        return "No appointments found to delete."
    print("Chatbot: Your scheduled appointments:")
    for i, (purpose, date, time) in enumerate(appointments[user]):
        print(f"{i+1}. {purpose} on {date} at {time}")
    print("Chatbot: Enter the number of the appointment you want to delete:")
    try:
        choice = int(input("You: ")) - 1
        if choice < 0 or choice >= len(appointments[user]):
            return "Invalid choice."
        del appointments[user][choice]
        return "Appointment deleted successfully."
    except ValueError:
        return "Invalid input."

def set_reminder(user):
    print("Chatbot: Please enter the reminder message:")
    message = input("You: ")
    print("Chatbot: Please enter the reminder date (YYYY-MM-DD):")
    date = input("You: ")
    print("Chatbot: Please enter the reminder time (HH:MM, 24-hour format):")
    time = input("You: ")

    try:
        reminder_datetime = datetime.datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
        current_datetime = datetime.datetime.now()

        if reminder_datetime <= current_datetime:
            return "Reminder date and time must be in the future."

        if user not in reminders:
            reminders[user] = []
        reminders[user].append((message, date, time))
        return f"Reminder set: '{message}' on {date} at {time}."
    except ValueError:
        return "Invalid date or time format. Please try again."
def edit_reminder(user):
    if user not in reminders or not reminders[user]:
        return "No reminders found to edit."
    print("Chatbot: Your scheduled reminders:")
    for i, (message, date, time) in enumerate(reminders[user]):
        print(f"{i+1}. '{message}' on {date} at {time}")
    print("Chatbot: Enter the number of the reminder you want to edit:")
    try:
        choice = int(input("You: ")) - 1
        if choice < 0 or choice >= len(reminders[user]):
            return "Invalid choice."
        print("Chatbot: Enter the new reminder message:")
        new_message = input("You: ")
        print("Chatbot: Enter the new date (YYYY-MM-DD):")
        new_date = input("You: ")
        print("Chatbot: Enter the new time (HH:MM, 24-hour format):")
        new_time = input("You: ")
        reminders[user][choice] = (new_message, new_date, new_time)
        return "Reminder updated successfully."
    except ValueError:
        return "Invalid input."

def delete_reminder(user):
    if user not in reminders or not reminders[user]:
        return "No reminders found to delete."
    print("Chatbot: Your scheduled reminders:")
    for i, (message, date, time) in enumerate(reminders[user]):
        print(f"{i+1}. '{message}' on {date} at {time}")
    print("Chatbot: Enter the number of the reminder you want to delete:")
    try:
        choice = int(input("You: ")) - 1
        if choice < 0 or choice >= len(reminders[user]):
            return "Invalid choice."
        del reminders[user][choice]
        return "Reminder deleted successfully."
    except ValueError:
        return "Invalid input."

def show_reminders():
    if not reminders:
        return "No reminders set."
    reminder_list = []
    for user, user_reminders in reminders.items():
        for message, date, time in user_reminders:
            reminder_list.append(f"{user}: '{message}' on {date} at {time}")
    return "Scheduled Reminders:\n" + "\n".join(reminder_list)


def get_response(user_input):
    user_input = user_input.lower()
    if user_input in ["hi", "hello", "hey"]:
        return random.choice(data["greeting"])
    elif user_input in ["bye", "goodbye"]:
        return random.choice(data["goodbye"])
    elif user_input in ["thanks", "thank you"]:
        return random.choice(data["thanks"])
    elif "schedule appointment" in user_input:
        return schedule_appointment("user")
    elif "all appointments" in user_input:
        return show_appointments()
    elif "set reminder" in user_input:
        return set_reminder("user")
    elif "all reminders" in user_input:
        return show_reminders()
    elif "edit appointment" in user_input:
        return edit_appointment("user")
    elif "delete appointment" in user_input:
        return delete_appointment("user")
    elif "edit reminder" in user_input:
        return edit_reminder("user")
    elif "delete reminder" in user_input:
        return delete_reminder("user")

    user_vec = vectorizer.transform([user_input])
    similarities = cosine_similarity(user_vec, X)
    index = similarities.argmax()
    if similarities[0, index] > 0.2:
        return faq_df.iloc[index, 1]
    return "I'm sorry, I didn't understand. Could you rephrase?"


def chatbot():
    print("Scheduler Chatbot: Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()
