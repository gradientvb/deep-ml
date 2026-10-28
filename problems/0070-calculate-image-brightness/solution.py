def calculate_brightness(img: list[list[int]]) -> float:
    # Validate: must be non-empty, rectangular, and pixel values in [0, 255]
    if not img or not img[0]:
        return -1
    width = len(img[0])
    total = 0
    count = 0
    for row in img:
        if len(row) != width:
            return -1
        for p in row:
            if not (0 <= p <= 255):
                return -1
            total += p
            count += 1
    return round(total / count, 2)