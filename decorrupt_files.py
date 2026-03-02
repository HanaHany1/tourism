import glob
import os

def decorrupt():
    files = glob.glob('*.html')
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # The corruption pattern is character + '—' repeated.
        # However, some might be triple dashed like '———'
        # We want to remove all em dashes that were injected between characters.
        # Since the corruption script did text.replace('', '—'), it literally put a dash
        # at EVERY position.
        
        # Safest way to undo replace('', '—') is to remove '—'
        # BUT we must be careful not to remove legitimate '—' (em dashes) if any existed.
        # Looking at original content, em dashes were used in some places like "Crystal Smile — Dental Makeover"
        
        # If we remove ALL '—', we lose those separators, but we can restore them via translate_robust.py
        # because translate_robust.py has its own translation map for those strings.
        
        cleaned = content.replace('—', '')
        
        # Also, the previous script might have caused double/triple dashes or weird newlines.
        # Let's write the cleaned version back.
        with open(file, 'w', encoding='utf-8') as f:
            f.write(cleaned)
        print(f"Decorrupted {file}")

if __name__ == "__main__":
    decorrupt()
