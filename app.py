import gradio as gr

def fitness_plan(name, goal):
    if goal.lower() == "weight loss":
        return f"{name}, your plan includes cardio 5x/week and a calorie deficit meal plan."
    elif goal.lower() == "muscle gain":
        return f"{name}, focus on strength training and high-protein meals!"
    else:
        return f"{name}, maintain a balanced routine of both cardio and strength!"

iface = gr.Interface(
    fn=fitness_plan,
    inputs=[
        gr.Textbox(label="Your Name"),
        gr.Dropdown(["Weight Loss", "Muscle Gain", "General Fitness"], label="Your Goal")
    ],
    outputs="text",
    title="Fitness Coach App",
    description="Get a simple fitness plan based on your goals."
)

iface.launch()
