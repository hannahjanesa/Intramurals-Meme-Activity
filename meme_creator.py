from PIL import Image, ImageDraw, ImageFont

# Load your background image
img = Image.open("background.jpg")
draw = ImageDraw.Draw(img)

# Try to use bold font, fallback to default
try:
    font_big = ImageFont.truetype("arialbd.ttf", 80)   # Bold Arial for title
    font = ImageFont.truetype("arial.ttf", 40)         # Regular for meme text
except:
    font_big = ImageFont.load_default()
    font = ImageFont.load_default()

# --- Text contents ---
title_text = "INTRAMURALS 2025"
top_text = "Instructor at the back: ‘Again, but with energy!"
bottom_text = "Students: dying under the sun 🌞💀 😅"

# --- Helper function to draw text with outline ---
def draw_text_with_outline(draw, position, text, font, fill, outline="black", outline_width=2):
    x, y = position
    # Draw outline
    for dx in range(-outline_width, outline_width + 1):
        for dy in range(-outline_width, outline_width + 1):
            if dx != 0 or dy != 0:
                draw.text((x + dx, y + dy), text, font=font, fill=outline)
    # Draw main text
    draw.text((x, y), text, font=font, fill=fill)

# --- Draw Center Title (rainbow colors per letter) ---
colors = ["red", "orange", "yellow", "green", "blue", "purple", "cyan", "magenta"]
letter_spacing = 5

# Calculate total width of the title for centering
total_width = sum(draw.textlength(ch, font=font_big) + letter_spacing for ch in title_text)
title_x = (img.width - total_width) // 2
title_y = img.height // 2 - 50

# Draw each letter with a different color
x = title_x
for i, ch in enumerate(title_text):
    color = colors[i % len(colors)]
    draw_text_with_outline(draw, (x, title_y), ch, font_big, fill=color, outline="black", outline_width=3)
    x += draw.textlength(ch, font=font_big) + letter_spacing

# --- Draw Top Text (centered) ---
top_x = (img.width - draw.textlength(top_text, font=font)) // 2
draw_text_with_outline(draw, (top_x, 30), top_text, font, fill="white")

# --- Draw Bottom Text (centered) ---
bottom_x = (img.width - draw.textlength(bottom_text, font=font)) // 2
draw_text_with_outline(draw, (bottom_x, img.height - 80), bottom_text, font, fill="white")

# --- Save Final Output ---
img.save("BSCS3A_SarigumbaHannah_Activity1.jpg", "JPEG")
print("✅ Meme created successfully! Check your folder for BSCS3A_SarigumbaHannah_Activity1.jpg")
