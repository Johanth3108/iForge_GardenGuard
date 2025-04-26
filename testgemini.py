import google.generativeai as genai

# Replace this with your actual API key
genai.configure(api_key="AIzaSyBoZJep3hdGb7hv7V79ByaJQdMAzJmWp9Q")

model = genai.GenerativeModel("gemini-pro")

def get_gemini_recommendation(soil, humidity):
    prompt = (
        f"My plant sensor recorded the following:\n"
        f"- Soil Moisture: {soil}%\n"
        f"- Air Humidity: {humidity}%\n"
        f"What can I do to improve my garden conditions?"
    )
    
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {e}"

# Example usage
if __name__ == "__main__":
    print(get_gemini_recommendation(40, 60))




# """AIzaSyBoZJep3hdGb7hv7V79ByaJQdMAzJmWp9Q


# You are an expert in gardening and plant care.

# Here's my garden sensor data of 10 onion plants in my garden:
# - Soil Moisture: 38%
# - Air Humidity: 72%
# - Air Temperature: 25°C

# Please:
# 1. Tell me about the current condition of the garden based on this data.
# 2. Recommend any actions I should take.
# 3. at the end give me 2 variables, 1. garden health out of 10, 2. any fertilizer needed (yes/no) if yes what fertilizer"""