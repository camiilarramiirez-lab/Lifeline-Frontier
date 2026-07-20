import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Lifeline Frontier | Professional Tactical Medical Gear",
    page_icon="🩹",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom CSS for Premium UI/UX
st.markdown("""
<style>
    /* Global Styles */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=Oswald:wght@500;700&display=swap');
    
    html {
        scroll-behavior: smooth;
    }
    
    .main {
        background-color: #0f1116;
        color: #e0e0e0;
        font-family: 'Inter', sans-serif;
    }
    
    h1, h2, h3 {
        font-family: 'Oswald', sans-serif;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Navigation Bar */
    .nav-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background: rgba(15, 17, 22, 0.95);
        padding: 15px 50px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        z-index: 1000;
        border-bottom: 2px solid #d32f2f;
        box-shadow: 0 4px 20px rgba(0,0,0,0.5);
    }
    
    .nav-logo {
        color: #d32f2f;
        font-size: 24px;
        font-weight: 700;
        font-family: 'Oswald', sans-serif;
        text-decoration: none;
    }
    
    .nav-links a {
        color: #ffffff;
        text-decoration: none;
        margin-left: 30px;
        font-weight: 600;
        font-size: 14px;
        transition: 0.3s;
    }
    
    .nav-links a:hover {
        color: #d32f2f;
    }

    /* Hero Section */
    .hero-section {
        padding: 150px 10% 100px 10%;
        background: linear-gradient(135deg, #1a1d24 0%, #0f1116 100%);
        text-align: center;
        border-bottom: 1px solid #333;
    }
    
    .hero-badge {
        background: #d32f2f;
        color: white;
        padding: 5px 15px;
        border-radius: 5px;
        font-size: 12px;
        font-weight: 700;
        display: inline-block;
        margin-bottom: 20px;
    }
    
    .hero-title {
        font-size: 4rem;
        margin-bottom: 20px;
        color: #ffffff;
        line-height: 1.1;
    }
    
    .hero-subtitle {
        font-size: 1.2rem;
        color: #a0a0a0;
        max-width: 800px;
        margin: 0 auto 40px auto;
    }

    /* Section Styling */
    .section-container {
        padding: 80px 10%;
    }
    
    .section-title {
        font-size: 2.5rem;
        color: #ffffff;
        margin-bottom: 40px;
        border-left: 5px solid #d32f2f;
        padding-left: 20px;
    }

    /* Blog Content Layout */
    .blog-content {
        background: #1a1d24;
        padding: 50px;
        border-radius: 15px;
        border: 1px solid #333;
        line-height: 1.8;
        font-size: 1.1rem;
        color: #d0d0d0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    
    .blog-content h1, .blog-content h2, .blog-content h3 {
        color: #d32f2f;
        margin-top: 30px;
        margin-bottom: 15px;
    }
    
    .blog-content p {
        margin-bottom: 20px;
    }

    /* Service Cards */
    .service-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 30px;
    }
    
    .service-card {
        background: #1e2129;
        padding: 40px;
        border-radius: 10px;
        border-top: 4px solid #d32f2f;
        transition: 0.3s;
    }
    
    .service-card:hover {
        transform: translateY(-10px);
        background: #252933;
    }
    
    .service-card h3 {
        color: #ffffff;
        margin-bottom: 15px;
    }
    
    .service-card p {
        color: #a0a0a0;
        font-size: 0.95rem;
    }

    /* Contact Section */
    .contact-box {
        background: linear-gradient(135deg, #d32f2f 0%, #b71c1c 100%);
        padding: 60px;
        border-radius: 20px;
        color: white;
        text-align: center;
    }
    
    .contact-info {
        font-size: 1.5rem;
        font-weight: 700;
        margin: 20px 0;
    }

    /* Footer */
    .footer {
        padding: 50px 10%;
        background: #0a0c10;
        text-align: center;
        border-top: 1px solid #333;
        color: #666;
    }

    /* Responsive Adjustments */
    @media (max-width: 768px) {
        .hero-title { font-size: 2.5rem; }
        .nav-container { padding: 15px 20px; }
        .nav-links { display: none; }
        .section-container { padding: 60px 5%; }
        .blog-content { padding: 30px; }
    }
</style>
""", unsafe_allow_html=True)

# Navigation Menu (Anchor links)
st.markdown("""
<div class="nav-container">
    <a href="#home" class="nav-logo">LIFELINE FRONTIER</a>
    <div class="nav-links">
        <a href="#home">HOME</a>
        <a href="#services">SERVICES</a>
        <a href="#about">ABOUT</a>
        <a href="#contact">CONTACT</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Hero Section
st.markdown('<div id="home"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="hero-section">
    <div class="hero-badge">MISSION-READY MEDICAL SOLUTIONS</div>
    <h1 class="hero-title">SURVIVAL IS NOT AN ACCIDENT.</h1>
    <p class="hero-subtitle">Professional-grade IFAKs, bleeding control solutions, and tactical medical equipment engineered for the highest stakes. When seconds count, we provide the edge you need.</p>
</div>
""", unsafe_allow_html=True)

# Main Content Section (Homepage.txt)
st.markdown('<div class="section-container">', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Emergency Preparedness Insights</h2>', unsafe_allow_html=True)

# Homepage content block
homepage_content = """
<div class="blog-content">
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
    <p>Anyone providing first aid should also think about personal safety. Disposable nitrile gloves, CPR barrier devices, and protective eyewear reduce the risk of exposure to bodily fluids. When selecting emergency equipment from <a href="https://flaresyn.com" style="color: #d32f2f; text-decoration: none; font-weight: bold;">FlareSyn</a>, many drivers also look for organized trauma solutions that keep protective equipment and lifesaving supplies together, making them easier to locate during stressful situations.</p>

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
st.markdown('</div>', unsafe_allow_html=True)

# Services Section
st.markdown('<div id="services"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-container">', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Mission-Ready Services</h2>', unsafe_allow_html=True)
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
        <h3>Fleet Preparedness</h3>
        <p>Comprehensive medical equipment planning for commercial fleets, first responder vehicles, and off-road expeditions.</p>
    </div>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# About Section
st.markdown('<div id="about"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-container" style="background: #161a21;">', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">About Lifeline Frontier</h2>', unsafe_allow_html=True)
st.markdown("""
<div style="max-width: 900px; line-height: 1.8; color: #a0a0a0; font-size: 1.1rem;">
    <p>Lifeline Frontier is a premier provider of tactical medical equipment and trauma care solutions. We operate at the intersection of professional medicine and field operations, ensuring that those who work in high-risk environments have access to the most reliable gear available.</p>
    <p>Our philosophy is simple: <strong>Reliability is the only metric that matters.</strong> Every component we recommend and every kit we build is vetted for rapid response in high-stress scenarios. Whether you are a first responder, a military professional, or a prepared citizen, we provide the tools necessary to bridge the gap between injury and professional medical care.</p>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Contact Section
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-container">', unsafe_allow_html=True)
st.markdown("""
<div class="contact-box">
    <h2 style="color: white; margin-bottom: 20px;">READY FOR THE FRONTIER?</h2>
    <p style="font-size: 1.2rem; margin-bottom: 30px;">Contact our tactical specialists for bulk quotes or custom kit consultations.</p>
    <div class="contact-info">support@flaresyn.com</div>
    <div class="contact-info">+1 925 897-9800</div>
    <p style="margin-top: 20px; font-weight: 600;">OPERATIONAL 24/7 FOR CRITICAL NEEDS</p>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <p>&copy; 2026 LIFELINE FRONTIER. ALL RIGHTS RESERVED.</p>
    <p style="font-size: 0.8rem; margin-top: 10px;">TACTICAL MEDICAL SOLUTIONS | TRAUMA CARE | EMERGENCY PREPAREDNESS</p>
</div>
""", unsafe_allow_html=True)
