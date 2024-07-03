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
public class ${root_class_name}:IKubernetesObject<V1ObjectMeta>, ISpec<${parent_class_name}Spec>
{
    [JsonPropertyName("apiVersion")]
    public string ApiVersion { get; set; }
    [JsonPropertyName("kind")]
    public string Kind { get; set; }
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
    <%
    upper_name = "".join(m.name[:1].upper() + m.name[1:])
    %>
    [JsonPropertyName("${m.name}")]
        % if m.type =="object":
    public ${upper_name} ${upper_name} { get; set; }
        % elif m.type =="array":
    public IList<${upper_name}> ${upper_name} { get; set; }
        % elif m.type =="integer":
    public int ${upper_name} { get; set; }
        % else:
    public ${m.type} ${upper_name} { get; set; }
        % endif
    %endfor
}
% endfor

