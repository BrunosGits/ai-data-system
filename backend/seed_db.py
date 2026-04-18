import random
from main import SessionLocal, Interaction

# This is our "Fake Data" source. 
# We use this to simulate real user feedback for BI analysis.
samples = [
    ("The interface is slow", "Technical", "Negative"),
    ("I love the new AI features!", "Product", "Positive"),
    ("How do I reset my password?", "Support", "Neutral"),
    ("The documentation is missing details on SQL", "Education", "Negative"),
    ("Great response speed!", "Performance", "Positive"),
    ("The mobile app crashes on login", "Technical", "Negative"),
    ("Excellent customer service experience", "Support", "Positive"),
    ("The search function is hard to find", "UX", "Neutral")
]

def seed_data(count=100):
    # Open a connection to our local SQLite database
    db = SessionLocal()
    print(f"🚀 Starting seed: Adding {count} records to study_data.db...")

    for i in range(count):
        # Pick a random feedback example from our list above
        text, cat, sentiment = random.choice(samples)
        
        # We simulate the LLM's response here so we don't have to pay for API calls
        fake_ai_answer = f"Automated analysis: Categorized as {cat} with a {sentiment} sentiment."

        # Create the database record object
        new_entry = Interaction(
            question=f"Feedback #{i+1}: {text}",
            answer=fake_ai_answer,
            category=cat
        )
        
        # Add it to the "staging area"
        db.add(new_entry)

    # Save everything to the .db file in one single move
    db.commit() 
    db.close()
    print("✅ Success! 100 records are now stored in your database.")

if __name__ == "__main__":
    seed_data(100)
