from config import CHUNK_SIZE, CHUNK_OVERLAP


def split_text(text):

    if not text.strip():
        return []

    chunks = []
    start = 0

    while start < len(text):

        end = min(start + CHUNK_SIZE, len(text))

        if end < len(text):

            boundary = text.rfind("\n", start, end)

            if boundary == -1:
                boundary = text.rfind(" ", start, end)

            if boundary > start:
                end = boundary

        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        if end >= len(text):
            break

        start = max(end - CHUNK_OVERLAP, start + 1)

    return chunks