import spacy
import streamlit as st

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

        # Display the modified text
        st.write(modified_text)

def annotate_entities(text, doc):
    modified_text = text

    for ent in doc.ents:
        entity_text = ent.text
        entity_label = ent.label_
        highlighted_text = f"**{entity_text} ({entity_label})**"
        modified_text = modified_text.replace(entity_text, highlighted_text)

    return modified_text

if __name__ == "__main__":
    main()


#cd "./OneDrive/Desktop/Atomic Asher/NER"
#C:\Users\Shruti\AppData\Local\Programs\Python\Python39\python.exe -m streamlit run app.py