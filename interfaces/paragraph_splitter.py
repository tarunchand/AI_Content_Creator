from config.config import Config
from utils.console_utility import Console


class ParagraphSplitter:
    def __init__(self, llm, prompt_template, text):
        self.llm = llm
        self.prompt_template = prompt_template
        self.text = text

    def split_data(self):
        parts = self.split_into_parts()
        final_parts = []
        i = 1
        n = len(parts)
        for part in parts:
            Console.info('Generating Paragraph : Part - ({}/{})'.format(i, n))
            paragraphs = self.llm.ask(self.prompt_template.get_prompt(part)).split("\n")
            for paragraph in paragraphs:
                if len(paragraph) > 0:
                    final_parts.append(paragraph)
            i += 1
        return final_parts

    def split_into_parts(self):
        sentences = self.text.replace("\n", " ").split(".")
        parts = []
        current_part_len = 0
        current_parts = []
        for sentence in sentences:
            if current_part_len + len(sentence) < Config.MAX_SPLIT_LENGTH:
                current_parts.append(sentence)
                current_part_len += len(sentence)
            else:
                parts.append(".".join(current_parts))
                current_parts = [sentence]
                current_part_len = len(sentence)
        if len(current_parts) > 0:
            parts.append(".".join(current_parts))
        return parts
