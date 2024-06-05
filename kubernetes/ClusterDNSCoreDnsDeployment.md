Cluster DNS in Kubernetes provides a way for applications to discover and communicate with services using DNS names instead of IP addresses. This simplifies service discovery and makes it easier to manage dynamic environments where the IP addresses of services and pods may change frequently. Here’s a detailed look at how Cluster DNS works and how it registers DNS records.

### How Cluster DNS Works

1. **CoreDNS Deployment**: In most Kubernetes clusters, CoreDNS (or kube-dns in older versions) is deployed as a set of pods running in the kube-system namespace. CoreDNS is responsible for providing DNS resolution within the cluster.

2. **DNS Resolution**:
   - **Service Discovery**: When a pod needs to connect to a service, it uses a DNS name (e.g., my-service.my-namespace.svc.cluster.local). The DNS request is intercepted by the kube-dns/CoreDNS pods.
   - **DNS Query Handling**: CoreDNS queries the Kubernetes API to resolve the DNS name to the corresponding ClusterIP of the service. If the service exists, CoreDNS returns the ClusterIP to the querying pod.

3. **Pod DNS**: Pods are configured to use the cluster DNS server as their DNS resolver by default. This is specified in the pod's `/etc/resolv.conf` file, which points to the IP of the CoreDNS service.

### How DNS Records Are Registered

1. **Service Creation**: When a service is created in Kubernetes, the API server notifies CoreDNS about the new service.
   - **Endpoints**: CoreDNS also monitors the endpoints of the service to ensure it has up-to-date information about the pods backing the service.

2. **DNS Record Types**:
   - **A Records**: CoreDNS creates A records for services. For example, a service named `my-service` in the `default` namespace will get an A record like `my-service.default.svc.cluster.local` pointing to its ClusterIP.
   - **SRV Records**: CoreDNS also creates SRV records for services that specify the port and protocol of the service. This is useful for discovering services that run on specific ports.

3. **Headless Services**: For headless services (those without a ClusterIP), CoreDNS creates A records for each pod backing the service. This allows direct DNS queries to return the IP addresses of the individual pods.

### Example of DNS Registration

Consider a service named `my-service` in the `default` namespace:

1. **Service Definition**:
    ```yaml
    apiVersion: v1
    kind: Service
    metadata:
      name: my-service
      namespace: default
    spec:
      selector:
        app: my-app
      ports:
        - protocol: TCP
          port: 80
          targetPort: 9376
    ```

2. **DNS Records**:
   - **A Record**: `my-service.default.svc.cluster.local` -> ClusterIP of `my-service`
   - **SRV Record**: `_http._tcp.my-service.default.svc.cluster.local` -> Port 80 of `my-service`

3. **Headless Service**:
    ```yaml
    apiVersion: v1
    kind: Service
    metadata:
      name: my-service
      namespace: default
    spec:
      clusterIP: None
      selector:
        app: my-app
      ports:
        - protocol: TCP
          port: 80
          targetPort: 9376
    ```

   - **A Records**: `my-service.default.svc.cluster.local` -> IPs of all pods with label `app: my-app`

### Configuring CoreDNS

CoreDNS can be configured using a ConfigMap in the `kube-system` namespace. Here’s an example configuration:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: coredns
  namespace: kube-system
data:
  Corefile: |
    .:53 {
        errors
        health {
          lameduck 5s
        }
        kubernetes cluster.local in-addr.arpa ip6.arpa {
          pods insecure
          fallthrough in-addr.arpa ip6.arpa
          ttl 30
        }
        prometheus :9153
        forward . /etc/resolv.conf
        cache 30
        loop
        reload
        loadbalance
    }
```

### Summary

- **Cluster DNS** provides DNS resolution within a Kubernetes cluster using CoreDNS.
- **CoreDNS** handles DNS queries by resolving service names to their corresponding ClusterIP addresses or pod IPs for headless services.
- **DNS Records** for services and pods are automatically created and updated by CoreDNS based on information from the Kubernetes API server.
- **Configuration** of CoreDNS is managed through a ConfigMap, allowing customization of DNS behavior within the cluster.

This system ensures reliable and dynamic service discovery, enabling pods to communicate with each other using stable DNS names.