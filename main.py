import yaml

from entity import EntityInstance


def load() -> str:
    x = '''
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  annotations:
    api-approved.kubernetes.io: https://github.com/kubernetes-sigs/gateway-api/pull/2997
    gateway.networking.k8s.io/bundle-version: v1.1.0
    gateway.networking.k8s.io/channel: standard
  creationTimestamp: "2024-07-02T12:01:51Z"
  generation: 1
  name: gatewayclasses.gateway.networking.k8s.io
  resourceVersion: "1199"
spec:
  conversion:
    strategy: None
  group: gateway.networking.k8s.io
  names:
    categories:
    - gateway-api
    kind: GatewayClass
    listKind: GatewayClassList
    plural: gatewayclasses
    shortNames:
    - gc
    singular: gatewayclass
  scope: Cluster
  versions:
  - additionalPrinterColumns:
    - jsonPath: .spec.controllerName
      name: Controller
      type: string
    - jsonPath: .status.conditions[?(@.type=="Accepted")].status
      name: Accepted
      type: string
    - jsonPath: .metadata.creationTimestamp
      name: Age
      type: date
    - jsonPath: .spec.description
      name: Description
      priority: 1
      type: string
    name: v1
    schema:
      openAPIV3Schema:
        description: |-
          GatewayClass describes a class of Gateways available to the user for creating
          Gateway resources.


          It is recommended that this resource be used as a template for Gateways. This
          means that a Gateway is based on the state of the GatewayClass at the time it
          was created and changes to the GatewayClass or associated parameters are not
          propagated down to existing Gateways. This recommendation is intended to
          limit the blast radius of changes to GatewayClass or associated parameters.
          If implementations choose to propagate GatewayClass changes to existing
          Gateways, that MUST be clearly documented by the implementation.


          Whenever one or more Gateways are using a GatewayClass, implementations SHOULD
          add the `gateway-exists-finalizer.gateway.networking.k8s.io` finalizer on the
          associated GatewayClass. This ensures that a GatewayClass associated with a
          Gateway is not deleted while in use.


          GatewayClass is a Cluster level resource.
        properties:
          apiVersion:
            description: |-
              APIVersion defines the versioned schema of this representation of an object.
              Servers should convert recognized schemas to the latest internal value, and
              may reject unrecognized values.
              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
            type: string
          kind:
            description: |-
              Kind is a string value representing the REST resource this object represents.
              Servers may infer this from the endpoint the client submits requests to.
              Cannot be updated.
              In CamelCase.
              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
            type: string
          metadata:
            type: object
          spec:
            description: Spec defines the desired state of GatewayClass.
            properties:
              controllerName:
                description: |-
                  ControllerName is the name of the controller that is managing Gateways of
                  this class. The value of this field MUST be a domain prefixed path.
                  Example: "example.net/gateway-controller".
                  This field is not mutable and cannot be empty.
                  Support: Core
                maxLength: 253
                minLength: 1
                pattern: ^[a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*\/[A-Za-z0-9\/\-._~%!$&'()*+,;=:]+$
                type: string
                x-kubernetes-validations:
                - message: Value is immutable
                  rule: self == oldSelf
              description:
                description: Description helps describe a GatewayClass with more details.
                maxLength: 64
                type: string
              parametersRef:
                description: |-
                  ParametersRef is a reference to a resource that contains the configuration
                  parameters corresponding to the GatewayClass. This is optional if the
                  controller does not require any additional configuration.
                  ParametersRef can reference a standard Kubernetes resource, i.e. ConfigMap,
                  or an implementation-specific custom resource. The resource can be
                  cluster-scoped or namespace-scoped.
                  If the referent cannot be found, the GatewayClass's "InvalidParameters"
                  status condition will be true.
                  A Gateway for this GatewayClass may provide its own `parametersRef`. When both are specified,
                  the merging behavior is implementation specific.
                  It is generally recommended that GatewayClass provides defaults that can be overridden by a Gateway.
                  Support: Implementation-specific
                properties:
                  group:
                    description: Group is the group of the referent.
                    maxLength: 253
                    pattern: ^$|^[a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*$
                    type: string
                  kind:
                    description: Kind is kind of the referent.
                    maxLength: 63
                    minLength: 1
                    pattern: ^[a-zA-Z]([-a-zA-Z0-9]*[a-zA-Z0-9])?$
                    type: string
                  name:
                    description: Name is the name of the referent.
                    maxLength: 253
                    minLength: 1
                    type: string
                  namespace:
                    description: |-
                      Namespace is the namespace of the referent.
                      This field is required when referring to a Namespace-scoped resource and
                      MUST be unset when referring to a Cluster-scoped resource.
                    maxLength: 63
                    minLength: 1
                    pattern: ^[a-z0-9]([-a-z0-9]*[a-z0-9])?$
                    type: string
                required:
                - group
                - kind
                - name
                type: object
            required:
            - controllerName
            type: object
          status:
            default:
              conditions:
              - lastTransitionTime: "1970-01-01T00:00:00Z"
                message: Waiting for controller
                reason: Waiting
                status: Unknown
                type: Accepted
            description: |-
              Status defines the current state of GatewayClass.
              Implementations MUST populate status on all GatewayClass resources which
              specify their controller name.
            properties:
              conditions:
                default:
                - lastTransitionTime: "1970-01-01T00:00:00Z"
                  message: Waiting for controller
                  reason: Pending
                  status: Unknown
                  type: Accepted
                description: |-
                  Conditions is the current status from the controller for
                  this GatewayClass.


                  Controllers should prefer to publish conditions using values
                  of GatewayClassConditionType for the type of each Condition.
                items:
                  description: "Condition contains details for one aspect of the current"
                  properties:
                    lastTransitionTime:
                      description: |-
                        lastTransitionTime is the last time the condition transitioned from one status to another.
                        This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable.
                      format: date-time
                      type: string
                    message:
                      description: |-
                        message is a human readable message indicating details about the transition.
                        This may be an empty string.
                      maxLength: 32768
                      type: string
                    observedGeneration:
                      description: |-
                        observedGeneration represents the .metadata.generation that the condition was set based upon.
                        For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date
                        with respect to the current state of the instance.
                      format: int64
                      minimum: 0
                      type: integer
                    reason:
                      description: |-
                        reason contains a programmatic identifier indicating the reason for the condition's last transition.
                        Producers of specific condition types may define expected values and meanings for this field,
                        and whether the values are considered a guaranteed API.
                        The value should be a CamelCase string.
                        This field may not be empty.
                      maxLength: 1024
                      minLength: 1
                      pattern: ^[A-Za-z]([A-Za-z0-9_,:]*[A-Za-z0-9_])?$
                      type: string
                    status:
                      description: status of the condition, one of True, False, Unknown.
                      enum:
                      - "True"
                      - "False"
                      - Unknown
                      type: string
                    type:
                      description: |-
                        type of condition in CamelCase or in foo.example.com/CamelCase.
                        ---
                        Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be
                        useful (see .node.status.conditions), the ability to deconflict is important.
                        The regex it matches is (dns1123SubdomainFmt/)?(qualifiedNameFmt)
                      maxLength: 316
                      pattern: ^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])$
                      type: string
                  required:
                  - lastTransitionTime
                  - message
                  - reason
                  - status
                  - type
                  type: object
                maxItems: 8
                type: array
                x-kubernetes-list-map-keys:
                - type
                x-kubernetes-list-type: map
            type: object
        required:
        - spec
        type: object
    served: true
    storage: true
    subresources:
      status: {}
  - additionalPrinterColumns:
    - jsonPath: .spec.controllerName
      name: Controller
      type: string
    - jsonPath: .status.conditions[?(@.type=="Accepted")].status
      name: Accepted
      type: string
    - jsonPath: .metadata.creationTimestamp
      name: Age
      type: date
    - jsonPath: .spec.description
      name: Description
      priority: 1
      type: string
    name: v1beta1
    schema:
      openAPIV3Schema:
        description: |-
          GatewayClass describes a class of Gateways available to the user for creating
          Gateway resources.


          It is recommended that this resource be used as a template for Gateways. This
          means that a Gateway is based on the state of the GatewayClass at the time it
          was created and changes to the GatewayClass or associated parameters are not
          propagated down to existing Gateways. This recommendation is intended to
          limit the blast radius of changes to GatewayClass or associated parameters.
          If implementations choose to propagate GatewayClass changes to existing
          Gateways, that MUST be clearly documented by the implementation.


          Whenever one or more Gateways are using a GatewayClass, implementations SHOULD
          add the `gateway-exists-finalizer.gateway.networking.k8s.io` finalizer on the
          associated GatewayClass. This ensures that a GatewayClass associated with a
          Gateway is not deleted while in use.


          GatewayClass is a Cluster level resource.
        properties:
          apiVersion:
            description: |-
              APIVersion defines the versioned schema of this representation of an object.
              Servers should convert recognized schemas to the latest internal value, and
              may reject unrecognized values.
              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
            type: string
          kind:
            description: |-
              Kind is a string value representing the REST resource this object represents.
              Servers may infer this from the endpoint the client submits requests to.
              Cannot be updated.
              In CamelCase.
              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
            type: string
          metadata:
            type: object
          spec:
            description: Spec defines the desired state of GatewayClass.
            properties:
              controllerName:
                description: |-
                  ControllerName is the name of the controller that is managing Gateways of
                  this class. The value of this field MUST be a domain prefixed path.


                  Example: "example.net/gateway-controller".


                  This field is not mutable and cannot be empty.


                  Support: Core
                maxLength: 253
                minLength: 1
                pattern: ^[a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*\/[A-Za-z0-9\/\-._~%!$&'()*+,;=:]+$
                type: string
                x-kubernetes-validations:
                - message: Value is immutable
                  rule: self == oldSelf
              description:
                description: Description helps describe a GatewayClass with more details.
                maxLength: 64
                type: string
              parametersRef:
                description: |-
                  ParametersRef is a reference to a resource that contains the configuration
                  parameters corresponding to the GatewayClass. This is optional if the
                  controller does not require any additional configuration.


                  ParametersRef can reference a standard Kubernetes resource, i.e. ConfigMap,
                  or an implementation-specific custom resource. The resource can be
                  cluster-scoped or namespace-scoped.


                  If the referent cannot be found, the GatewayClass's "InvalidParameters"
                  status condition will be true.


                  A Gateway for this GatewayClass may provide its own `parametersRef`. When both are specified,
                  the merging behavior is implementation specific.
                  It is generally recommended that GatewayClass provides defaults that can be overridden by a Gateway.


                  Support: Implementation-specific
                properties:
                  group:
                    description: Group is the group of the referent.
                    maxLength: 253
                    pattern: ^$|^[a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*$
                    type: string
                  kind:
                    description: Kind is kind of the referent.
                    maxLength: 63
                    minLength: 1
                    pattern: ^[a-zA-Z]([-a-zA-Z0-9]*[a-zA-Z0-9])?$
                    type: string
                  name:
                    description: Name is the name of the referent.
                    maxLength: 253
                    minLength: 1
                    type: string
                  namespace:
                    description: |-
                      Namespace is the namespace of the referent.
                      This field is required when referring to a Namespace-scoped resource and
                      MUST be unset when referring to a Cluster-scoped resource.
                    maxLength: 63
                    minLength: 1
                    pattern: ^[a-z0-9]([-a-z0-9]*[a-z0-9])?$
                    type: string
                required:
                - group
                - kind
                - name
                type: object
            required:
            - controllerName
            type: object
          status:
            default:
              conditions:
              - lastTransitionTime: "1970-01-01T00:00:00Z"
                message: Waiting for controller
                reason: Waiting
                status: Unknown
                type: Accepted
            description: |-
              Status defines the current state of GatewayClass.


              Implementations MUST populate status on all GatewayClass resources which
              specify their controller name.
            properties:
              conditions:
                default:
                - lastTransitionTime: "1970-01-01T00:00:00Z"
                  message: Waiting for controller
                  reason: Pending
                  status: Unknown
                  type: Accepted
                description: |-
                  Conditions is the current status from the controller for
                  this GatewayClass.


                  Controllers should prefer to publish conditions using values
                  of GatewayClassConditionType for the type of each Condition.
                items:
                  description: ""
                  properties:
                    lastTransitionTime:
                      description: |-
                        lastTransitionTime is the last time the condition transitioned from one status to another.
                        This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable.
                      format: date-time
                      type: string
                    message:
                      description: |-
                        message is a human readable message indicating details about the transition.
                        This may be an empty string.
                      maxLength: 32768
                      type: string
                    observedGeneration:
                      description: |-
                        observedGeneration represents the .metadata.generation that the condition was set based upon.
                        For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date
                        with respect to the current state of the instance.
                      format: int64
                      minimum: 0
                      type: integer
                    reason:
                      description: |-
                        reason contains a programmatic identifier indicating the reason for the condition's last transition.
                        Producers of specific condition types may define expected values and meanings for this field,
                        and whether the values are considered a guaranteed API.
                        The value should be a CamelCase string.
                        This field may not be empty.
                      maxLength: 1024
                      minLength: 1
                      pattern: ^[A-Za-z]([A-Za-z0-9_,:]*[A-Za-z0-9_])?$
                      type: string
                    status:
                      description: status of the condition, one of True, False, Unknown.
                      enum:
                      - "True"
                      - "False"
                      - Unknown
                      type: string
                    type:
                      description: |-
                        type of condition in CamelCase or in foo.example.com/CamelCase.
                        ---
                        Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be
                        useful (see .node.status.conditions), the ability to deconflict is important.
                        The regex it matches is (dns1123SubdomainFmt/)?(qualifiedNameFmt)
                      maxLength: 316
                      pattern: ^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])$
                      type: string
                  required:
                  - lastTransitionTime
                  - message
                  - reason
                  - status
                  - type
                  type: object
                maxItems: 8
                type: array
                x-kubernetes-list-map-keys:
                - type
                x-kubernetes-list-type: map
            type: object
        required:
        - spec
        type: object
    served: true
    storage: false
    subresources:
      status: {}
status:
  acceptedNames:
    categories:
    - gateway-api
    kind: GatewayClass
    listKind: GatewayClassList
    plural: gatewayclasses
    shortNames:
    - gc
    singular: gatewayclass
  conditions:
  - lastTransitionTime: "2024-07-02T12:01:51Z"
    message: approved in https://github.com/kubernetes-sigs/gateway-api/pull/2997
    reason: ApprovedAnnotation
    status: "True"
    type: KubernetesAPIApprovalPolicyConformant
  - lastTransitionTime: "2024-07-02T12:01:51Z"
    message: no conflicts found
    reason: NoConflicts
    status: "True"
    type: NamesAccepted
  - lastTransitionTime: "2024-07-02T12:01:51Z"
    message: the initial names have been accepted
    reason: InitialNamesAccepted
    status: "True"
    type: Established
  storedVersions:
  - v1
    '''

    return x


def load(file_name):
    with open("input/" + file_name) as f:
        return f.read()


def start():
    yaml_data = load("referencegrants.yaml")
    data = yaml.safe_load(yaml_data)
    versions = data["spec"]["versions"]
    parent_class_name = data["spec"]["names"]["kind"]

    for version in versions:
        EntityInstance.clear()
        version_name = version["name"]
        specs = version["schema"]["openAPIV3Schema"]["properties"]["spec"]
        status = version["schema"]["openAPIV3Schema"]["properties"]["status"]
        class_desc = specs["description"]
        root_class_name = upper_first(f'{version_name + parent_class_name}')
        print(f'class_desc: {class_desc}')
        print(f'root_class_name: {version_name + parent_class_name}\n\n')
        process_spec(specs, f'{parent_class_name}Spec')
        process_status(status, f'{parent_class_name}Status')
        output(root_class_name, parent_class_name)


def output(root_class_name, parent_class_name):
    from mako.template import Template
    mytemplate = Template(filename='tmpl.mako')
    out = mytemplate.render(data=EntityInstance.get_entities(),
                            root_class_name=root_class_name,
                            parent_class_name=parent_class_name)
    # 将out写入文件
    with open(f'output/{root_class_name}.cs', 'w', encoding='utf-8') as f:
        f.write(out)


def process_status(dicts: dict, parent_class_name=""):
    parent_class_name = upper_first(parent_class_name)
    inst = EntityInstance(parent_class_name)
    properties = dicts["properties"]
    for fd in properties:
        field_type = properties[fd]["type"]
        inst.entity(parent_class_name).add_field(fd, field_type)
        if field_type == "array":
            process_status(properties[fd]["items"], fd)
        if field_type == "string":
            print(
                f'parent_class_name: {parent_class_name} \nfield: {fd}  {field_type}'
            )


def process_spec(dicts: dict, parent_class_name=""):
    parent_class_name = upper_first(parent_class_name)
    inst = EntityInstance(parent_class_name)
    properties = dicts["properties"]
    for field in properties:
        if "description" == field:
            continue
        field_desc = properties[field]["description"]
        field_type = properties[field]["type"]
        inst.entity(parent_class_name).add_field(field, field_type)
        if field_type == "object":
            print(
                f'parent_class_name: {parent_class_name}\nfield: {field}  {field_type} '
            )
            process_spec(properties[field], field)
        if field_type == "string":
            print(
                f'parent_class_name: {parent_class_name}\nfield: {field}  {field_type}'
            )


def upper_first(s):
    return s[:1].upper() + s[1:]


if __name__ == '__main__':
    start()
    # for k in EntityInstance.entities.keys():
    #     entity = EntityInstance.entity(k)
    #     print(entity.class_name)
    #     print(len(entity.fields))
    #     for field in entity.fields:
    #         print(f'{field.name}  {field.type}')
    #     print(f'\n\n')
