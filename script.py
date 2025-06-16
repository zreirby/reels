import openai

# SET YOUR OPENROUTER API KEY HERE
client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"#GET API KEY FROM OPEN ROUTER
)
def generate_youtube_script(topic):
    prompt = f"""
    Write a full script of 2 minutes YouTube video titled'{topic}'.
    Start with a casual, engaging introduction that instantly grabs the viewer’s attention using storytelling or relatable hooks.
    Then, smoothly explore the main points or insights about {topic}—at least 4 key ideas—woven into a natural, conversational narrative with simple examples. Avoid explicitly labeling each point as 'Benefit' or 'Tip' or 'intro music' and 'outro music'.
    Keep the tone energetic, friendly, and informal—like a creator talking directly to their audience. Do not include any timestamps or structured sections or intro and outro music and avoid using host and do not use any scene to be written in words.
    End with a motivating and uplifting conclusion that encourages viewers to think or act, while keeping the tone fun and easygoing.
    """

    response = client.chat.completions.create(
        model="meta-llama/llama-3.3-8b-instruct:free",
        messages=[
            {"role": "system", "content": "You are a helpful YouTube video scriptwriter."},
            {"role": "user", "content": prompt}
        ]
    )

    script = response.choices[0].message.content
    return script


def save_script_to_file(script, filename="script.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(script)


def main():
    topic = input("Enter the topic for the YouTube video: ")
    print("\nGenerating script, please wait...\n")

    script = generate_youtube_script(topic)

    print("\nGenerated Script:\n")
    print(script)

    save_script_to_file(script)
    print("\n✅ Script saved successfully to 'script.txt'.")


if __name__ == "__main__":
    main()
