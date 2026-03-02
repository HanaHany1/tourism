import glob
import os

def create_arabic_files():
    # List of English files to convert
    english_files = [
        'index.html', 'about.html', 'contact.html', 'destinations.html',
        'hospitals.html', 'packages.html', 'treatments.html'
    ]

    for file in english_files:
        if os.path.exists(file):
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Change to Arabic/RTL
            content = content.replace('<html lang="en">', '<html lang="ar" dir="rtl">')
            
            # Inject Cairo Font
            cairo_font = '<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap" rel="stylesheet">'
            if '</head>' in content:
                content = content.replace('</head>', f'    <!-- Arabic Font -->\n    {cairo_font}\n</head>')

            # Update Language Toggle in content
            # This looks for the nav-actions area to ensure the Arabic toggle is active
            if 'EN | العربية' in content:
                content = content.replace('EN | العربية', '<a href="{0}.html">EN</a> | <a href="{0}-ar.html" class="active">العربية</a>'.format(file.replace('.html', '')))
            
            # Create the -ar.html file
            ar_filename = file.replace('.html', '-ar.html')
            with open(ar_filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Created {ar_filename}")

if __name__ == "__main__":
    create_arabic_files()
