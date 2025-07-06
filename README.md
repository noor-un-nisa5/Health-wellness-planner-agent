Health & Wellness Planner Agent 🏃‍♀️

An advanced, AI-powered personal health and wellness planner built using OpenAI Agents SDK. This project acts as your intelligent digital wellness assistant: it understands your goals, creates customized diet and workout plans, handles illness-specific recommendations, and helps track your progress all through natural language conversation.

🚀 Features

- Understands user health goals (e.g., weight loss or gain)
- Generates personalized **meal plans** (vegetarian & non-vegetarian) with detailed food items
- Suggests customized **workout routines** (for fat loss or weight gain)
- Handles disease-specific guidance (e.g., diabetes, BP, thyroid, migraine) with safe diet suggestions
- Multi-turn conversation support and real-time interaction
- Context-aware tracking & progress scheduling
- Modular, scalable code structure with separate agents and tools
- Supports **Streamlit UI** for a friendly web chatbot experience

💬 Example User Inputs
I want to lose 5 kg in 2 months
I am diabetic
I have thyroid and migraine
I want to gain/lose 8 kg in 4 months



🗂️ Project Structure

health_wellness_agent/
├── agents/
│ ├── escalation_agent.py
│ ├── injury_support_agent.py
│ └── nutrition_expert_agent.py
├── tools/
│ ├── goal_analyzer.py
│ ├── meal_planner.py
│ ├── workout_recommender.py
│ ├── scheduler.py
│ └── tracker.py
├── utils/
│ └── openai_mock.py
├── context.py
├── agent.py
├── hooks.py
├── main.py
├── app.py # Streamlit frontend
└── README.md


Run CLI version (console-based)
python main.py

Run Streamlit app (recommended)
streamlit run app.py



💡 How It Works
The agent uses specialized tools and agents:

GoalAnalyzerTool: Parses and structures user goals like "lose 5 kg in 2 months"

MealPlannerTool: Generates detailed 7-day meal plans for both vegetarians and non-vegetarians

WorkoutRecommenderTool: Suggests safe and effective workouts based on user goals

CheckinSchedulerTool: Helps schedule weekly progress checks

ProgressTrackerTool: Tracks progress and updates

NutritionExpertAgent: Handles medical/disease-specific diet and workout suggestions (diabetes, BP, migraine, thyroid)

InjurySupportAgent: Advises users with injuries

EscalationAgent: Refers to a human trainer if needed






Special thanks to OpenAI for providing an incredible foundation for agent-based AI systems, and to all open-source contributors helping make personalized health tools accessible to everyone. ❤️


