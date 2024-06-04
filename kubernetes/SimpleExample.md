Sure, here are the YAML configurations for creating a simple pod deployment, a secret, and then mounting the secret to the pod as an environment variable in Kubernetes.

### Step 1: Create a Secret

First, let's create a secret. Save the following YAML into a file named `secret.yaml`:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: my-secret
type: Opaque
data:
  username: bXktdXNlcm5hbWU=  # Base64 encoded value of 'my-username'
  password: bXktcGFzc3dvcmQ=  # Base64 encoded value of 'my-password'
```

### Step 2: Create a Simple Pod Deployment

Next, create a deployment. Save the following YAML into a file named `deployment.yaml`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: my-container
        image: nginx:latest
        env:
        - name: SECRET_USERNAME
          valueFrom:
            secretKeyRef:
              name: my-secret
              key: username
        - name: SECRET_PASSWORD
          valueFrom:
            secretKeyRef:
              name: my-secret
              key: password
```

### Applying the Configurations

To apply these configurations to your Kubernetes cluster, use the `kubectl apply` command:

```sh
kubectl apply -f secret.yaml
kubectl apply -f deployment.yaml
```

### Explanation

1. **Secret Configuration (`secret.yaml`)**:
   - The `username` and `password` fields in the secret are base64 encoded.
   - `bXktdXNlcm5hbWU=` is the base64 encoding of `my-username`.
   - `bXktcGFzc3dvcmQ=` is the base64 encoding of `my-password`.

2. **Deployment Configuration (`deployment.yaml`)**:
   - A deployment named `my-deployment` is created with one replica of an `nginx` container.
   - The environment variables `SECRET_USERNAME` and `SECRET_PASSWORD` are populated with the values from the `my-secret` secret.

By following these steps, you will have a pod running with the secret mounted as environment variables.

Sure! Here's how you can add a simple ConfigMap to the deployment. We'll first create a ConfigMap and then update the deployment to use this ConfigMap.

### Step 1: Create a ConfigMap

Save the following YAML into a file named `configmap.yaml`:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-configmap
data:
  my-config-key: my-config-value
```

### Step 2: Update the Deployment to Use the ConfigMap

Update your deployment YAML file (`deployment.yaml`) to include the ConfigMap as an environment variable:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: my-container
        image: nginx:latest
        env:
        - name: SECRET_USERNAME
          valueFrom:
            secretKeyRef:
              name: my-secret
              key: username
        - name: SECRET_PASSWORD
          valueFrom:
            secretKeyRef:
              name: my-secret
              key: password
        - name: CONFIG_VALUE
          valueFrom:
            configMapKeyRef:
              name: my-configmap
              key: my-config-key
```

### Applying the Configurations

To apply these configurations to your Kubernetes cluster, use the `kubectl apply` command:

```sh
kubectl apply -f secret.yaml
kubectl apply -f configmap.yaml
kubectl apply -f deployment.yaml
```

### Explanation

1. **ConfigMap Configuration (`configmap.yaml`)**:
   - A ConfigMap named `my-configmap` is created with a single key-value pair (`my-config-key: my-config-value`).

2. **Updated Deployment Configuration (`deployment.yaml`)**:
   - The environment variable `CONFIG_VALUE` is added to the container, which retrieves its value from the `my-configmap` ConfigMap using the key `my-config-key`.

By following these steps, your deployment will have both the secret and the ConfigMap values available as environment variables in the pod.

