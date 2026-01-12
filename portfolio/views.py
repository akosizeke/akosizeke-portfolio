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
                "live_url": "https://govhire-updated.onrender.com/",
                "repo_url": "https://github.com/akosizeke/govhire",
                "tech_stack": "Django, Postgres, Tailwind",
                "featured": True,
            },
            {
                "title": "Face Recognition Attendance Monitoring",
                "description": "Attendance system that uses face recognition for fast log-ins.",
                "live_url": "https://face-recognition-live-attendance.onrender.com/",
                "repo_url": "https://github.com/akosizeke/face-recognition-live-attendance-monitoring",
                "tech_stack": "Python, OpenCV, Django",
                "featured": False,
            },
        ]

    # Build a filmstrip list of 8 items, cycling through available projects.
    filmstrip = []
    project_items = list(projects)
    if project_items:
        idx = 0
        while len(filmstrip) < 8:
            p = project_items[idx % len(project_items)]
            filmstrip.append(
                {
                    "title": getattr(p, "title", "") or (p.get("title") if isinstance(p, dict) else ""),
                    "description": getattr(p, "description", "") or (p.get("description") if isinstance(p, dict) else ""),
                    "tag": "Preview",
                    "image": (
                        getattr(p, "film_image", "")
                        or getattr(p, "image", "")
                        or getattr(p, "image_url", "")
                        or (p.get("film_image") if isinstance(p, dict) else "")
                        or (p.get("image") if isinstance(p, dict) else "")
                        or ""
                    ),
                }
            )
            idx += 1
    else:
        filmstrip = [
            {
                "title": "Project Preview",
                "description": "Add your first project to showcase here.",
                "tag": "Preview",
                "image": "",
            }
        ] * 8

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
                "technologies": ["Python", "Django", "APIs", "JavaScript", "System Dev"],
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
        "filmstrip": filmstrip,
    }
    return render(request, "portfolio/home.html", context)
