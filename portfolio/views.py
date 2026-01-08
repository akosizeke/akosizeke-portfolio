from django.shortcuts import render

from projects.models import Project


def home(request):
    projects = list(
        Project.objects.order_by("-featured", "sort_order", "-created_at", "title")[:2]
    )
    if not projects:
        projects = [
            {
                "title": "GovHire",
                "description": "Portal for quickly finding and posting government job openings.",
                "live_url": "https://govhire.example.com",
                "repo_url": "https://github.com/akosizeke/govhire",
                "tech_stack": "Django, Postgres, Tailwind",
                "featured": True,
            },
            {
                "title": "Face Recognition Attendance Monitoring",
                "description": "Attendance system that uses face recognition for fast log-ins.",
                "live_url": "https://fr-attendance.example.com",
                "repo_url": "https://github.com/akosizeke/face-recognition-live-attendance-monitoring",
                "tech_stack": "Python, OpenCV, Django",
                "featured": False,
            },
        ]

    context = {
        "name": "Zeke",
        "last_name_accent": "Refuncion",
        "headline": "System Developer",
        "role": "Web Developer",
        "avatar_initials": "Z",
        "avatar_url": "",
        "profile_image": "portfolio/IMG_9986.JPG",
        "intro": (
            "I build clean, reliable web experiences with a focus on simple but solid "
            "user journeys."
        ),
        "stats": [
            {"value": "3 months", "label": "Experience"},
            {"value": "2", "label": "Projects Delivered"},
        ],
        "skills": ["Python", "Django", "HTML/CSS", "JavaScript", "UI/UX basics"],
        "education": [
            {
                "school": "Bulacan Polytechnic College",
                "program": "Bachelor of Science in Information Systems (BSIS)",
                "years": "2021 - 2025",
                "badge": "Bachelor's Degree",
                "highlight_title": "Service Award (2025)",
                "highlight_desc": "Recognized for Service Award in Student Government.",
                "logo_text": "BPC",
                "logo_image": "portfolio/bpclogo-1-1.png",
            }
        ],
        "experiences": [
            {
                "role": "System Developer",
                "company": "Provincial Government of Bulacan",
                "team": "Provincial Information Technology Office",
                "period": "2025 - Present",
                "current": True,
                "summary": (
                    "Building and maintaining provincial systems with secure, scalable, and user-friendly implementations."
                ),
                "technologies": ["Python", "Django", "APIs", "Automation"],
                "logo_text": "PGB",
                "logo_image": "portfolio/Official-Logo-1 (1).png",
            }
        ],
        "tech_categories": [
            {
                "title": "Programming",
                "items": [
                    "Python (Django)",
                    "JavaScript",
                    "HTML & CSS",
                    "C#",
                    "C++",
                    "Laravel",
                    ".NET",
                ],
            },
            {
                "title": "Design",
                "items": [
                    "Wireframing & user flows",
                    "Responsive UI implementation",
                    "Design systems basics",
                    "Accessibility-first layouts",
                ],
            },
            {
                "title": "Systems",
                "items": [
                    "Process automation",
                    "Version control (Git/GitHub)",
                ],
            },
        ],
        "projects": projects,
        "contact": {
            "email": "ezekielsuarezrefuncion@gmail.com",
            "linkedin": "https://www.linkedin.com/in/ezekiel-refuncion-77538b36a",
            "github": "https://github.com/akosizeke",
            "resume_url": "#",
        },
    }
    return render(request, "portfolio/home.html", context)
