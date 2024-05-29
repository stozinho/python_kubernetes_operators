# Kubernetes Operator Pattern
This is a dir for all things Kubernetes Operator Pattern. 
Operator SDK at top level, which builds upon `kubebuilder`. 

Extend Kube API with custom resources. 

Define a custom resource with a Custom Resource Definition (CRD). 

Implement a controller (written in Go) to implement the custom functionality. The controllers watches for new CRDs to be created and then acts accordingly - reconcile current state with desired state (e.g. create new object). 


