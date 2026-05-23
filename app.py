import os
from flask import Flask, render_template, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "dev-secret-key")

# Portfolio Data
PORTFOLIO_DATA = {
    "name": os.getenv("PORTFOLIO_NAME", "Pranav Kotawar"),
    "title": os.getenv("PORTFOLIO_TITLE", "Junior DevOps Engineer"),
    "email": os.getenv("PORTFOLIO_EMAIL", "pranavkotawar@outlook.com"),
    "phone": os.getenv("PORTFOLIO_PHONE", "+91-7972758711"),
    "github": os.getenv("PORTFOLIO_GITHUB", "https://github.com/PranavKotawar2001"),
    "location": os.getenv("PORTFOLIO_LOCATION", "Nagpur, Maharashtra, India"),
    "availability": os.getenv("PORTFOLIO_AVAILABILITY", "Open to Remote"),
    "summary": (
        "Results-driven DevOps Engineer with 1.5+ years of hands-on production experience "
        "building cloud-native infrastructure, CI/CD pipelines, and containerized microservices. "
        "Proficient in AWS EKS, Kubernetes, Docker, Terraform, and Jenkins, with a strong focus "
        "on automation, zero-downtime deployments, and system reliability."
    ),
    "experience": [
        {
            "role": "Junior DevOps Engineer",
            "company": "Hisan Labs Private Limited",
            "location": "Pune",
            "period": "Oct 2024 – May 2026",
            "points": [
                "Managed Git repositories on GitHub/GitLab with structured branching strategies and PR workflows",
                "Built and maintained CI/CD pipelines with Jenkins, reducing deployment time by ~35%",
                "Designed optimized Dockerfiles using multi-stage builds, reducing image size by up to 60%",
                "Administered Amazon EKS clusters serving 5+ microservices with 99.9% uptime",
                "Configured HPA for auto-scaling during traffic spikes, maintaining response SLAs",
                "Implemented monitoring with Datadog across 12+ services, reducing MTTR by ~40%",
                "Automated AWS infrastructure provisioning using Terraform with S3 remote state",
                "Configured EC2, IAM, ALB, NGINX Ingress, and CloudFront for production traffic",
            ]
        }
    ],
    "skills": {
        "Cloud": ["AWS (EKS, EC2, IAM, ALB, CloudFront, CloudWatch, S3, RDS)", "Azure", "GCP"],
        "Containers": ["Docker", "Docker Compose", "Kubernetes", "Helm", "HPA", "StatefulSets"],
        "CI/CD": ["Jenkins", "GitHub Actions", "GitLab CI", "Pipeline Design"],
        "IaC": ["Terraform", "Ansible", "AWS CloudFormation"],
        "Monitoring": ["Datadog", "Prometheus", "Grafana", "CloudWatch"],
        "Scripting": ["Bash", "Shell", "Python", "YAML", "Groovy (Jenkinsfile)"],
        "VCS": ["Git", "GitHub", "GitLab"],
        "OS & Tools": ["Linux (Ubuntu, Amazon Linux)", "JIRA", "VS Code"],
    },
    "projects": [
        {
            "name": "AirTravel Microservices Booking System",
            "tech": ["Docker", "Kubernetes", "Helm", "Jenkins", "GitHub", "Datadog", "AWS"],
            "points": [
                "Containerized 5 independent microservices reducing final image sizes by 55%",
                "Orchestrated Helm-based deployments with zero service interruption across releases",
                "Configured Kubernetes networking with Services, Ingress, and NetworkPolicies",
                "Implemented HPA enabling auto-scale from 2 to 10 replicas under traffic load",
                "Built end-to-end Jenkins CI/CD pipelines triggered by GitHub push events",
            ]
        },
        {
            "name": "CORE CRUD – Multi-Tier Application Deployment",
            "tech": ["Docker", "Kubernetes", "Jenkins", "Terraform", "AWS EC2", "Prometheus", "Grafana", "MySQL"],
            "points": [
                "Architected a containerized 3-tier application (React, Java backend, MySQL) on Kubernetes",
                "Automated AWS infrastructure provisioning using Terraform with remote state management",
                "Implemented Prometheus and Grafana dashboards tracking latency, error rates, and utilization",
                "Managed secure config using Kubernetes Secrets, eliminating hardcoded credentials",
                "Implemented structured GitHub branching with version tagging across dev and production",
            ]
        }
    ],
    "education": [
        {
            "degree": "B.Tech — Computer Science & Engineering",
            "institution": "Priyadarshini College of Engineering, Nagpur",
            "year": "2025",
            "score": "75%"
        },
        {
            "degree": "Diploma — Information Technology",
            "institution": "Government Polytechnic, Bramhapuri",
            "year": "2022",
            "score": "79.88%"
        }
    ],
    "languages": ["English (Professional)", "Marathi (Native)", "Hindi (Fluent)"]
}


@app.route("/")
def index():
    return render_template("index.html", data=PORTFOLIO_DATA)


@app.route("/api/portfolio")
def api_portfolio():
    return jsonify(PORTFOLIO_DATA)


if __name__ == "__main__":
    debug_mode = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    port = int(os.getenv("PORT", 5000))
    app.run(debug=debug_mode, host="0.0.0.0", port=port)
