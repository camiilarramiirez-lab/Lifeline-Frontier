import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="Lifeline Frontier | Tactical Medical Gear",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- Custom CSS for a Tactical Theme ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Roboto+Mono:wght@400;700&display=swap');

    :root {
        --primary-color: #E4002B; /* Deep Red */
        --secondary-color: #0F1116; /* Dark Charcoal */
        --text-color: #E0E0E0; /* Light Gray */
        --accent-color: #00FF00; /* Bright Green for highlights */
        --bg-dark: #0A0C10;
        --bg-medium: #1A1D24;
        --bg-light: #2A2E38;
    }

    html {
        scroll-behavior: smooth;
    }

    body {
        font-family: 'Roboto Mono', monospace;
        color: var(--text-color);
        background-color: var(--secondary-color);
    }

    h1, h2, h3, h4, h5, h6 {
        font-family: 'Orbitron', sans-serif;
        color: var(--primary-color);
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-top: 1.5em;
        margin-bottom: 0.8em;
    }

    h1 {
        font-size: 3.5em;
        color: var(--text-color);
        text-align: center;
        line-height: 1.2;
    }

    h2 {
        font-size: 2.2em;
        border-bottom: 2px solid var(--primary-color);
        padding-bottom: 10px;
        margin-top: 2em;
    }

    h3 {
        font-size: 1.6em;
        color: var(--accent-color);
    }

    p {
        line-height: 1.7;
        margin-bottom: 1em;
        font-size: 1.05em;
    }

    a {
        color: var(--primary-color);
        text-decoration: none;
        transition: color 0.3s ease;
    }

    a:hover {
        color: var(--accent-color);
        text-decoration: underline;
    }

    /* Streamlit Overrides */
    .stApp {
        background-color: var(--secondary-color);
        color: var(--text-color);
    }
    .stMarkdown {
        color: var(--text-color);
    }
    .css-1d391kg, .css-18e3th9, .css-1lcbmhc { /* Main content padding adjustments */
        padding-top: 0;
        padding-bottom: 0;
    }
    .block-container {
        padding-top: 2rem; /* Adjust as needed */
        padding-bottom: 2rem;
        padding-left: 10%;
        padding-right: 10%;
    }

    /* --- Navigation Bar --- */
    .navbar {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background: var(--bg-dark);
        padding: 15px 10%;
        display: flex;
        justify-content: space-between;
        align-items: center;
        z-index: 1000;
        border-bottom: 3px solid var(--primary-color);
        box-shadow: 0 5px 20px rgba(0,0,0,0.6);
    }
    .navbar-logo {
        color: var(--primary-color);
        font-family: 'Orbitron', sans-serif;
        font-size: 28px;
        font-weight: 700;
        text-decoration: none;
        letter-spacing: 2px;
    }
    .navbar-links a {
        color: var(--text-color);
        text-decoration: none;
        margin-left: 35px;
        font-weight: 700;
        font-size: 15px;
        transition: color 0.3s ease, transform 0.2s ease;
        position: relative;
    }
    .navbar-links a::after {
        content: '';
        position: absolute;
        width: 0;
        height: 2px;
        display: block;
        margin-top: 5px;
        right: 0;
        background: var(--accent-color);
        transition: width 0.4s ease;
        -webkit-transition: width 0.4s ease;
    }
    .navbar-links a:hover::after {
        width: 100%;
        left: 0;
        background: var(--primary-color);
    }
    .navbar-links a:hover {
        color: var(--primary-color);
        transform: translateY(-2px);
    }

    /* --- Hero Section --- */
    .hero-section {
        padding: 200px 10% 120px 10%; /* Adjusted for fixed navbar */
        background: linear-gradient(145deg, var(--bg-medium) 0%, var(--bg-dark) 100%);
        text-align: center;
        border-bottom: 1px solid #333;
        position: relative;
        overflow: hidden;
    }
    .hero-section::before {
        content: '';
        position: absolute;
        top: -50px;
        left: -50px;
        right: -50px;
        bottom: -50px;
        background: url('https://www.transparenttextures.com/patterns/carbon-fibre.png') repeat; /* Subtle texture */
        opacity: 0.1;
        z-index: 0;
    }
    .hero-content {
        position: relative;
        z-index: 1;
    }
    .hero-badge {
        background: var(--primary-color);
        color: white;
        padding: 8px 20px;
        border-radius: 5px;
        font-size: 0.9em;
        font-weight: 700;
        display: inline-block;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(228, 0, 43, 0.4);
    }
    .hero-title {
        font-size: 4.5em;
        margin-bottom: 25px;
        color: var(--text-color);
        line-height: 1.1;
        text-shadow: 0 0 15px rgba(228, 0, 43, 0.7);
    }
    .hero-subtitle {
        font-size: 1.3em;
        color: #A0A0A0;
        max-width: 900px;
        margin: 0 auto 50px auto;
        font-family: 'Roboto Mono', monospace;
    }

    /* --- General Section Styling --- */
    .section-spacing {
        padding-top: 80px;
        padding-bottom: 80px;
    }
    .section-alt-bg {
        background-color: var(--bg-medium);
    }

    /* --- Blog Content Layout --- */
    .blog-container {
        background: var(--bg-medium);
        padding: 60px;
        border-radius: 12px;
        border: 1px solid #333;
        box-shadow: 0 10px 30px rgba(0,0,0,0.4);
    }
    .blog-container h1, .blog-container h2, .blog-container h3 {
        color: var(--primary-color);
        margin-top: 2em;
        margin-bottom: 0.8em;
    }
    .blog-container p {
        margin-bottom: 1em;
    }

    /* --- Service Cards --- */
    .service-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 30px;
        margin-top: 40px;
    }
    .service-card {
        background: var(--bg-light);
        padding: 40px;
        border-radius: 10px;
        border-left: 5px solid var(--primary-color);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }
    .service-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 25px rgba(0,0,0,0.5);
    }
    .service-card h3 {
        color: var(--text-color);
        margin-bottom: 15px;
        font-size: 1.4em;
    }
    .service-card p {
        color: #B0B0B0;
        font-size: 0.95em;
    }

    /* --- About Section --- */
    .about-content {
        max-width: 900px;
        margin: 0 auto;
        line-height: 1.8;
        color: #B0B0B0;
        font-size: 1.1em;
    }
    .about-content strong {
        color: var(--primary-color);
    }

    /* --- Contact Section --- */
    .contact-box {
        background: linear-gradient(135deg, var(--primary-color) 0%, #A00020 100%);
        padding: 70px;
        border-radius: 15px;
        color: white;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    .contact-box h2 {
        color: white;
        margin-bottom: 25px;
        font-size: 2.5em;
    }
    .contact-box p {
        font-size: 1.3em;
        margin-bottom: 35px;
        color: #F0F0F0;
    }
    .contact-info {
        font-size: 1.8em;
        font-weight: 700;
        margin: 15px 0;
        color: white;
        font-family: 'Orbitron', sans-serif;
    }

    /* --- Footer --- */
    .footer {
        padding: 50px 10%;
        background: var(--bg-dark);
        text-align: center;
        border-top: 1px solid #333;
        color: #666;
        font-size: 0.9em;
    }
    .footer p {
        margin: 5px 0;
    }

    /* --- Scroll to Top Button --- */
    .scroll-to-top {
        position: fixed;
        bottom: 30px;
        right: 30px;
        background-color: var(--primary-color);
        color: white;
        border-radius: 50%;
        width: 50px;
        height: 50px;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 28px;
        text-decoration: none;
        box-shadow: 0 4px 15px rgba(0,0,0,0.4);
        z-index: 999;
        transition: background-color 0.3s ease, transform 0.2s ease;
    }
    .scroll-to-top:hover {
        background-color: var(--accent-color);
        transform: translateY(-3px);
    }

    /* --- Responsive Adjustments --- */
    @media (max-width: 1024px) {
        .navbar, .block-container {
            padding-left: 5%;
            padding-right: 5%;
        }
        .hero-title {
            font-size: 3.5em;
        }
        .hero-subtitle {
            font-size: 1.1em;
        }
        .section-title {
            font-size: 2em;
        }
        .blog-container {
            padding: 40px;
        }
        .contact-box {
            padding: 50px;
        }
    }

    @media (max-width: 768px) {
        .navbar {
            flex-direction: column;
            padding: 15px 5%;
        }
        .navbar-links {
            margin-top: 15px;
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
        }
        .navbar-links a {
            margin: 0 15px 10px 15px;
        }
        .hero-section {
            padding-top: 180px; /* Adjust for stacked navbar */
            padding-bottom: 80px;
        }
        .hero-title {
            font-size: 2.8em;
        }
        .hero-subtitle {
            font-size: 1em;
        }
        .section-title {
            font-size: 1.8em;
        }
        .blog-container {
            padding: 25px;
        }
        .service-card {
            padding: 30px;
        }
        .contact-box {
            padding: 30px;
        }
        .contact-info {
            font-size: 1.4em;
        }
    }

    @media (max-width: 480px) {
        .hero-title {
            font-size: 2em;
        }
        .hero-subtitle {
            font-size: 0.9em;
        }
        .section-title {
            font-size: 1.5em;
        }
        .blog-container {
            padding: 15px;
        }
        .navbar-logo {
            font-size: 22px;
        }
        .navbar-links a {
            font-size: 13px;
            margin: 0 10px 8px 10px;
        }
    }
</style>
""", unsafe_allow_html=True)

# --- Navigation Bar ---
st.markdown("""
<div class="navbar">
    <a href="#home" class="navbar-logo">LIFELINE FRONTIER</a>
    <div class="navbar-links">
        <a href="#home">HOME</a>
        <a href="#services">SERVICES</a>
        <a href="#about">ABOUT</a>
        <a href="#contact">CONTACT</a>
    </div>
</div>
""", unsafe_allow_html=True)

# --- Hero Section ---
st.markdown("<div id='home'></div>", unsafe_allow_html=True)
st.markdown("""
<div class="hero-section">
    <div class="hero-content">
        <div class="hero-badge">MISSION-CRITICAL MEDICAL SOLUTIONS</div>
        <h1 class="hero-title">EQUIPPING THE FRONTLINE.<br>SAVING LIVES.</h1>
        <p class="hero-subtitle">Specializing in professional IFAKs, bleeding control, and mission-ready first aid equipment for high-risk, field, and emergency environments.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# --- Main Content Section (Homepage.txt) ---
st.markdown("<div class='section-spacing'>", unsafe_allow_html=True)
st.markdown("<h2>Emergency Preparedness Insights</h2>", unsafe_allow_html=True)

homepage_content = """
<div class="blog-container">
    <h1>Which Trauma Supplies Are Most Useful for Vehicle Emergency Preparedness?</h1>
    
    <p>Being prepared for a roadside emergency means having more than a standard first-aid kit. The most useful trauma supplies are those that help control severe bleeding, protect wounds, stabilize injuries, and support someone until professional medical help arrives. Choosing practical equipment before an emergency happens can make your response faster and more effective. This guide explains which trauma supplies deserve space in your vehicle, how to organize them, and what factors to consider when building a dependable emergency kit.</p>

    <h2>Why Vehicle Trauma Preparedness Deserves Careful Planning</h2>
    <p>Road emergencies can happen during daily commutes, long-distance trips, off-road adventures, or even while parked on the roadside. Although emergency services are often available, weather conditions, heavy traffic, or remote locations may delay their arrival. Having the right trauma supplies allows you to provide immediate care during those critical first minutes.</p>
    <p>Common vehicle-related injuries include deep cuts from broken glass, heavy bleeding, burns, sprains, fractures, and injuries caused by impact. While no emergency kit replaces professional medical treatment, properly selected supplies can help reduce complications until trained responders take over.</p>

    <h2>Trauma Supplies That Provide the Greatest Practical Value</h2>
    
    <h3>Bleeding Control Essentials</h3>
    <p>Severe bleeding is one of the most urgent medical emergencies after a vehicle collision. A well-equipped trauma kit should include sterile gauze, compression bandages, pressure dressings, and a quality tourniquet intended for emergency use. Hemostatic gauze may also be appropriate for trained users when dealing with difficult-to-control bleeding. Having multiple sizes of dressings allows you to respond to different wound types without improvising.</p>

    <h3>Wound Protection and Infection Prevention</h3>
    <p>After bleeding has been controlled, protecting the wound becomes the next priority. Adhesive bandages, sterile dressings, antiseptic wipes, medical tape, and disposable gloves help reduce contamination while keeping injuries covered. These supplies are useful not only after traffic accidents but also during roadside repairs, camping trips, or other travel situations where cuts and abrasions may occur.</p>

    <h3>Supplies for Burns, Fractures, and Immobilization</h3>
    <p>Vehicle emergencies sometimes involve burns from hot engine components, electrical systems, or fires. Burn dressings designed for first aid can help cool and protect injured skin. Triangular bandages, elastic wraps, and compact splints are valuable for supporting suspected fractures or sprains while minimizing unnecessary movement until emergency responders arrive.</p>

    <h3>Personal Protective Equipment</h3>
    <p>Anyone providing first aid should also think about personal safety. Disposable nitrile gloves, CPR barrier devices, and protective eyewear reduce the risk of exposure to bodily fluids. When selecting emergency equipment from <a href="https://flaresyn.com" style="color: var(--primary-color); text-decoration: underline; font-weight: bold;">FlareSyn</a>, many drivers also look for organized trauma solutions that keep protective equipment and lifesaving supplies together, making them easier to locate during stressful situations.</p>

    <h2>How to Build a Vehicle Trauma Kit That Fits Your Driving Habits</h2>
    <p>Not every driver needs the same equipment. Someone who commutes a few miles each day may only require a compact trauma kit with essential bleeding control and wound care items. On the other hand, people who frequently travel through rural areas, transport family members, work on construction sites, or enjoy outdoor recreation often benefit from carrying additional dressings, splints, emergency blankets, flashlights, and backup gloves.</p>
    <p>Think about where you drive most often, how quickly emergency services can reach you, and whether you regularly travel in areas with limited cell coverage. Your answers will help determine how comprehensive your vehicle trauma kit should be.</p>
    
    <h2>Keeping Supplies Organized and Ready to Use</h2>
    <p>A trauma kit is only useful if you can reach what you need quickly. Store supplies inside a clearly labeled case that remains secure while driving but is still easily accessible. Group similar items together, such as bleeding control equipment, wound care supplies, protective gear, and immobilization materials, so you can locate them without searching through the entire kit.</p>
    <p>Inspect the contents several times each year. Replace expired products, damaged packaging, missing gloves, depleted medications if included, and batteries for flashlights or other emergency tools. Regular inspections ensure your supplies remain ready when you need them most.</p>

    <h2>Common Mistakes That Reduce Emergency Preparedness</h2>
    <p>One common mistake is purchasing specialized equipment without learning how to use it correctly. Even the best trauma supplies become far less effective if the user is unfamiliar with their application. Taking a basic first-aid or bleeding-control course builds confidence and helps you respond more appropriately during emergencies.</p>
    <p>Another mistake is relying solely on a small household first-aid kit. While these kits are useful for minor cuts and scrapes, they often lack the supplies needed for serious traumatic injuries. Expanding your vehicle kit with purpose-built trauma equipment provides a more practical level of preparedness.</p>

    <h2>Choosing Reliable Trauma Supplies for Long-Term Readiness</h2>
    <p>Selecting dependable trauma supplies means looking beyond the number of items included in a kit. Durable storage, clearly organized compartments, quality medical components, and equipment appropriate for your level of training all contribute to effective emergency preparedness. Whether you drive across town every day or regularly travel long distances, investing time in building a thoughtful vehicle trauma kit helps ensure you are better prepared to respond calmly and safely if an unexpected emergency occurs.</p>
</div>
"""
st.markdown(homepage_content, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- Services Section ---
st.markdown("<div id='services' class='section-spacing section-alt-bg'></div>", unsafe_allow_html=True)
st.markdown("<h2>Mission-Ready Services</h2>", unsafe_allow_html=True)
st.markdown("""
<div class="service-grid">
    <div class="service-card">
        <h3>IFAK Customization</h3>
        <p>Tailored Individual First Aid Kits designed for specific mission profiles, from low-profile EDC to full-scale tactical operations.</p>
    </div>
    <div class="service-card">
        <h3>Bleeding Control Solutions</h3>
        <p>Expertly curated hemorrhage control kits featuring TCCC-recommended tourniquets and hemostatic agents.</p>
    </div>
    <div class="service-card">
        <h3>Tactical Medical Training</h3>
        <p>Specialized courses and resources for effective use of trauma supplies in high-stress, emergency situations.</p>
    </div>
    <div class="service-card">
        <h3>Fleet & Organizational Preparedness</h3>
        <p>Comprehensive medical equipment planning and supply chain solutions for commercial fleets, first responders, and large organizations.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# --- About Section ---
st.markdown("<div id='about' class='section-spacing'></div>", unsafe_allow_html=True)
st.markdown("<h2>About Lifeline Frontier</h2>", unsafe_allow_html=True)
st.markdown("""
<div class="about-content">
    <p>Lifeline Frontier is a premier provider of tactical medical equipment and trauma care solutions. We operate at the intersection of professional medicine and field operations, ensuring that those who work in high-risk environments have access to the most reliable gear available.</p>
    <p>Our philosophy is simple: <strong>Reliability is the only metric that matters.</strong> Every component we recommend and every kit we build is vetted for rapid response in high-stress scenarios. Whether you are a first responder, a military professional, or a prepared citizen, we provide the tools necessary to bridge the gap between injury and professional medical care.</p>
    <p>We are committed to empowering individuals and organizations with the knowledge and equipment to make a difference when it matters most. Our products are rigorously tested and selected to meet the demands of real-world emergencies, ensuring peak performance under pressure.</p>
</div>
""", unsafe_allow_html=True)

# --- Contact Section ---
st.markdown("<div id='contact' class='section-spacing section-alt-bg'></div>", unsafe_allow_html=True)
st.markdown("""
<div class="contact-box">
    <h2>READY FOR THE FRONTIER?</h2>
    <p>Connect with our tactical specialists for bulk quotes, custom kit consultations, or training inquiries.</p>
    <div class="contact-info">✉️ support@lifelinefrontier.com</div>
    <div class="contact-info">📞 +1 (925) 897-9800</div>
    <p style="margin-top: 30px; font-weight: 700; font-size: 1.1em; color: #F0F0F0;">OPERATIONAL 24/7 FOR CRITICAL NEEDS</p>
</div>
""", unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
<div class="footer">
    <p>&copy; 2026 LIFELINE FRONTIER. ALL RIGHTS RESERVED.</p>
    <p>TACTICAL MEDICAL SOLUTIONS | TRAUMA CARE | EMERGENCY PREPAREDNESS</p>
</div>
""", unsafe_allow_html=True)

# --- Scroll to Top Button ---
st.markdown("""
<a href="#home" class="scroll-to-top">↑</a>
""", unsafe_allow_html=True)
