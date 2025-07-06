import streamlit as st
import asyncio
from agent import HealthWellnessPlannerAgent
from context import UserSessionContext


agent = HealthWellnessPlannerAgent()


context = UserSessionContext(
    name="User",
    uid=1,
    goal=None,
    diet_preferences=None,
    workout_plan=None,
    meal_plan=None,
    injury_notes=None,
    handoff_logs=[],
    progress_logs=[]
)

st.title("💪🏽 Health & Wellness Planner Agent")
st.write("Ask me anything about your health goals, diet, workout, or illnesses!")

user_input = st.text_input("💬 Type your message:", "")

if st.button("Submit") or user_input:
    async def run_agent():
        response = await agent(user_input, context)
        return response

    response = asyncio.run(run_agent())
    st.write("🤖 **Agent Reply:**")
    st.write(response)
