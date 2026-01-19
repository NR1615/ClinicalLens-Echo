import os
import base64
import io
from PIL import Image
import anthropic

def encode_image_to_base64(image_path: str) -> tuple[str, str]:
    with open(image_path, "rb") as f:
        image_bytes = f.read()

    image = Image.open(io.BytesIO(image_bytes))

    format_map = {
        "JPEG": "image/jpeg",
        "PNG": "image/png",
        "WEBP": "image/webp",
        "GIF": "image/gif",
    }

    media_type = format_map.get(image.format)
    if not media_type:
        raise RuntimeError(f"Unsupported image format: {image.format}")

    image_base64 = base64.b64encode(image_bytes).decode("utf-8")
    return image_base64, media_type


def analyze_image_with_query(Query: str, image_base64: str, media_type: str) -> str:
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY not found")

    client = anthropic.Anthropic(api_key=api_key)

    chunks = []
    with client.messages.stream(
        model="claude-sonnet-4-5-20250929",
        max_tokens=1024,
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": media_type,
                            "data": image_base64,
                        },
                    },
                    {"type": "text", "text": Query},
                ],
            }
        ],
    ) as stream:
        for text in stream.text_stream:
            chunks.append(text)

    return "".join(chunks)
