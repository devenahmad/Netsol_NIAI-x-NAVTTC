# Task 65 - Microsoft Azure AI
#
# The task says to watch the Microsoft Learn video lectures (weeks 10, 11, 12):
#   AI-900 fundamentals: https://learn.microsoft.com/en-us/training/paths/prepare-teach-ai-900-fundamentals-academic-programs/
#   AI-102 associate:    https://learn.microsoft.com/en-us/training/paths/prepare-teach-ai-102-microsoft-design-implement-azure/
#
# That part is watching, not code. This file is the hands-on part of topics covered in those weeks (text analysis, image analysis, speech, translation).
#
# SETUP
#   1. make a free Azure account -> portal.azure.com
#   2. create an "Azure AI services" resource (one key works for vision, language, etc)
#   3. copy its key and endpoint, then set them as environment variables:
#        export AZURE_AI_KEY="your key"
#        export AZURE_AI_ENDPOINT="https://yourname.cognitiveservices.azure.com/"
#   4. pip install azure-ai-textanalytics azure-ai-vision-imageanalysis azure-cognitiveservices-speech
#
# Without a key the script just prints what it WOULD do, so it still runs.

import os

KEY = os.environ.get("AZURE_AI_KEY")
ENDPOINT = os.environ.get("AZURE_AI_ENDPOINT")


def need_key():
    if not KEY or not ENDPOINT:
        print("   (no AZURE_AI_KEY / AZURE_AI_ENDPOINT set, skipping the real call)")
        return True
    return False


# 1. language: sentiment, key phrases, entities
def text_analysis():
    print("1. text analysis")
    docs = [
        "The hotel was clean and the staff in Lahore were very friendly.",
        "The food was cold and the service was terrible.",
    ]
    if need_key():
        return
    from azure.core.credentials import AzureKeyCredential
    from azure.ai.textanalytics import TextAnalyticsClient

    client = TextAnalyticsClient(ENDPOINT, AzureKeyCredential(KEY))

    for d, r in zip(docs, client.analyze_sentiment(docs)):
        print("  ", r.sentiment, "-", d)

    for r in client.extract_key_phrases(docs):
        print("   key phrases:", r.key_phrases)

    for r in client.recognize_entities(docs):
        print("   entities:", [(e.text, e.category) for e in r.entities])

    print("   language:", client.detect_language(["Ye ek test hai"])[0].primary_language.name)


# 2. vision: describe an image, read text from it
def image_analysis():
    print("2. image analysis")
    url = "https://learn.microsoft.com/azure/ai-services/computer-vision/media/quickstarts/presentation.png"
    if need_key():
        return
    from azure.core.credentials import AzureKeyCredential
    from azure.ai.vision.imageanalysis import ImageAnalysisClient
    from azure.ai.vision.imageanalysis.models import VisualFeatures

    client = ImageAnalysisClient(ENDPOINT, AzureKeyCredential(KEY))
    result = client.analyze_from_url(
        image_url=url,
        visual_features=[VisualFeatures.CAPTION, VisualFeatures.READ, VisualFeatures.TAGS],
    )
    if result.caption:
        print("   caption:", result.caption.text, round(result.caption.confidence, 2))
    if result.tags:
        print("   tags:", [t.name for t in result.tags.list[:6]])
    if result.read:
        for block in result.read.blocks:
            for line in block.lines:
                print("   text:", line.text)


# 3. speech to text
def speech_to_text():
    print("3. speech to text")
    region = os.environ.get("AZURE_SPEECH_REGION")
    key = os.environ.get("AZURE_SPEECH_KEY")
    if not key or not region:
        print("   (set AZURE_SPEECH_KEY and AZURE_SPEECH_REGION to try this, skipping)")
        return
    import azure.cognitiveservices.speech as speech

    cfg = speech.SpeechConfig(subscription=key, region=region)
    recognizer = speech.SpeechRecognizer(speech_config=cfg)
    print("   say something...")
    result = recognizer.recognize_once()
    print("   heard:", result.text)


# 4. translation (plain REST call)
def translate():
    print("4. translation")
    key = os.environ.get("AZURE_TRANSLATOR_KEY")
    region = os.environ.get("AZURE_TRANSLATOR_REGION")
    if not key or not region:
        print("   (set AZURE_TRANSLATOR_KEY and AZURE_TRANSLATOR_REGION to try this, skipping)")
        return
    import requests

    r = requests.post(
        "https://api.cognitive.microsofttranslator.com/translate",
        params={"api-version": "3.0", "to": ["ur", "fr"]},
        headers={"Ocp-Apim-Subscription-Key": key, "Ocp-Apim-Subscription-Region": region},
        json=[{"text": "Good morning, how are you?"}],
    )
    for t in r.json()[0]["translations"]:
        print("  ", t["to"], "->", t["text"])


if __name__ == "__main__":
    text_analysis()
    image_analysis()
    speech_to_text()
    translate()
    print("\ndone")