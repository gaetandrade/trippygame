# backend/src/ai_core/models.py
from typing import List, Dict, Any, Optional
from enum import Enum

class ModelProvider(Enum):
    HUGGING_FACE = "hugging_face"
    OPENAI = "openai"
    LOCAL = "local"
    CUSTOM_API = "custom_api"

class ModelType(Enum):
    TEXT_TO_IMAGE = "text_to_image"
    TEXT_TO_AUDIO = "text_to_audio"
    TEXT_GENERATION = "text_generation"
    AUDIO_TO_TEXT = "audio_to_text"
    # Add more types as needed

class AIModel:
    """
    Represents a generic AI model.
    """
    def __init__(self,
                 model_id: str,
                 name: str,
                 description: str,
                 model_type: ModelType,
                 provider: ModelProvider,
                 config: Optional[Dict[str, Any]] = None):
        self.model_id = model_id  # Unique identifier for the model
        self.name = name          # User-friendly name
        self.description = description
        self.model_type = model_type
        self.provider = provider
        self.config = config if config else {} # Provider-specific config (API keys, paths, etc.)
        self.variants: List[ModelVariant] = []

    def add_variant(self, variant: 'ModelVariant'):
        self.variants.append(variant)

    def __repr__(self):
        return f"<AIModel(id='{self.model_id}', name='{self.name}', type='{self.model_type.value}')>"

class ModelVariant:
    """
    Represents a specific version or fine-tuned instance of an AIModel.
    """
    def __init__(self,
                 variant_id: str,
                 model: AIModel,
                 version: str,
                 source_url: Optional[str] = None, # e.g., Hugging Face model hub URL, local path
                 parameters: Optional[Dict[str, Any]] = None): # Default generation parameters
        self.variant_id = variant_id # Unique identifier for the variant
        self.model = model
        self.version = version
        self.source_url = source_url
        self.parameters = parameters if parameters else {}
        # Potentially add performance metrics, deployment status etc. here later

    def __repr__(self):
        return f"<ModelVariant(id='{self.variant_id}', model='{self.model.name}', version='{self.version}')>"

# Example Usage (for illustration, not part of the core classes)
if __name__ == '__main__':
    # Generic Stable Diffusion model
    sd_model = AIModel(model_id="stable-diffusion",
                       name="Stable Diffusion",
                       description="Text-to-image generation model.",
                       model_type=ModelType.TEXT_TO_IMAGE,
                       provider=ModelProvider.HUGGING_FACE)

    # Specific variant of Stable Diffusion
    sd_variant_1_5 = ModelVariant(variant_id="sd-1-5",
                                  model=sd_model,
                                  version="1.5",
                                  source_url="runwayml/stable-diffusion-v1-5")
    sd_model.add_variant(sd_variant_1_5)

    print(sd_model)
    print(sd_variant_1_5)
