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
                "description": "Portal para sa mabilis na paghanap at pag-post ng government job openings.",
                "live_url": "https://govhire.example.com",
                "repo_url": "https://github.com/akosizeke/govhire",
                "tech_stack": "Django, Postgres, Tailwind",
                "featured": True,
            },
            {
                "title": "Face Recognition Attendance Monitoring",
                "description": "Attendance system na gumagamit ng face recognition para sa mabilis na log-in.",
                "live_url": "https://fr-attendance.example.com",
                "repo_url": "https://github.com/akosizeke/face-recognition-attendance",
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
            "Mahilig ako gumawa ng malilinis na website at simple pero solid na "
            "karanasan para sa mga gumagamit."
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
