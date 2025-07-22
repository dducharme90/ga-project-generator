"""
Georgia Standards Database for Middle School Education
Supporting Mathematics, English Language Arts, Social Studies, and Science for grades 6-8
"""

def get_standards_data():
    """
    Returns a comprehensive standards database for Georgia middle school content areas.
    This represents real standards from the Georgia Department of Education.
    """
    return {
        "Georgia": {
            "Mathematics": {
                "6th": {
                    "MGSE6.RP.1": {
                        "title": "Understand the concept of a ratio and use ratio language",
                        "elements": {
                            "MGSE6.RP.1a": "Describe the relationship between two quantities using ratio language",
                            "MGSE6.RP.1b": "Use ratio and rate reasoning to solve real-world problems",
                            "MGSE6.RP.1c": "Make tables of equivalent ratios relating quantities with whole number measurements"
                        }
                    },
                    "MGSE6.RP.2": {
                        "title": "Understand the concept of a unit rate",
                        "elements": {
                            "MGSE6.RP.2a": "Find a percent of a quantity as a rate per 100",
                            "MGSE6.RP.2b": "Solve problems involving finding the whole given a part and the percent",
                            "MGSE6.RP.2c": "Use ratio reasoning to convert measurement units"
                        }
                    },
                    "MGSE6.NS.1": {
                        "title": "Interpret and compute quotients of fractions",
                        "elements": {
                            "MGSE6.NS.1a": "Divide fractions by fractions using visual models and equations",
                            "MGSE6.NS.1b": "Apply and extend previous understandings of multiplication and division",
                            "MGSE6.NS.1c": "Solve real world problems involving division of fractions by fractions"
                        }
                    },
                    "MGSE6.NS.2": {
                        "title": "Fluently divide multi-digit numbers using the standard algorithm",
                        "elements": {
                            "MGSE6.NS.2a": "Fluently add, subtract, multiply, and divide multi-digit decimals",
                            "MGSE6.NS.2b": "Use the standard algorithm for each operation",
                            "MGSE6.NS.2c": "Apply number properties to justify computational strategies"
                        }
                    },
                    "MGSE6.EE.1": {
                        "title": "Write and evaluate numerical expressions involving whole-number exponents",
                        "elements": {
                            "MGSE6.EE.1a": "Write and evaluate expressions involving whole-number exponents",
                            "MGSE6.EE.1b": "Apply the properties of operations to generate equivalent expressions",
                            "MGSE6.EE.1c": "Identify when two expressions are equivalent"
                        }
                    },
                    "MGSE6.G.1": {
                        "title": "Find the area of right triangles, other triangles, and special quadrilaterals",
                        "elements": {
                            "MGSE6.G.1a": "Compose and decompose shapes to find areas of polygons",
                            "MGSE6.G.1b": "Apply these techniques to solve real-world and mathematical problems",
                            "MGSE6.G.1c": "Use formulas for area and perimeter of rectangles to solve problems"
                        }
                    }
                },
                "7th": {
                    "MGSE7.RP.1": {
                        "title": "Compute unit rates associated with ratios of fractions",
                        "elements": {
                            "MGSE7.RP.1a": "Recognize and represent proportional relationships between quantities",
                            "MGSE7.RP.1b": "Decide whether two quantities are in a proportional relationship",
                            "MGSE7.RP.1c": "Identify the constant of proportionality in various representations"
                        }
                    },
                    "MGSE7.NS.1": {
                        "title": "Apply and extend previous understandings of addition and subtraction",
                        "elements": {
                            "MGSE7.NS.1a": "Describe situations in which opposite quantities combine to make 0",
                            "MGSE7.NS.1b": "Understand p + q as the number located a distance |q| from p",
                            "MGSE7.NS.1c": "Show that a number and its opposite have a sum of 0"
                        }
                    },
                    "MGSE7.EE.3": {
                        "title": "Solve multi-step real-life and mathematical problems",
                        "elements": {
                            "MGSE7.EE.3a": "Solve problems posed with positive and negative rational numbers",
                            "MGSE7.EE.3b": "Apply properties of operations to calculate with numbers in any form",
                            "MGSE7.EE.3c": "Convert between forms as appropriate and assess reasonableness of answers"
                        }
                    },
                    "MGSE7.G.4": {
                        "title": "Know the formulas for the area and circumference of a circle",
                        "elements": {
                            "MGSE7.G.4a": "Use formulas for area and circumference of circles to solve problems",
                            "MGSE7.G.4b": "Give an informal derivation of the relationship between circumference and area",
                            "MGSE7.G.4c": "Solve real-world and mathematical problems involving area and volume"
                        }
                    },
                    "MGSE7.SP.1": {
                        "title": "Understand that statistics can be used to gain information about a population",
                        "elements": {
                            "MGSE7.SP.1a": "Understand that generalizations about a population from a sample are valid",
                            "MGSE7.SP.1b": "Use data from a random sample to draw inferences about a population",
                            "MGSE7.SP.1c": "Generate multiple samples to gauge the variation in estimates or predictions"
                        }
                    }
                },
                "8th": {
                    "MGSE8.NS.1": {
                        "title": "Know that numbers that are not rational are called irrational",
                        "elements": {
                            "MGSE8.NS.1a": "Understand informally that every number has a decimal expansion",
                            "MGSE8.NS.1b": "Convert a decimal expansion which repeats eventually into a rational number",
                            "MGSE8.NS.1c": "Use rational approximations of irrational numbers to compare sizes"
                        }
                    },
                    "MGSE8.EE.1": {
                        "title": "Know and apply the properties of integer exponents",
                        "elements": {
                            "MGSE8.EE.1a": "Know and apply the properties of integer exponents to generate equivalent expressions",
                            "MGSE8.EE.1b": "Use square root and cube root symbols to represent solutions",
                            "MGSE8.EE.1c": "Evaluate square roots of small perfect squares and cube roots"
                        }
                    },
                    "MGSE8.F.1": {
                        "title": "Understand that a function is a rule that assigns to each input exactly one output",
                        "elements": {
                            "MGSE8.F.1a": "Understand that a function assigns exactly one output to each input",
                            "MGSE8.F.1b": "Compare properties of two functions each represented in a different way",
                            "MGSE8.F.1c": "Interpret the equation y = mx + b as defining a linear function"
                        }
                    },
                    "MGSE8.G.1": {
                        "title": "Verify experimentally the properties of rotations, reflections, and translations",
                        "elements": {
                            "MGSE8.G.1a": "Lines are taken to lines, and line segments to line segments of the same length",
                            "MGSE8.G.1b": "Angles are taken to angles of the same measure",
                            "MGSE8.G.1c": "Parallel lines are taken to parallel lines"
                        }
                    },
                    "MGSE8.G.7": {
                        "title": "Apply the Pythagorean Theorem to determine unknown side lengths",
                        "elements": {
                            "MGSE8.G.7a": "Explain a proof of the Pythagorean Theorem and its converse",
                            "MGSE8.G.7b": "Apply the Pythagorean Theorem to find the distance between two points",
                            "MGSE8.G.7c": "Apply the Pythagorean Theorem to solve real-world problems"
                        }
                    }
                }
            },
            "English Language Arts": {
                "6th": {
                    "ELAGSE6.RL.1": {
                        "title": "Cite textual evidence to support analysis of what the text says explicitly",
                        "elements": {
                            "ELAGSE6.RL.1a": "Cite textual evidence to support analysis of what the text says explicitly",
                            "ELAGSE6.RL.1b": "Draw inferences from the text",
                            "ELAGSE6.RL.1c": "Provide textual evidence for inferences drawn from the text"
                        }
                    },
                    "ELAGSE6.RL.2": {
                        "title": "Determine a theme or central idea of a text",
                        "elements": {
                            "ELAGSE6.RL.2a": "Determine a theme or central idea of a text and how it is conveyed",
                            "ELAGSE6.RL.2b": "Analyze how theme is conveyed through particular details",
                            "ELAGSE6.RL.2c": "Provide a summary of the text distinct from personal opinions"
                        }
                    },
                    "ELAGSE6.W.1": {
                        "title": "Write arguments to support claims with clear reasons and relevant evidence",
                        "elements": {
                            "ELAGSE6.W.1a": "Introduce claim(s) and organize the reasons and evidence clearly",
                            "ELAGSE6.W.1b": "Support claim(s) with clear reasons and relevant evidence",
                            "ELAGSE6.W.1c": "Use words, phrases, and clauses to clarify the relationships among claims and reasons"
                        }
                    },
                    "ELAGSE6.SL.1": {
                        "title": "Engage effectively in a range of collaborative discussions",
                        "elements": {
                            "ELAGSE6.SL.1a": "Come to discussions prepared, having read or studied required material",
                            "ELAGSE6.SL.1b": "Follow rules for collegial discussions and decision-making",
                            "ELAGSE6.SL.1c": "Pose and respond to specific questions with elaboration and detail"
                        }
                    },
                    "ELAGSE6.L.1": {
                        "title": "Demonstrate command of the conventions of standard English grammar",
                        "elements": {
                            "ELAGSE6.L.1a": "Ensure that pronouns are in the proper case",
                            "ELAGSE6.L.1b": "Use intensive pronouns",
                            "ELAGSE6.L.1c": "Recognize and correct inappropriate shifts in pronoun number and person"
                        }
                    }
                },
                "7th": {
                    "ELAGSE7.RL.1": {
                        "title": "Cite several pieces of textual evidence to support analysis",
                        "elements": {
                            "ELAGSE7.RL.1a": "Cite several pieces of textual evidence to support analysis of what the text says explicitly",
                            "ELAGSE7.RL.1b": "Draw inferences from the text",
                            "ELAGSE7.RL.1c": "Provide multiple pieces of textual evidence for inferences"
                        }
                    },
                    "ELAGSE7.W.1": {
                        "title": "Write arguments to support claims with clear reasons and relevant evidence",
                        "elements": {
                            "ELAGSE7.W.1a": "Introduce claim(s), acknowledge alternate or opposing claims",
                            "ELAGSE7.W.1b": "Organize the reasons and evidence logically",
                            "ELAGSE7.W.1c": "Support claim(s) with logical reasoning and relevant evidence"
                        }
                    },
                    "ELAGSE7.SL.4": {
                        "title": "Present claims and findings, emphasizing salient points",
                        "elements": {
                            "ELAGSE7.SL.4a": "Present claims and findings, emphasizing salient points in a focused manner",
                            "ELAGSE7.SL.4b": "Use appropriate eye contact, adequate volume, and clear pronunciation",
                            "ELAGSE7.SL.4c": "Include multimedia components and visual displays in presentations"
                        }
                    },
                    "ELAGSE7.L.3": {
                        "title": "Use knowledge of language and its conventions",
                        "elements": {
                            "ELAGSE7.L.3a": "Choose language that expresses ideas precisely and concisely",
                            "ELAGSE7.L.3b": "Recognize and eliminate wordiness and redundancy",
                            "ELAGSE7.L.3c": "Maintain consistency in style and tone"
                        }
                    },
                    "ELAGSE7.RI.8": {
                        "title": "Trace and evaluate the argument and specific claims in a text",
                        "elements": {
                            "ELAGSE7.RI.8a": "Trace and evaluate the argument and specific claims in a text",
                            "ELAGSE7.RI.8b": "Assess whether reasoning is sound and evidence is relevant and sufficient",
                            "ELAGSE7.RI.8c": "Recognize when irrelevant evidence is introduced"
                        }
                    }
                },
                "8th": {
                    "ELAGSE8.RL.1": {
                        "title": "Cite textual evidence that most strongly supports analysis",
                        "elements": {
                            "ELAGSE8.RL.1a": "Cite textual evidence that most strongly supports an analysis of what the text says explicitly",
                            "ELAGSE8.RL.1b": "Draw inferences from the text",
                            "ELAGSE8.RL.1c": "Cite the textual evidence that most strongly supports an analysis of inferences drawn"
                        }
                    },
                    "ELAGSE8.W.1": {
                        "title": "Write arguments to support claims with clear reasons and relevant evidence",
                        "elements": {
                            "ELAGSE8.W.1a": "Introduce claim(s), acknowledge and distinguish the claim(s) from alternate or opposing claims",
                            "ELAGSE8.W.1b": "Organize the reasons and evidence logically",
                            "ELAGSE8.W.1c": "Support claim(s) with logical reasoning and relevant evidence"
                        }
                    },
                    "ELAGSE8.SL.1": {
                        "title": "Engage effectively in a range of collaborative discussions",
                        "elements": {
                            "ELAGSE8.SL.1a": "Come to discussions prepared, having read or researched material under study",
                            "ELAGSE8.SL.1b": "Follow rules for collegial discussions and decision-making, track progress toward goals",
                            "ELAGSE8.SL.1c": "Pose questions that connect the ideas of several speakers and respond with relevant observations"
                        }
                    },
                    "ELAGSE8.L.1": {
                        "title": "Demonstrate command of the conventions of standard English grammar",
                        "elements": {
                            "ELAGSE8.L.1a": "Explain the function of verbals (gerunds, participles, infinitives) in general",
                            "ELAGSE8.L.1b": "Form and use verbs in the active and passive voice",
                            "ELAGSE8.L.1c": "Recognize and correct inappropriate shifts in verb voice and mood"
                        }
                    },
                    "ELAGSE8.RI.6": {
                        "title": "Determine an author's point of view or purpose in a text",
                        "elements": {
                            "ELAGSE8.RI.6a": "Determine an author's point of view or purpose in a text",
                            "ELAGSE8.RI.6b": "Analyze how the author acknowledges and responds to conflicting evidence or viewpoints",
                            "ELAGSE8.RI.6c": "Evaluate the effectiveness of the author's response to conflicting evidence"
                        }
                    }
                }
            },
            "Science": {
                "6th": {
                    "S6E1": {
                        "title": "Universe",
                        "elements": {
                            "S6E1.a": "Relate the Nature of Science to the progression of basic historical scientific theories as they describe our solar system and the Big Bang",
                            "S6E1.b": "Describe the position of the solar system in the Milky Way galaxy and the universe",
                            "S6E1.c": "Compare and contrast the planets in terms of size, surface features, distance from sun, and ability to support life",
                            "S6E1.d": "Explain the motion of objects in the day/night sky in terms of relative position",
                            "S6E1.e": "Explain that gravity is the force that governs the motion in the solar system"
                        }
                    },
                    "S6E2": {
                        "title": "Earth-Moon-Sun Relationship",
                        "elements": {
                            "S6E2.a": "Develop models to explain the phases of the moon",
                            "S6E2.b": "Construct explanations for lunar and solar eclipses",
                            "S6E2.c": "Relate the tilt of the earth to the distribution of sunlight throughout the year and to its effect on climate"
                        }
                    },
                    "S6E3": {
                        "title": "Water",
                        "elements": {
                            "S6E3.a": "Explain that a large portion of the Earth's surface is water, consisting of oceans, rivers, lakes, underground water, and ice",
                            "S6E3.b": "Relate various atmospheric conditions to stages of the water cycle",
                            "S6E3.c": "Describe the composition, location, and subsurface topography of the world's oceans",
                            "S6E3.d": "Explain the causes of waves, currents, and tides"
                        }
                    },
                    "S6E4": {
                        "title": "Climate and Weather",
                        "elements": {
                            "S6E4.a": "Demonstrate that land and water absorb and lose heat at different rates and explain the resulting effects on weather patterns",
                            "S6E4.b": "Relate unequal heating of land and water surfaces to form large global wind systems and weather events",
                            "S6E4.c": "Relate how moisture evaporating from the oceans affects the weather patterns and weather events"
                        }
                    }
                },
                "7th": {
                    "S7L1": {
                        "title": "Biodiversity and Classification",
                        "elements": {
                            "S7L1.a": "Develop and defend a model that categorizes organisms based on common characteristics",
                            "S7L1.b": "Evaluate historical models of how organisms were classified based on physical characteristics and how that led to the six kingdom system"
                        }
                    },
                    "S7L2": {
                        "title": "Cells and Body Systems",
                        "elements": {
                            "S7L2.a": "Develop a model and construct an explanation of how cell structures contribute to the function of the cell as a system",
                            "S7L2.b": "Develop and use a conceptual model of how cells are organized into tissues, tissues into organs, organs into systems, and systems into organisms"
                        }
                    },
                    "S7L3": {
                        "title": "Genetics and Reproduction",
                        "elements": {
                            "S7L3.a": "Construct an explanation supported with scientific evidence of the role of genes and chromosomes in the process of inheriting a specific trait",
                            "S7L3.b": "Develop and use a model to describe how asexual reproduction results in offspring with identical genetic information while sexual reproduction results in genetic variation",
                            "S7L3.c": "Ask questions to gather and synthesize information about how humans influence inheritance of desired traits through selective breeding"
                        }
                    },
                    "S7L4": {
                        "title": "Ecology",
                        "elements": {
                            "S7L4.a": "Construct an explanation for patterns of interactions observed in different ecosystems in terms of relationships among organisms and abiotic components",
                            "S7L4.b": "Develop a model to describe the cycling of matter and flow of energy among biotic and abiotic components of an ecosystem",
                            "S7L4.c": "Analyze and interpret data to provide evidence for how resource availability, disease, climate, and human activity affect individual organisms, populations, communities, and ecosystems"
                        }
                    },
                    "S7L5": {
                        "title": "Evolution",
                        "elements": {
                            "S7L5.a": "Use mathematical representations to evaluate explanations of how natural selection leads to changes in specific traits of populations over successive generations",
                            "S7L5.b": "Construct an explanation based on evidence that describes how genetic variation and environmental factors influence probability of survival and reproduction of species",
                            "S7L5.c": "Analyze and interpret data for patterns in the fossil record that document existence, diversity, and extinction of organisms and their relationships to modern organisms"
                        }
                    }
                },
                "8th": {
                    "S8P1": {
                        "title": "Matter",
                        "elements": {
                            "S8P1.a": "Distinguish between atoms and molecules",
                            "S8P1.b": "Describe the difference between pure substances (elements and compounds) and mixtures",
                            "S8P1.c": "Describe the movement of particles in solids, liquids, gases, and plasma states",
                            "S8P1.d": "Distinguish between physical and chemical properties of matter as physical (density, melting point, boiling point) or chemical (reactivity, combustibility)",
                            "S8P1.e": "Distinguish between changes in matter as physical or chemical (development of a gas, formation of precipitate, and change in color)"
                        }
                    },
                    "S8P2": {
                        "title": "Energy Conservation and Transformation",
                        "elements": {
                            "S8P2.a": "Plan and carry out investigations to verify that energy is neither created nor destroyed, only transformed",
                            "S8P2.b": "Develop models to demonstrate that energy can be converted from one form to another",
                            "S8P2.c": "Analyze and interpret data to create graphic representations that show the relationship between kinetic energy, mass, and velocity",
                            "S8P2.d": "Describe how heat can be transferred through matter by the collisions of atoms (conduction) or through space (radiation). In a liquid or gas, currents will facilitate the transfer of heat (convection)"
                        }
                    },
                    "S8P3": {
                        "title": "Force, Mass, and Motion",
                        "elements": {
                            "S8P3.a": "Determine the relationship between velocity and acceleration",
                            "S8P3.b": "Demonstrate the effect of balanced and unbalanced forces on an object in terms of gravity, inertia, and friction",
                            "S8P3.c": "Demonstrate the effect of simple machines (lever, inclined plane, pulley, wedge, screw, and wheel and axle) on work"
                        }
                    },
                    "S8P4": {
                        "title": "Waves",
                        "elements": {
                            "S8P4.a": "Identify the characteristics of electromagnetic and mechanical waves",
                            "S8P4.b": "Describe how the behavior of light waves is manipulated causing reflection, refraction diffraction, and absorption",
                            "S8P4.c": "Explain how the human eye sees objects and colors in terms of wave-lengths",
                            "S8P4.d": "Describe how the behavior of waves is affected by medium (such as air, water, solids)",
                            "S8P4.e": "Relate the properties of sound to everyday experiences",
                            "S8P4.f": "Diagram the parts of the wave and explain how the parts are affected by changes in amplitude and pitch"
                        }
                    },
                    "S8P5": {
                        "title": "Gravity, Electricity, and Magnetism",
                        "elements": {
                            "S8P5.a": "Recognize that every object exerts gravitational force on every other object and that the force exerted depends on how much mass the objects have and how far apart they are",
                            "S8P5.b": "Demonstrate the advantages and disadvantages of series and parallel circuits and how they transfer energy",
                            "S8P5.c": "Investigate and explain that electric currents and magnets can exert force on each other"
                        }
                    }
                }
            },
            "Social Studies": {
                "6th": {
                    "SS6.G.1": {
                        "title": "Geographic reasoning",
                        "elements": {
                            "SS6.G.1.1": "Use maps and other geographic representations, geospatial technologies, and spatial thinking",
                            "SS6.G.1.2": "Analyze the interaction between humans and their environment in order to explain how humans modify the physical environment",
                            "SS6.G.1.3": "Explain how the physical and human characteristics of places and regions are connected to human identities and cultures"
                        }
                    },
                    "SS6.H.1": {
                        "title": "Historical thinking",
                        "elements": {
                            "SS6.H.1.1": "Create and use a chronological sequence of related events to compare developments",
                            "SS6.H.1.2": "Analyze connections among events and developments in broader historical contexts",
                            "SS6.H.1.3": "Classify a series of historical events and developments as examples of change and/or continuity"
                        }
                    },
                    "SS6.E.1": {
                        "title": "Economic decision making",
                        "elements": {
                            "SS6.E.1.1": "Explain how economic decisions affect individuals, families, businesses, and society",
                            "SS6.E.1.2": "Compare the costs and benefits of different choices",
                            "SS6.E.1.3": "Analyze the relationship between education, income, and job opportunities"
                        }
                    },
                    "SS6.C.1": {
                        "title": "Civic ideals and practices",
                        "elements": {
                            "SS6.C.1.1": "Explain origins, functions, and structure of government with reference to the U.S. Constitution",
                            "SS6.C.1.2": "Explain how the Constitution establishes a system of government that has powers, responsibilities, and limits",
                            "SS6.C.1.3": "Analyze the relationship between historical context and how political ideas and institutions have developed over time"
                        }
                    }
                },
                "7th": {
                    "SS7.G.1": {
                        "title": "Human systems",
                        "elements": {
                            "SS7.G.1.1": "Analyze how cultural and environmental characteristics affect the distribution and movement of people, goods, and ideas",
                            "SS7.G.1.2": "Explain how cultural patterns and economic decisions influence environments and the daily lives of people",
                            "SS7.G.1.3": "Evaluate the impact of location, climate, and physical characteristics on population distribution and the size and spacing of cities"
                        }
                    },
                    "SS7.H.1": {
                        "title": "Historical context",
                        "elements": {
                            "SS7.H.1.1": "Analyze connections among events and developments in broader historical contexts",
                            "SS7.H.1.2": "Use a working knowledge and understanding of historical periods and patterns of change within and across cultures",
                            "SS7.H.1.3": "Classify series of historical events and developments as examples of change and/or continuity"
                        }
                    },
                    "SS7.E.1": {
                        "title": "Market economy",
                        "elements": {
                            "SS7.E.1.1": "Explain how specialization encourages trade between countries",
                            "SS7.E.1.2": "Analyze the relationship between investment in human capital and gross domestic product",
                            "SS7.E.1.3": "Evaluate the costs and benefits of different allocation methods for distributing scarce goods and services"
                        }
                    },
                    "SS7.C.1": {
                        "title": "Government and citizenship",
                        "elements": {
                            "SS7.C.1.1": "Compare different types of governments and their ability to promote the common good and protect individual rights",
                            "SS7.C.1.2": "Analyze the role of citizens in government and the importance of civic virtue to the common good",
                            "SS7.C.1.3": "Evaluate the relationship between political concepts and historical change"
                        }
                    }
                },
                "8th": {
                    "SS8.H.1": {
                        "title": "American Revolution era",
                        "elements": {
                            "SS8.H.1.1": "Evaluate the impact of European exploration and settlement on American Indians and on colonization and settlement patterns",
                            "SS8.H.1.2": "Describe the development of the colonial regions and analyze the differences between them",
                            "SS8.H.1.3": "Analyze the ideological, military, social, and diplomatic aspects of the American Revolution"
                        }
                    },
                    "SS8.H.2": {
                        "title": "Early Republic and antebellum eras",
                        "elements": {
                            "SS8.H.2.1": "Analyze the challenge of maintaining a balance between state and federal power as evident in the early Republic",
                            "SS8.H.2.2": "Analyze how the early Republic struggled with the tension between the ideals of the Revolution and slavery",
                            "SS8.H.2.3": "Evaluate the relationship between westward expansion and the rise of sectionalism"
                        }
                    },
                    "SS8.C.1": {
                        "title": "Constitutional principles",
                        "elements": {
                            "SS8.C.1.1": "Analyze ideas and principles contained in the founding documents of the United States",
                            "SS8.C.1.2": "Explain how the Constitution establishes a system of government that has powers, responsibilities, and limits",
                            "SS8.C.1.3": "Analyze the relationship between the Bill of Rights and individual liberty"
                        }
                    },
                    "SS8.E.1": {
                        "title": "Early American economic systems",
                        "elements": {
                            "SS8.E.1.1": "Analyze the relationship between geography, immigration, and economic development in early America",
                            "SS8.E.1.2": "Explain how economic development contributed to the development of American identity and national unity",
                            "SS8.E.1.3": "Evaluate the impact of technology and transportation systems on economic development and regional specialization"
                        }
                    }
                }
            }
        }
    }

def get_states(standards_data):
    """Return list of available states"""
    return list(standards_data.keys())

def get_content_areas(standards_data, state):
    """Return list of content areas for a given state"""
    return list(standards_data.get(state, {}).keys())

def get_grades(standards_data, state, content_area):
    """Return list of grade levels for a given state and content area"""
    return list(standards_data.get(state, {}).get(content_area, {}).keys())

def get_standards(standards_data, state, content_area, grade):
    """Return dictionary of standards for given state, content area, and grade"""
    return standards_data.get(state, {}).get(content_area, {}).get(grade, {})

def get_sub_standards(standards_data, state, content_area, grade, standard):
    """Return dictionary of sub-standards for given parameters"""
    standards = get_standards(standards_data, state, content_area, grade)
    return standards.get(standard, {}).get('elements', {})