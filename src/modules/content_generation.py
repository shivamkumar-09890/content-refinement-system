from openai import OpenAI
import yaml
import os

# Load configuration from YAML file
def load_config(config_path):
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

# Load system prompt and model settings from config.yaml
config = load_config("src\modules\Module_config.yaml")

# Load API key from environment variables
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)

def generate_content(prompt, grade_level, subject):
    """
    Generate content based on user input, grade level, and subject.

    Args:
        prompt (str): User query or topic.
        grade_level (str): Grade level for the content (e.g., "Grade 5").
        subject (str): Subject for the content (e.g., "Mathematics").

    Returns:
        str: Generated educational content.
    """
    # Fetch system prompt template from config.yaml
    system_prompt_template = config["content_generation"]["system_prompt"]
    system_prompt = system_prompt_template.format(grade_level=grade_level, subject=subject)

    # Make a call to the OpenAI API
    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
            ],
            model=config["content_generation"]["model"],
            temperature=config["content_generation"]["temperature"],
            max_tokens=config["content_generation"]["max_tokens"]
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        print(f"Error: {e}")
        return "An error occurred while generating content."

# if __name__ == "__main__":
#     # Example usage
#     print("Welcome to the Content Generation Tool")

#     # Take user input for grade level and subject
#     grade_level = input("input Grade ").strip()
#     subject = input("input subject").strip()
#     prompt = input("prompt:").strip() #I wish to know about Akbar the indain mugal emperor

#     print("\nGenerating content...\n")

#     # Generate content
#     content = generate_content(prompt, grade_level, subject)

#     # Display the generated content
#     print("Generated Content:\n")
#     print(content)
