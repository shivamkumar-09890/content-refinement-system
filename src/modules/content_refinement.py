from openai import OpenAI
import yaml
import os

# Load configuration from YAML file
def load_config(config_path):
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

# Load settings from config.yaml
config = load_config(r"src\modules\Module_config.yaml")["content_refinement"]

# Load API key from environment variables
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)

def refine_content(content):
    """
    Refine the generated content to improve clarity, coherence, and readability.

    Args:
        content (str): The raw generated educational content.

    Returns:
        str: The refined educational content.
    """
    # Define system prompt from YAML config
    system_prompt = config["system_prompt"]

    try:
        response = client.chat.completions.create(
            model=config["model"],
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Refine the following content:\n\n{content}"},
            ],
            temperature=config["temperature"],
            max_tokens=config["max_tokens"]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error: {e}")
        return "An error occurred while refining content."

# if __name__ == "__main__":
#     # Example usage
#     print("Welcome to the Content Refinement Tool")

#     # Get user input (simulating generated content)
#     raw_content = input("Enter the raw generated content to refine:\n") 
#     """Sure, I'd be happy to teach you about Akbar, one of the most famous emperors from India's history! Akbar was a Mughal emperor, and he ruled India from 1556 to 1605. He became the emperor when he was very young, just around 13 years old. His full name was Jalal-ud-din Muhammad Akbar, but people usually just called him Akbar. Akbar was known for being a very wise and fair ruler. He believed in treating all people equally, regardless of their religion. This was very special because during his time, many rulers did not do this. One of the big things Akbar did was create a new kind of religion called Din-i-Ilahi, which means 'Religion of God'. This religion took good things from many different religions and put them all together, showing Akbar's respect for all beliefs. Akbar was also a big lover of art and culture. He built many beautiful buildings, like the city of Fatehpur Sikri. He also loved to learn, and he invited scholars, poets, artists, and architects from different parts of the world to his court.He also introduced a new system of tax collection known as 'Zabt' which was a more fair way of collecting taxes from the people. Akbar's reign is considered one of the most important periods in Indian history because of the peace, prosperity, and cultural developments that took place during his time. Even though he couldn't read or write, he was a very wise and effective ruler. He greatly expanded the Mughal Empire, making it one of the most powerful empires of his time. I hope this helps you understand who Akbar was and why he was so important!"""

#     print("\nRefining content...\n")

#     # Refine content
#     refined_content = refine_content(raw_content)

#     # Display the refined content
#     print("Refined Content:\n")
#     print(refined_content)
