def get_bot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! I can help you schedule an appointment or answer common questions. What would you like to do?"
    
    elif "schedule" in user_input or "appointment" in user_input:
        return "Sure! Let's schedule an appointment.\n What date would you like to book? (YYYY-MM-DD)"
    
    elif "support" in user_input or "help" in user_input:
        return "I can assist with appointment scheduling, working hours, or general inquiries. What do you need help with?"
    
    elif "working hours" in user_input or "timing" in user_input:
        return "Our working hours are 9:00 AM to 6:00 PM from Monday to Friday."
    
    elif "contact" in user_input:
        return "You can contact us at supportme@gmail.com or call +1 234 567 890."
    
    else:
        return "I'm not sure how to respond to that. Try asking about scheduling an appointment or getting support."

def schedule_appointment():
    date = input("📅 Enter date (YYYY-MM-DD): ")
    time = input("⏰ Enter time (HH:MM AM/PM): ")
    purpose = input("📝 Enter purpose of appointment: ")
    
    print(f"\n✅ Appointment Confirmed!\n📅 Date: {date}\n⏰ Time: {time}\n📝 Purpose: {purpose}")
    print("Chatbot: Your appointment has been scheduled. You can continue asking questions or type 'exit' to quit.\n")

def chatbot():
    print("Chatbot: Hello! I am your customer support bot. Type 'exit' anytime to stop.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! Have a great day! 😊")
            break
        
        bot_response = get_bot_response(user_input)
        print(f"Chatbot: {bot_response}")
        
        if "Let's schedule an appointment" in bot_response: 
            schedule_appointment()

chatbot()
