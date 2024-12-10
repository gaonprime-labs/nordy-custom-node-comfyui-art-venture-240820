from .color_blend import ColorBlend
from .color_correct import ColorCorrect

NODE_CLASS_MAPPINGS = {
    "ColorBlend_legacy_ccc62030": ColorBlend,
    "ColorCorrect_legacy_ccc62030": ColorCorrect,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ColorBlend_legacy_ccc62030": "Color Blend (legacy_ccc62030)",
    "ColorCorrect_legacy_ccc62030": "Color Correct (legacy_ccc62030)",
}
