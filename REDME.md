# 🚀 Pranav Kotawar Portfolio Website Deployment on AWS EKS using Jenkins, Docker & Kubernetes

## 📌 Project Overview

This project demonstrates a complete production-style CI/CD pipeline implementation for deploying a containerized Python-based portfolio application on an Amazon EKS cluster using Jenkins, Docker, Kubernetes, Helm, Prometheus, and Grafana.

The application is developed using **Python** and deployed using modern DevOps and cloud-native technologies.

The primary objective of this project is to automate the software delivery lifecycle using modern DevOps practices including:

- Continuous Integration
- Continuous Deployment
- Containerization
- Kubernetes Orchestration
- Monitoring & Observability
- Automated Infrastructure Workflow

---

# 🏗️ Architecture

```text
Developer
    ↓
GitHub Repository
    ↓
Jenkins Pipeline
    ↓
SonarQube Code Analysis
    ↓
Docker Image Build
    ↓
Docker Hub Registry
    ↓
Amazon EKS Cluster
    ↓
Kubernetes Deployment
    ↓
Prometheus Monitoring
    ↓
Grafana Dashboard Visualization
```

---

# ⚙️ Tech Stack

| Technology | Purpose                    |
| ---------- | -------------------------- |
| Python     | Application Development    |
| Jenkins    | CI/CD Automation           |
| Docker     | Containerization           |
| Kubernetes | Container Orchestration    |
| Amazon EKS | Managed Kubernetes Cluster |
| Helm       | Kubernetes Package Manager |
| SonarQube  | Code Quality Analysis      |
| Prometheus | Monitoring & Metrics       |
| Grafana    | Visualization & Dashboards |
| AWS CLI    | AWS Resource Management    |
| kubectl    | Kubernetes Management      |

---

# 📂 Project Workflow

## 1️⃣ Source Code Management

The Python-based portfolio application source code is maintained in GitHub. Jenkins automatically pulls the latest source code during every pipeline execution.

---

## 2️⃣ Continuous Integration

Jenkins automates:

- Source code pull
- Code quality scanning
- Docker image creation
- Image push to Docker Hub
- Kubernetes deployment

---

## 3️⃣ SonarQube Code Analysis

Static code analysis is integrated using SonarQube to ensure code quality and maintainability.

### SonarQube Pipeline Stage

```groovy
stage('Test') {
    steps {
        withSonarQubeEnv('Sonar') {
            sh '''
                sonar-scanner \
                -Dsonar.projectKey=python-app \
                -Dsonar.sources=. \
                -Dsonar.python.version=3
            '''
        }
    }
}
```

---

# 🐳 Docker Containerization

The Python application is containerized using Docker for portability and scalability.

## Docker Build Stage

```groovy
stage('Docker-Image-Build'){
    steps{
        sh 'docker build -t pranavsudhirkotawar/portfolio:latest .'
    }
}
```

---

# 📦 Docker Hub Integration

After building the Docker image, Jenkins pushes the image to Docker Hub.

## Docker Push Stage

```groovy
stage('Push-Image-to-Docker-Hub'){
    steps{
        sh '''
            docker push pranavsudhirkotawar/portfolio:latest
        '''
    }
}
```

---

# ☸️ Kubernetes Deployment on Amazon EKS

The application is deployed to the Amazon EKS cluster using Kubernetes manifests.

## Deployment Stage

```groovy
stage('Deploy'){
    steps{
        sh 'kubectl apply -f k8s/'
    }
}
```

---

# 📊 Monitoring & Observability

## 🔹 Prometheus

Prometheus is integrated for collecting:

- CPU metrics
- Memory utilization
- Network statistics
- Pod monitoring
- Cluster health monitoring

### Sample Prometheus Queries

#### CPU Usage

```promql
sum (rate (container_cpu_usage_seconds_total{namespace="default"}[1m])) / sum (machine_cpu_cores) * 100
```

#### Memory Usage

```promql
sum (container_memory_usage_bytes{namespace="default"}) by (pod)
```

#### Network Usage

```promql
sum(rate(container_network_receive_bytes_total{namespace="default"}[5m])) by (pod)
```

---

## 🔹 Grafana

Grafana is integrated with Prometheus for:

- Real-time dashboards
- Cluster monitoring
- Resource visualization
- Application observability

---

# 🔄 Jenkins CI/CD Pipeline

```groovy
pipeline{
    agent any

    stages{

        stage('Pull'){
            steps{
                git 'https://github.com/PranavKotawar2001/Pranav-Kotawar-Devops-Portfolio.git'
            }
        }

        stage('Test'){
            steps{
                withSonarQubeEnv('Sonar') {
                    sh '''
                        sonar-scanner \
                        -Dsonar.projectKey=python-app \
                        -Dsonar.sources=. \
                        -Dsonar.python.version=3
                    '''
                }
            }
        }

        stage('Docker-Image-Build'){
            steps{
                sh 'docker build -t pranavsudhirkotawar/portfolio:latest .'
            }
        }

        stage('Push-Image-to-Docker-Hub'){
            steps{
                sh '''
                    docker push pranavsudhirkotawar/portfolio:latest
                '''
            }
        }

        stage('Deploy'){
            steps{
                sh 'kubectl apply -f k8s/'
            }
        }
    }
}
```

---

# 📁 Kubernetes Resources Used

- Namespace
- Deployment
- Service
- Configurations
- Monitoring Stack

---

# ✅ Key Features

- End-to-End CI/CD Automation
- Python-Based Application Deployment
- Docker-Based Containerization
- Kubernetes Orchestration
- Amazon EKS Integration
- SonarQube Code Analysis
- Monitoring using Prometheus
- Grafana Dashboard Integration
- Automated Application Deployment
- Scalable Cloud-Native Infrastructure

---

# 📈 Project Outcome

This project successfully demonstrates practical implementation of:

- DevOps automation
- Python application deployment
- Kubernetes administration
- Containerized application deployment
- CI/CD pipeline orchestration
- Monitoring and observability
- Cloud-native deployment architecture

The implementation reflects production-oriented deployment practices using modern DevOps tools and cloud technologies.

---

# 👨‍💻 Author

## Pranav Kotawar

DevOps Engineer | Cloud Enthusiast | Kubernetes & Docker Practitioner
