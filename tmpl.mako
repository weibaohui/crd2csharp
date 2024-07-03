using System.Collections.Generic;
using System.Text.Json.Serialization;
using k8s;
using k8s.Models;
namespace Entity.Crd;

public class ${root_class_name}List:IKubernetesObject<V1ListMeta>, IItems<${root_class_name}>
{
    [JsonPropertyName("apiVersion")]
    public string ApiVersion { get; set; }
    [JsonPropertyName("kind")]
    public string Kind { get; set; }
    [JsonPropertyName("metadata")]
    public V1ListMeta Metadata { get; set; }
    public IList<${root_class_name}> Items { get; set; }
}
public class ${root_class_name}:KubernetesObject, IMetadata<V1ObjectMeta>, ISpec<${parent_class_name}Spec>
{
    [JsonPropertyName("metadata")]
    public V1ObjectMeta Metadata { get; set; }
    [JsonPropertyName("spec")]
    public ${parent_class_name}Spec Spec { get; set; }
    [JsonPropertyName("status")]
    public ${parent_class_name}Status Status { get; set; }
}
% for a in data:
public class ${data[a].class_name}
{
    % for m in data[a].fields:
    [JsonPropertyName("${m.name}")]
        % if m.type =="object":
    public ${m.name} ${m.name} { get; set; }
        % elif m.type =="array":
    public IList<${m.name}> ${m.name} { get; set; }
        % else:
    public ${m.type} ${m.name} { get; set; }
        % endif
    %endfor
}
% endfor
