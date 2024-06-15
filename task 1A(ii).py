import demoji

demoji.download_codes()

def convert_emojis_to_text(text):
    return demoji.replace(text, demoji.findall(text))

example_text = "I love programming! 😍🚀 #coding #python"

converted_text = convert_emojis_to_text(example_text)

print("Original text:", example_text)
print("Converted text:", converted_text)
