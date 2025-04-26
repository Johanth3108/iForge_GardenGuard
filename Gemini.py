from google import genai

client = genai.Client(api_key="AIzaSyBoZJep3hdGb7hv7V79ByaJQdMAzJmWp9Q")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="""You are an expert in gardening and plant care.

Here's my garden sensor data of 10 onion plants in my garden:
- Soil Moisture: 3%
- Air Humidity: 72%
- Air Temperature: 5°C

Please:
1. first Tell me about the current condition of the garden based on this data.
2. second give me only 2 variables without extra words, 1. garden health out of 10, 2. any fertilizer needed (yes/no) if yes what fertilizer""",
)

print(response.text)