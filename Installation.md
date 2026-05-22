# Pranav potfolio website deployment on EKS cluster using Docker Kubernetis and jenkins

### Requirment

**_ Docker _**
**_ Docker Hub Login _**
**_ jenkins _**
**_ AWS CLI _**
**_ Kubectl _**
**_ helm _**

## install Jenkins

install java

```bash
sudo apt install fontconfig openjdk-21-jre
```

```bash
sudo wget -O /etc/apt/keyrings/jenkins-keyring.asc \
  https://pkg.jenkins.io/debian/jenkins.io-2026.key
echo "deb [signed-by=/etc/apt/keyrings/jenkins-keyring.asc]" \
  https://pkg.jenkins.io/debian binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt update
sudo apt install jenkins
```

```bash
systemctl start jenkins
```

```bash
systemctl status jebkins
```

### take access of Jenkins

## Docker Installation

```bash
sudo apt install docker.io -y
```

```bash
sudo usermod -aG docker $USER
```

```bash
newgrp docker
```

```bash
sudo usermod -aG docker jenkins
```

## AWS CLI install

```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
```

```bash
sudo apt install unzip -y
```

```bash
unzip awscliv2.zip
```

```bash
sudo ./aws/install
```

```bash
aws configure
```

```bash
cp -rv .aws/ /var/lib/jenkins/
```

```bash
 chown -R jenkins /var/lib/jenkins/.aws/
```

## Install kubectl

```bash
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
```

```bash
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
```

```bash
aws eks update-kubecongif --name < cluster name > --region < region >
```

```bash
sudo cp -rv .kube/ /var/lib/jenkins/
```

```bash
sudo chown -R jenkins /var/lib/jenkins/.kube/
```

## Install Helm

```bash
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
sudo chmod 700 get_helm.sh
./get_helm.sh
```

## Install Promethius and Graphana

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add stable https://charts.helm.sh/stable
helm repo update
kubectl create namespace monitoring
helm install kind-prometheus prometheus-community/kube-prometheus-stack --namespace monitoring --set prometheus.service.nodePort=30000 --set prometheus.service.type=NodePort --set grafana.service.nodePort=31000 --set grafana.service.type=NodePort --set alertmanager.service.nodePort=32000 --set alertmanager.service.type=NodePort --set prometheus-node-exporter.service.nodePort=32001 --set prometheus-node-exporter.service.type=NodePort
kubectl get svc -n monitoring
kubectl get namespace
```

### Few promethius query

```bash
sum (rate (container_cpu_usage_seconds_total{namespace="default"}[1m])) / sum (machine_cpu_cores) * 100

sum (container_memory_usage_bytes{namespace="default"}) by (pod)


sum(rate(container_network_receive_bytes_total{namespace="default"}[5m])) by (pod)
sum(rate(container_network_transmit_bytes_total{namespace="default"}[5m])) by (pod)

```
