"""
Accessibility modifications and accommodations for educational projects
Based on special education best practices and inclusive design principles
"""

def get_accessibility_options():
    """
    Return list of accessibility modification categories
    """
    return [
        "Cognitive Abilities Support",
        "Gifted & Talented Extensions", 
        "504 Plan Accommodations",
        "IEP Modifications",
        "Behavioral Support Accommodations",
        "English Language Learner Support",
        "Physical Accessibility Accommodations",
        "Sensory Processing Support",
        "Executive Function Support",
        "Social-Emotional Learning Support"
    ]

def get_accessibility_descriptions():
    """
    Return detailed descriptions for each accessibility modification type
    """
    return {
        "Cognitive Abilities Support": "Modifications for students with intellectual disabilities, including simplified instructions, visual supports, concrete examples, extended time, and alternative demonstration methods while maintaining core learning objectives.",
        
        "Gifted & Talented Extensions": "Enrichment activities for advanced learners including deeper inquiry questions, independent research opportunities, leadership roles, creative expression options, and accelerated or compacted curriculum elements.",
        
        "504 Plan Accommodations": "Accommodations for students with documented disabilities under Section 504, including environmental modifications, presentation accommodations, response accommodations, timing adjustments, and setting changes.",
        
        "IEP Modifications": "Individualized modifications for students with disabilities under IDEA, including altered learning objectives, specialized instruction methods, alternative assessment formats, and support from special education professionals.",
        
        "Behavioral Support Accommodations": "Structured supports for students with behavioral challenges including clear expectations, positive reinforcement systems, break opportunities, choice-making options, and de-escalation strategies.",
        
        "English Language Learner Support": "Language supports for ELL students including visual aids, translation resources, simplified vocabulary, peer translation support, extended time, and cultural relevance connections.",
        
        "Physical Accessibility Accommodations": "Modifications for students with physical disabilities including alternative materials, adaptive equipment, positioning supports, modified workspace setup, and assistive technology integration.",
        
        "Sensory Processing Support": "Accommodations for sensory processing differences including noise reduction options, tactile alternatives, visual schedules, sensory breaks, and environmental modifications.",
        
        "Executive Function Support": "Supports for organization and planning challenges including task breakdown, checklists, visual organizers, time management tools, and structured routines.",
        
        "Social-Emotional Learning Support": "Supports for social-emotional development including emotion regulation strategies, social skills practice, conflict resolution tools, and relationship building activities."
    }

def get_modification_strategies(modification_type):
    """
    Return specific strategies for each modification type
    """
    strategies = {
        "Cognitive Abilities Support": {
            "instruction": [
                "Break complex tasks into smaller, sequential steps",
                "Use concrete, hands-on materials and examples", 
                "Provide visual supports and graphic organizers",
                "Implement peer buddy systems",
                "Use simplified vocabulary while maintaining concepts"
            ],
            "assessment": [
                "Allow alternative demonstration methods",
                "Provide extended time for completion",
                "Use portfolio-based assessment",
                "Accept verbal responses in place of written",
                "Focus on progress rather than grade-level standards"
            ],
            "materials": [
                "High-interest, age-appropriate materials",
                "Manipulatives and tactile resources",
                "Picture schedules and visual cues",
                "Technology supports and apps",
                "Simplified text versions"
            ]
        },
        
        "Gifted & Talented Extensions": {
            "instruction": [
                "Provide open-ended, complex problems",
                "Encourage independent research and inquiry",
                "Offer leadership and mentoring opportunities",
                "Allow for creative and innovative solutions",
                "Connect to real-world applications"
            ],
            "assessment": [
                "Portfolio and project-based assessment",
                "Self-reflection and goal-setting",
                "Peer evaluation opportunities",
                "Exhibition and presentation formats",
                "Advanced rubrics with higher-order thinking"
            ],
            "materials": [
                "Primary source documents",
                "Advanced texts and resources",
                "Technology for research and creation",
                "Professional-level tools and software",
                "Access to expert mentors and professionals"
            ]
        },
        
        "504 Plan Accommodations": {
            "instruction": [
                "Preferential seating arrangements",
                "Reduced distractions in environment",
                "Clear, consistent routines and expectations",
                "Multiple means of presenting information",
                "Regular check-ins and progress monitoring"
            ],
            "assessment": [
                "Extended time for assignments and tests",
                "Alternative testing environments",
                "Modified test formats (oral, multiple choice)",
                "Assistive technology for responses",
                "Frequent breaks during assessments"
            ],
            "materials": [
                "Large print or digital text options",
                "Audio recordings of instructions",
                "Calculator or computational aids",
                "Note-taking supports",
                "Organizational tools and planners"
            ]
        }
    }
    
    return strategies.get(modification_type, {})

def generate_accommodation_suggestions(modifications_list, content_area, grade_level):
    """
    Generate specific accommodation suggestions based on selected modifications,
    content area, and grade level
    """
    suggestions = {}
    
    for modification in modifications_list:
        suggestions[modification] = {
            "general": get_modification_strategies(modification),
            "content_specific": get_content_specific_accommodations(modification, content_area),
            "grade_specific": get_grade_specific_accommodations(modification, grade_level)
        }
    
    return suggestions

def get_content_specific_accommodations(modification_type, content_area):
    """
    Get accommodations specific to content areas
    """
    content_accommodations = {
        "Mathematics": {
            "Cognitive Abilities Support": [
                "Use manipulatives for abstract concepts",
                "Provide number lines and hundreds charts",
                "Break word problems into steps",
                "Use real-world examples for math concepts"
            ],
            "Gifted & Talented Extensions": [
                "Explore mathematical patterns and relationships",
                "Connect to advanced mathematical concepts",
                "Real-world problem solving applications",
                "Mathematical modeling opportunities"
            ]
        },
        
        "English Language Arts": {
            "Cognitive Abilities Support": [
                "Use graphic organizers for writing",
                "Provide sentence starters and frames",
                "Audio recordings of texts",
                "Picture books for complex concepts"
            ],
            "Gifted & Talented Extensions": [
                "Advanced literary analysis",
                "Creative writing opportunities",
                "Research and presentation projects",
                "Cross-textual comparisons"
            ]
        },
        
        "Science": {
            "Cognitive Abilities Support": [
                "Hands-on experiments and demonstrations",
                "Science journals with pictures and words",
                "Step-by-step lab procedures",
                "Safety modifications as needed"
            ],
            "Gifted & Talented Extensions": [
                "Independent research projects",
                "Advanced experimental design",
                "Real-world scientific applications",
                "Connections to current scientific discoveries"
            ]
        },
        
        "Social Studies": {
            "Cognitive Abilities Support": [
                "Timeline and map activities",
                "Role-playing historical events",
                "Picture books about historical topics",
                "Community connections and field trips"
            ],
            "Gifted & Talented Extensions": [
                "Primary source analysis",
                "Debate and discussion opportunities",
                "Current events connections",
                "Leadership and civic engagement projects"
            ]
        }
    }
    
    return content_accommodations.get(content_area, {}).get(modification_type, [])

def get_grade_specific_accommodations(modification_type, grade_level):
    """
    Get accommodations specific to grade levels
    """
    grade_accommodations = {
        "6th": {
            "Cognitive Abilities Support": [
                "Transition supports for middle school structure",
                "Organizational systems and routines",
                "Peer support and buddy systems",
                "Visual schedules and reminders"
            ],
            "Gifted & Talented Extensions": [
                "Independent study opportunities",
                "Mentorship with older students",
                "Academic competitions and challenges",
                "Advanced course access"
            ]
        },
        
        "7th": {
            "Cognitive Abilities Support": [
                "Social skills development activities",
                "Self-advocacy skill building",
                "Study skills and learning strategies",
                "Technology supports for organization"
            ],
            "Gifted & Talented Extensions": [
                "Leadership roles in school activities",
                "Community service learning",
                "Advanced research methodologies",
                "Cross-curricular project opportunities"
            ]
        },
        
        "8th": {
            "Cognitive Abilities Support": [
                "High school transition planning",
                "Career exploration activities", 
                "Self-determination skill development",
                "IEP transition goal setting"
            ],
            "Gifted & Talented Extensions": [
                "High school course preparation",
                "Advanced placement readiness",
                "Community internship opportunities",
                "College and career exploration"
            ]
        }
    }
    
    return grade_accommodations.get(grade_level, {}).get(modification_type, [])
