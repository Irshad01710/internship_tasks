from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from datetime import datetime

chatbot = ChatBot("AppointmentBot")
trainer = ListTrainer(chatbot)

trainer.train([
    "Hello", "Hello! I can help you schedule an appointment or answer common questions. What would you like to do?",
    "Hi", "Hello! I can help you schedule an appointment or answer common questions. What would you like to do?",
    "Schedule", "Sure! Let's schedule an appointment. What date would you like to book? (YYYY-MM-DD)",
    "Appointment", "Sure! Let's schedule an appointment. What date would you like to book? (YYYY-MM-DD)",
    "Working hours", "Our working hours are 9:00 AM to 6:00 PM from Monday to Friday.",
    "Contact", "You can contact us at supportme@gmail.com or call +1 234 567 890.",
    "Support", "You can contact us at supportme@gmail.com or call +1 234 567 890."
])

appointments = {}

def schedule_appointment():
    date_str = input("📅 Enter date (YYYY-MM-DD): ")
    time_str = input("⏰ Enter time (HH:MM AM/PM): ")
    
    try:
        appointment_datetime = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %I:%M %p")
        current_datetime = datetime.now()
        
        if appointment_datetime < current_datetime:
            print("\n❌ Error: The selected date and time have already passed. Please choose a correct slot.")
            return
        
        if appointment_datetime.hour < 9 or appointment_datetime.hour > 18:
            print("\n❌ Error: Appointments can only be scheduled between working hours.")
            return
    except ValueError:
        print("\n❌ Error: Invalid date or time format. Please enter in the correct format (YYYY-MM-DD and HH:MM AM/PM).")
        return
    
    if date_str in appointments and time_str in appointments[date_str]:
        print("\n❌ This time slot is already booked. Please choose a different time.")
        return
    
    purpose = input("📝 Enter purpose of appointment: ")
    
    if date_str not in appointments:
        appointments[date_str] = {}
    appointments[date_str][time_str] = purpose
    
    print(f"\n✅ Appointment Confirmed!\n📅 Date: {date_str}\n⏰ Time: {time_str}\n📝 Purpose: {purpose}")
    print("Chatbot: Your appointment has been scheduled. You can continue asking questions or type 'exit' to quit.\n")

def chat():
    print("Chatbot: Hello! I am your customer support bot. Type 'exit' anytime to stop.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! Have a great day! 😊")
            break
        
        response = chatbot.get_response(user_input)
        print(f"Chatbot: {response}")
        
        if "Let's schedule an appointment" in str(response):
            schedule_appointment()

chat()
