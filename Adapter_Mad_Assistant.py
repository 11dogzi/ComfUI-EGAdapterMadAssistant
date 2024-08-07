import random

class EGIPAdapter_Mad_Assistant:
    CATEGORY_KEYS = ['0layer', '1layer', '2layer', '3layer', '4layer', '5layer', '6layer', '7layer', '8layer', '9layer', '10layer', '11layer']
    OPTIONS = {str(i): str(i) for i in range(0, 12)}

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                **cls.get_input_types_from_keys(cls.CATEGORY_KEYS),
                "Random": (["Yes", "No"], {"default": "No"}),
                "seed": ("INT", {"default": 0, "min": -1125899906842624, "max": 1125899906842624}),
            }
        }

    @staticmethod
    def get_input_types_from_keys(keys):
        input_types = {}
        for i, key in enumerate(keys):
            # Hide the super key by not including it in the input_types dictionary
            input_types[f"{key} Weight"] = ("FLOAT", {"default": 0.0, "min": 0.0, "max": 1.0, "step": 0.1, "display": "slider"})
        return input_types

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("layer_weights",)
    FUNCTION = "generate_prompt"
    CATEGORY = "ipadapter"

    def generate_prompt(self, **kwargs):
        prompt_parts = {str(i): 0.0 for i in range(0, 12)}
        for i, key in enumerate(self.CATEGORY_KEYS):
            # Since the super key is hidden, we use the index to find the corresponding weight
            weight_key = f"{key} Weight"
            if weight_key in kwargs and kwargs[weight_key] is not None:
                weight = kwargs[weight_key]
                prompt_parts[str(i)] = weight
        
        if kwargs.get("Random") == "Yes":
            for key in self.CATEGORY_KEYS:
                options = list(self.OPTIONS.keys())
                random_choice = random.choice(options)
                weight_key = f"{key} Weight"
                if prompt_parts[str(int(random_choice))] == 0.0:
                    weight = random.uniform(0.0, 1.0)
                    prompt_parts[random_choice] = weight

        layer_weights = ','.join(f"{k}:{int(v)}" if v in {0.0, 1.0} else f"{k}:{v:.1f}" for k, v in prompt_parts.items())
        return (layer_weights,)

import random

class EGIPAdapter_Mad_AssistantV1:
    CATEGORY_KEYS = ['0layer', '1layer', '2layer', '3layer', '4layer', '5layer', '6layer', '7layer', '8layer', '9layer', '10layer', '11layer']
    OPTIONS = {str(i): str(i) for i in range(0, 12)}

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                **cls.get_input_types_from_keys(cls.CATEGORY_KEYS),
                "Random": (["Yes", "No"], {"default": "No"}),
                "seed": ("INT", {"default": 0, "min": -1125899906842624, "max": 1125899906842624}),
            }
        }

    @staticmethod
    def get_input_types_from_keys(keys):
        input_types = {}
        for i, key in enumerate(keys):
            # Hide the super key by not including it in the input_types dictionary
            input_types[f"{key} Weight"] = ("FLOAT", {"default": 0.0, "min": -1.0, "max": 1.0, "step": 0.1, "display": "slider"})
        return input_types

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("layer_weights",)
    FUNCTION = "generate_prompt"
    CATEGORY = "ipadapter"

    def generate_prompt(self, **kwargs):
        prompt_parts = {str(i): 0.0 for i in range(0, 12)}
        for i, key in enumerate(self.CATEGORY_KEYS):
            # Since the super key is hidden, we use the index to find the corresponding weight
            weight_key = f"{key} Weight"
            if weight_key in kwargs and kwargs[weight_key] is not None:
                weight = kwargs[weight_key]
                prompt_parts[str(i)] = weight
        
        if kwargs.get("Random") == "Yes":
            for key in self.CATEGORY_KEYS:
                options = list(self.OPTIONS.keys())
                random_choice = random.choice(options)
                weight_key = f"{key} Weight"
                if prompt_parts[str(int(random_choice))] == 0.0:
                    weight = random.uniform(-1.0, 1.0)
                    prompt_parts[random_choice] = weight

        layer_weights = ','.join(f"{k}:{int(v)}" if v in {-1.0, 0.0, 1.0} else f"{k}:{v:.1f}" for k, v in prompt_parts.items())
        return (layer_weights,)

class EGIPAdapter_Mad_AssistantV2:
    CATEGORY_KEYS = ['0layer', '1layer', '2layer', '3layer', '4layer', '5layer', '6layer', '7layer', '8layer', '9layer', '10layer', '11layer']
    OPTIONS = {str(i): str(i) for i in range(0, 12)}

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                **cls.get_input_types_from_keys(cls.CATEGORY_KEYS),
                "Random": (["Yes", "No"], {"default": "No"}),
                "seed": ("INT", {"default": 0, "min": -1125899906842624, "max": 1125899906842624}),
            }
        }

    @staticmethod
    def get_input_types_from_keys(keys):
        input_types = {}
        for i, key in enumerate(keys):
            # Hide the super key by not including it in the input_types dictionary
            input_types[f"{key} Weight"] = ("FLOAT", {"default": 0.0, "min": -2.0, "max": 2.0, "step": 0.1, "display": "slider"})
        return input_types

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("layer_weights",)
    FUNCTION = "generate_prompt"
    CATEGORY = "ipadapter"

    def generate_prompt(self, **kwargs):
        prompt_parts = {str(i): 0.0 for i in range(0, 12)}
        for i, key in enumerate(self.CATEGORY_KEYS):
            # Since the super key is hidden, we use the index to find the corresponding weight
            weight_key = f"{key} Weight"
            if weight_key in kwargs and kwargs[weight_key] is not None:
                weight = kwargs[weight_key]
                prompt_parts[str(i)] = weight
        
        if kwargs.get("Random") == "Yes":
            for key in self.CATEGORY_KEYS:
                options = list(self.OPTIONS.keys())
                random_choice = random.choice(options)
                weight_key = f"{key} Weight"
                if prompt_parts[str(int(random_choice))] == 0.0:
                    weight = random.uniform(-2.0, 2.0)
                    prompt_parts[random_choice] = weight

        layer_weights = ','.join(f"{k}:{int(v)}" if v in {-2.0, -1.0, 0.0, 1.0, 2.0} else f"{k}:{v:.1f}" for k, v in prompt_parts.items())
        return (layer_weights,)

class EGIPAdapter_Mad_AssistantV3:
    CATEGORY_KEYS = ['0layer', '1layer', '2layer', '3layer', '4layer', '5layer', '6layer', '7layer', '8layer', '9layer', '10layer', '11layer']
    OPTIONS = {str(i): str(i) for i in range(0, 12)}

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                **cls.get_input_types_from_keys(cls.CATEGORY_KEYS),
                "Random": (["Yes", "No"], {"default": "No"}),
                "seed": ("INT", {"default": 0, "min": -1125899906842624, "max": 1125899906842624}),
            }
        }

    @staticmethod
    def get_input_types_from_keys(keys):
        input_types = {}
        for i, key in enumerate(keys):
            # Hide the super key by not including it in the input_types dictionary
            input_types[f"{key} Weight"] = ("FLOAT", {"default": 0.0, "min": -3.0, "max": 3.0, "step": 0.1, "display": "slider"})
        return input_types

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("layer_weights",)
    FUNCTION = "generate_prompt"
    CATEGORY = "ipadapter"

    def generate_prompt(self, **kwargs):
        prompt_parts = {str(i): 0.0 for i in range(0, 12)}
        for i, key in enumerate(self.CATEGORY_KEYS):
            # Since the super key is hidden, we use the index to find the corresponding weight
            weight_key = f"{key} Weight"
            if weight_key in kwargs and kwargs[weight_key] is not None:
                weight = kwargs[weight_key]
                prompt_parts[str(i)] = weight
        
        if kwargs.get("Random") == "Yes":
            for key in self.CATEGORY_KEYS:
                options = list(self.OPTIONS.keys())
                random_choice = random.choice(options)
                weight_key = f"{key} Weight"
                if prompt_parts[str(int(random_choice))] == 0.0:
                    weight = random.uniform(-3.0, 3.0)
                    prompt_parts[random_choice] = weight

        layer_weights = ','.join(f"{k}:{int(v)}" if v in {-3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0} else f"{k}:{v:.1f}" for k, v in prompt_parts.items())
        return (layer_weights,)

class EGIPAdapter_Mad_AssistantV4:
    CATEGORY_KEYS = ['0layer', '1layer', '2layer', '3layer', '4layer', '5layer', '6layer', '7layer', '8layer', '9layer', '10layer', '11layer']
    OPTIONS = {str(i): str(i) for i in range(0, 12)}

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                **cls.get_input_types_from_keys(cls.CATEGORY_KEYS),
                "Random": (["Yes", "No"], {"default": "No"}),
                "seed": ("INT", {"default": 0, "min": -1125899906842624, "max": 1125899906842624}),
            }
        }

    @staticmethod
    def get_input_types_from_keys(keys):
        input_types = {}
        for i, key in enumerate(keys):
            # Hide the super key by not including it in the input_types dictionary
            input_types[f"{key} Weight"] = ("FLOAT", {"default": 0.0, "min": -4.0, "max": 4.0, "step": 0.1, "display": "slider"})
        return input_types

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("layer_weights",)
    FUNCTION = "generate_prompt"
    CATEGORY = "ipadapter"

    def generate_prompt(self, **kwargs):
        prompt_parts = {str(i): 0.0 for i in range(0, 12)}
        for i, key in enumerate(self.CATEGORY_KEYS):
            # Since the super key is hidden, we use the index to find the corresponding weight
            weight_key = f"{key} Weight"
            if weight_key in kwargs and kwargs[weight_key] is not None:
                weight = kwargs[weight_key]
                prompt_parts[str(i)] = weight
        
        if kwargs.get("Random") == "Yes":
            for key in self.CATEGORY_KEYS:
                options = list(self.OPTIONS.keys())
                random_choice = random.choice(options)
                weight_key = f"{key} Weight"
                if prompt_parts[str(int(random_choice))] == 0.0:
                    weight = random.uniform(-4.0, 4.0)
                    prompt_parts[random_choice] = weight

        layer_weights = ','.join(f"{k}:{int(v)}" if v in {-4.0,-3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0} else f"{k}:{v:.1f}" for k, v in prompt_parts.items())
        return (layer_weights,)

class EGIPAdapter_Mad_AssistantV5:
    CATEGORY_KEYS = ['0layer', '1layer', '2layer', '3layer', '4layer', '5layer', '6layer', '7layer', '8layer', '9layer', '10layer', '11layer']
    OPTIONS = {str(i): str(i) for i in range(0, 12)}

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                **cls.get_input_types_from_keys(cls.CATEGORY_KEYS),
                "Random": (["Yes", "No"], {"default": "No"}),
                "seed": ("INT", {"default": 0, "min": -1125899906842624, "max": 1125899906842624}),
            }
        }

    @staticmethod
    def get_input_types_from_keys(keys):
        input_types = {}
        for i, key in enumerate(keys):
            # Hide the super key by not including it in the input_types dictionary
            input_types[f"{key} Weight"] = ("FLOAT", {"default": 0.0, "min": -5.0, "max": 5.0, "step": 0.1, "display": "slider"})
        return input_types

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("layer_weights",)
    FUNCTION = "generate_prompt"
    CATEGORY = "ipadapter"

    def generate_prompt(self, **kwargs):
        prompt_parts = {str(i): 0.0 for i in range(0, 12)}
        for i, key in enumerate(self.CATEGORY_KEYS):
            # Since the super key is hidden, we use the index to find the corresponding weight
            weight_key = f"{key} Weight"
            if weight_key in kwargs and kwargs[weight_key] is not None:
                weight = kwargs[weight_key]
                prompt_parts[str(i)] = weight
        
        if kwargs.get("Random") == "Yes":
            for key in self.CATEGORY_KEYS:
                options = list(self.OPTIONS.keys())
                random_choice = random.choice(options)
                weight_key = f"{key} Weight"
                if prompt_parts[str(int(random_choice))] == 0.0:
                    weight = random.uniform(-5.0, 5.0)
                    prompt_parts[random_choice] = weight

        layer_weights = ','.join(f"{k}:{int(v)}" if v in {-5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0} else f"{k}:{v:.1f}" for k, v in prompt_parts.items())
        return (layer_weights,)

class EGIPAdapter_Mad_AssistantV6:
    CATEGORY_KEYS = ['0layer', '1layer', '2layer', '3layer', '4layer', '5layer', '6layer', '7layer', '8layer', '9layer', '10layer', '11layer']
    OPTIONS = {str(i): str(i) for i in range(0, 12)}

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                **cls.get_input_types_from_keys(cls.CATEGORY_KEYS),
                "Random": (["Yes", "No"], {"default": "No"}),
                "seed": ("INT", {"default": 0, "min": -1125899906842624, "max": 1125899906842624}),
            }
        }

    @staticmethod
    def get_input_types_from_keys(keys):
        input_types = {}
        for i, key in enumerate(keys):
            # Hide the super key by not including it in the input_types dictionary
            input_types[f"{key} Weight"] = ("FLOAT", {"default": 0.0, "min": -5.0, "max": 5.0, "step": 0.1})
        return input_types

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("layer_weights",)
    FUNCTION = "generate_prompt"
    CATEGORY = "ipadapter"

    def generate_prompt(self, **kwargs):
        prompt_parts = {str(i): 0.0 for i in range(0, 12)}
        for i, key in enumerate(self.CATEGORY_KEYS):
            # Since the super key is hidden, we use the index to find the corresponding weight
            weight_key = f"{key} Weight"
            if weight_key in kwargs and kwargs[weight_key] is not None:
                weight = kwargs[weight_key]
                prompt_parts[str(i)] = weight
        
        if kwargs.get("Random") == "Yes":
            for key in self.CATEGORY_KEYS:
                options = list(self.OPTIONS.keys())
                random_choice = random.choice(options)
                weight_key = f"{key} Weight"
                if prompt_parts[str(int(random_choice))] == 0.0:
                    weight = random.uniform(-5.0, 5.0)
                    prompt_parts[random_choice] = weight

        layer_weights = ','.join(f"{k}:{int(v)}" if v in {-5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0} else f"{k}:{v:.1f}" for k, v in prompt_parts.items())
        return (layer_weights,)

NODE_CLASS_MAPPINGS = {
    "EGIPAdapter_Mad_Assistant": EGIPAdapter_Mad_Assistant,
    "EGIPAdapter_Mad_AssistantV1": EGIPAdapter_Mad_AssistantV1,
    "EGIPAdapter_Mad_AssistantV2": EGIPAdapter_Mad_AssistantV2,
    "EGIPAdapter_Mad_AssistantV3": EGIPAdapter_Mad_AssistantV3,
    "EGIPAdapter_Mad_AssistantV4": EGIPAdapter_Mad_AssistantV4,
    "EGIPAdapter_Mad_AssistantV5": EGIPAdapter_Mad_AssistantV5,
    "EGIPAdapter_Mad_AssistantV6": EGIPAdapter_Mad_AssistantV6
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "EGIPAdapter_Mad_Assistant": "IPAdapter Mad Assistant",
    "EGIPAdapter_Mad_AssistantV1": "IPAdapter Mad Assistant V1",
    "EGIPAdapter_Mad_AssistantV2": "IPAdapter Mad Assistant V2",
    "EGIPAdapter_Mad_AssistantV3": "IPAdapter Mad Assistant V3",
    "EGIPAdapter_Mad_AssistantV4": "IPAdapter Mad Assistant V4",
    "EGIPAdapter_Mad_AssistantV5": "IPAdapter Mad Assistant V5",
    "EGIPAdapter_Mad_AssistantV6": "IPAdapter Mad Assistant V6"
}
