#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

# Create a new image with a gradient background
size = 1024
img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Create a rounded rectangle background with a nice gradient-like effect
# Using a deep blue to purple gradient simulation
margin = 100
corner_radius = 200

# Draw rounded rectangle background
def draw_rounded_rectangle(draw, xy, radius, fill):
    x1, y1, x2, y2 = xy
    draw.rectangle([x1 + radius, y1, x2 - radius, y2], fill=fill)
    draw.rectangle([x1, y1 + radius, x2, y2 - radius], fill=fill)
    draw.pieslice([x1, y1, x1 + 2 * radius, y1 + 2 * radius], 180, 270, fill=fill)
    draw.pieslice([x2 - 2 * radius, y1, x2, y1 + 2 * radius], 270, 360, fill=fill)
    draw.pieslice([x1, y2 - 2 * radius, x1 + 2 * radius, y2], 90, 180, fill=fill)
    draw.pieslice([x2 - 2 * radius, y2 - 2 * radius, x2, y2], 0, 90, fill=fill)

# Draw background with gradient effect (simulated with multiple layers)
colors = [
    (70, 130, 180),   # Steel blue
    (65, 105, 225),   # Royal blue
    (75, 0, 130),     # Indigo
]

# Draw main background
draw_rounded_rectangle(draw, (margin, margin, size - margin, size - margin), 
                       corner_radius, colors[1])

# Try to use a system font, fall back to default if not available
try:
    # Try different font options
    font_size = 600
    font_paths = [
        '/System/Library/Fonts/Helvetica.ttc',
        '/System/Library/Fonts/Avenir.ttc',
        '/Library/Fonts/Arial.ttf',
        '/System/Library/Fonts/Supplemental/Arial.ttf'
    ]
    
    font = None
    for font_path in font_paths:
        if os.path.exists(font_path):
            try:
                font = ImageFont.truetype(font_path, font_size)
                break
            except:
                continue
    
    if font is None:
        # Use default font if no system fonts work
        font = ImageFont.load_default()
        print("Warning: Using default font, text may be small")
except:
    font = ImageFont.load_default()
    print("Warning: Using default font, text may be small")

# Draw the letter "R" in white
text = "R"
# Get text bounding box
bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

# Center the text
x = (size - text_width) // 2
y = (size - text_height) // 2 - 50  # Slight upward adjustment for visual balance

# Add a subtle shadow
shadow_offset = 8
draw.text((x + shadow_offset, y + shadow_offset), text, font=font, fill=(0, 0, 0, 100))

# Draw the main text
draw.text((x, y), text, font=font, fill=(255, 255, 255, 255))

# Save the image
output_path = 'src-tauri/icons/icon_new.png'
img.save(output_path, 'PNG')
print(f"Icon created successfully at {output_path}")
print(f"Icon size: {size}x{size}")
