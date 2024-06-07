To configure Prometheus on Kubernetes to scrape metrics using a pull-based system, you need to set up a `prometheus.yml` file that specifies how Prometheus should discover targets dynamically. Kubernetes service discovery mechanisms are used to automatically discover targets (such as pods, services, or nodes) without manually updating the configuration for each new deployment.

Here's an example of what the `prometheus.yml` file might look like when set up to scrape metrics from Kubernetes targets:

```yaml
global:
  scrape_interval: 15s
  evaluation_interval: 15s
  # scrape_timeout is set to the global default (10s).

scrape_configs:
  # Scrape the Prometheus instances themselves
  - job_name: 'prometheus'
    kubernetes_sd_configs:
      - role: pod
    relabel_configs:
      - source_labels: [__meta_kubernetes_namespace, __meta_kubernetes_pod_name]
        action: keep
        regex: monitoring;prometheus.*

  # Scrape all pods with a specific annotation
  - job_name: 'kubernetes-pods'
    kubernetes_sd_configs:
      - role: pod
    relabel_configs:
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
        action: keep
        regex: 'true'
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_path]
        action: replace
        target_label: __metrics_path__
        regex: (.+)
      - source_labels: [__address__, __meta_kubernetes_pod_annotation_prometheus_io_port]
        action: replace
        target_label: __address__
        regex: (.+):(?:\d+);(\d+)
        replacement: $1:$2

  # Scrape all services with a specific annotation
  - job_name: 'kubernetes-services'
    kubernetes_sd_configs:
      - role: service
    relabel_configs:
      - source_labels: [__meta_kubernetes_service_annotation_prometheus_io_scrape]
        action: keep
        regex: 'true'
      - source_labels: [__meta_kubernetes_service_annotation_prometheus_io_path]
        action: replace
        target_label: __metrics_path__
        regex: (.+)
      - source_labels: [__address__, __meta_kubernetes_service_annotation_prometheus_io_port]
        action: replace
        target_label: __address__
        regex: (.+):(?:\d+);(\d+)
        replacement: $1:$2
```

### Explanation

1. **Global Configuration:**
   - `scrape_interval` and `evaluation_interval` set the global intervals for scraping and rule evaluation.

2. **Scrape Configurations:**
   - **Prometheus Job:**
     - Scrapes Prometheus instances running in the `monitoring` namespace.
     - Uses `kubernetes_sd_configs` to discover pods with the role `pod`.
     - `relabel_configs` is used to filter and modify labels for the discovered targets. In this case, it keeps only the pods whose names match the pattern `prometheus.*`.

   - **Kubernetes Pods Job:**
     - Scrapes all pods in the cluster.
     - Uses `kubernetes_sd_configs` with the role `pod` to discover pods.
     - Uses `relabel_configs` to:
       - Keep only pods with the annotation `prometheus.io/scrape: 'true'`.
       - Replace the metrics path if specified in the annotation `prometheus.io/path`.
       - Replace the port if specified in the annotation `prometheus.io/port`.

   - **Kubernetes Services Job:**
     - Scrapes all services in the cluster.
     - Uses `kubernetes_sd_configs` with the role `service` to discover services.
     - Uses `relabel_configs` to:
       - Keep only services with the annotation `prometheus.io/scrape: 'true'`.
       - Replace the metrics path if specified in the annotation `prometheus.io/path`.
       - Replace the port if specified in the annotation `prometheus.io/port`.

### Service Discovery

- **Kubernetes Service Discovery (`kubernetes_sd_configs`)**: Prometheus dynamically discovers targets using Kubernetes API. This means that any new pod or service annotated for scraping will automatically be discovered without needing to update the `prometheus.yml` file.

- **Annotations**: By using annotations on Kubernetes objects (pods or services), you can control which targets Prometheus should scrape. For example:
  - `prometheus.io/scrape: 'true'` to enable scraping.
  - `prometheus.io/path: '/metrics'` to specify the metrics path.
  - `prometheus.io/port: '8080'` to specify the port to scrape.

This setup ensures that Prometheus automatically discovers and scrapes metrics from new deployments, making the monitoring system dynamic and scalable.