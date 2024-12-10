from .segmenter import ISNetLoader, ISNetSegment

NODE_CLASS_MAPPINGS = {
    "ISNetLoader_legacy_ccc62030": ISNetLoader,
    "ISNetSegment_legacy_ccc62030": ISNetSegment,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "ISNetLoader_legacy_ccc62030": "ISNet Loader (legacy_ccc62030)",
    "ISNetSegment_legacy_ccc62030": "ISNet Segment (legacy_ccc62030)",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
