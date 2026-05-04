import re, os

PUBLIC = "/Users/andrewcapener/Dropbox/DME/empower-site/public"

with open(f"{PUBLIC}/detail_team-member.html") as f:
    TEMPLATE = f.read()

MEMBERS = [
    {
        "slug": "patrick-dowling",
        "name": "Patrick Dowling",
        "title": "President &amp; CEO",
        "img": "/images/cms/4995DCC1-EF51-4E11-BF11-1751AA65CE22.PNG",
        "bio": "<p>Patrick Dowling is the Chief Executive Officer of Empower EIT, where he leads the company's strategic vision, operational execution, and long-term growth across the energy value chain. With nearly three decades of leadership experience spanning both the energy and healthcare sectors, Mr. Dowling has built a reputation for driving transformational growth, scaling complex organizations, and delivering consistent financial and operational performance.</p><p>At Empower EIT, Mr. Dowling is responsible for overseeing the company's integrated upstream, midstream, and downstream initiatives, positioning the organization as a next-generation energy platform. He has led key corporate transformation efforts that have strengthened market positioning, expanded revenue streams, and improved capital efficiency.</p><p>Prior to joining Empower EIT, Mr. Dowling served as Chief Executive Officer of Hill Country Oil &amp; Gas, where he successfully executed acquisition-driven growth strategies. He also served as Director of Business Development at Cenikor Foundation, where he drove over $10 million in revenue growth within two years, and Chief Operating Officer at ProTouch Staffing.</p><p>Mr. Dowling served as President &amp; CEO of Dow Energy Solutions, leading a national sales organization of over 2,000 professionals and generating more than $20 million in annual revenue. Earlier roles include Chief Operating Officer and National Director at Nurses 24/7, where he helped scale the business to a $150 million enterprise.</p><p>Mr. Dowling studied Business and Managerial Economics at Rider University and Business Management at the University of Delaware.</p>"
    },
    {
        "slug": "ian-ensell",
        "name": "Ian Ensell",
        "title": "Chief Operating Officer",
        "img": "/images/cms/9CA50E1F-ABC9-47B2-8835-BC61B3DEE356.PNG",
        "bio": "<p>Ian Ensell serves as Chief Operating Officer of Empower EIT, where he leads the company's day-to-day operational strategy across drilling, extraction, processing, and logistics. He is responsible for building and scaling high-performance operational teams while ensuring execution aligns with the company's safety, regulatory, and cost-efficiency standards.</p><p>Ian brings nearly two decades of hands-on experience across premier U.S. basins, including the Permian/Delaware, DJ Basin, Powder River, and Uintah. His background spans complex drilling environments, including extended-reach laterals, managed pressure drilling (MPD), and high-pressure well control scenarios.</p><p>Prior to joining Empower EIT, Ian held the position of Drilling Superintendent at Devon Energy, supporting up to 26 active rigs. Devon Energy merged with WPX Energy where Ian held the same position, playing a key role in driving continuous improvement across drilling programs.</p><p>Earlier in his career, Ian served as CEO of Freedom Drilling Services, where he built HSE programs with zero recordable incidents over multiple years. He also held critical field roles with Anadarko Petroleum and Scientific Drilling International, developing deep expertise in wellsite operations and directional drilling.</p>"
    },
    {
        "slug": "preston-mceachern",
        "name": "Dr. Preston McEachern",
        "title": "Chief Technology Officer",
        "img": "/images/cms/96B98194-5E3A-48EA-AF5D-9629A3081F54.PNG",
        "bio": "<p>Preston McEachern serves as Chief Technology Officer of Empower EIT, where he leads the company's technology vision, innovation strategy, and deployment of advanced extraction and processing systems across its vertically integrated lithium platform. He oversees the development and commercialization of Empower's direct lithium extraction (DLE) technologies, water treatment solutions, and integrated energy systems.</p><p>Dr. McEachern brings more than 25 years of leadership at the intersection of environmental chemistry, water systems, and energy technology. He is widely recognized as a leading expert in water treatment and resource recovery, with deep experience spanning oil &amp; gas, mining, and industrial process optimization.</p><p>Prior to joining Empower, Dr. McEachern served as Chief Operating Officer of AquaMin Lithium and Water Recovery and Conductive Energy. Earlier, as Founder and CEO of Purlucid Treatment Solutions, he raised over $14 million and successfully commercialized wastewater treatment systems for major oil sands operators in Alberta.</p><p>His career also includes serving as Vice President of Research &amp; Development at Tervita Corporation, where he expanded the company's innovation platform, increased its patent portfolio by 50%, and secured over $10 million in external research funding.</p><p>Dr. McEachern holds a Ph.D. in Environmental Chemistry and Ecology from the University of Alberta. A named inventor on multiple patents, he is a driving force behind Empower's technological differentiation in next-generation lithium extraction.</p>"
    },
    {
        "slug": "angel-testani",
        "name": "Dr. Angel Testani",
        "title": "SVP, Human Resources, Safety &amp; Sustainability",
        "img": "/images/cms/Screenshot-2026-01-30-at-7.28.06-PM.png",
        "bio": "<p>Dr. Angeline \"Angel\" Testani serves as Senior Vice President of Human Resources, Safety &amp; Sustainability at Empower EIT. She brings a unique combination of leadership, regulatory expertise, and operational excellence across healthcare, financial services, and energy.</p><p>At Empower EIT, Dr. Testani is responsible for building and scaling the company's human capital strategy, safety programs, and enterprise-wide sustainability initiatives. She has led the development of employee onboarding, risk management frameworks, safety protocols, and internal systems to support operational efficiency and regulatory readiness.</p><p>Prior to joining Empower, she served as Chief Compliance Officer at Douglas Scott Securities, establishing comprehensive compliance programs aligned with federal and state regulatory standards. Earlier, she held senior leadership roles including Assistant Vice President of Clinical Services at Cenikor Foundation and Director of Quality at CommUnityCare Health Centers.</p><p>Dr. Testani also serves as an Adjunct Professor at Concordia University, teaching graduate-level courses in leadership development, organizational ethics, and healthcare policy.</p><p>She holds a Ph.D. in Organization and Management (Leadership specialization), an MBA in Global Business, and a Master of Science in Social Work. She is also a certified Project Management Professional (PMP) and SHRM Certified Professional (SHRM-CP).</p>"
    },
    {
        "slug": "james-chaney",
        "name": "James Chaney",
        "title": "Senior Advisor",
        "img": "/images/cms/34A4FB6D-DD54-4538-A968-7F7A428CB6A4.jpeg",
        "bio": "<p>James Chaney serves as Senior Advisor at Empower EIT, where he plays a critical role in advancing the company's reservoir strategy, technical diligence, and integration of subsurface expertise across its expanding energy and lithium portfolio.</p><p>Mr. Chaney is a highly accomplished petroleum engineer and senior executive with more than four decades of experience in reservoir engineering, asset development, and large-scale oil and gas operations. He brings a proven track record of value creation through the acquisition, optimization, and monetization of complex energy assets.</p><p>Prior to joining Empower EIT, Mr. Chaney spent over 14 years at Hunt Oil Company, where he served as Senior Vice President of Reserves &amp; Evaluation Engineering. Under his leadership, production in the West Texas region increased from approximately 5,000 BOEPD to over 70,000 BOEPD, driven by the drilling of more than 200 horizontal wells. He also led the acquisition of a $480 million West Texas asset package and the formation and sale of a $1.4 billion DrillCo partnership.</p><p>Prior to Hunt Oil, Mr. Chaney was a Reservoir Engineering Advisor at Pioneer Natural Resources. He began his career at Schlumberger, developing deep expertise in well testing, completions design, and reservoir performance evaluation.</p><p>He holds a B.S. in Mining Engineering with honors from the Missouri University of Science and Technology and is a licensed Professional Engineer in Texas.</p>"
    },
    {
        "slug": "elliott-edge",
        "name": "Elliott Edge",
        "title": "SVP, Reservoir Engineering",
        "img": "/images/cms/Screenshot-2026-03-11-at-2.16.32-PM.png",
        "bio": "<p>Elliott Edge serves as SVP of Reservoir Engineering at Empower EIT, supporting the integration of advanced technologies and helping drive the company's vision of building a fully vertically integrated lithium platform. His expertise in engineering, systems integration, and technology commercialization plays a key role in advancing Empower's mission.</p><p>Elliott is a technology-driven executive, investor, and entrepreneur with a strong track record of building and scaling businesses across the energy and technology sectors. He is CEO of both Velonex Technologies and Palmer Technology Solutions, and Founder of Rose Rock Holdings LLC, a private investment firm focused on acquiring and growing businesses across multiple sectors.</p><p>Prior to his entrepreneurial ventures, Elliott served as an engineer at Apache Corporation and later as a Senior Engineer at WPX Energy, specializing in reservoir engineering, simulation, and integrated asset development.</p><p>Elliott holds a Master of Business Administration from Harvard Business School and a Bachelor's degree in Petroleum Engineering from the University of Oklahoma.</p>"
    },
]

def make_page(member, template):
    page = template
    name = member["name"]
    title = member["title"]
    img = member["img"]
    bio = member["bio"]

    # Update meta title
    page = re.sub(r'<title>[^<]*</title>', f'<title>{name} — Empower EIT</title>', page)

    # Update meta description
    page = re.sub(
        r'<meta content="[^"]*" name="description"/>',
        f'<meta content="{name}, {title} at Empower EIT." name="description"/>',
        page
    )

    # Update OG title
    page = re.sub(
        r'<meta content="[^"]*" property="og:title"/>',
        f'<meta content="{name} — Empower EIT" property="og:title"/>',
        page
    )

    # Replace placeholder image
    page = page.replace(
        'src="https://d3e54v103j8qbb.cloudfront.net/plugins/Basic/assets/placeholder.60f9b1840c.svg" loading="lazy" alt="" class="image w-dyn-bind-empty"',
        f'src="{img}" loading="lazy" alt="{name}" class="image"'
    )

    # Fill name
    page = page.replace(
        '<h1 class="heading-style-h2 text-weight-normal w-dyn-bind-empty"></h1>',
        f'<h1 class="heading-style-h2 text-weight-normal">{name}</h1>'
    )

    # Fill title
    page = page.replace(
        '<div class="text-style-allcaps text-size-small w-dyn-bind-empty"></div>',
        f'<div class="text-style-allcaps text-size-small">{title}</div>'
    )

    # Fill bio
    page = page.replace(
        '<div class="text-rich-text w-dyn-bind-empty w-richtext"></div>',
        f'<div class="text-rich-text w-richtext">{bio}</div>'
    )

    return page

for member in MEMBERS:
    page = make_page(member, TEMPLATE)
    filename = f"team-{member['slug']}.html"
    path = os.path.join(PUBLIC, filename)
    with open(path, 'w') as f:
        f.write(page)
    print(f"✅ {filename}")

print(f"\nCreated {len(MEMBERS)} pages")
