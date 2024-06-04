# Kubernetes Operator Pattern
This is a dir for all things Kubernetes Operator Pattern. 
Operator SDK at top level, which builds upon `kubebuilder`. 

Extend Kube API with custom resources. 

Define a custom resource with a Custom Resource Definition (CRD). 

Implement a controller (written in Go) to implement the custom functionality. The controllers watches for new CRDs to be created and then acts accordingly - reconcile current state with desired state (e.g. create new object). 

https://medium.com/@santoshpai/creating-a-kubernetes-operator-using-operator-sdk-43b69ff82cb



https://sdk.operatorframework.io/

https://github.com/operator-framework

https://kubernetes.io/docs/concepts/extend-kubernetes/operator/

https://docs.python.org/3/

https://pkg.go.dev/sigs.k8s.io/controller-runtime#section-readme

https://book.kubebuilder.io/cronjob-tutorial/empty-main