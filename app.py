import spacy
import streamlit as st
import random 

def generate_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r}, {g}, {b})"

def main():
    # Load the trained model
    trained_model = spacy.load("ner_pretrained_model")

    st.title("Named Entity Recognition")
    st.write("Enter your text below:")

    # User input
    example_text = st.text_input("Text")

    # Process user input when button is clicked
    if st.button("Analyze"):
        doc = trained_model(example_text)

        # Process the text and display the modified text with labeled entities
        modified_text = annotate_entities(example_text, doc)

        # Display the modified text with different background boxes for each entity
        st.markdown(modified_text, unsafe_allow_html=True)

def annotate_entities(text, doc):
    modified_text = text
    entity_colors = {}


    for ent in doc.ents:
        entity_text = ent.text
        entity_label = ent.label_

         # Generate a random color for the entity label if it doesn't exist
        if entity_label not in entity_colors:
            entity_colors[entity_label] = generate_random_color()

        # Apply background color and bold font to the entity
        highlighted_text = f"<span style='background-color: {entity_colors[entity_label]}; font-weight: bold;'>{entity_text} ({entity_label})</span>"
        modified_text = modified_text.replace(entity_text, highlighted_text)

    return modified_text

if __name__ == "__main__":
    main()


