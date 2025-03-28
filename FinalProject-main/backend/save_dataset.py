import json

# Copy the dataset and save it
dataset = {
    "data": [
        {
            "tag": "greeting",
            "question": "Hi",
            "response": "Hello! How can I help you today?"
        },
        {
            "tag": "greeting",
            "question": "Good morning",
            "response": "Good morning! How can I assist you?"
        },
        {
            "tag": "assignments",
            "question": "Are there any assignments?",
            "response": "Yes, you have a Machine Learning assignment due on March 5th."
        },
        {
            "tag": "assignments",
            "question": "Deadline for the DBMS assignment?",
            "response": "The DBMS assignment is due on March 10th."
        },
        {
            "tag": "exams",
            "question": "When is the midterm exam?",
            "response": "Your midterm exam is on March 20th."
        },
        {
            "tag": "exams",
            "question": "Do we have an exam this week?",
            "response": "No, the next exam is scheduled for next month."
        },
        {
            "tag": "events",
            "question": "What events are coming up?",
            "response": "The annual tech fest is happening on April 5th."
        },
        {
            "tag": "events",
            "question": "When is the sports day?",
            "response": "Sports day is scheduled for March 25th."
        },
        {
            "tag": "lecture_schedule",
            "question": "What classes do I have today?",
            "response": "You have Data Science at 10 AM and AI at 2 PM."
        },
        {
            "tag": "lecture_schedule",
            "question": "When is the next Python class?",
            "response": "Your next Python class is on Wednesday at 11 AM."
        },
        {
            "tag": "study_material",
            "question": "Where can I find AI study materials?",
            "response": "AI study materials are available on the college portal under the 'Resources' section."
        },
        {
            "tag": "study_material",
            "question": "Do you have notes on Deep Learning?",
            "response": "Yes, Deep Learning notes are uploaded on the class drive."
        },
        {
            "tag": "reminders",
            "question": "Remind me about the project submission",
            "response": "Your project submission deadline is on March 12th."
        },
        {
            "tag": "reminders",
            "question": "Any important deadlines this week?",
            "response": "Yes, your AI assignment is due on March 1st, and the project report submission is on March 4th."
        },
        {
            "tag": "faq",
            "question": "How do I reset my student portal password?",
            "response": "You can reset your password by clicking on 'Forgot Password' on the login page."
        },
        {
            "tag": "faq",
            "question": "Where can I get my ID card?",
            "response": "You can collect your ID card from the administration office."
        }
    ]
}


with open("chatbot_dataset.json", "w") as file:
    json.dump(dataset, file, indent=4)

print("Dataset saved successfully!")