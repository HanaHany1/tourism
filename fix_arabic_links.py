import glob
import re

translations = {
    # Desktop Nav Links
    '>Home<': '>الرئيسية<',
    '>Treatments<': '>العلاجات<',
    '>Packages<': '>الباقات<',
    '>Destinations<': '>الوجهات<',
    '>Hospitals<': '>المستشفيات<',
    '>About Us<': '>من نحن<',
    '>Contact<': '>اتصل بنا<',
    
    # Common text
    'Get Free Quote': 'احصل على عرض سعر',
    'Your trusted partner for world-class medical treatments abroad.': 'شريكك الموثوق لعلاجات طبية عالمية المستوى في الخارج.',
    
    # Footer
    'Quick Links': 'روابط سريعة',
    'Top Destinations': 'أفضل الوجهات',
    'All rights reserved.': 'جميع الحقوق محفوظة.',
    'Privacy': 'الخصوصية',
    'Terms': 'الشروط',
    
    # Fix Destinations side bug
    'Cairo': 'القاهرة',
    'Alexandria': 'الإسكندرية',
    'Sharm El Sheikh': 'شرم الشيخ',
    'Hurghada': 'الغردقة',
    'Luxor': 'الأقصر',
    'Aswan': 'أسوان',
    'Fayoum': 'الفيوم',
    'Ain Sokhna': 'العين السخنة'
}

for ar_file in glob.glob('*-ar.html'):
    with open(ar_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Apply text translations
    for eng, ara in translations.items():
        content = content.replace(eng, ara)
        
    # Fix the links to point to -ar versions
    pages = ['index', 'treatments', 'packages', 'destinations', 'hospitals', 'about', 'contact']
    
    for page in pages:
        # Avoid creating index-ar-ar.html
        content = re.sub(f'href="{page}.html"', f'href="{page}-ar.html"', content)
        
    # Exceptional case: Language toggle EN button should remain pointing to .html
    for page in pages:
        # Find exactly the EN toggle link and revert it back to English target
        content = re.sub(f'href="{page}-ar.html"([^>]*>EN</a>)', f'href="{page}.html"\\1', content)

    # Some additional missed text in headers etc
    content = content.replace("Medical Tourism Destinations", "وجهات السياحة العلاجية")
    content = content.replace("Explore", "استكشف")
    content = content.replace("Top <span class=\"text-primary\">Medical Destinations</span>", "أفضل <span class=\"text-primary\">الوجهات الطبية</span>")
    content = content.replace("Our Global <span style=\"color:var(--clr-accent)\">Footprint</span>", "بصمتنا <span style=\"color:var(--clr-accent)\">العالمية</span>")
    content = content.replace("Countries", "دول")
    content = content.replace("Partner Hospitals", "مستشفيات شريكة")
    content = content.replace("Certified Doctors", "أطباء معتمدون")
    content = content.replace("Patients Served", "مرضى تمت خدمتهم")
    content = content.replace("Why Abroad?", "لماذا في الخارج؟")
    content = content.replace("Benefits of Medical <span class=\"text-primary\">Tourism</span>", "فوائد السياحة <span class=\"text-primary\">العلاجية</span>")
    content = content.replace("Dramatic Cost Savings", "توفير هائل في التكاليف")
    content = content.replace("No Waiting Lists", "لا قوائم انتظار")
    content = content.replace("World-Class Surgeons", "جراحون عالميون")
    content = content.replace("Recovery in Paradise", "التعافي في الجنة")
    content = content.replace("Cultural Enrichment", "إثراء ثقافي")
    content = content.replace("Privacy &amp; Discretion", "الخصوصية والسرية")
    content = content.replace("Privacy & Discretion", "الخصوصية والسرية")

    with open(ar_file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Links and remaining text fixed in Arabic files.")
