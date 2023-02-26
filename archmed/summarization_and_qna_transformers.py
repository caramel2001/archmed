import re
from transformers import (
    AutoTokenizer,
    AutoModelForQuestionAnswering,
    AutoModel,
    AutoModelForSeq2SeqLM,
)
import torch


def clean_text(intro_txt):
    intro_txt = intro_txt.replace("- ", "")
    regex = r"\[\d+\]"
    intro_txt = re.sub(regex, "", intro_txt)
    return intro_txt


# Get summary of text


def getModelSummarizer(link, dir):
    """Model loading function"""
    tokenizer = AutoTokenizer.from_pretrained(link, cache_dir=dir)
    model = AutoModelForSeq2SeqLM.from_pretrained(link, cache_dir=dir)
    return tokenizer, model


def generateSummary(model, tokenizer, txt):
    """Helper function"""
    inputs = tokenizer.encode_plus(txt, return_tensors="pt", truncation=True)
    summary_ids = model.generate(
        inputs["input_ids"], num_beams=4, max_length=70, early_stopping=True
    )
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary


def getSummary(intro_txt, dir):
    """CALL THIS ONE TO GET SUMMARY OF ABSTRACT"""

    link = "PeterBanning71/t5-small-finetuned-bioMedv1"
    tokenizer, model = getModelSummarizer(link, dir)
    summary = generateSummary(model, tokenizer, intro_txt)
    return summary


# Get answer for a question based on context


def getModel_QNA(dir):
    """Model loading function"""
    name = "dmis-lab/biobert-base-cased-v1.1-squad"

    tokenizer = AutoTokenizer.from_pretrained(name, model_max_length=512, cache_dir=dir)
    model = AutoModelForQuestionAnswering.from_pretrained(name, cache_dir=dir)
    return tokenizer, model


def generateAnswer(question, context, model, tokenizer):
    """Helper function"""
    inputs = tokenizer.encode_plus(
        question, context, add_special_tokens=True, return_tensors="pt"
    )
    start_logits, end_logits = model(**inputs).start_logits, model(**inputs).end_logits
    start_index = torch.argmax(start_logits)
    end_index = torch.argmax(end_logits)
    answer = tokenizer.convert_tokens_to_string(
        tokenizer.convert_ids_to_tokens(
            inputs["input_ids"][0][start_index : end_index + 1]
        )
    )
    return answer


def getAnswer(question, large_context, dir, tokenizer, model):
    """CALL THIS ONE TO GET ANSWER TO QUESTION"""

    # question = 'What is the name of the disease that is spreading around?'

    # large_context = "The long-term success of the public health response to the coremic will depend..."
    context = getSummary(large_context)

    answer = generateAnswer(question, context, model, tokenizer)
    return answer
