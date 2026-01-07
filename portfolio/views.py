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
        "projects": projects,
        "contact": {
            "email": "ezekielsuarezrefuncion@gmail.com",
            "linkedin": "https://www.linkedin.com/in/ezekiel-refuncion-77538b36a",
            "github": "https://github.com/akosizeke",
        },
    }
    return render(request, "portfolio/home.html", context)
