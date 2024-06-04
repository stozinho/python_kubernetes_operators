Kubernetes Kustomize is a configuration management tool native to Kubernetes that allows users to customize Kubernetes application configurations without having to resort to templating or forking. Introduced in Kubernetes 1.14, it provides a way to manage configuration files in a more declarative and manageable manner.

### Key Features of Kustomize:

1. **Overlay System:**
   - Kustomize allows you to define a base configuration and create overlays on top of it. Overlays can be used to customize the base configuration for different environments like development, staging, and production.

2. **No Templating Language:**
   - Unlike tools such as Helm, Kustomize does not use a templating language. Instead, it relies on YAML transformations which makes it simpler and less error-prone for managing configurations.

3. **Resource Patching:**
   - You can patch resources with strategic merges and JSON patches, enabling you to modify specific fields in Kubernetes resources without duplicating the entire configuration.

4. **Secret and ConfigMap Generation:**
   - Kustomize can generate ConfigMaps and Secrets from files or literal values. This helps manage sensitive data and configuration details more securely and efficiently.

5. **Built-in Resource Management:**
   - It includes capabilities for customizing resources such as adding common labels, annotations, and modifying the namespace. This helps in managing resources more consistently across environments.

### Basic Concepts:

1. **Base:**
   - A base is a directory containing a set of Kubernetes manifests (YAML files) which define your application’s resources.

2. **Overlay:**
   - An overlay is a customization layer applied on top of a base. Overlays can be organized into different environments or configurations.

3. **Kustomization.yaml:**
   - This file is the heart of Kustomize. It declares the resources, configurations, and transformations that should be applied. Each directory managed by Kustomize contains a `kustomization.yaml` file.

### Example Workflow:

1. **Directory Structure:**
   ```
   my-app/
     ├── base/
     │   ├── deployment.yaml
     │   ├── service.yaml
     │   └── kustomization.yaml
     ├── overlays/
         ├── dev/
         │   ├── kustomization.yaml
         │   └── patch.yaml
         ├── staging/
         │   ├── kustomization.yaml
         │   └── patch.yaml
         └── prod/
             ├── kustomization.yaml
             └── patch.yaml
   ```

2. **Base `kustomization.yaml`:**
   ```yaml
   resources:
     - deployment.yaml
     - service.yaml
   ```

3. **Overlay `kustomization.yaml`:**
   ```yaml
   bases:
     - ../../base
   patchesStrategicMerge:
     - patch.yaml
   ```

4. **Applying the Configuration:**
   - To apply the configuration for the `dev` environment, you would navigate to the `overlays/dev` directory and run:
     ```sh
     kubectl apply -k .
     ```

### Use Cases:

- **Environment-Specific Customization:**
  Create different overlays for various environments (development, staging, production) to manage environment-specific configurations.

- **Modular Configuration Management:**
  Manage and reuse base configurations across multiple projects or services, ensuring consistency and reducing duplication.

- **Dynamic Resource Management:**
  Easily adjust configurations for different clusters or deployments, making it simpler to manage and deploy applications at scale.

Kustomize integrates seamlessly with `kubectl`, the Kubernetes command-line tool, making it an ideal choice for Kubernetes users who want to manage configurations in a more structured and less error-prone way.

Kustomize and Helm are both popular tools used for managing Kubernetes configurations, but they serve different purposes and use different approaches. They are not strictly competing tools, but rather complementary, depending on your specific needs and preferences.

### Kustomize:

1. **Configuration Management:**
   - Kustomize focuses on configuration management and customization without the use of templating. It provides a way to declaratively manage and customize Kubernetes YAML configurations.

2. **YAML Transformations:**
   - It uses plain YAML and allows users to create overlays, patches, and transformations directly on the YAML files. This approach avoids the complexity of templating languages.

3. **Built-in Kubernetes Integration:**
   - Kustomize is built into `kubectl` (from version 1.14 onwards), allowing users to manage configurations directly using `kubectl apply -k`.

4. **Use Cases:**
   - Ideal for environments where you need straightforward customization of YAML files, such as adding labels, changing image tags, or adjusting configurations across different environments.

### Helm:

1. **Package Management:**
   - Helm is a package manager for Kubernetes, which enables users to define, install, and upgrade even the most complex Kubernetes applications. Helm uses charts, which are collections of files describing a related set of Kubernetes resources.

2. **Templating System:**
   - Helm uses a powerful templating system that allows users to create highly configurable and reusable Kubernetes manifests. This includes the use of Go templates to dynamically generate YAML files based on input values.

3. **Release Management:**
   - Helm manages releases of applications, making it easier to deploy, rollback, and manage the lifecycle of Kubernetes applications.

4. **Use Cases:**
   - Suitable for packaging and distributing applications, managing complex deployments, and using pre-packaged applications from Helm repositories (like Bitnami).

### Comparison:

- **Complexity and Flexibility:**
  - **Helm** provides more flexibility and is better suited for complex applications that require dynamic configurations and a templating system.
  - **Kustomize** is simpler and is ideal for straightforward customization of Kubernetes YAML configurations without introducing the complexity of templating.

- **Use Case Fit:**
  - **Helm** is well-suited for applications that need to be packaged, versioned, and shared, especially when leveraging community charts or managing releases.
  - **Kustomize** is a good fit for managing environment-specific configurations and applying straightforward customizations to Kubernetes manifests.

- **Learning Curve:**
  - **Helm** can have a steeper learning curve due to its templating language and the complexity of managing Helm charts.
  - **Kustomize** has a gentler learning curve as it leverages native YAML syntax and focuses on overlaying and patching configurations.

### Complementary Usage:

Many Kubernetes users find value in using both tools together:
- Use **Helm** for deploying and managing complex applications and leveraging community charts.
- Use **Kustomize** for managing and customizing configurations, especially for environment-specific settings.

In summary, while Kustomize and Helm serve different primary purposes—configuration customization and package management, respectively—they can complement each other well depending on the needs of your Kubernetes application deployment strategy.

# Example of `Kustomize` YAML Transformations 

## NB - Helm templates Yaml; Kustomize makes us of Yaml transformations (as opposed to templating)

Certainly! Kustomize uses a different approach compared to traditional templating systems. Instead of embedding variables within YAML files, Kustomize relies on overlaying and patching existing YAML configurations. Here are some examples to illustrate how Kustomize works.

### Example 1: Basic Overlay

Let's say you have a base configuration for a deployment and a service. You want to customize this configuration for different environments such as development and production.

#### Directory Structure:

```
my-app/
  ├── base/
  │   ├── deployment.yaml
  │   ├── service.yaml
  │   └── kustomization.yaml
  ├── overlays/
      ├── dev/
      │   ├── kustomization.yaml
      │   └── patch.yaml
      └── prod/
          ├── kustomization.yaml
          └── patch.yaml
```

#### Base Deployment (`base/deployment.yaml`):

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
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
        - name: my-app
          image: my-app:latest
          ports:
            - containerPort: 80
```

#### Base Service (`base/service.yaml`):

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-app
spec:
  selector:
    app: my-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
```

#### Base Kustomization (`base/kustomization.yaml`):

```yaml
resources:
  - deployment.yaml
  - service.yaml
```

### Overlay for Development Environment

#### Dev Patch (`overlays/dev/patch.yaml`):

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 2
  template:
    spec:
      containers:
        - name: my-app
          image: my-app:dev
```

#### Dev Kustomization (`overlays/dev/kustomization.yaml`):

```yaml
bases:
  - ../../base
patchesStrategicMerge:
  - patch.yaml
```

### Overlay for Production Environment

#### Prod Patch (`overlays/prod/patch.yaml`):

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3
  template:
    spec:
      containers:
        - name: my-app
          image: my-app:prod
```

#### Prod Kustomization (`overlays/prod/kustomization.yaml`):

```yaml
bases:
  - ../../base
patchesStrategicMerge:
  - patch.yaml
```

### Applying the Configurations

To apply the configuration for the development environment, navigate to the `overlays/dev` directory and run:

```sh
kubectl apply -k .
```

To apply the configuration for the production environment, navigate to the `overlays/prod` directory and run:

```sh
kubectl apply -k .
```

### Example 2: ConfigMap and Secret Generation

Kustomize can generate ConfigMaps and Secrets from literal values or files.

#### Directory Structure:

```
my-app/
  ├── base/
  │   ├── deployment.yaml
  │   ├── kustomization.yaml
  └── overlays/
      ├── dev/
      │   └── kustomization.yaml
      └── prod/
          └── kustomization.yaml
```

#### Base Deployment (`base/deployment.yaml`):

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
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
        - name: my-app
          image: my-app:latest
          env:
            - name: CONFIG_VALUE
              valueFrom:
                configMapKeyRef:
                  name: my-app-config
                  key: configValue
            - name: SECRET_VALUE
              valueFrom:
                secretKeyRef:
                  name: my-app-secret
                  key: secretValue
          ports:
            - containerPort: 80
```

#### Base Kustomization (`base/kustomization.yaml`):

```yaml
resources:
  - deployment.yaml

configMapGenerator:
  - name: my-app-config
    literals:
      - configValue=defaultConfig

secretGenerator:
  - name: my-app-secret
    literals:
      - secretValue=defaultSecret
```

### Overlay for Development Environment

#### Dev Kustomization (`overlays/dev/kustomization.yaml`):

```yaml
bases:
  - ../../base

configMapGenerator:
  - name: my-app-config
    literals:
      - configValue=devConfig

secretGenerator:
  - name: my-app-secret
    literals:
      - secretValue=devSecret
```

### Overlay for Production Environment

#### Prod Kustomization (`overlays/prod/kustomization.yaml`):

```yaml
bases:
  - ../../base

configMapGenerator:
  - name: my-app-config
    literals:
      - configValue=prodConfig

secretGenerator:
  - name: my-app-secret
    literals:
      - secretValue=prodSecret
```

By using Kustomize in this way, you can manage environment-specific configurations and secrets without duplicating YAML files or resorting to complex templating. This approach ensures a clean and manageable configuration setup.