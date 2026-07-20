import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="Lifeline Frontier | Tactical Medical Gear",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- Premium Tactical CSS ---
st.markdown("""
<style>
    /* Import high-quality fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Oswald:wght@500;700&display=swap');

    /* Global styling */
    .stApp {
        background-color: #0F1116;
        color: #E0E0E0;
        font-family: 'Inter', sans-serif;
    }

    /* Headings */
    h1, h2, h3 {
        font-family: 'Oswald', sans-serif;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    h1 { color: #FFFFFF; font-size: 3rem !important; margin-bottom: 0.5rem !important; }
    h2 { color: #E4002B; font-size: 2rem !important; margin-top: 2rem !important; border-bottom: 1px solid #333; padding-bottom: 10px; }
    h3 { color: #00FF00; font-size: 1.4rem !important; margin-top: 1.5rem !important; }

    /* Custom Header */
    .custom-header {
        background-color: #0A0C10;
        padding: 20px 5%;
        border-bottom: 3px solid #E4002B;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 30px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    }
    .header-logo {
        color: #E4002B;
        font-family: 'Oswald', sans-serif;
        font-size: 28px;
        font-weight: 700;
        text-decoration: none;
    }
    .header-nav a {
        color: #FFFFFF;
        text-decoration: none;
        margin-left: 25px;
        font-weight: 600;
        font-size: 14px;
        text-transform: uppercase;
    }
    .header-nav a:hover { color: #E4002B; }

    /* Content Blocks */
    .content-card {
        background-color: #1A1D24;
        padding: 40px;
        border-radius: 10px;
        border: 1px solid #333;
        line-height: 1.8;
        margin-bottom: 30px;
    }

    /* Service Card */
    .service-box {
        background-color: #252933;
        padding: 25px;
        border-radius: 8px;
        border-left: 4px solid #E4002B;
        height: 100%;
    }

    /* Contact Banner */
    .contact-banner {
        background: linear-gradient(135deg, #E4002B 0%, #8B0000 100%);
        padding: 50px;
        border-radius: 15px;
        text-align: center;
        color: white;
        margin-top: 50px;
    }

    /* Footer */
    .footer {
        text-align: center;
        padding: 40px;
        color: #666;
        font-size: 0.9rem;
        border-top: 1px solid #333;
        margin-top: 50px;
    }

    /* Link Styling */
    .keyword-link {
        color: #E4002B;
        font-weight: bold;
        text-decoration: underline;
    }

    /* Mobile adjustments */
    @media (max-width: 768px) {
        .custom-header { flex-direction: column; padding: 15px; }
        .header-nav { margin-top: 15px; }
        .header-nav a { margin: 0 10px; }
        .content-card { padding: 20px; }
    }
</style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("""
<div class="custom-header">
    <a href="#" class="header-logo">LIFELINE FRONTIER</a>
    <div class="header-nav">
        <a href="#home">Home</a>
        <a href="#preparedness">Insights</a>
        <a href="#services">Services</a>
        <a href="#about">About</a>
        <a href="#contact">Contact</a>
    </div>
</div>
""", unsafe_allow_html=True)

# --- Hero Section ---
st.markdown("<div id='home'></div>", unsafe_allow_html=True)
hero_col1, hero_col2, hero_col3 = st.columns([1, 4, 1])
with hero_col2:
    st.markdown("<h1 style='text-align: center;'>SURVIVAL IS NOT AN ACCIDENT.</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.2rem; color: #AAA;'>Professional Tactical Medical Gear & Trauma Care Solutions for High-Risk Environments.</p>", unsafe_allow_html=True)
    st.markdown("<hr style='border: 1px solid #E4002B; width: 100px; margin: 20px auto;'>", unsafe_allow_html=True)

# --- Main Content (Homepage.txt) ---
st.markdown("<div id='preparedness'></div>", unsafe_allow_html=True)
st.markdown("<div class='content-card'>", unsafe_allow_html=True)

st.markdown("<h2>Which Trauma Supplies Are Most Useful for Vehicle Emergency Preparedness?</h2>", unsafe_allow_html=True)
st.markdown("<p>Being prepared for a roadside emergency means having more than a standard first-aid kit. The most useful trauma supplies are those that help control severe bleeding, protect wounds, stabilize injuries, and support someone until professional medical help arrives. Choosing practical equipment before an emergency happens can make your response faster and more effective. This guide explains which trauma supplies deserve space in your vehicle, how to organize them, and what factors to consider when building a dependable emergency kit.</p>", unsafe_allow_html=True)

st.markdown("<h2>Why Vehicle Trauma Preparedness Deserves Careful Planning</h2>", unsafe_allow_html=True)
st.markdown("<p>Road emergencies can happen during daily commutes, long-distance trips, off-road adventures, or even while parked on the roadside. Although emergency services are often available, weather conditions, heavy traffic, or remote locations may delay their arrival. Having the right trauma supplies allows you to provide immediate care during those critical first minutes.</p>", unsafe_allow_html=True)
st.markdown("<p>Common vehicle-related injuries include deep cuts from broken glass, heavy bleeding, burns, sprains, fractures, and injuries caused by impact. While no emergency kit replaces professional medical treatment, properly selected supplies can help reduce complications until trained responders take over.</p>", unsafe_allow_html=True)

st.markdown("<h2>Trauma Supplies That Provide the Greatest Practical Value</h2>", unsafe_allow_html=True)

st.markdown("<h3>Bleeding Control Essentials</h3>", unsafe_allow_html=True)
st.markdown("<p>Severe bleeding is one of the most urgent medical emergencies after a vehicle collision. A well-equipped trauma kit should include sterile gauze, compression bandages, pressure dressings, and a quality tourniquet intended for emergency use. Hemostatic gauze may also be appropriate for trained users when dealing with difficult-to-control bleeding. Having multiple sizes of dressings allows you to respond to different wound types without improvising.</p>", unsafe_allow_html=True)

st.markdown("<h3>Wound Protection and Infection Prevention</h3>", unsafe_allow_html=True)
st.markdown("<p>After bleeding has been controlled, protecting the wound becomes the next priority. Adhesive bandages, sterile dressings, antiseptic wipes, medical tape, and disposable gloves help reduce contamination while keeping injuries covered. These supplies are useful not only after traffic accidents but also during roadside repairs, camping trips, or other travel situations where cuts and abrasions may occur.</p>", unsafe_allow_html=True)

st.markdown("<h3>Supplies for Burns, Fractures, and Immobilization</h3>", unsafe_allow_html=True)
st.markdown("<p>Vehicle emergencies sometimes involve burns from hot engine components, electrical systems, or fires. Burn dressings designed for first aid can help cool and protect injured skin. Triangular bandages, elastic wraps, and compact splints are valuable for supporting suspected fractures or sprains while minimizing unnecessary movement until emergency responders arrive.</p>", unsafe_allow_html=True)

st.markdown("<h3>Personal Protective Equipment</h3>", unsafe_allow_html=True)
st.markdown(f"<p>Anyone providing first aid should also think about personal safety. Disposable nitrile gloves, CPR barrier devices, and protective eyewear reduce the risk of exposure to bodily fluids. When selecting emergency equipment from <a href='https://flaresyn.com' class='keyword-link'>FlareSyn</a>, many drivers also look for organized trauma solutions that keep protective equipment and lifesaving supplies together, making them easier to locate during stressful situations.</p>", unsafe_allow_html=True)

st.markdown("<h2>How to Build a Vehicle Trauma Kit That Fits Your Driving Habits</h2>", unsafe_allow_html=True)
st.markdown("<p>Not every driver needs the same equipment. Someone who commutes a few miles each day may only require a compact trauma kit with essential bleeding control and wound care items. On the other hand, people who frequently travel through rural areas, transport family members, work on construction sites, or enjoy outdoor recreation often benefit from carrying additional dressings, splints, emergency blankets, flashlights, and backup gloves.</p>", unsafe_allow_html=True)
st.markdown("<p>Think about where you drive most often, how quickly emergency services can reach you, and whether you regularly travel in areas with limited cell coverage. Your answers will help determine how comprehensive your vehicle trauma kit should be.</p>", unsafe_allow_html=True)

st.markdown("<h2>Keeping Supplies Organized and Ready to Use</h2>", unsafe_allow_html=True)
st.markdown("<p>A trauma kit is only useful if you can reach what you need quickly. Store supplies inside a clearly labeled case that remains secure while driving but is still easily accessible. Group similar items together, such as bleeding control equipment, wound care supplies, protective gear, and immobilization materials, so you can locate them without searching through the entire kit.</p>", unsafe_allow_html=True)
st.markdown("<p>Inspect the contents several times each year. Replace expired products, damaged packaging, missing gloves, depleted medications if included, and batteries for flashlights or other emergency tools. Regular inspections ensure your supplies remain ready when you need them most.</p>", unsafe_allow_html=True)

st.markdown("<h2>Common Mistakes That Reduce Emergency Preparedness</h2>", unsafe_allow_html=True)
st.markdown("<p>One common mistake is purchasing specialized equipment without learning how to use it correctly. Even the best trauma supplies become far less effective if the user is unfamiliar with their application. Taking a basic first-aid or bleeding-control course builds confidence and helps you respond more appropriately during emergencies.</p>", unsafe_allow_html=True)
st.markdown("<p>Another mistake is relying solely on a small household first-aid kit. While these kits are useful for minor cuts and scrapes, they often lack the supplies needed for serious traumatic injuries. Expanding your vehicle kit with purpose-built trauma equipment provides a more practical level of preparedness.</p>", unsafe_allow_html=True)

st.markdown("<h2>Choosing Reliable Trauma Supplies for Long-Term Readiness</h2>", unsafe_allow_html=True)
st.markdown("<p>Selecting dependable trauma supplies means looking beyond the number of items included in a kit. Durable storage, clearly organized compartments, quality medical components, and equipment appropriate for your level of training all contribute to effective emergency preparedness. Whether you drive across town every day or regularly travel long distances, investing time in building a thoughtful vehicle trauma kit helps ensure you are better prepared to respond calmly and safely if an unexpected emergency occurs.</p>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# --- Services Section ---
st.markdown("<div id='services'></div>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; margin-bottom: 30px;'>MISSION-READY SERVICES</h2>", unsafe_allow_html=True)
serv_col1, serv_col2, serv_col3 = st.columns(3)
with serv_col1:
    st.markdown("""<div class='service-box'><h3>IFAK Customization</h3><p>Tailored Individual First Aid Kits designed for specific mission profiles, from low-profile EDC to full-scale tactical operations.</p></div>""", unsafe_allow_html=True)
with serv_col2:
    st.markdown("""<div class='service-box'><h3>Bleeding Control</h3><p>Expertly curated hemorrhage control kits featuring TCCC-recommended tourniquets and hemostatic agents.</p></div>""", unsafe_allow_html=True)
with serv_col3:
    st.markdown("""<div class='service-box'><h3>Fleet Preparedness</h3><p>Comprehensive medical equipment planning for commercial fleets, first responders, and off-road expeditions.</p></div>""", unsafe_allow_html=True)

# --- About Section ---
st.markdown("<div id='about'></div>", unsafe_allow_html=True)
st.markdown("<div class='content-card' style='margin-top: 50px;'>", unsafe_allow_html=True)
st.markdown("<h2>About Lifeline Frontier</h2>", unsafe_allow_html=True)
st.markdown("<p>Lifeline Frontier is a premier provider of tactical medical equipment and trauma care solutions. We operate at the intersection of professional medicine and field operations, ensuring that those who work in high-risk environments have access to the most reliable gear available.</p>", unsafe_allow_html=True)
st.markdown("<p>Our philosophy is simple: <strong>Reliability is the only metric that matters.</strong> Every component we recommend and every kit we build is vetted for rapid response in high-stress scenarios. Whether you are a first responder, a military professional, or a prepared citizen, we provide the tools necessary to bridge the gap between injury and professional medical care.</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- Contact Section ---
st.markdown("<div id='contact'></div>", unsafe_allow_html=True)
st.markdown("""
<div class="contact-banner">
    <h2 style="color: white; border: none;">READY FOR THE FRONTIER?</h2>
    <p>Contact our tactical specialists for bulk quotes or custom kit consultations.</p>
    <div class="contact-info">support@flaresyn.com</div>
    <div class="contact-info">+1 925 897-9800</div>
    <p style="margin-top: 20px; font-weight: 700; opacity: 0.8;">OPERATIONAL 24/7 FOR CRITICAL NEEDS</p>
</div>
""", unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
<div class="footer">
    <p>&copy; 2026 LIFELINE FRONTIER. ALL RIGHTS RESERVED.</p>
    <p>TACTICAL MEDICAL SOLUTIONS | TRAUMA CARE | EMERGENCY PREPAREDNESS</p>
</div>
""", unsafe_allow_html=True)
