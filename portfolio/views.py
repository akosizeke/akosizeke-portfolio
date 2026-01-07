from django.shortcuts import render

from projects.models import Project


def home(request):
    projects = list(
        Project.objects.order_by("-featured", "sort_order", "-created_at", "title")[:4]
    )
    if not projects:
        projects = [
            {
                "title": "Project One",
                "description": "Maliit na web app para sa personal na gastos.",
                "live_url": "#",
                "repo_url": "#",
                "tech_stack": "Django, SQLite, Tailwind",
                "featured": True,
            },
            {
                "title": "Project Two",
                "description": "Landing page na mabilis at mobile-friendly.",
                "live_url": "#",
                "repo_url": "#",
                "tech_stack": "HTML, CSS, JS",
                "featured": False,
            },
        ]

    context = {
        "name": "Zeke",
        "role": "Web Developer",
        "intro": (
            "Mahilig ako gumawa ng malilinis na website at simple pero solid na "
            "karanasan para sa mga gumagamit."
        ),
        "skills": ["Python", "Django", "HTML/CSS", "JavaScript", "UI/UX basics"],
        "projects": projects,
        "contact": {"email": "you@example.com", "linkedin": "#", "github": "#"},
    }
    return render(request, "portfolio/home.html", context)
