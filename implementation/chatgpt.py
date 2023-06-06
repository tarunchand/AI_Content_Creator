import os
from interfaces.llm import LLM
from revChatGPT.V1 import Chatbot
from utils.file_utility import FileUtility
from interfaces.prompt_template import PromptTemplate
from interfaces.paragraph_splitter import ParagraphSplitter
from interfaces.image_prompt_generator import ImagePromptGenerator


class ChatGPT(LLM):
    def __init__(self):
        chatgpt_auth = FileUtility.load_json_file(os.path.join('config', 'chatgpt_auth.json'))
        self.chatgpt = Chatbot(config={
            "access_token": chatgpt_auth["accessToken"]
        })

    def ask(self, prompt: str):
        response = ""
        for data in self.chatgpt.ask(
                prompt
        ):
            response = data["message"]
        return response


class ChatGPTParagraphSplitter(ParagraphSplitter):
    def __init__(self, text):
        super().__init__(ChatGPT(), ChatGPTParagraphTemplate(), text)


class ChatGPTParagraphTemplate(PromptTemplate):
    def __init__(self):
        super().__init__()

    def get_prompt(self, text):
        return 'Split the below text into meaningful paragraphs:\n\n' + text + '\n'


class ChatGPTImagePromptGenerator(ImagePromptGenerator):
    def __init__(self, paragraphs):
        super().__init__(ChatGPT(), ChatGPTImageGenPromptTemplate(), paragraphs)


class ChatGPTImageGenPromptTemplate(PromptTemplate):
    def __init__(self):
        super().__init__()

    def get_prompt(self, text):
        return '''
I want you to write one DALLE-2 prompt which exactly describes an IDEA. The prompt should be in JSON format. 

Below is the format of the prompt
{ "landscape": <description of landscape in the below IDEA>, "entity": <description of person or object or animal or 
any entity in the below IDEA>, "modifiers": <mood, style, lighting, and other aspects of the scene in the idea>}

For example:- 
{
  "landscape": "heart of the African savannah, grasslands, epic sky, golden rays of the sun",
  "entity": "Majestic Elephant named Kibo, grey skin elephant, elephant with robust tusks, butterflies, 
  diverse creatures",
  "modifiers": "cinematic view, floral, sharp focus, intricate details,serene demeanor, high detail, warm lighting, 
  volumetric, godrays, vivid, beautiful"
}

Below is the idea you have to write prompt for
IDEA : ''' + text


class ChatGPTMotivationalTemplate(PromptTemplate):
    def __init__(self):
        super().__init__()

    def get_prompt(self, text):
        return text


class ChatGPTMotivationalPersonTemplate(PromptTemplate):
    def __init__(self):
        super().__init__()

    def get_prompt(self, text):
        return text


class ChatGPTMysteryTemplate(PromptTemplate):
    def __init__(self):
        super().__init__()

    def get_prompt(self, text):
        return text


class ChatGPTHorrorTemplate(PromptTemplate):
    def __init__(self):
        super().__init__()

    def get_prompt(self, text):
        return text


class ChatGPTEducationalTemplate(PromptTemplate):
    def __init__(self):
        super().__init__()

    def get_prompt(self, text):
        return text
