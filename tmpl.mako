
public class ${root_class_name}List:IKubernetesObject<V1ListMeta>, IItems<${root_class_name}>
{
    public string ApiVersion { get; set; }
    public string Kind { get; set; }
    public V1ListMeta Metadata { get; set; }
    public IList<${root_class_name}> Items { get; set; }
}
public class ${root_class_name}:KubernetesObject, IMetadata<V1ObjectMeta>, ISpec<${parent_class_name}Spec>
{
    public V1ObjectMeta Metadata { get; set; }
    public ${parent_class_name}Spec Spec { get; set; }
    public ${parent_class_name}Status Status { get; set; }
}
% for a in data:
public class ${data[a].class_name}
{
    % for m in data[a].fields:
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
