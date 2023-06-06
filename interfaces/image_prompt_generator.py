import json
from utils.console_utility import Console
from config.config import Config


class ImagePromptGenerator:
    def __init__(self, llm, prompt_template, paragraphs):
        self.llm = llm
        self.prompt_template = prompt_template
        self.paragraphs = paragraphs

    def generate_prompt(self, no_images):
        paragraphs_per_prompt = 1
        if len(self.paragraphs) > no_images:
            paragraphs_per_prompt = len(self.paragraphs) // no_images
            if len(self.paragraphs) % no_images != 0:
                paragraphs_per_prompt += 1
        merged_paragraphs = []
        for i in range(0, len(self.paragraphs), paragraphs_per_prompt):
            if i + paragraphs_per_prompt > len(self.paragraphs):
                list_of_paragraphs = self.paragraphs[i:]
            else:
                list_of_paragraphs = self.paragraphs[i:i + paragraphs_per_prompt]
            merged_paragraphs.append(list_of_paragraphs)
        prompts = []
        i = 1
        n = len(merged_paragraphs)
        for paragraph in merged_paragraphs:
            Console.info('Generating Image Prompt : Part - ({}/{})'.format(i, n))
            response = self.llm.ask(self.prompt_template.get_prompt(' '.join(paragraph)))
            response_dict = json.loads(response)
            response_dict['modifiers'] = response_dict['modifiers'].split(',')
            if len(response_dict['modifiers']) > Config.IMAGE_PROMPT_MAX_MODIFIERS:
                response_dict['modifiers'] = ','.join(response_dict['modifiers'][:Config.IMAGE_PROMPT_MAX_MODIFIERS])
            else:
                response_dict['modifiers'] = ','.join(response_dict['modifiers'])
            prompt = response_dict['landscape'] + ', ' + response_dict['entity'] + ', ' + response_dict['modifiers']
            prompts.append(prompt)
            i += 1
        return prompts, merged_paragraphs
