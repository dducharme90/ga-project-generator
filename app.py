import streamlit as st
import os
from standards_database import get_standards_data, get_states, get_content_areas, get_grades, get_standards, get_sub_standards
from project_generator import generate_comprehensive_project
from accessibility_modifications import get_accessibility_options, get_accessibility_descriptions

# Page configuration
st.set_page_config(
    page_title="Georgia Middle School Project Generator",
    page_icon="🍑",
    layout="wide"
)

# Custom CSS for modern, school-friendly design
st.markdown("""
<style>
    /* Main app styling */
    .main {
        padding: 2rem 1rem;
    }
    
    /* Header styling */
    .header-container {
        background: linear-gradient(135deg, #1f4e8b 0%, #3b82f6 100%);
        padding: 2rem;
        margin: -1rem -1rem 2rem -1rem;
        border-radius: 0 0 20px 20px;
        box-shadow: 0 4px 15px rgba(31, 78, 139, 0.2);
    }
    
    .header-title {
        color: white;
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
        text-align: center;
    }
    
    .header-subtitle {
        color: #e2e8f0;
        font-size: 1.1rem;
        text-align: center;
        margin: 0.5rem 0 0 0;
        font-weight: 300;
    }
    
    /* Section styling */
    .section-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        margin-bottom: 1.5rem;
        border-left: 4px solid #1f4e8b;
    }
    
    .section-title {
        color: #1f4e8b;
        font-size: 1.3rem;
        font-weight: 600;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    /* Form styling */
    .stSelectbox label {
        color: #374151 !important;
        font-weight: 500 !important;
    }
    
    .stMultiSelect label {
        color: #374151 !important;
        font-weight: 500 !important;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #1f4e8b 0%, #3b82f6 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(31, 78, 139, 0.2);
    }
    
    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 8px rgba(31, 78, 139, 0.3);
    }
    
    /* Success message styling */
    .success-card {
        background: #f0f9ff;
        border: 1px solid #0ea5e9;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    /* Info boxes */
    .info-box {
        background: #fef3c7;
        border-left: 4px solid #f59e0b;
        padding: 1rem;
        border-radius: 0 8px 8px 0;
        margin: 1rem 0;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'standards_data' not in st.session_state:
    st.session_state.standards_data = get_standards_data()

def main():
    # Modern header
    st.markdown("""
    <div class="header-container">
        <h1 class="header-title">🍑 Georgia Middle School Project Generator</h1>
        <p class="header-subtitle">Create comprehensive, standards-aligned educational projects with built-in accessibility support</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize all variables with defaults to avoid UnboundLocalError
    selected_state = "Georgia"  # Fixed to Georgia
    selected_content_area = ""
    selected_grade = ""
    selected_standard = ""
    selected_sub_standard = ""
    standard_info = {}
    sub_standards = {}
    selected_group_size = ""
    selected_environment = ""
    selected_time = ""
    selected_modifications = []
    
    # Create two columns for better layout
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div class="section-card">
            <div class="section-title">📚 Standards Selection</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Content Area selection (Georgia only)
        content_areas = get_content_areas(st.session_state.standards_data, selected_state)
        selected_content_area = st.selectbox(
            "📖 Content Area",
            options=[""] + content_areas,
            key="content_area_select",
            help="Choose the subject area for your project"
        )
        
        if selected_content_area:
            # Grade selection
            grades = get_grades(st.session_state.standards_data, selected_state, selected_content_area)
            selected_grade = st.selectbox(
                "🎯 Grade Level",
                options=[""] + grades,
                key="grade_select",
                help="Select the target grade level"
            )
            
            if selected_grade:
                # Standard selection
                standards = get_standards(st.session_state.standards_data, selected_state, selected_content_area, selected_grade)
                selected_standard = st.selectbox(
                    "📋 Standard",
                    options=[""] + list(standards.keys()),
                    key="standard_select",
                    help="Choose the specific standard to address"
                )
                
                if selected_standard:
                    # Get standard info for display
                    standard_info = standards[selected_standard]
                    st.markdown(f"""
                    <div class="info-box">
                        <strong>{selected_standard}:</strong> {standard_info.get('title', 'No title available')}
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Sub-standard selection
                    sub_standards = get_sub_standards(st.session_state.standards_data, selected_state, selected_content_area, selected_grade, selected_standard)
                    if sub_standards:
                        selected_sub_standard = st.selectbox(
                            "🎯 Sub-Standard",
                            options=[""] + list(sub_standards.keys()),
                            key="sub_standard_select",
                            help="Choose specific learning element"
                        )
                        
                        if selected_sub_standard:
                            st.markdown(f"""
                            <div class="success-card">
                                <strong>{selected_sub_standard}:</strong> {sub_standards[selected_sub_standard]}
                            </div>
                            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="section-card">
            <div class="section-title">⚙️ Project Configuration</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Group size selection
        group_options = ["Solo Project", "Pair Work", "Small Groups (3-4)", "Large Groups (5-6)"]
        selected_group_size = st.selectbox(
            "👥 Group Size",
            options=[""] + group_options,
            key="group_size_select",
            help="Choose how students will work together"
        )
        
        # Learning environment selection
        environment_options = ["Brick & Mortar Classroom", "Virtual Learning Environment"]
        selected_environment = st.selectbox(
            "🏫 Learning Environment",
            options=[""] + environment_options,
            key="environment_select",
            help="Select physical or virtual classroom setting"
        )
        
        # Time selection
        time_options = ["1 Class Period", "2-3 Class Periods", "1 Week", "2 Weeks", "1 Month"]
        selected_time = st.selectbox(
            "⏰ Project Duration",
            options=[""] + time_options,
            key="time_select",
            help="How much time should this project take?"
        )
        
        # Accessibility modifications
        st.markdown("""
        <div class="section-card">
            <div class="section-title">♿ Accessibility Support</div>
        </div>
        """, unsafe_allow_html=True)
        
        accessibility_options = get_accessibility_options()
        selected_modifications = st.multiselect(
            "🎯 Accessibility Modifications",
            options=accessibility_options,
            key="accessibility_select",
            help="Choose accommodations for students with special needs"
        )
        
        # Display descriptions for selected modifications
        if selected_modifications:
            with st.expander("View Selected Modification Details"):
                descriptions = get_accessibility_descriptions()
                for mod in selected_modifications:
                    st.write(f"**{mod}:** {descriptions.get(mod, 'No description available')}")
    
    # Generation section
    st.markdown("---")
    
    # Check if all required fields are filled
    can_generate = all([
        selected_state,
        selected_content_area,
        selected_grade,
        selected_standard,
        selected_sub_standard,
        selected_group_size,
        selected_environment,
        selected_time
    ])
    
    if can_generate:
        if st.button("🚀 Generate Comprehensive Project Package", type="primary", use_container_width=True):
            with st.spinner("Generating comprehensive project package... This may take a moment."):
                
                # Prepare project configuration
                project_config = {
                    'state': selected_state,
                    'content_area': selected_content_area,
                    'grade': selected_grade,
                    'standard': selected_standard,
                    'standard_title': standard_info.get('title', ''),
                    'sub_standard': selected_sub_standard,
                    'sub_standard_description': sub_standards[selected_sub_standard],
                    'group_size': selected_group_size,
                    'environment': selected_environment,
                    'time_allotment': selected_time,
                    'accessibility_modifications': selected_modifications
                }
                
                # Generate the project
                result = generate_comprehensive_project(project_config)
                
                if result.startswith("❌"):
                    st.error(result)
                else:
                    st.success("✅ Project package generated successfully!")
                    
                    # Display the generated content
                    st.markdown("## 📋 Generated Project Package")
                    
                    # Create tabs for different sections
                    if selected_modifications:
                        tab_names = ["Standard Project", "Formal Lesson Plan"] + [f"{mod} Version" for mod in selected_modifications]
                    else:
                        tab_names = ["Standard Project", "Formal Lesson Plan"]
                    
                    tabs = st.tabs(tab_names)
                    
                    # Parse the result to separate different sections
                    sections = result.split("---SECTION_SEPARATOR---")
                    
                    with tabs[0]:
                        st.markdown("### 📘 Standard Project")
                        st.markdown(sections[0] if len(sections) > 0 else result)
                    
                    with tabs[1]:
                        st.markdown("### 📄 Formal Lesson Plan")
                        st.markdown(sections[1] if len(sections) > 1 else "Lesson plan included in main project.")
                    
                    # Accessibility modification tabs
                    if selected_modifications and len(sections) > 2:
                        for i, mod in enumerate(selected_modifications):
                            with tabs[i + 2]:
                                st.markdown(f"### ♿ {mod} Version")
                                section_index = i + 2
                                if section_index < len(sections):
                                    st.markdown(sections[section_index])
                                else:
                                    st.markdown("Accessibility modifications included in main project.")
    else:
        st.info("👆 Please complete all required selections above to generate your project package.")
        
        # Show what's missing
        missing_fields = []
        if not selected_state: missing_fields.append("State")
        if not selected_content_area: missing_fields.append("Content Area")
        if not selected_grade: missing_fields.append("Grade Level")
        if not selected_standard: missing_fields.append("Standard")
        if not selected_sub_standard: missing_fields.append("Sub-Standard")
        
        if missing_fields:
            st.warning(f"Missing required fields: {', '.join(missing_fields)}")

if __name__ == "__main__":
    main()
