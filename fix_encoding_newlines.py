import glob
import os

def fix_files():
    for file in glob.glob('*-ar.html') + glob.glob('*.html'):
        if os.path.exists(file):
            with open(file, 'rb') as f:
                content = f.read()
            
            # Try to decode and clean
            try:
                text = content.decode('utf-8')
            except UnicodeDecodeError:
                # Fallback to latin-1 if utf-8 fails, then encode back to utf-8 properly
                text = content.decode('latin-1')

            # Replace the weird diamond question mark characters if they appear as strings
            # text = text.replace('', '—') # DELETED: This line caused corruption by inserting dashes between every character
            text = text.replace('ممتاز', 'ممتاز') # Ensure Arabic is clean
            
            # Remove excessive newlines (more than 2)
            lines = text.splitlines()
            cleaned_lines = []
            for line in lines:
                if line.strip() == "" and cleaned_lines and cleaned_lines[-1].strip() == "":
                    continue
                cleaned_lines.append(line)
            
            text = "\n".join(cleaned_lines)
            
            with open(file, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"Fixed {file}")

if __name__ == "__main__":
    fix_files()
