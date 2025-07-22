import requests
import os

# Get API key from environment variable with fallback
API_KEY = os.getenv("OPENROUTER_API_KEY", "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")

def generate_comprehensive_project(config):
    """
    Generate a comprehensive project package with accessibility modifications
    and formal lesson plan using OpenRouter API
    """
    
    # Construct the comprehensive prompt
    prompt = construct_comprehensive_prompt(config)
    
    # Make API call
    result = call_openrouter_api(prompt)
    
    return result

def construct_comprehensive_prompt(config):
    """
    Construct a detailed prompt for generating comprehensive educational content
    """
    
    environment_context = get_environment_context(config['environment'])
    
    base_prompt = f"""
You are an expert educational curriculum designer and special education specialist. Generate a complete, comprehensive, grade-appropriate, and engaging educational project package with the following specifications:

**PROJECT SPECIFICATIONS:**
- State: {config['state']}
- Content Area: {config['content_area']} 
- Grade Level: {config['grade']}
- Standard: {config['standard']} - {config['standard_title']}
- Sub-Standard: {config['sub_standard']} - {config['sub_standard_description']}
- Group Configuration: {config['group_size']}
- Learning Environment: {config['environment']}
- Time Allotment: {config['time_allotment']}

{environment_context}

**REQUIRED OUTPUT SECTIONS:**

## 1. STANDARD PROJECT VERSION

### Project Title
Create an engaging, grade-appropriate title that captures the essence of the learning objectives.

### Driving Question
Develop a compelling essential question that guides student inquiry and connects to real-world applications.

### Project Overview & Learning Objectives
- Detailed project description (2-3 paragraphs)
- Clear alignment to the specified standard and sub-standard
- Grade-appropriate language and concepts with vocabulary in bold
- Real-world connections and relevance

### Materials & Resources List
{get_materials_section(config['environment'])}

### Implementation Timeline
Break down the project into phases across the {config['time_allotment']} timeframe:
- Phase breakdown with specific activities
- Milestones and checkpoints
- Assessment touchpoints

### Detailed Activity Instructions
Step-by-step instructions for:
- Project introduction and setup
- Core learning activities
- {get_group_instructions(config['group_size'])}
- Culminating activities

### Assessment & Rubric
Create a detailed 4-category rubric aligned to the standard:
- Content Knowledge & Understanding
- Application of Skills
- {get_group_assessment(config['group_size'])}
- Communication & Presentation

### Post-Project Comprehension Questions
5-7 thought-provoking questions that assess understanding and encourage reflection.

---SECTION_SEPARATOR---

## 2. FORMAL LESSON PLAN FOR ADMINISTRATIVE SUBMISSION

### Lesson Plan Header
- Teacher: [Teacher Name]
- Subject: {config['content_area']}
- Grade Level: {config['grade']}
- Duration: {config['time_allotment']}
- Date: [Date]

### Standards Alignment
- Primary Standard: {config['standard']} - {config['standard_title']}
- Sub-Standard: {config['sub_standard']} - {config['sub_standard_description']}
- Cross-curricular connections (if applicable)

### Learning Objectives
Students will be able to:
- [3-4 specific, measurable objectives using action verbs]

### Essential Question(s)
- Primary driving question
- Supporting inquiry questions

### Assessment Plan
- Formative assessments throughout project
- Summative assessment criteria
- Differentiation strategies for diverse learners

### Materials & Technology Requirements
- Detailed supply list with quantities
- Technology tools and platforms needed
- Safety considerations (if applicable)

### Instructional Sequence
**Opening/Hook** ({get_time_breakdown(config['time_allotment'], 'opening')})
- Engagement strategy
- Prior knowledge activation

**Development/Exploration** ({get_time_breakdown(config['time_allotment'], 'main')})
- Core learning activities
- Guided practice opportunities
- Independent/group work time

**Closure/Reflection** ({get_time_breakdown(config['time_allotment'], 'closure')})
- Summary and reflection activities
- Preview of next steps

### Differentiation & Accommodations
- Strategies for diverse learning needs
- Extension activities for advanced learners
- Support structures for struggling students

### Home-School Connection
- Family engagement opportunities
- At-home extensions or preparation

### Administrative Notes
- Professional development connections
- Curriculum mapping alignment
- Data collection points for school improvement

{generate_accessibility_sections(config['accessibility_modifications'])}
"""

    return base_prompt

def get_environment_context(environment):
    """Generate environment-specific context for project generation"""
    if environment == "Virtual Learning Environment":
        return """
**IMPORTANT: This is a VIRTUAL learning environment project. All activities, materials, and interactions must be designed for online/digital delivery. Do not include any physical materials, hands-on manipulatives, or in-person activities. Focus on:**
- Digital tools and online platforms
- Virtual collaboration and communication
- Screen-based activities and simulations
- Online research and digital resources
- Video conferencing and digital presentation tools
- Cloud-based collaboration platforms
- Digital assessment and feedback methods
"""
    else:
        return """
**IMPORTANT: This is a BRICK & MORTAR classroom project. Design activities for in-person learning with physical materials and face-to-face interactions. Include:**
- Physical manipulatives and hands-on materials
- In-person collaboration and group work
- Laboratory equipment and classroom tools
- Print resources and physical books
- Face-to-face presentations and discussions
- Physical classroom environment considerations
"""

def get_materials_section(environment):
    """Generate appropriate materials section based on learning environment"""
    if environment == "Virtual Learning Environment":
        return """
### Digital Materials & Technology Requirements
- Required software/platforms and account setup instructions
- Hardware requirements and alternatives
- Digital resources and online databases
- Virtual collaboration tools
- Screen recording/presentation software
- Internet connectivity requirements"""
    else:
        return """
### Physical Materials List
- Consumable supplies with specific quantities
- Reusable equipment and tools
- Technology requirements (computers, tablets, etc.)
- Safety equipment (if applicable)
- Reference materials and books
- Storage and organization supplies"""

def get_group_instructions(group_size):
    """Generate group-specific instructions"""
    if "Solo" in group_size:
        return "Individual work strategies and self-monitoring techniques"
    elif "Pair" in group_size:
        return "Partner collaboration protocols and role assignments"
    elif "Small Groups" in group_size:
        return "Small group dynamics and individual accountability measures"
    else:
        return "Large group management and participation strategies"

def get_group_assessment(group_size):
    """Generate appropriate assessment criteria for group configuration"""
    if "Solo" in group_size:
        return "Individual Accountability & Self-Reflection"
    else:
        return "Collaboration & Teamwork"

def get_time_breakdown(time_allotment, phase):
    """Generate time estimates for different lesson phases"""
    time_mapping = {
        "30 minutes": {"opening": "5 min", "main": "20 min", "closure": "5 min"},
        "1 hour": {"opening": "10 min", "main": "40 min", "closure": "10 min"},
        "1 class period": {"opening": "10 min", "main": "30 min", "closure": "10 min"},
        "2 class periods": {"opening": "15 min", "main": "60 min", "closure": "15 min"},
        "3 class periods": {"opening": "20 min", "main": "90 min", "closure": "20 min"},
        "1 week": {"opening": "Day 1", "main": "Days 2-4", "closure": "Day 5"},
        "2 weeks": {"opening": "Days 1-2", "main": "Days 3-8", "closure": "Days 9-10"},
        "3 weeks": {"opening": "Week 1", "main": "Weeks 2-3", "closure": "End of Week 3"},
        "1 month": {"opening": "Week 1", "main": "Weeks 2-3", "closure": "Week 4"}
    }
    
    return time_mapping.get(time_allotment, {}).get(phase, "TBD")

def generate_accessibility_sections(modifications):
    """Generate sections for each accessibility modification"""
    if not modifications:
        return ""
    
    sections = []
    
    for modification in modifications:
        sections.append(f"""
---SECTION_SEPARATOR---

## 3. ACCESSIBILITY MODIFICATION: {modification.upper()}

### Modified Project Overview
- Adaptation rationale and educational philosophy
- Maintained learning objectives with adjusted delivery methods
- Specific accommodations and supports

### Modified Implementation Strategy
- Adjusted timeline and pacing
- Alternative activity formats
- Additional scaffolding and support structures
- Modified group configurations (if applicable)

### Specialized Materials & Resources
- Assistive technology requirements
- Alternative format materials
- Sensory considerations
- Additional support tools

### Modified Assessment Approach
- Alternative assessment formats
- Adjusted success criteria while maintaining rigor
- Multi-modal demonstration options
- Progress monitoring strategies

### Support Personnel & Training
- Recommended staff training or collaboration
- Specialist consultation recommendations
- Family communication strategies

### Implementation Notes for Educators
- Preparation requirements
- Classroom environment modifications
- Peer support strategies
- Crisis or challenge response protocols
""")
    
    return "\n".join(sections)

def call_openrouter_api(prompt):
    """Make API call to OpenRouter"""
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {
                "role": "system", 
                "content": "You are an expert educational curriculum designer, special education specialist, and lesson planning professional. You create comprehensive, standards-aligned educational materials that are engaging, grade-appropriate, rigorous, and accessible. Your responses are detailed, practical, and ready for immediate classroom implementation."
            },
            {
                "role": "user", 
                "content": prompt
            }
        ],
        "max_tokens": 4000,
        "temperature": 0.7
    }

    try:
        response = requests.post(url, headers=headers, json=body, timeout=60)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return f"❌ Error: {response.status_code} — {response.text}"
    except requests.exceptions.Timeout:
        return "❌ Error: Request timed out. Please try again."
    except requests.exceptions.RequestException as e:
        return f"❌ Error: Network error occurred - {str(e)}"
    except Exception as e:
        return f"❌ Error: Unexpected error occurred - {str(e)}"
