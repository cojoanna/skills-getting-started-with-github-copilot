"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    # Intellectual activities
    "Science Club": {
        "description": "Conduct experiments and explore scientific concepts",
        "schedule": "Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 16,
        "participants": ["eva@mergington.edu"]
    },
    "Robotics Team": {
        "description": "Design, build, and program robots for competitions",
        "schedule": "Saturdays, 1:00 PM - 3:00 PM",
        "max_participants": 10,
        "participants": ["liam@mergington.edu"]
    },
    # Artistic activities
    "Photography Club": {
        "description": "Learn photography techniques and showcase your work",
        "schedule": "Fridays, 4:00 PM - 5:30 PM",
        "max_participants": 12,
        "participants": ["mia@mergington.edu"]
    },
    "Music Ensemble": {
        "description": "Perform music in a group and participate in concerts",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["jack@mergington.edu"]
    },
    # Sports related activities
    "Track and Field": {
        "description": "Train and compete in running, jumping, and throwing events",
        "schedule": "Tuesdays and Fridays, 4:00 PM - 5:30 PM",
        "max_participants": 20,
        "participants": ["oliver@mergington.edu"]
    },
    "Tennis Club": {
        "description": "Practice tennis skills and play matches",
        "schedule": "Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 8,
        "participants": ["ava@mergington.edu"]
    },
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Math Olympiad": {
        "description": "Prepare for math competitions and solve challenging problems",
        "schedule": "Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 15,
        "participants": ["alice@mergington.edu"]
    },
    "Debate Team": {
        "description": "Develop public speaking and argumentation skills",
        "schedule": "Mondays, 3:30 PM - 5:00 PM",
        "max_participants": 10,
        "participants": ["ben@mergington.edu"]
    },

    # Artistic activities
    "Art Club": {
        "description": "Explore painting, drawing, and sculpture",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 18,
        "participants": ["lucy@mergington.edu"]
    },
    "Drama Society": {
        "description": "Act, direct, and produce school plays",
        "schedule": "Tuesdays, 4:00 PM - 5:30 PM",
        "max_participants": 20,
        "participants": ["sam@mergington.edu"]
    },

    # Sports related activities
    "Soccer Team": {
        "description": "Practice and compete in soccer matches",
        "schedule": "Mondays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 22,
        "participants": ["james@mergington.edu"]
    },
    "Basketball Team": {
        "description": "Train and play basketball games",
        "schedule": "Wednesdays and Fridays, 4:00 PM - 5:30 PM",
        "max_participants": 15,
        "participants": ["lily@mergington.edu"]
    },
    "Swimming Club": {
        "description": "Swimming lessons and competitions",
        "schedule": "Saturdays, 10:00 AM - 12:00 PM",
        "max_participants": 12,
        "participants": ["noah@mergington.edu"]
    },

    # Existing activities
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
}
   


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    # Validate student is not already signed up for the activity
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]
    # Validate student is not already signed up for the activity
    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
