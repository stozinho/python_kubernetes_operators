Creating a simple Helm chart for this deployment involves generating the Helm chart structure and templates, and then defining the resources (deployment, secret, and configmap) within those templates. Below are the steps to create a Helm chart for your deployment.

### Step 1: Create the Helm Chart Structure

Use the Helm CLI to create a new chart:

```sh
helm create my-chart
```

This command generates a directory structure similar to:

```
my-chart/
├── Chart.yaml
├── values.yaml
├── charts/
├── templates/
│   ├── deployment.yaml
│   ├── _helpers.tpl
│   ├── hpa.yaml
│   ├── ingress.yaml
│   ├── service.yaml
│   └── serviceaccount.yaml
└── .helmignore
```

### Step 2: Define the ConfigMap Template

Create a file named `configmap.yaml` inside the `templates` directory with the following content:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ .Release.Name }}-configmap
data:
  my-config-key: {{ .Values.config.myConfigKey | quote }}
```

### Step 3: Define the Secret Template

Create a file named `secret.yaml` inside the `templates` directory with the following content:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: {{ .Release.Name }}-secret
type: Opaque
data:
  username: {{ .Values.secret.username | b64enc | quote }}
  password: {{ .Values.secret.password | b64enc | quote }}
```

### Step 4: Define the Deployment Template

Replace the content of `deployment.yaml` inside the `templates` directory with the following:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .Release.Name }}-deployment
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      app: {{ .Release.Name }}
  template:
    metadata:
      labels:
        app: {{ .Release.Name }}
    spec:
      containers:
      - name: my-container
        image: {{ .Values.image.repository }}:{{ .Values.image.tag }}
        env:
        - name: SECRET_USERNAME
          valueFrom:
            secretKeyRef:
              name: {{ .Release.Name }}-secret
              key: username
        - name: SECRET_PASSWORD
          valueFrom:
            secretKeyRef:
              name: {{ .Release.Name }}-secret
              key: password
        - name: CONFIG_VALUE
          valueFrom:
            configMapKeyRef:
              name: {{ .Release.Name }}-configmap
              key: my-config-key
```

### Step 5: Update `values.yaml`

Update the `values.yaml` file to include the default values for your secret, configmap, and other configurations:

```yaml
replicaCount: 1

image:
  repository: nginx
  tag: latest

secret:
  username: "my-username"
  password: "my-password"

config:
  myConfigKey: "my-config-value"
```

### Step 6: Package and Deploy the Chart

Use the Helm CLI to deploy the chart:

```sh
helm install my-release my-chart
```

Replace `my-release` with the name you want to give to your release. This command will create the deployment, secret, and configmap based on the templates and values defined.

### Full Structure of `my-chart` Directory

Here's how your `my-chart` directory should look:

```
my-chart/
├── Chart.yaml
├── values.yaml
├── charts/
├── templates/
│   ├── configmap.yaml
│   ├── secret.yaml
│   ├── deployment.yaml
│   └── _helpers.tpl
└── .helmignore
```

By following these steps, you've created a Helm chart that deploys a Kubernetes deployment, a secret, and a configmap with the ability to configure these resources through Helm values.

To handle different values for Dev and Prod environments in a Helm chart, you can use separate values files for each environment. Helm allows you to override the default values in `values.yaml` with environment-specific values files.

Here’s how you can set this up:

### Step 1: Create Environment-Specific Values Files

Create two additional values files: `values-dev.yaml` and `values-prod.yaml`.

#### `values-dev.yaml`:

```yaml
replicaCount: 1

image:
  repository: nginx
  tag: latest

secret:
  username: "dev-username"
  password: "dev-password"

config:
  myConfigKey: "dev-config-value"
```

#### `values-prod.yaml`:

```yaml
replicaCount: 3

image:
  repository: nginx
  tag: stable

secret:
  username: "prod-username"
  password: "prod-password"

config:
  myConfigKey: "prod-config-value"
```

### Step 2: Use Environment-Specific Values Files During Deployment

When deploying your Helm chart, specify the values file appropriate for the environment using the `-f` or `--values` flag.

#### For Dev Environment:

```sh
helm install my-release my-chart -f values-dev.yaml
```

#### For Prod Environment:

```sh
helm install my-release my-chart -f values-prod.yaml
```

### Full Structure of `my-chart` Directory

Your `my-chart` directory should now look like this:

```
my-chart/
├── Chart.yaml
├── values.yaml
├── values-dev.yaml
├── values-prod.yaml
├── charts/
├── templates/
│   ├── configmap.yaml
│   ├── secret.yaml
│   ├── deployment.yaml
│   └── _helpers.tpl
└── .helmignore
```

### Step 3: Helm Upgrade with Environment-Specific Values

If you need to upgrade an existing release with new values, you can also use the `helm upgrade` command with the environment-specific values file:

#### For Dev Environment:

```sh
helm upgrade my-release my-chart -f values-dev.yaml
```

#### For Prod Environment:

```sh
helm upgrade my-release my-chart -f values-prod.yaml
```

### Summary

1. **Create environment-specific values files (`values-dev.yaml` and `values-prod.yaml`)** containing configurations for Dev and Prod environments, respectively.
2. **Deploy or upgrade** the Helm chart using the appropriate values file with the `-f` or `--values` flag.

This approach allows you to maintain a single Helm chart while easily managing different configurations for different environments.

