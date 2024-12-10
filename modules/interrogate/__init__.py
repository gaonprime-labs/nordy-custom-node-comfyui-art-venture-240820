from .blip_node import BlipLoader, BlipCaption
from .danbooru import DeepDanbooruCaption

NODE_CLASS_MAPPINGS = {
    "BLIPLoader_legacy_ccc62030": BlipLoader,
    "BLIPCaption_legacy_ccc62030": BlipCaption,
    "DeepDanbooruCaption_legacy_ccc62030": DeepDanbooruCaption,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "BLIPLoader_legacy_ccc62030": "BLIP Loader (legacy_ccc62030)",
    "BLIPCaption_legacy_ccc62030": "BLIP Caption (legacy_ccc62030)",
    "DeepDanbooruCaption_legacy_ccc62030": "Deep Danbooru Caption (legacy_ccc62030)",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
