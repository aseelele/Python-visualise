# generate_slides.py

import os

# --- Configuration ---
# This path is relative to your index.html file, which is in the project root.
# It should point to where you copied your 'presentation' folder in Step 2.1.
IMAGE_FOLDER_RELATIVE_PATH = "img/presentation/"

# Prefix of your image files (e.g., "Slide" for Slide1.PNG)
IMAGE_PREFIX = "Slide"

# File extension of your images (e.g., "PNG")
IMAGE_EXTENSION = "PNG"

# Total number of slides (you have 80)
NUM_SLIDES = 80

# --- HTML Generation ---
html_output = []

for i in range(1, NUM_SLIDES + 1):
    image_filename = f"{IMAGE_PREFIX}{i}.{IMAGE_EXTENSION}"
    full_image_path = f"{IMAGE_FOLDER_RELATIVE_PATH}{image_filename}"

    # You can customize the title for each slide
    slide_title = f"Python Tutor Visualization: Step {i}"

    # Generate the HTML for each slide
    # The 'style' attribute helps images fit the slide area
    slide_html = f"""
        <section>
            <h2>{slide_title}</h2>
            <img src="{full_image_path}" alt="{slide_title}" style="max-width: 90%; max-height: 80vh; margin: auto; display: block;">
            <!-- Optional: Add more text or captions here if needed for specific slides -->
        </section>
    """
    html_output.append(slide_html)

# Print the generated HTML to the console
# You will copy this output and paste it into your index.html
for line in html_output:
    print(line)

print("\n--- HTML Generation Complete ---")
print("Copy the output above and paste it into the <div class=\"slides\"> section of your index.html.")