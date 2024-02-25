import logging

from llama_cpp import Llama


class GPT:
    def __init__(self):
        # Loading model
        self.llm = Llama(
            model_path="./gpt/wizardlm-1.0-uncensored-llama2-13b.Q5_K_S.gguf"
        )
        logging.debug(self.llm)

    def get_answer(self, question: str) -> str:
        # Waiting for llm output
        logging.debug('starting to request the model')
        output = self.llm(
            f"You are a helpful AI assistant.\n\nUSER: {question}\nASSISTANT:",
            max_tokens=512,
            stop=["ASSISTANT:"],
            echo=True,
        )
        # Llm output
        logging.debug('outpuuuuuuuut')
        logging.debug(output)
        return output["choices"][0]["text"].split(
            "ASSISTANT: ", 1
        )[-1]  # type: ignore
