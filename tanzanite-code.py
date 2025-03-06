from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

model_name = "unitary/unbiased-toxic-roberta"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

def detect_toxicity(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    
    with torch.no_grad():
        outputs = model(**inputs)
    
    scores = torch.sigmoid(outputs.logits).squeeze().tolist()

    categories = ["toxicity", "severe_toxicity", "obscene", "threat", "insult", "identity_attack"]
    
    result = {cat: round(score, 4) for cat, score in zip(categories, scores)}
    
    return result

def detect_toxicity_with_label(text):
    scores = detect_toxicity(text)
    toxic_label = "Non-Toxic" if max(scores.values()) < 0.5 else "Toxic"
    return scores, toxic_label

if __name__ == "__main__":
    text = input("Enter a sentence: ")
    toxicity_scores, label = detect_toxicity_with_label(text)

    print("\nToxicity Analysis:")
    for category, score in toxicity_scores.items():
        print(f"{category}: {score}")

    print(f"\nOverall Label: {label}")
