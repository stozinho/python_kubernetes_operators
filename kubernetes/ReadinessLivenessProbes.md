Kubernetes readiness and liveness probes are mechanisms that help ensure the reliability and availability of applications running within a Kubernetes cluster. They monitor the state of applications and their components, enabling Kubernetes to take corrective actions if necessary.

### Liveness Probes

**Purpose:** 
Liveness probes determine if an application is running properly. If a liveness probe fails, Kubernetes considers the container to be in a failed state and will kill and restart it.

**Common Use Cases:**
- Detecting and remedying application deadlocks.
- Recovering from situations where an application is unable to recover on its own.

**Types of Liveness Probes:**
1. **HTTP GET Probe:** Kubernetes sends an HTTP GET request to a specified endpoint. If the response code is between 200 and 399, the container is considered alive.
2. **TCP Socket Probe:** Kubernetes attempts to establish a TCP connection to a specified port. If the connection can be established, the container is considered alive.
3. **Exec Probe:** Kubernetes runs a specified command inside the container. If the command returns a 0 exit status, the container is considered alive.

**Configuration Example:**
```yaml
livenessProbe:
  httpGet:
    path: /healthz
    port: 8080
  initialDelaySeconds: 3
  periodSeconds: 3
```

### Readiness Probes

**Purpose:** 
Readiness probes determine if an application is ready to serve traffic. If a readiness probe fails, Kubernetes will temporarily remove the container from the service's endpoints, meaning it won't receive any traffic until it becomes ready again.

**Common Use Cases:**
- Ensuring an application is fully initialized and ready to serve requests.
- Handling applications that might temporarily go into an unready state but don't need to be restarted (e.g., during heavy load or maintenance).

**Types of Readiness Probes:**
1. **HTTP GET Probe:** Similar to liveness, it sends an HTTP GET request to a specified endpoint.
2. **TCP Socket Probe:** Similar to liveness, it attempts to establish a TCP connection.
3. **Exec Probe:** Similar to liveness, it runs a specified command inside the container.

**Configuration Example:**
```yaml
readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 10
```

### Key Differences

1. **Purpose:**
   - **Liveness Probes:** Ensure that the application is running and, if not, restart it.
   - **Readiness Probes:** Ensure that the application is ready to serve traffic and, if not, temporarily remove it from the load balancer.

2. **Actions Taken on Failure:**
   - **Liveness Probe Failure:** Container is restarted.
   - **Readiness Probe Failure:** Container is removed from the service endpoints but is not restarted.

### Best Practices

- **Separate Concerns:** Use liveness probes to detect and recover from application crashes and hangs, and readiness probes to manage traffic and load balancing.
- **Grace Periods:** Set appropriate `initialDelaySeconds` to give the application enough time to start before probes begin.
- **Resource Considerations:** Ensure that probes are not too frequent to avoid unnecessary load on the application.

By correctly configuring liveness and readiness probes, you can significantly enhance the resilience and reliability of applications running in your Kubernetes cluster.