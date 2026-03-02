import glob
import re

translations = {
    # packages.html
    "الكل-Inclusive Medical Packages": "باقات طبية شاملة",
    "Treatment + hotel + transfers + optional tours — everything bundled at transparent prices, no hidden fees.": "العلاج + الفندق + التنقلات + الجولات الاختيارية — كل شيء مجمع بأسعار شفافة، بدون رسوم خفية.",
    "Choose Your <span class=\"text-primary\">Perfect Package</span>": "اختر <span class=\"text-primary\">باقتك المثالية</span>",
    "Every package is fully customizable. Contact us for a bespoke quote.": "كل باقة قابلة للتخصيص بالكامل. اتصل بنا للحصول على عرض سعر مخصص.",
    "Crystal Smile — أسنان Makeover": "ابتسامة كريستال — تجميل الأسنان",
    "Full mouth E-max veneer set (10—20 units)": "طقم قشور إيماكس كامل للفم (10-20 وحدة)",
    "7 nights at 5★ Nile view hotel": "7 ليالي في فندق 5 نجوم مطل على النيل",
    "VIP airport pickup & all clinic transfers": "استقبال VIP من المطار وجميع تنقلات العيادة",
    "Optional Pyramids & القاهرة city tour": "جولة اختيارية في الأهرامات ومدينة القاهرة",
    "Dedicated bilingual coordinator": "منسق ثنائي اللغة مخصص",
    "International travel & medical insurance": "تأمين سفر وطبي دولي",
    "Glow Retreat — تجميل Surgery": "منتجع التوهج — جراحة التجميل",
    "Rhinoplasty or liposuction (choice)": "تجميل الأنف أو شفط الدهون (حسب الاختيار)",
    "14 nights Red Sea luxury recovery resort": "14 ليلة ترفيهية للاستشفاء في منتجع بالبحر الأحمر",
    "Daily spa & massage access": "دخول يومي للسبا والمساج",
    "Airport transfer + clinical transport": "النقل من المطار + النقل للعيادة",
    "Optional desert safari & snorkeling": "سفاري صحراوي وغوص اختياري",
    "Post-op follow-up consultations x3": "3 استشارات متابعة بعد العملية",
    "Renewed Motion — Joint Replacement": "حركة متجددة — استبدال المفاصل",
    "Total knee or hip replacement surgery": "جراحة استبدال الركبة أو الورك بالكامل",
    "21 nights Mediterranean recovery hotel + physiotherapy": "21 ليلة في فندق استشفاء على البحر المتوسط + علاج طبيعي",
    "Daily physio sessions (12 total)": "جلسات علاج طبيعي يومية (12 إجمالاً)",
    "Private ambulance & all transfers": "إسعاف خاص وجميع التنقلات",
    "Optional الإسكندرية library & city tour when mobile": "جولة اختيارية في مكتبة الإسكندرية ومدينة الإسكندرية التراثية",
    "12-month online aftercare program": "برنامج رعاية بعد العملية عبر الإنترنت لمدة 12 شهرًا",
    "Heart Strong — قلب Care": "قلب قوي — رعاية القلب",
    "Coronary bypass (CABG) or angioplasty": "تحويل مسار الشريان التاجي أو القسطرة",
    "14 nights hospital recovery room": "14 ليلة في غرفة إفاقة بالمستشفى",
    "Full cardiac rehabilitation program": "برنامج إعادة تأهيل قلبي كامل",
    "Dedicated ICU nursing staff": "طاقم تمريض مخصص للعناية المركزة",
    "Airport & hospital transfers": "النقل بين المطار والمستشفى",
    "1-year telemedicine follow-up": "متابعة عبر التطبيب عن بعد لمدة سنة",
    "الكل-inclusive من": "باقات شاملة تبدأ من",
    "Book Now": "احجز الآن",
    "Most Popular": "الأكثر شعبية",
    "Premium": "ممتاز",
    "Basic": "أساسي",
    "VIP": "شخصيات هامة",
    "Compare Packages": "مقارنـة الباقات",
    "Medical Procedure": "الإجراء الطبي",
    
    # about.html
    "About Medora": "عن ميدورا",
    "We exist to make world-class healthcare accessible, affordable, and stress-free for everyone — wherever they are.": "نحن هنا لجعل الرعاية الصحية العالمية بمتناول الجميع، وبأسعار معقولة، وخالية من التوتر — أينما كانوا.",
    "Healthcare Without <span class=\"text-primary\">Borders</span>": "رعاية صحية بلا <span class=\"text-primary\">حدود</span>",
    'Medora was founded by a team of medical professionals, travel experts, and patient advocates who believed one simple truth: <strong style="color:var(--clr-navy)">no one should be denied excellent healthcare because of geography or cost.</strong>': 'تأسست ميدورا على يد فريق من المتخصصين الطبيين، وخبراء السفر، والمدافعين عن حقوق المرضى الذين آمنوا بحقيقة واحدة بسيطة: <strong style="color:var(--clr-navy)">لا ينبغي حرمان أي شخص من الرعاية الصحية الممتازة بسبب موقعه الجغرافي أو التكلفة.</strong>',
    "Over a decade later, we have helped more than 15,000 patients من 80+ countries access life-changing medical procedures — while experiencing the beauty and culture of some of the world's most extraordinary destinations.": "بعد أكثر من عقد، ساعدنا أكثر من 15,000 مريض من 80+ دولة في الوصول إلى إجراءات طبية غيّرت حياتهم — مع الاستمتاع بجمال وثقافة بعض أروع الوجهات في العالم.",
    "To connect patients with world-class, affordable healthcare — guided by trust, transparency, and compassion.": "ربط المرضى برعاية صحية عالمية المستوى وبأسعار معقولة — بتوجيه من الثقة، والشفافية، والتعاطف.",
    "A world where every person has access to excellent healthcare, regardless of where they live or what they earn.": "عالم يمتلك فيه كل شخص الحق في الوصول إلى رعاية صحية ممتازة، بغض النظر عن مكان إقامته أو دخله.",
    "What <span class=\"text-primary\">Drives</span> Us": "ما <span class=\"text-primary\">يحفزنا</span>",
    "Trust & Safety First": "الثقة والسلامة أولاً",
    "Every partner hospital is JCI-accredited, on-site inspected, and regularly reviewed. We never compromise on patient safety.": "جميع المستشفيات الشريكة معتمدة من JCI، وتخضع للتفتيش الميداني والمراجعة الدورية. نحن لا نساوم أبدًا على سلامة المرضى.",
    "Uncompromising Quality": "جودة لا مساومة عليها",
    "We partner only with hospitals ranked in the top 10% globally for clinical outcomes, patient satisfaction, and infrastructure.": "نحن نتشارك فقط مع المستشفيات المُصنفة ضمن أفضل 10% عالميًا من حيث النتائج السريرية، ورضا المرضى، والبنية التحتية.",
    "Patient-First Service": "خدمة تركز على المريض",
    "Your journey is unique. We tailor every package, provide 24/7 support, and treat every patient like a family member.": "رحلتك فريدة من نوعها. نحن نصمم كل باقة خصيصًا لك، ونقدم دعمًا على مدار الساعة، ونعامل كل مريض كفرد من العائلة.",
    "Full Transparency": "شفافية تامة",
    "No hidden fees, no surprise charges. Every cost — treatment, hotel, transfer, tour — is itemised and agreed upfront.": "لا رسوم خفية ولا تكاليف مفاجئة. يتم تفصيل جميع التكاليف والاتفاق عليها مسبقًا.",
    "Global Accessibility": "سهولة الوصول العالمية",
    "We speak 15+ languages and operate in 50+ countries to ensure no patient is left without guidance or support.": "نتحدث بأكثر من 15 لغة ونعمل في 50+ دولة لضمان عدم ترك أي مريض بدون توجيه أو دعم.",
    "Ethical & Sustainable": "أخلاقية ومستدامة",
    "We support local medical communities, choose eco-conscious hotels, and reinvest in global health equity initiatives.": "ندعم المجتمعات الطبية المحلية، ونختار فنادق صديقة للبيئة، ونعيد الاستثمار في مبادرات العدالة الصحية.",
    "A Decade of <span class=\"text-primary\">Impact</span>": "عقد من <span class=\"text-primary\">التأثير</span>",
    "Medora Founded": "تأسيس ميدورا",
    "Started in القاهرة with 5 top-tier partner hospitals and a dedicated medical coordinator team.": "بدأنا في القاهرة مع 5 مستشفيات شريكة عليا وفريق متخصص.",
    "Expanded to الإسكندرية & Red Sea": "توسعة إلى الإسكندرية والبحر الأحمر",
    "Launched exclusive recovery packages in الإسكندرية and شرم الشيخ.": "أطلقنا باقات استشفاء حصرية في الإسكندرية وشرم الشيخ.",
    "JCI Partnership Programme": "برنامج شراكة JCI",
    "Established our exclusive JCI accreditation audit programme, becoming the first medical tourism company to publish real outcomes data.": "أسسنا برنامج التدقيق لاعتماد JCI ونشرنا بيانات نتائج حقيقية.",
    "Cultural Tourism Integration": "دمج السياحة الثقافية",
    "Partnered with premium Egyptian tour operators to offer Pyramids and Nile Cruise recovery packages.": "شراكات مع وكالات سفر مصرية لتقديم باقات استشفاء في الأهرامات والنيل.",
    "Former head of international patient services at Acibadem Group. MD, Harvard Medical School.": "خدمات المرضى الدولية. دكتوراه في الطب، كلية الطب بجامعة هارفارد.",
    "15 years in global healthcare logistics. Former VP at International SOS. MBA, INSEAD.": "15 سنة في الخدمات اللوجستية الصحية العالمية وحاصل على ماجستير في إدارة الأعمال.",
    "JCI auditor & former NHS consultant. Oversees all hospital partnerships and clinical standards.": "مراجع JCI واستشاري سابق في المستشفيات، يشرف على المعايير السريرية.",
    "Specialist in international patient coordination. Personally oversees complex care pathways.": "أخصائي في تنسيق المرضى الدوليين. يشرف شخصياً على مسارات الرعاية المعقدة.",
    "Founded — Serving Patients Since": "تأسست — تخدم المرضى منذ",
    "Trust in International": "الثقة دولياً",
        
    # Destinations.html
    "Top Egyptian cities, 200+ hospitals — discover where world-class healthcare meets extraordinary travel.": "أفضل المدن المصرية، أكثر من 200 مستشفى — اكتشف حيث تلتقي الرعاية الصحية العالمية بالسفر الاستثنائي.",
    "Contact our destination team to match you with the perfect city and hospital for your procedure.": "تواصل مع فريقنا للوجهات لاختيار المدينة والمستشفى الأنسب لإجراءك الطبي.",
    "Plan Your Trip": "خطط لرحلتك",
    
    # Hospitals.html
    "Renowned for cardiology, oncology, and transplant surgeries. Egypt’s first JCI-accredited facility.": "مشهورة بأمراض القلب والأورام وجراحات الزراعة. أول منشأة بمصر تحصل على JCI.",
    "One of the largest private hospital networks in MENA, providing state-of-the-art multi-specialty care.": "واحدة من أكبر شبكات المستشفيات الخاصة بالشرق الأوسط، تقديم رعاية حديثة.",
    "A leader in comprehensive medical care, perfectly situated by the Nile with top-tier international standard.": "رائدة في الرعاية الطبية الشاملة والمطلة على النيل وفقاً للمعايير العالمية.",
    "Alexandria's top medical hub, specializing in minimally invasive procedures and excellent patient recovery.": "أهم مركز طبي في الإسكندرية متخصص في الإجراءات الدقيقة بامتياز للتعافي.",
    "Combine elite healthcare with resort living. Ideal for dialyses, cosmetic recovery, and orthopedics.": "اجمع بين الرعاية الممتازة ومنتجع سياحي مبهر للتعافي والتجميل وجراحة العظام.",
    "Premium boutique hospital inside the exclusive El Gouna resort town, blending European standards with Red Sea relaxation.": "مستشفى فاخرة داخل منتجع الجونة، تخلط بين المعايير الأوروبية والراحة في البحر الأحمر.",
    "Cardiology, Oncology, Orthopedics": "أمراض القلب والأورام وجراحة العظام",
    "General Surgery, Neurology, Orthopedics": "الجراحة العامة والمخ والأعصاب وجراحة العظام",
    "Spine Surgery, Cosmetic, Dental": "جراحة العمود الفقري والتجميل وطب الأسنان",
    "Cardiothoracic Surgery, Urology": "جراحة القلب الصدري والمسالك البولية",
    "Bariatrics, Cosmetic, Nephrology": "جراحات السمنة والتجميل وأمراض الكلى",
    "Orthopedics, Cosmetics, Dental": "جراحة العظام والتجميل وطب الأسنان",
    "Established": "تأسست عام",
    
    # Treatments.html
    "Browse our full catalogue — performed by board-certified specialists at JCI-accredited hospitals.": "تصفح الكتالوج الكامل المنجز بواسطة خبراء معتمدين في مستشفيات حاصلة على شهادة JCI.",
    "Transformative procedures by internationally trained plastic surgeons in accredited clinics across القاهرة, الإسكندرية, and شرم الشيخ.": "إجراءات غيّرت الحياة على يد جراحي تجميل مدربين دولياً في النخبة عبر القاهرة، الإسكندرية وعبر شرم الشيخ.",
    "Full-mouth makeovers, implants, and cosmetic dentistry — at 60—80% less than Western prices, using European-grade materials.": "تعديل كامل للفم والزراعة والتجميل بأسعار مخفضة بمواد أوروبية بنسبة 60-80% مقارنة بالغرب.",
    "Advanced joint replacement, spinal surgery, and sports medicine by fellowship-trained surgeons in top Egyptian orthopedic centers.": "استبدال المفاصل وجراحات العمود الفقري والطب الرياضي بأيدي أمهر الجراحين في مصر.",
    "Comprehensive cardiac care from world-renowned surgeons using the latest minimally-invasive and hybrid catheterization techniques.": "رعاية قلبية شاملة وأحدث تقنيات القسطرة الهجينة من أشهر جراحي العالم.",
    "Holistic health programs combining medical check-ups, detox retreats, and luxury spa experiences in Red Sea resorts and Nile cruises.": "برامج صحية متكاملة تضم الفحوصات والديتوكس ومنتجعات البحر الأحمر الفاخرة ورحلات النيل.",
    "Cutting-edge cancer diagnosis and treatment at internationally recognised cancer centres — proton therapy, immunotherapy, and targeted treatments.": "علاج وتشخيص السرطان في أفضل المراكز المعتمدة وبأحدث التكنولوجيا، الإشعاع، والمناعي.",
    "Yes — every partner hospital holds JCI accreditation and is regularly audited by our team.": "نعم – جميع المستشفيات الشريكة معتمدة من JCI والمراجعة باستمرار من قِبل فريقنا.",
    
    # Contact.html
    "Get a free, no-obligation treatment plan and quote within 24 hours. Our global coordinators are ready to help.": "احصل على استشارة وخطة تعافي مجانية بدون التزامات خلال 24 ساعة بمساعدة منسقينا العالميين.",
    "Let's Build Your <span class=\"text-primary\">Journey</span>": "لنصنع <span class=\"text-primary\">رحلتك</span>",
    "Cosmetic / Plastic Surgery": "جراحة التجميل والتجميل",
    "Your request has been securely sent. A Medora coordinator will contact you via email or WhatsApp within 24 hours.": "تم إرسال طلبك بأمان. وسيقوم منسقنا بالتواصل معك قريباً خلال 24 ساعة.",
}

for file in glob.glob('*-ar.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pre-clean known weird characters
    content = content.replace("—", "—")
    content = content.replace("&amp;", "&")
    
    for eng, ara in translations.items():
        # Clean eng just in case
        clean_eng = eng.replace("&amp;", "&")
        
        # Escape pattern
        pattern_str = re.escape(clean_eng)
        
        # Replace escaped spaces with \s+ to match multiline formatting
        pattern_str = pattern_str.replace(r'\ ', r'\s+')
        
        # Compile pattern
        pattern = re.compile(pattern_str, re.IGNORECASE)
        content = pattern.sub(ara, content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Robust regex translation applied successfully!")
