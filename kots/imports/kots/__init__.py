import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from ._jsii import *

import cdk8s
import constructs


@jsii.data_type(
    jsii_type="kots.KotsApiAirgapSpec",
    jsii_struct_bases=[],
    name_mapping={
        "app_slug": "appSlug",
        "channel_id": "channelId",
        "channel_name": "channelName",
        "release_notes": "releaseNotes",
        "signature": "signature",
        "update_cursor": "updateCursor",
        "version_label": "versionLabel",
    },
)
class KotsApiAirgapSpec:
    def __init__(
        self,
        *,
        app_slug: typing.Optional[builtins.str] = None,
        channel_id: typing.Optional[builtins.str] = None,
        channel_name: typing.Optional[builtins.str] = None,
        release_notes: typing.Optional[builtins.str] = None,
        signature: typing.Optional[builtins.str] = None,
        update_cursor: typing.Optional[builtins.str] = None,
        version_label: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AirgapSpec defines the desired state of AirgapSpec.

        :param app_slug: 
        :param channel_id: 
        :param channel_name: 
        :param release_notes: 
        :param signature: 
        :param update_cursor: 
        :param version_label: 

        :schema: KotsApiAirgapSpec
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if app_slug is not None:
            self._values["app_slug"] = app_slug
        if channel_id is not None:
            self._values["channel_id"] = channel_id
        if channel_name is not None:
            self._values["channel_name"] = channel_name
        if release_notes is not None:
            self._values["release_notes"] = release_notes
        if signature is not None:
            self._values["signature"] = signature
        if update_cursor is not None:
            self._values["update_cursor"] = update_cursor
        if version_label is not None:
            self._values["version_label"] = version_label

    @builtins.property
    def app_slug(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiAirgapSpec#appSlug
        '''
        result = self._values.get("app_slug")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def channel_id(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiAirgapSpec#channelID
        '''
        result = self._values.get("channel_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def channel_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiAirgapSpec#channelName
        '''
        result = self._values.get("channel_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def release_notes(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiAirgapSpec#releaseNotes
        '''
        result = self._values.get("release_notes")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def signature(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiAirgapSpec#signature
        '''
        result = self._values.get("signature")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update_cursor(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiAirgapSpec#updateCursor
        '''
        result = self._values.get("update_cursor")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_label(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiAirgapSpec#versionLabel
        '''
        result = self._values.get("version_label")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KotsApiAirgapSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kots.KotsApiApplicationSpec",
    jsii_struct_bases=[],
    name_mapping={
        "title": "title",
        "additional_images": "additionalImages",
        "additional_namespaces": "additionalNamespaces",
        "allow_rollback": "allowRollback",
        "graphs": "graphs",
        "icon": "icon",
        "kubectl_version": "kubectlVersion",
        "kustomize_version": "kustomizeVersion",
        "ports": "ports",
        "proxy_public_images": "proxyPublicImages",
        "release_notes": "releaseNotes",
        "require_minimal_rbac_privileges": "requireMinimalRbacPrivileges",
        "status_informers": "statusInformers",
    },
)
class KotsApiApplicationSpec:
    def __init__(
        self,
        *,
        title: builtins.str,
        additional_images: typing.Optional[typing.Sequence[builtins.str]] = None,
        additional_namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_rollback: typing.Optional[builtins.bool] = None,
        graphs: typing.Optional[typing.Sequence["KotsApiApplicationSpecGraphs"]] = None,
        icon: typing.Optional[builtins.str] = None,
        kubectl_version: typing.Optional[builtins.str] = None,
        kustomize_version: typing.Optional[builtins.str] = None,
        ports: typing.Optional[typing.Sequence["KotsApiApplicationSpecPorts"]] = None,
        proxy_public_images: typing.Optional[builtins.bool] = None,
        release_notes: typing.Optional[builtins.str] = None,
        require_minimal_rbac_privileges: typing.Optional[builtins.bool] = None,
        status_informers: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''ApplicationSpec defines the desired state of ApplicationSpec.

        :param title: 
        :param additional_images: 
        :param additional_namespaces: 
        :param allow_rollback: 
        :param graphs: 
        :param icon: 
        :param kubectl_version: 
        :param kustomize_version: 
        :param ports: 
        :param proxy_public_images: 
        :param release_notes: 
        :param require_minimal_rbac_privileges: 
        :param status_informers: 

        :schema: KotsApiApplicationSpec
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "title": title,
        }
        if additional_images is not None:
            self._values["additional_images"] = additional_images
        if additional_namespaces is not None:
            self._values["additional_namespaces"] = additional_namespaces
        if allow_rollback is not None:
            self._values["allow_rollback"] = allow_rollback
        if graphs is not None:
            self._values["graphs"] = graphs
        if icon is not None:
            self._values["icon"] = icon
        if kubectl_version is not None:
            self._values["kubectl_version"] = kubectl_version
        if kustomize_version is not None:
            self._values["kustomize_version"] = kustomize_version
        if ports is not None:
            self._values["ports"] = ports
        if proxy_public_images is not None:
            self._values["proxy_public_images"] = proxy_public_images
        if release_notes is not None:
            self._values["release_notes"] = release_notes
        if require_minimal_rbac_privileges is not None:
            self._values["require_minimal_rbac_privileges"] = require_minimal_rbac_privileges
        if status_informers is not None:
            self._values["status_informers"] = status_informers

    @builtins.property
    def title(self) -> builtins.str:
        '''
        :schema: KotsApiApplicationSpec#title
        '''
        result = self._values.get("title")
        assert result is not None, "Required property 'title' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def additional_images(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: KotsApiApplicationSpec#additionalImages
        '''
        result = self._values.get("additional_images")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def additional_namespaces(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: KotsApiApplicationSpec#additionalNamespaces
        '''
        result = self._values.get("additional_namespaces")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allow_rollback(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: KotsApiApplicationSpec#allowRollback
        '''
        result = self._values.get("allow_rollback")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def graphs(self) -> typing.Optional[typing.List["KotsApiApplicationSpecGraphs"]]:
        '''
        :schema: KotsApiApplicationSpec#graphs
        '''
        result = self._values.get("graphs")
        return typing.cast(typing.Optional[typing.List["KotsApiApplicationSpecGraphs"]], result)

    @builtins.property
    def icon(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiApplicationSpec#icon
        '''
        result = self._values.get("icon")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kubectl_version(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiApplicationSpec#kubectlVersion
        '''
        result = self._values.get("kubectl_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kustomize_version(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiApplicationSpec#kustomizeVersion
        '''
        result = self._values.get("kustomize_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ports(self) -> typing.Optional[typing.List["KotsApiApplicationSpecPorts"]]:
        '''
        :schema: KotsApiApplicationSpec#ports
        '''
        result = self._values.get("ports")
        return typing.cast(typing.Optional[typing.List["KotsApiApplicationSpecPorts"]], result)

    @builtins.property
    def proxy_public_images(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: KotsApiApplicationSpec#proxyPublicImages
        '''
        result = self._values.get("proxy_public_images")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def release_notes(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiApplicationSpec#releaseNotes
        '''
        result = self._values.get("release_notes")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def require_minimal_rbac_privileges(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: KotsApiApplicationSpec#requireMinimalRBACPrivileges
        '''
        result = self._values.get("require_minimal_rbac_privileges")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def status_informers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: KotsApiApplicationSpec#statusInformers
        '''
        result = self._values.get("status_informers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KotsApiApplicationSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kots.KotsApiApplicationSpecGraphs",
    jsii_struct_bases=[],
    name_mapping={
        "title": "title",
        "duration_seconds": "durationSeconds",
        "legend": "legend",
        "queries": "queries",
        "query": "query",
        "y_axis_format": "yAxisFormat",
        "y_axis_template": "yAxisTemplate",
    },
)
class KotsApiApplicationSpecGraphs:
    def __init__(
        self,
        *,
        title: builtins.str,
        duration_seconds: typing.Optional[jsii.Number] = None,
        legend: typing.Optional[builtins.str] = None,
        queries: typing.Optional[typing.Sequence["KotsApiApplicationSpecGraphsQueries"]] = None,
        query: typing.Optional[builtins.str] = None,
        y_axis_format: typing.Optional[builtins.str] = None,
        y_axis_template: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param title: 
        :param duration_seconds: 
        :param legend: 
        :param queries: 
        :param query: 
        :param y_axis_format: https://github.com/grafana/grafana/blob/009d58c4a228b89046fdae02aa82cf5ff05e5e69/packages/grafana-ui/src/utils/valueFormats/categories.ts.
        :param y_axis_template: 

        :schema: KotsApiApplicationSpecGraphs
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "title": title,
        }
        if duration_seconds is not None:
            self._values["duration_seconds"] = duration_seconds
        if legend is not None:
            self._values["legend"] = legend
        if queries is not None:
            self._values["queries"] = queries
        if query is not None:
            self._values["query"] = query
        if y_axis_format is not None:
            self._values["y_axis_format"] = y_axis_format
        if y_axis_template is not None:
            self._values["y_axis_template"] = y_axis_template

    @builtins.property
    def title(self) -> builtins.str:
        '''
        :schema: KotsApiApplicationSpecGraphs#title
        '''
        result = self._values.get("title")
        assert result is not None, "Required property 'title' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def duration_seconds(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: KotsApiApplicationSpecGraphs#durationSeconds
        '''
        result = self._values.get("duration_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def legend(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiApplicationSpecGraphs#legend
        '''
        result = self._values.get("legend")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def queries(
        self,
    ) -> typing.Optional[typing.List["KotsApiApplicationSpecGraphsQueries"]]:
        '''
        :schema: KotsApiApplicationSpecGraphs#queries
        '''
        result = self._values.get("queries")
        return typing.cast(typing.Optional[typing.List["KotsApiApplicationSpecGraphsQueries"]], result)

    @builtins.property
    def query(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiApplicationSpecGraphs#query
        '''
        result = self._values.get("query")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def y_axis_format(self) -> typing.Optional[builtins.str]:
        '''https://github.com/grafana/grafana/blob/009d58c4a228b89046fdae02aa82cf5ff05e5e69/packages/grafana-ui/src/utils/valueFormats/categories.ts.

        :schema: KotsApiApplicationSpecGraphs#yAxisFormat
        '''
        result = self._values.get("y_axis_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def y_axis_template(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiApplicationSpecGraphs#yAxisTemplate
        '''
        result = self._values.get("y_axis_template")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KotsApiApplicationSpecGraphs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kots.KotsApiApplicationSpecGraphsQueries",
    jsii_struct_bases=[],
    name_mapping={"query": "query", "legend": "legend"},
)
class KotsApiApplicationSpecGraphsQueries:
    def __init__(
        self,
        *,
        query: builtins.str,
        legend: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param query: 
        :param legend: 

        :schema: KotsApiApplicationSpecGraphsQueries
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "query": query,
        }
        if legend is not None:
            self._values["legend"] = legend

    @builtins.property
    def query(self) -> builtins.str:
        '''
        :schema: KotsApiApplicationSpecGraphsQueries#query
        '''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def legend(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiApplicationSpecGraphsQueries#legend
        '''
        result = self._values.get("legend")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KotsApiApplicationSpecGraphsQueries(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kots.KotsApiApplicationSpecPorts",
    jsii_struct_bases=[],
    name_mapping={
        "service_name": "serviceName",
        "service_port": "servicePort",
        "application_url": "applicationUrl",
        "local_port": "localPort",
    },
)
class KotsApiApplicationSpecPorts:
    def __init__(
        self,
        *,
        service_name: builtins.str,
        service_port: jsii.Number,
        application_url: typing.Optional[builtins.str] = None,
        local_port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param service_name: 
        :param service_port: 
        :param application_url: 
        :param local_port: 

        :schema: KotsApiApplicationSpecPorts
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "service_name": service_name,
            "service_port": service_port,
        }
        if application_url is not None:
            self._values["application_url"] = application_url
        if local_port is not None:
            self._values["local_port"] = local_port

    @builtins.property
    def service_name(self) -> builtins.str:
        '''
        :schema: KotsApiApplicationSpecPorts#serviceName
        '''
        result = self._values.get("service_name")
        assert result is not None, "Required property 'service_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_port(self) -> jsii.Number:
        '''
        :schema: KotsApiApplicationSpecPorts#servicePort
        '''
        result = self._values.get("service_port")
        assert result is not None, "Required property 'service_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def application_url(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiApplicationSpecPorts#applicationUrl
        '''
        result = self._values.get("application_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def local_port(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: KotsApiApplicationSpecPorts#localPort
        '''
        result = self._values.get("local_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KotsApiApplicationSpecPorts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kots.KotsApiConfigSpec",
    jsii_struct_bases=[],
    name_mapping={"groups": "groups"},
)
class KotsApiConfigSpec:
    def __init__(self, *, groups: typing.Sequence["KotsApiConfigSpecGroups"]) -> None:
        '''ConfigSpec defines the desired state of ConfigSpec.

        :param groups: 

        :schema: KotsApiConfigSpec
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "groups": groups,
        }

    @builtins.property
    def groups(self) -> typing.List["KotsApiConfigSpecGroups"]:
        '''
        :schema: KotsApiConfigSpec#groups
        '''
        result = self._values.get("groups")
        assert result is not None, "Required property 'groups' is missing"
        return typing.cast(typing.List["KotsApiConfigSpecGroups"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KotsApiConfigSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kots.KotsApiConfigSpecGroups",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "title": "title",
        "description": "description",
        "items": "items",
        "when": "when",
    },
)
class KotsApiConfigSpecGroups:
    def __init__(
        self,
        *,
        name: builtins.str,
        title: builtins.str,
        description: typing.Optional[builtins.str] = None,
        items: typing.Optional[typing.Sequence["KotsApiConfigSpecGroupsItems"]] = None,
        when: typing.Optional["KotsApiConfigSpecGroupsWhen"] = None,
    ) -> None:
        '''
        :param name: 
        :param title: 
        :param description: 
        :param items: 
        :param when: QuotedBool is a string type that can also unmarshal raw yaml bools.

        :schema: KotsApiConfigSpecGroups
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "title": title,
        }
        if description is not None:
            self._values["description"] = description
        if items is not None:
            self._values["items"] = items
        if when is not None:
            self._values["when"] = when

    @builtins.property
    def name(self) -> builtins.str:
        '''
        :schema: KotsApiConfigSpecGroups#name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def title(self) -> builtins.str:
        '''
        :schema: KotsApiConfigSpecGroups#title
        '''
        result = self._values.get("title")
        assert result is not None, "Required property 'title' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiConfigSpecGroups#description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def items(self) -> typing.Optional[typing.List["KotsApiConfigSpecGroupsItems"]]:
        '''
        :schema: KotsApiConfigSpecGroups#items
        '''
        result = self._values.get("items")
        return typing.cast(typing.Optional[typing.List["KotsApiConfigSpecGroupsItems"]], result)

    @builtins.property
    def when(self) -> typing.Optional["KotsApiConfigSpecGroupsWhen"]:
        '''QuotedBool is a string type that can also unmarshal raw yaml bools.

        :schema: KotsApiConfigSpecGroups#when
        '''
        result = self._values.get("when")
        return typing.cast(typing.Optional["KotsApiConfigSpecGroupsWhen"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KotsApiConfigSpecGroups(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kots.KotsApiConfigSpecGroupsItems",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "type": "type",
        "affix": "affix",
        "count_by_group": "countByGroup",
        "data": "data",
        "default": "default",
        "error": "error",
        "filename": "filename",
        "help_text": "helpText",
        "hidden": "hidden",
        "items": "items",
        "minimum_count": "minimumCount",
        "multiple": "multiple",
        "multi_value": "multiValue",
        "readonly": "readonly",
        "recommended": "recommended",
        "repeatable": "repeatable",
        "required": "required",
        "templates": "templates",
        "title": "title",
        "value": "value",
        "values_by_group": "valuesByGroup",
        "when": "when",
        "write_once": "writeOnce",
    },
)
class KotsApiConfigSpecGroupsItems:
    def __init__(
        self,
        *,
        name: builtins.str,
        type: builtins.str,
        affix: typing.Optional[builtins.str] = None,
        count_by_group: typing.Optional[typing.Mapping[builtins.str, jsii.Number]] = None,
        data: typing.Optional[builtins.str] = None,
        default: typing.Optional["KotsApiConfigSpecGroupsItemsDefault"] = None,
        error: typing.Optional[builtins.str] = None,
        filename: typing.Optional[builtins.str] = None,
        help_text: typing.Optional[builtins.str] = None,
        hidden: typing.Optional[builtins.bool] = None,
        items: typing.Optional[typing.Sequence["KotsApiConfigSpecGroupsItemsItems"]] = None,
        minimum_count: typing.Optional[jsii.Number] = None,
        multiple: typing.Optional[builtins.bool] = None,
        multi_value: typing.Optional[typing.Sequence[builtins.str]] = None,
        readonly: typing.Optional[builtins.bool] = None,
        recommended: typing.Optional[builtins.bool] = None,
        repeatable: typing.Optional[builtins.bool] = None,
        required: typing.Optional[builtins.bool] = None,
        templates: typing.Optional[typing.Sequence["KotsApiConfigSpecGroupsItemsTemplates"]] = None,
        title: typing.Optional[builtins.str] = None,
        value: typing.Optional["KotsApiConfigSpecGroupsItemsValue"] = None,
        values_by_group: typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, builtins.str]]] = None,
        when: typing.Optional["KotsApiConfigSpecGroupsItemsWhen"] = None,
        write_once: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param name: 
        :param type: 
        :param affix: 
        :param count_by_group: 
        :param data: 
        :param default: BoolOrString is a type that can hold an bool or a string. When used in JSON or YAML marshalling and unmarshalling, it produces or consumes the inner type. This allows you to have, for example, a JSON field that can accept a booolean string or raw bool.
        :param error: 
        :param filename: 
        :param help_text: 
        :param hidden: 
        :param items: 
        :param minimum_count: 
        :param multiple: 
        :param multi_value: 
        :param readonly: 
        :param recommended: 
        :param repeatable: 
        :param required: 
        :param templates: 
        :param title: 
        :param value: BoolOrString is a type that can hold an bool or a string. When used in JSON or YAML marshalling and unmarshalling, it produces or consumes the inner type. This allows you to have, for example, a JSON field that can accept a booolean string or raw bool.
        :param values_by_group: 
        :param when: QuotedBool is a string type that can also unmarshal raw yaml bools.
        :param write_once: 

        :schema: KotsApiConfigSpecGroupsItems
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "type": type,
        }
        if affix is not None:
            self._values["affix"] = affix
        if count_by_group is not None:
            self._values["count_by_group"] = count_by_group
        if data is not None:
            self._values["data"] = data
        if default is not None:
            self._values["default"] = default
        if error is not None:
            self._values["error"] = error
        if filename is not None:
            self._values["filename"] = filename
        if help_text is not None:
            self._values["help_text"] = help_text
        if hidden is not None:
            self._values["hidden"] = hidden
        if items is not None:
            self._values["items"] = items
        if minimum_count is not None:
            self._values["minimum_count"] = minimum_count
        if multiple is not None:
            self._values["multiple"] = multiple
        if multi_value is not None:
            self._values["multi_value"] = multi_value
        if readonly is not None:
            self._values["readonly"] = readonly
        if recommended is not None:
            self._values["recommended"] = recommended
        if repeatable is not None:
            self._values["repeatable"] = repeatable
        if required is not None:
            self._values["required"] = required
        if templates is not None:
            self._values["templates"] = templates
        if title is not None:
            self._values["title"] = title
        if value is not None:
            self._values["value"] = value
        if values_by_group is not None:
            self._values["values_by_group"] = values_by_group
        if when is not None:
            self._values["when"] = when
        if write_once is not None:
            self._values["write_once"] = write_once

    @builtins.property
    def name(self) -> builtins.str:
        '''
        :schema: KotsApiConfigSpecGroupsItems#name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: KotsApiConfigSpecGroupsItems#type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def affix(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiConfigSpecGroupsItems#affix
        '''
        result = self._values.get("affix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def count_by_group(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, jsii.Number]]:
        '''
        :schema: KotsApiConfigSpecGroupsItems#countByGroup
        '''
        result = self._values.get("count_by_group")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, jsii.Number]], result)

    @builtins.property
    def data(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiConfigSpecGroupsItems#data
        '''
        result = self._values.get("data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default(self) -> typing.Optional["KotsApiConfigSpecGroupsItemsDefault"]:
        '''BoolOrString is a type that can hold an bool or a string.

        When used in JSON or YAML marshalling and unmarshalling, it produces or consumes the inner type.  This allows you to have, for example, a JSON field that can accept a booolean string or raw bool.

        :schema: KotsApiConfigSpecGroupsItems#default
        '''
        result = self._values.get("default")
        return typing.cast(typing.Optional["KotsApiConfigSpecGroupsItemsDefault"], result)

    @builtins.property
    def error(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiConfigSpecGroupsItems#error
        '''
        result = self._values.get("error")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def filename(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiConfigSpecGroupsItems#filename
        '''
        result = self._values.get("filename")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def help_text(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiConfigSpecGroupsItems#help_text
        '''
        result = self._values.get("help_text")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hidden(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: KotsApiConfigSpecGroupsItems#hidden
        '''
        result = self._values.get("hidden")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def items(
        self,
    ) -> typing.Optional[typing.List["KotsApiConfigSpecGroupsItemsItems"]]:
        '''
        :schema: KotsApiConfigSpecGroupsItems#items
        '''
        result = self._values.get("items")
        return typing.cast(typing.Optional[typing.List["KotsApiConfigSpecGroupsItemsItems"]], result)

    @builtins.property
    def minimum_count(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: KotsApiConfigSpecGroupsItems#minimumCount
        '''
        result = self._values.get("minimum_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def multiple(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: KotsApiConfigSpecGroupsItems#multiple
        '''
        result = self._values.get("multiple")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def multi_value(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: KotsApiConfigSpecGroupsItems#multi_value
        '''
        result = self._values.get("multi_value")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def readonly(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: KotsApiConfigSpecGroupsItems#readonly
        '''
        result = self._values.get("readonly")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def recommended(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: KotsApiConfigSpecGroupsItems#recommended
        '''
        result = self._values.get("recommended")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def repeatable(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: KotsApiConfigSpecGroupsItems#repeatable
        '''
        result = self._values.get("repeatable")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def required(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: KotsApiConfigSpecGroupsItems#required
        '''
        result = self._values.get("required")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def templates(
        self,
    ) -> typing.Optional[typing.List["KotsApiConfigSpecGroupsItemsTemplates"]]:
        '''
        :schema: KotsApiConfigSpecGroupsItems#templates
        '''
        result = self._values.get("templates")
        return typing.cast(typing.Optional[typing.List["KotsApiConfigSpecGroupsItemsTemplates"]], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiConfigSpecGroupsItems#title
        '''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional["KotsApiConfigSpecGroupsItemsValue"]:
        '''BoolOrString is a type that can hold an bool or a string.

        When used in JSON or YAML marshalling and unmarshalling, it produces or consumes the inner type.  This allows you to have, for example, a JSON field that can accept a booolean string or raw bool.

        :schema: KotsApiConfigSpecGroupsItems#value
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional["KotsApiConfigSpecGroupsItemsValue"], result)

    @builtins.property
    def values_by_group(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, builtins.str]]]:
        '''
        :schema: KotsApiConfigSpecGroupsItems#valuesByGroup
        '''
        result = self._values.get("values_by_group")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def when(self) -> typing.Optional["KotsApiConfigSpecGroupsItemsWhen"]:
        '''QuotedBool is a string type that can also unmarshal raw yaml bools.

        :schema: KotsApiConfigSpecGroupsItems#when
        '''
        result = self._values.get("when")
        return typing.cast(typing.Optional["KotsApiConfigSpecGroupsItemsWhen"], result)

    @builtins.property
    def write_once(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: KotsApiConfigSpecGroupsItems#write_once
        '''
        result = self._values.get("write_once")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KotsApiConfigSpecGroupsItems(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KotsApiConfigSpecGroupsItemsDefault(
    metaclass=jsii.JSIIMeta,
    jsii_type="kots.KotsApiConfigSpecGroupsItemsDefault",
):
    '''BoolOrString is a type that can hold an bool or a string.

    When used in JSON or YAML marshalling and unmarshalling, it produces or consumes the inner type.  This allows you to have, for example, a JSON field that can accept a booolean string or raw bool.

    :schema: KotsApiConfigSpecGroupsItemsDefault
    '''

    @jsii.member(jsii_name="fromBoolean") # type: ignore[misc]
    @builtins.classmethod
    def from_boolean(
        cls,
        value: builtins.bool,
    ) -> "KotsApiConfigSpecGroupsItemsDefault":
        '''
        :param value: -
        '''
        return typing.cast("KotsApiConfigSpecGroupsItemsDefault", jsii.sinvoke(cls, "fromBoolean", [value]))

    @jsii.member(jsii_name="fromString") # type: ignore[misc]
    @builtins.classmethod
    def from_string(cls, value: builtins.str) -> "KotsApiConfigSpecGroupsItemsDefault":
        '''
        :param value: -
        '''
        return typing.cast("KotsApiConfigSpecGroupsItemsDefault", jsii.sinvoke(cls, "fromString", [value]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="value")
    def value(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.get(self, "value"))


@jsii.data_type(
    jsii_type="kots.KotsApiConfigSpecGroupsItemsItems",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "title": "title",
        "default": "default",
        "recommended": "recommended",
        "value": "value",
    },
)
class KotsApiConfigSpecGroupsItemsItems:
    def __init__(
        self,
        *,
        name: builtins.str,
        title: builtins.str,
        default: typing.Optional["KotsApiConfigSpecGroupsItemsItemsDefault"] = None,
        recommended: typing.Optional[builtins.bool] = None,
        value: typing.Optional["KotsApiConfigSpecGroupsItemsItemsValue"] = None,
    ) -> None:
        '''
        :param name: 
        :param title: 
        :param default: BoolOrString is a type that can hold an bool or a string. When used in JSON or YAML marshalling and unmarshalling, it produces or consumes the inner type. This allows you to have, for example, a JSON field that can accept a booolean string or raw bool.
        :param recommended: 
        :param value: BoolOrString is a type that can hold an bool or a string. When used in JSON or YAML marshalling and unmarshalling, it produces or consumes the inner type. This allows you to have, for example, a JSON field that can accept a booolean string or raw bool.

        :schema: KotsApiConfigSpecGroupsItemsItems
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "title": title,
        }
        if default is not None:
            self._values["default"] = default
        if recommended is not None:
            self._values["recommended"] = recommended
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def name(self) -> builtins.str:
        '''
        :schema: KotsApiConfigSpecGroupsItemsItems#name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def title(self) -> builtins.str:
        '''
        :schema: KotsApiConfigSpecGroupsItemsItems#title
        '''
        result = self._values.get("title")
        assert result is not None, "Required property 'title' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default(self) -> typing.Optional["KotsApiConfigSpecGroupsItemsItemsDefault"]:
        '''BoolOrString is a type that can hold an bool or a string.

        When used in JSON or YAML marshalling and unmarshalling, it produces or consumes the inner type.  This allows you to have, for example, a JSON field that can accept a booolean string or raw bool.

        :schema: KotsApiConfigSpecGroupsItemsItems#default
        '''
        result = self._values.get("default")
        return typing.cast(typing.Optional["KotsApiConfigSpecGroupsItemsItemsDefault"], result)

    @builtins.property
    def recommended(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: KotsApiConfigSpecGroupsItemsItems#recommended
        '''
        result = self._values.get("recommended")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def value(self) -> typing.Optional["KotsApiConfigSpecGroupsItemsItemsValue"]:
        '''BoolOrString is a type that can hold an bool or a string.

        When used in JSON or YAML marshalling and unmarshalling, it produces or consumes the inner type.  This allows you to have, for example, a JSON field that can accept a booolean string or raw bool.

        :schema: KotsApiConfigSpecGroupsItemsItems#value
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional["KotsApiConfigSpecGroupsItemsItemsValue"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KotsApiConfigSpecGroupsItemsItems(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KotsApiConfigSpecGroupsItemsItemsDefault(
    metaclass=jsii.JSIIMeta,
    jsii_type="kots.KotsApiConfigSpecGroupsItemsItemsDefault",
):
    '''BoolOrString is a type that can hold an bool or a string.

    When used in JSON or YAML marshalling and unmarshalling, it produces or consumes the inner type.  This allows you to have, for example, a JSON field that can accept a booolean string or raw bool.

    :schema: KotsApiConfigSpecGroupsItemsItemsDefault
    '''

    @jsii.member(jsii_name="fromBoolean") # type: ignore[misc]
    @builtins.classmethod
    def from_boolean(
        cls,
        value: builtins.bool,
    ) -> "KotsApiConfigSpecGroupsItemsItemsDefault":
        '''
        :param value: -
        '''
        return typing.cast("KotsApiConfigSpecGroupsItemsItemsDefault", jsii.sinvoke(cls, "fromBoolean", [value]))

    @jsii.member(jsii_name="fromString") # type: ignore[misc]
    @builtins.classmethod
    def from_string(
        cls,
        value: builtins.str,
    ) -> "KotsApiConfigSpecGroupsItemsItemsDefault":
        '''
        :param value: -
        '''
        return typing.cast("KotsApiConfigSpecGroupsItemsItemsDefault", jsii.sinvoke(cls, "fromString", [value]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="value")
    def value(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.get(self, "value"))


class KotsApiConfigSpecGroupsItemsItemsValue(
    metaclass=jsii.JSIIMeta,
    jsii_type="kots.KotsApiConfigSpecGroupsItemsItemsValue",
):
    '''BoolOrString is a type that can hold an bool or a string.

    When used in JSON or YAML marshalling and unmarshalling, it produces or consumes the inner type.  This allows you to have, for example, a JSON field that can accept a booolean string or raw bool.

    :schema: KotsApiConfigSpecGroupsItemsItemsValue
    '''

    @jsii.member(jsii_name="fromBoolean") # type: ignore[misc]
    @builtins.classmethod
    def from_boolean(
        cls,
        value: builtins.bool,
    ) -> "KotsApiConfigSpecGroupsItemsItemsValue":
        '''
        :param value: -
        '''
        return typing.cast("KotsApiConfigSpecGroupsItemsItemsValue", jsii.sinvoke(cls, "fromBoolean", [value]))

    @jsii.member(jsii_name="fromString") # type: ignore[misc]
    @builtins.classmethod
    def from_string(
        cls,
        value: builtins.str,
    ) -> "KotsApiConfigSpecGroupsItemsItemsValue":
        '''
        :param value: -
        '''
        return typing.cast("KotsApiConfigSpecGroupsItemsItemsValue", jsii.sinvoke(cls, "fromString", [value]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="value")
    def value(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.get(self, "value"))


@jsii.data_type(
    jsii_type="kots.KotsApiConfigSpecGroupsItemsTemplates",
    jsii_struct_bases=[],
    name_mapping={
        "api_version": "apiVersion",
        "kind": "kind",
        "name": "name",
        "namespace": "namespace",
        "yaml_path": "yamlPath",
    },
)
class KotsApiConfigSpecGroupsItemsTemplates:
    def __init__(
        self,
        *,
        api_version: builtins.str,
        kind: builtins.str,
        name: builtins.str,
        namespace: typing.Optional[builtins.str] = None,
        yaml_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param api_version: 
        :param kind: 
        :param name: 
        :param namespace: 
        :param yaml_path: 

        :schema: KotsApiConfigSpecGroupsItemsTemplates
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "api_version": api_version,
            "kind": kind,
            "name": name,
        }
        if namespace is not None:
            self._values["namespace"] = namespace
        if yaml_path is not None:
            self._values["yaml_path"] = yaml_path

    @builtins.property
    def api_version(self) -> builtins.str:
        '''
        :schema: KotsApiConfigSpecGroupsItemsTemplates#apiVersion
        '''
        result = self._values.get("api_version")
        assert result is not None, "Required property 'api_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kind(self) -> builtins.str:
        '''
        :schema: KotsApiConfigSpecGroupsItemsTemplates#kind
        '''
        result = self._values.get("kind")
        assert result is not None, "Required property 'kind' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''
        :schema: KotsApiConfigSpecGroupsItemsTemplates#name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiConfigSpecGroupsItemsTemplates#namespace
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def yaml_path(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiConfigSpecGroupsItemsTemplates#yamlPath
        '''
        result = self._values.get("yaml_path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KotsApiConfigSpecGroupsItemsTemplates(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KotsApiConfigSpecGroupsItemsValue(
    metaclass=jsii.JSIIMeta,
    jsii_type="kots.KotsApiConfigSpecGroupsItemsValue",
):
    '''BoolOrString is a type that can hold an bool or a string.

    When used in JSON or YAML marshalling and unmarshalling, it produces or consumes the inner type.  This allows you to have, for example, a JSON field that can accept a booolean string or raw bool.

    :schema: KotsApiConfigSpecGroupsItemsValue
    '''

    @jsii.member(jsii_name="fromBoolean") # type: ignore[misc]
    @builtins.classmethod
    def from_boolean(cls, value: builtins.bool) -> "KotsApiConfigSpecGroupsItemsValue":
        '''
        :param value: -
        '''
        return typing.cast("KotsApiConfigSpecGroupsItemsValue", jsii.sinvoke(cls, "fromBoolean", [value]))

    @jsii.member(jsii_name="fromString") # type: ignore[misc]
    @builtins.classmethod
    def from_string(cls, value: builtins.str) -> "KotsApiConfigSpecGroupsItemsValue":
        '''
        :param value: -
        '''
        return typing.cast("KotsApiConfigSpecGroupsItemsValue", jsii.sinvoke(cls, "fromString", [value]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="value")
    def value(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.get(self, "value"))


class KotsApiConfigSpecGroupsItemsWhen(
    metaclass=jsii.JSIIMeta,
    jsii_type="kots.KotsApiConfigSpecGroupsItemsWhen",
):
    '''QuotedBool is a string type that can also unmarshal raw yaml bools.

    :schema: KotsApiConfigSpecGroupsItemsWhen
    '''

    @jsii.member(jsii_name="fromBoolean") # type: ignore[misc]
    @builtins.classmethod
    def from_boolean(cls, value: builtins.bool) -> "KotsApiConfigSpecGroupsItemsWhen":
        '''
        :param value: -
        '''
        return typing.cast("KotsApiConfigSpecGroupsItemsWhen", jsii.sinvoke(cls, "fromBoolean", [value]))

    @jsii.member(jsii_name="fromString") # type: ignore[misc]
    @builtins.classmethod
    def from_string(cls, value: builtins.str) -> "KotsApiConfigSpecGroupsItemsWhen":
        '''
        :param value: -
        '''
        return typing.cast("KotsApiConfigSpecGroupsItemsWhen", jsii.sinvoke(cls, "fromString", [value]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="value")
    def value(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.get(self, "value"))


class KotsApiConfigSpecGroupsWhen(
    metaclass=jsii.JSIIMeta,
    jsii_type="kots.KotsApiConfigSpecGroupsWhen",
):
    '''QuotedBool is a string type that can also unmarshal raw yaml bools.

    :schema: KotsApiConfigSpecGroupsWhen
    '''

    @jsii.member(jsii_name="fromBoolean") # type: ignore[misc]
    @builtins.classmethod
    def from_boolean(cls, value: builtins.bool) -> "KotsApiConfigSpecGroupsWhen":
        '''
        :param value: -
        '''
        return typing.cast("KotsApiConfigSpecGroupsWhen", jsii.sinvoke(cls, "fromBoolean", [value]))

    @jsii.member(jsii_name="fromString") # type: ignore[misc]
    @builtins.classmethod
    def from_string(cls, value: builtins.str) -> "KotsApiConfigSpecGroupsWhen":
        '''
        :param value: -
        '''
        return typing.cast("KotsApiConfigSpecGroupsWhen", jsii.sinvoke(cls, "fromString", [value]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="value")
    def value(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.get(self, "value"))


@jsii.data_type(
    jsii_type="kots.KotsApiConfigvaluesSpec",
    jsii_struct_bases=[],
    name_mapping={"values": "values"},
)
class KotsApiConfigvaluesSpec:
    def __init__(
        self,
        *,
        values: typing.Mapping[builtins.str, "KotsApiConfigvaluesSpecValues"],
    ) -> None:
        '''ConfigValuesSpec defines the desired state of ConfigValue.

        :param values: 

        :schema: KotsApiConfigvaluesSpec
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "values": values,
        }

    @builtins.property
    def values(self) -> typing.Mapping[builtins.str, "KotsApiConfigvaluesSpecValues"]:
        '''
        :schema: KotsApiConfigvaluesSpec#values
        '''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.Mapping[builtins.str, "KotsApiConfigvaluesSpecValues"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KotsApiConfigvaluesSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kots.KotsApiConfigvaluesSpecValues",
    jsii_struct_bases=[],
    name_mapping={
        "data": "data",
        "data_plaintext": "dataPlaintext",
        "default": "default",
        "filename": "filename",
        "repeatable_item": "repeatableItem",
        "value": "value",
        "value_plaintext": "valuePlaintext",
    },
)
class KotsApiConfigvaluesSpecValues:
    def __init__(
        self,
        *,
        data: typing.Optional[builtins.str] = None,
        data_plaintext: typing.Optional[builtins.str] = None,
        default: typing.Optional[builtins.str] = None,
        filename: typing.Optional[builtins.str] = None,
        repeatable_item: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
        value_plaintext: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param data: 
        :param data_plaintext: 
        :param default: 
        :param filename: 
        :param repeatable_item: 
        :param value: 
        :param value_plaintext: 

        :schema: KotsApiConfigvaluesSpecValues
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if data is not None:
            self._values["data"] = data
        if data_plaintext is not None:
            self._values["data_plaintext"] = data_plaintext
        if default is not None:
            self._values["default"] = default
        if filename is not None:
            self._values["filename"] = filename
        if repeatable_item is not None:
            self._values["repeatable_item"] = repeatable_item
        if value is not None:
            self._values["value"] = value
        if value_plaintext is not None:
            self._values["value_plaintext"] = value_plaintext

    @builtins.property
    def data(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiConfigvaluesSpecValues#data
        '''
        result = self._values.get("data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_plaintext(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiConfigvaluesSpecValues#dataPlaintext
        '''
        result = self._values.get("data_plaintext")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiConfigvaluesSpecValues#default
        '''
        result = self._values.get("default")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def filename(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiConfigvaluesSpecValues#filename
        '''
        result = self._values.get("filename")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def repeatable_item(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiConfigvaluesSpecValues#repeatableItem
        '''
        result = self._values.get("repeatable_item")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiConfigvaluesSpecValues#value
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value_plaintext(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiConfigvaluesSpecValues#valuePlaintext
        '''
        result = self._values.get("value_plaintext")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KotsApiConfigvaluesSpecValues(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kots.KotsApiHelmchartSpec",
    jsii_struct_bases=[],
    name_mapping={
        "chart": "chart",
        "builder": "builder",
        "exclude": "exclude",
        "helm_version": "helmVersion",
        "namespace": "namespace",
        "optional_values": "optionalValues",
        "use_helm_install": "useHelmInstall",
        "values": "values",
    },
)
class KotsApiHelmchartSpec:
    def __init__(
        self,
        *,
        chart: "KotsApiHelmchartSpecChart",
        builder: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        exclude: typing.Optional["KotsApiHelmchartSpecExclude"] = None,
        helm_version: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        optional_values: typing.Optional[typing.Sequence["KotsApiHelmchartSpecOptionalValues"]] = None,
        use_helm_install: typing.Optional[builtins.bool] = None,
        values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''HelmChartSpec defines the desired state of HelmChartSpec.

        :param chart: 
        :param builder: 
        :param exclude: BoolOrString is a type that can hold an bool or a string. When used in JSON or YAML marshalling and unmarshalling, it produces or consumes the inner type. This allows you to have, for example, a JSON field that can accept a booolean string or raw bool.
        :param helm_version: 
        :param namespace: 
        :param optional_values: 
        :param use_helm_install: 
        :param values: 

        :schema: KotsApiHelmchartSpec
        '''
        if isinstance(chart, dict):
            chart = KotsApiHelmchartSpecChart(**chart)
        self._values: typing.Dict[str, typing.Any] = {
            "chart": chart,
        }
        if builder is not None:
            self._values["builder"] = builder
        if exclude is not None:
            self._values["exclude"] = exclude
        if helm_version is not None:
            self._values["helm_version"] = helm_version
        if namespace is not None:
            self._values["namespace"] = namespace
        if optional_values is not None:
            self._values["optional_values"] = optional_values
        if use_helm_install is not None:
            self._values["use_helm_install"] = use_helm_install
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def chart(self) -> "KotsApiHelmchartSpecChart":
        '''
        :schema: KotsApiHelmchartSpec#chart
        '''
        result = self._values.get("chart")
        assert result is not None, "Required property 'chart' is missing"
        return typing.cast("KotsApiHelmchartSpecChart", result)

    @builtins.property
    def builder(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''
        :schema: KotsApiHelmchartSpec#builder
        '''
        result = self._values.get("builder")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def exclude(self) -> typing.Optional["KotsApiHelmchartSpecExclude"]:
        '''BoolOrString is a type that can hold an bool or a string.

        When used in JSON or YAML marshalling and unmarshalling, it produces or consumes the inner type.  This allows you to have, for example, a JSON field that can accept a booolean string or raw bool.

        :schema: KotsApiHelmchartSpec#exclude
        '''
        result = self._values.get("exclude")
        return typing.cast(typing.Optional["KotsApiHelmchartSpecExclude"], result)

    @builtins.property
    def helm_version(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiHelmchartSpec#helmVersion
        '''
        result = self._values.get("helm_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiHelmchartSpec#namespace
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def optional_values(
        self,
    ) -> typing.Optional[typing.List["KotsApiHelmchartSpecOptionalValues"]]:
        '''
        :schema: KotsApiHelmchartSpec#optionalValues
        '''
        result = self._values.get("optional_values")
        return typing.cast(typing.Optional[typing.List["KotsApiHelmchartSpecOptionalValues"]], result)

    @builtins.property
    def use_helm_install(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: KotsApiHelmchartSpec#useHelmInstall
        '''
        result = self._values.get("use_helm_install")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''
        :schema: KotsApiHelmchartSpec#values
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KotsApiHelmchartSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kots.KotsApiHelmchartSpecChart",
    jsii_struct_bases=[],
    name_mapping={"chart_version": "chartVersion", "name": "name"},
)
class KotsApiHelmchartSpecChart:
    def __init__(self, *, chart_version: builtins.str, name: builtins.str) -> None:
        '''
        :param chart_version: 
        :param name: 

        :schema: KotsApiHelmchartSpecChart
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "chart_version": chart_version,
            "name": name,
        }

    @builtins.property
    def chart_version(self) -> builtins.str:
        '''
        :schema: KotsApiHelmchartSpecChart#chartVersion
        '''
        result = self._values.get("chart_version")
        assert result is not None, "Required property 'chart_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''
        :schema: KotsApiHelmchartSpecChart#name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KotsApiHelmchartSpecChart(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KotsApiHelmchartSpecExclude(
    metaclass=jsii.JSIIMeta,
    jsii_type="kots.KotsApiHelmchartSpecExclude",
):
    '''BoolOrString is a type that can hold an bool or a string.

    When used in JSON or YAML marshalling and unmarshalling, it produces or consumes the inner type.  This allows you to have, for example, a JSON field that can accept a booolean string or raw bool.

    :schema: KotsApiHelmchartSpecExclude
    '''

    @jsii.member(jsii_name="fromBoolean") # type: ignore[misc]
    @builtins.classmethod
    def from_boolean(cls, value: builtins.bool) -> "KotsApiHelmchartSpecExclude":
        '''
        :param value: -
        '''
        return typing.cast("KotsApiHelmchartSpecExclude", jsii.sinvoke(cls, "fromBoolean", [value]))

    @jsii.member(jsii_name="fromString") # type: ignore[misc]
    @builtins.classmethod
    def from_string(cls, value: builtins.str) -> "KotsApiHelmchartSpecExclude":
        '''
        :param value: -
        '''
        return typing.cast("KotsApiHelmchartSpecExclude", jsii.sinvoke(cls, "fromString", [value]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="value")
    def value(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.get(self, "value"))


@jsii.data_type(
    jsii_type="kots.KotsApiHelmchartSpecOptionalValues",
    jsii_struct_bases=[],
    name_mapping={
        "recursive_merge": "recursiveMerge",
        "when": "when",
        "values": "values",
    },
)
class KotsApiHelmchartSpecOptionalValues:
    def __init__(
        self,
        *,
        recursive_merge: builtins.bool,
        when: builtins.str,
        values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param recursive_merge: 
        :param when: 
        :param values: 

        :schema: KotsApiHelmchartSpecOptionalValues
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "recursive_merge": recursive_merge,
            "when": when,
        }
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def recursive_merge(self) -> builtins.bool:
        '''
        :schema: KotsApiHelmchartSpecOptionalValues#recursiveMerge
        '''
        result = self._values.get("recursive_merge")
        assert result is not None, "Required property 'recursive_merge' is missing"
        return typing.cast(builtins.bool, result)

    @builtins.property
    def when(self) -> builtins.str:
        '''
        :schema: KotsApiHelmchartSpecOptionalValues#when
        '''
        result = self._values.get("when")
        assert result is not None, "Required property 'when' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''
        :schema: KotsApiHelmchartSpecOptionalValues#values
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KotsApiHelmchartSpecOptionalValues(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kots.KotsApiIdentitySpec",
    jsii_struct_bases=[],
    name_mapping={
        "identity_issuer_url": "identityIssuerUrl",
        "oidc_redirect_uris": "oidcRedirectUris",
        "require_identity_provider": "requireIdentityProvider",
        "id_tokens_expiration": "idTokensExpiration",
        "oauth2_always_show_login_screen": "oauth2AlwaysShowLoginScreen",
        "roles": "roles",
        "signing_keys_expiration": "signingKeysExpiration",
        "supported_providers": "supportedProviders",
        "web_config": "webConfig",
    },
)
class KotsApiIdentitySpec:
    def __init__(
        self,
        *,
        identity_issuer_url: builtins.str,
        oidc_redirect_uris: typing.Sequence[builtins.str],
        require_identity_provider: "KotsApiIdentitySpecRequireIdentityProvider",
        id_tokens_expiration: typing.Optional[builtins.str] = None,
        oauth2_always_show_login_screen: typing.Optional[builtins.bool] = None,
        roles: typing.Optional[typing.Sequence["KotsApiIdentitySpecRoles"]] = None,
        signing_keys_expiration: typing.Optional[builtins.str] = None,
        supported_providers: typing.Optional[typing.Sequence[builtins.str]] = None,
        web_config: typing.Optional["KotsApiIdentitySpecWebConfig"] = None,
    ) -> None:
        '''
        :param identity_issuer_url: 
        :param oidc_redirect_uris: 
        :param require_identity_provider: BoolOrString is a type that can hold an bool or a string. When used in JSON or YAML marshalling and unmarshalling, it produces or consumes the inner type. This allows you to have, for example, a JSON field that can accept a booolean string or raw bool.
        :param id_tokens_expiration: 
        :param oauth2_always_show_login_screen: 
        :param roles: 
        :param signing_keys_expiration: 
        :param supported_providers: 
        :param web_config: 

        :schema: KotsApiIdentitySpec
        '''
        if isinstance(web_config, dict):
            web_config = KotsApiIdentitySpecWebConfig(**web_config)
        self._values: typing.Dict[str, typing.Any] = {
            "identity_issuer_url": identity_issuer_url,
            "oidc_redirect_uris": oidc_redirect_uris,
            "require_identity_provider": require_identity_provider,
        }
        if id_tokens_expiration is not None:
            self._values["id_tokens_expiration"] = id_tokens_expiration
        if oauth2_always_show_login_screen is not None:
            self._values["oauth2_always_show_login_screen"] = oauth2_always_show_login_screen
        if roles is not None:
            self._values["roles"] = roles
        if signing_keys_expiration is not None:
            self._values["signing_keys_expiration"] = signing_keys_expiration
        if supported_providers is not None:
            self._values["supported_providers"] = supported_providers
        if web_config is not None:
            self._values["web_config"] = web_config

    @builtins.property
    def identity_issuer_url(self) -> builtins.str:
        '''
        :schema: KotsApiIdentitySpec#identityIssuerURL
        '''
        result = self._values.get("identity_issuer_url")
        assert result is not None, "Required property 'identity_issuer_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def oidc_redirect_uris(self) -> typing.List[builtins.str]:
        '''
        :schema: KotsApiIdentitySpec#oidcRedirectUris
        '''
        result = self._values.get("oidc_redirect_uris")
        assert result is not None, "Required property 'oidc_redirect_uris' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def require_identity_provider(self) -> "KotsApiIdentitySpecRequireIdentityProvider":
        '''BoolOrString is a type that can hold an bool or a string.

        When used in JSON or YAML marshalling and unmarshalling, it produces or consumes the inner type.  This allows you to have, for example, a JSON field that can accept a booolean string or raw bool.

        :schema: KotsApiIdentitySpec#requireIdentityProvider
        '''
        result = self._values.get("require_identity_provider")
        assert result is not None, "Required property 'require_identity_provider' is missing"
        return typing.cast("KotsApiIdentitySpecRequireIdentityProvider", result)

    @builtins.property
    def id_tokens_expiration(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiIdentitySpec#idTokensExpiration
        '''
        result = self._values.get("id_tokens_expiration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth2_always_show_login_screen(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: KotsApiIdentitySpec#oauth2AlwaysShowLoginScreen
        '''
        result = self._values.get("oauth2_always_show_login_screen")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def roles(self) -> typing.Optional[typing.List["KotsApiIdentitySpecRoles"]]:
        '''
        :schema: KotsApiIdentitySpec#roles
        '''
        result = self._values.get("roles")
        return typing.cast(typing.Optional[typing.List["KotsApiIdentitySpecRoles"]], result)

    @builtins.property
    def signing_keys_expiration(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiIdentitySpec#signingKeysExpiration
        '''
        result = self._values.get("signing_keys_expiration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def supported_providers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: KotsApiIdentitySpec#supportedProviders
        '''
        result = self._values.get("supported_providers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def web_config(self) -> typing.Optional["KotsApiIdentitySpecWebConfig"]:
        '''
        :schema: KotsApiIdentitySpec#webConfig
        '''
        result = self._values.get("web_config")
        return typing.cast(typing.Optional["KotsApiIdentitySpecWebConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KotsApiIdentitySpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KotsApiIdentitySpecRequireIdentityProvider(
    metaclass=jsii.JSIIMeta,
    jsii_type="kots.KotsApiIdentitySpecRequireIdentityProvider",
):
    '''BoolOrString is a type that can hold an bool or a string.

    When used in JSON or YAML marshalling and unmarshalling, it produces or consumes the inner type.  This allows you to have, for example, a JSON field that can accept a booolean string or raw bool.

    :schema: KotsApiIdentitySpecRequireIdentityProvider
    '''

    @jsii.member(jsii_name="fromBoolean") # type: ignore[misc]
    @builtins.classmethod
    def from_boolean(
        cls,
        value: builtins.bool,
    ) -> "KotsApiIdentitySpecRequireIdentityProvider":
        '''
        :param value: -
        '''
        return typing.cast("KotsApiIdentitySpecRequireIdentityProvider", jsii.sinvoke(cls, "fromBoolean", [value]))

    @jsii.member(jsii_name="fromString") # type: ignore[misc]
    @builtins.classmethod
    def from_string(
        cls,
        value: builtins.str,
    ) -> "KotsApiIdentitySpecRequireIdentityProvider":
        '''
        :param value: -
        '''
        return typing.cast("KotsApiIdentitySpecRequireIdentityProvider", jsii.sinvoke(cls, "fromString", [value]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="value")
    def value(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.get(self, "value"))


@jsii.data_type(
    jsii_type="kots.KotsApiIdentitySpecRoles",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "description": "description", "name": "name"},
)
class KotsApiIdentitySpecRoles:
    def __init__(
        self,
        *,
        id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: 
        :param description: 
        :param name: 

        :schema: KotsApiIdentitySpecRoles
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "id": id,
        }
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> builtins.str:
        '''
        :schema: KotsApiIdentitySpecRoles#id
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiIdentitySpecRoles#description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiIdentitySpecRoles#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KotsApiIdentitySpecRoles(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kots.KotsApiIdentitySpecWebConfig",
    jsii_struct_bases=[],
    name_mapping={"theme": "theme", "title": "title"},
)
class KotsApiIdentitySpecWebConfig:
    def __init__(
        self,
        *,
        theme: typing.Optional["KotsApiIdentitySpecWebConfigTheme"] = None,
        title: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param theme: 
        :param title: 

        :schema: KotsApiIdentitySpecWebConfig
        '''
        if isinstance(theme, dict):
            theme = KotsApiIdentitySpecWebConfigTheme(**theme)
        self._values: typing.Dict[str, typing.Any] = {}
        if theme is not None:
            self._values["theme"] = theme
        if title is not None:
            self._values["title"] = title

    @builtins.property
    def theme(self) -> typing.Optional["KotsApiIdentitySpecWebConfigTheme"]:
        '''
        :schema: KotsApiIdentitySpecWebConfig#theme
        '''
        result = self._values.get("theme")
        return typing.cast(typing.Optional["KotsApiIdentitySpecWebConfigTheme"], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiIdentitySpecWebConfig#title
        '''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KotsApiIdentitySpecWebConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kots.KotsApiIdentitySpecWebConfigTheme",
    jsii_struct_bases=[],
    name_mapping={
        "favicon_base64": "faviconBase64",
        "logo_base64": "logoBase64",
        "logo_url": "logoUrl",
        "style_css_base64": "styleCssBase64",
    },
)
class KotsApiIdentitySpecWebConfigTheme:
    def __init__(
        self,
        *,
        favicon_base64: typing.Optional[builtins.str] = None,
        logo_base64: typing.Optional[builtins.str] = None,
        logo_url: typing.Optional[builtins.str] = None,
        style_css_base64: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param favicon_base64: 
        :param logo_base64: 
        :param logo_url: 
        :param style_css_base64: 

        :schema: KotsApiIdentitySpecWebConfigTheme
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if favicon_base64 is not None:
            self._values["favicon_base64"] = favicon_base64
        if logo_base64 is not None:
            self._values["logo_base64"] = logo_base64
        if logo_url is not None:
            self._values["logo_url"] = logo_url
        if style_css_base64 is not None:
            self._values["style_css_base64"] = style_css_base64

    @builtins.property
    def favicon_base64(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiIdentitySpecWebConfigTheme#faviconBase64
        '''
        result = self._values.get("favicon_base64")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logo_base64(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiIdentitySpecWebConfigTheme#logoBase64
        '''
        result = self._values.get("logo_base64")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logo_url(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiIdentitySpecWebConfigTheme#logoUrl
        '''
        result = self._values.get("logo_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def style_css_base64(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiIdentitySpecWebConfigTheme#styleCssBase64
        '''
        result = self._values.get("style_css_base64")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KotsApiIdentitySpecWebConfigTheme(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kots.KotsApiIdentityconfigsSpec",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "admin_console_address": "adminConsoleAddress",
        "ca_cert_pem_base64": "caCertPemBase64",
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "dex_connectors": "dexConnectors",
        "disable_password_auth": "disablePasswordAuth",
        "groups": "groups",
        "identity_service_address": "identityServiceAddress",
        "ingress_config": "ingressConfig",
        "insecure_skip_tls_verify": "insecureSkipTlsVerify",
        "storage": "storage",
    },
)
class KotsApiIdentityconfigsSpec:
    def __init__(
        self,
        *,
        enabled: builtins.bool,
        admin_console_address: typing.Optional[builtins.str] = None,
        ca_cert_pem_base64: typing.Optional[builtins.str] = None,
        client_id: typing.Optional[builtins.str] = None,
        client_secret: typing.Optional["KotsApiIdentityconfigsSpecClientSecret"] = None,
        dex_connectors: typing.Optional["KotsApiIdentityconfigsSpecDexConnectors"] = None,
        disable_password_auth: typing.Optional[builtins.bool] = None,
        groups: typing.Optional[typing.Sequence["KotsApiIdentityconfigsSpecGroups"]] = None,
        identity_service_address: typing.Optional[builtins.str] = None,
        ingress_config: typing.Optional["KotsApiIdentityconfigsSpecIngressConfig"] = None,
        insecure_skip_tls_verify: typing.Optional[builtins.bool] = None,
        storage: typing.Optional["KotsApiIdentityconfigsSpecStorage"] = None,
    ) -> None:
        '''
        :param enabled: 
        :param admin_console_address: 
        :param ca_cert_pem_base64: 
        :param client_id: 
        :param client_secret: 
        :param dex_connectors: 
        :param disable_password_auth: 
        :param groups: 
        :param identity_service_address: 
        :param ingress_config: 
        :param insecure_skip_tls_verify: 
        :param storage: 

        :schema: KotsApiIdentityconfigsSpec
        '''
        if isinstance(client_secret, dict):
            client_secret = KotsApiIdentityconfigsSpecClientSecret(**client_secret)
        if isinstance(dex_connectors, dict):
            dex_connectors = KotsApiIdentityconfigsSpecDexConnectors(**dex_connectors)
        if isinstance(ingress_config, dict):
            ingress_config = KotsApiIdentityconfigsSpecIngressConfig(**ingress_config)
        if isinstance(storage, dict):
            storage = KotsApiIdentityconfigsSpecStorage(**storage)
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
        }
        if admin_console_address is not None:
            self._values["admin_console_address"] = admin_console_address
        if ca_cert_pem_base64 is not None:
            self._values["ca_cert_pem_base64"] = ca_cert_pem_base64
        if client_id is not None:
            self._values["client_id"] = client_id
        if client_secret is not None:
            self._values["client_secret"] = client_secret
        if dex_connectors is not None:
            self._values["dex_connectors"] = dex_connectors
        if disable_password_auth is not None:
            self._values["disable_password_auth"] = disable_password_auth
        if groups is not None:
            self._values["groups"] = groups
        if identity_service_address is not None:
            self._values["identity_service_address"] = identity_service_address
        if ingress_config is not None:
            self._values["ingress_config"] = ingress_config
        if insecure_skip_tls_verify is not None:
            self._values["insecure_skip_tls_verify"] = insecure_skip_tls_verify
        if storage is not None:
            self._values["storage"] = storage

    @builtins.property
    def enabled(self) -> builtins.bool:
        '''
        :schema: KotsApiIdentityconfigsSpec#enabled
        '''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(builtins.bool, result)

    @builtins.property
    def admin_console_address(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiIdentityconfigsSpec#adminConsoleAddress
        '''
        result = self._values.get("admin_console_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ca_cert_pem_base64(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiIdentityconfigsSpec#caCertPemBase64
        '''
        result = self._values.get("ca_cert_pem_base64")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_id(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiIdentityconfigsSpec#clientID
        '''
        result = self._values.get("client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_secret(
        self,
    ) -> typing.Optional["KotsApiIdentityconfigsSpecClientSecret"]:
        '''
        :schema: KotsApiIdentityconfigsSpec#clientSecret
        '''
        result = self._values.get("client_secret")
        return typing.cast(typing.Optional["KotsApiIdentityconfigsSpecClientSecret"], result)

    @builtins.property
    def dex_connectors(
        self,
    ) -> typing.Optional["KotsApiIdentityconfigsSpecDexConnectors"]:
        '''
        :schema: KotsApiIdentityconfigsSpec#dexConnectors
        '''
        result = self._values.get("dex_connectors")
        return typing.cast(typing.Optional["KotsApiIdentityconfigsSpecDexConnectors"], result)

    @builtins.property
    def disable_password_auth(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: KotsApiIdentityconfigsSpec#disablePasswordAuth
        '''
        result = self._values.get("disable_password_auth")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def groups(
        self,
    ) -> typing.Optional[typing.List["KotsApiIdentityconfigsSpecGroups"]]:
        '''
        :schema: KotsApiIdentityconfigsSpec#groups
        '''
        result = self._values.get("groups")
        return typing.cast(typing.Optional[typing.List["KotsApiIdentityconfigsSpecGroups"]], result)

    @builtins.property
    def identity_service_address(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiIdentityconfigsSpec#identityServiceAddress
        '''
        result = self._values.get("identity_service_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ingress_config(
        self,
    ) -> typing.Optional["KotsApiIdentityconfigsSpecIngressConfig"]:
        '''
        :schema: KotsApiIdentityconfigsSpec#ingressConfig
        '''
        result = self._values.get("ingress_config")
        return typing.cast(typing.Optional["KotsApiIdentityconfigsSpecIngressConfig"], result)

    @builtins.property
    def insecure_skip_tls_verify(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: KotsApiIdentityconfigsSpec#insecureSkipTLSVerify
        '''
        result = self._values.get("insecure_skip_tls_verify")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def storage(self) -> typing.Optional["KotsApiIdentityconfigsSpecStorage"]:
        '''
        :schema: KotsApiIdentityconfigsSpec#storage
        '''
        result = self._values.get("storage")
        return typing.cast(typing.Optional["KotsApiIdentityconfigsSpecStorage"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KotsApiIdentityconfigsSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kots.KotsApiIdentityconfigsSpecClientSecret",
    jsii_struct_bases=[],
    name_mapping={"value": "value", "value_encrypted": "valueEncrypted"},
)
class KotsApiIdentityconfigsSpecClientSecret:
    def __init__(
        self,
        *,
        value: typing.Optional[builtins.str] = None,
        value_encrypted: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param value: 
        :param value_encrypted: 

        :schema: KotsApiIdentityconfigsSpecClientSecret
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if value is not None:
            self._values["value"] = value
        if value_encrypted is not None:
            self._values["value_encrypted"] = value_encrypted

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiIdentityconfigsSpecClientSecret#value
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value_encrypted(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiIdentityconfigsSpecClientSecret#valueEncrypted
        '''
        result = self._values.get("value_encrypted")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KotsApiIdentityconfigsSpecClientSecret(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kots.KotsApiIdentityconfigsSpecDexConnectors",
    jsii_struct_bases=[],
    name_mapping={
        "value": "value",
        "value_encrypted": "valueEncrypted",
        "value_from": "valueFrom",
    },
)
class KotsApiIdentityconfigsSpecDexConnectors:
    def __init__(
        self,
        *,
        value: typing.Optional[typing.Sequence["KotsApiIdentityconfigsSpecDexConnectorsValue"]] = None,
        value_encrypted: typing.Optional[builtins.str] = None,
        value_from: typing.Optional["KotsApiIdentityconfigsSpecDexConnectorsValueFrom"] = None,
    ) -> None:
        '''
        :param value: 
        :param value_encrypted: 
        :param value_from: 

        :schema: KotsApiIdentityconfigsSpecDexConnectors
        '''
        if isinstance(value_from, dict):
            value_from = KotsApiIdentityconfigsSpecDexConnectorsValueFrom(**value_from)
        self._values: typing.Dict[str, typing.Any] = {}
        if value is not None:
            self._values["value"] = value
        if value_encrypted is not None:
            self._values["value_encrypted"] = value_encrypted
        if value_from is not None:
            self._values["value_from"] = value_from

    @builtins.property
    def value(
        self,
    ) -> typing.Optional[typing.List["KotsApiIdentityconfigsSpecDexConnectorsValue"]]:
        '''
        :schema: KotsApiIdentityconfigsSpecDexConnectors#value
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[typing.List["KotsApiIdentityconfigsSpecDexConnectorsValue"]], result)

    @builtins.property
    def value_encrypted(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiIdentityconfigsSpecDexConnectors#valueEncrypted
        '''
        result = self._values.get("value_encrypted")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value_from(
        self,
    ) -> typing.Optional["KotsApiIdentityconfigsSpecDexConnectorsValueFrom"]:
        '''
        :schema: KotsApiIdentityconfigsSpecDexConnectors#valueFrom
        '''
        result = self._values.get("value_from")
        return typing.cast(typing.Optional["KotsApiIdentityconfigsSpecDexConnectorsValueFrom"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KotsApiIdentityconfigsSpecDexConnectors(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kots.KotsApiIdentityconfigsSpecDexConnectorsValue",
    jsii_struct_bases=[],
    name_mapping={"config": "config", "id": "id", "name": "name", "type": "type"},
)
class KotsApiIdentityconfigsSpecDexConnectorsValue:
    def __init__(
        self,
        *,
        config: typing.Any,
        id: builtins.str,
        name: builtins.str,
        type: builtins.str,
    ) -> None:
        '''
        :param config: 
        :param id: 
        :param name: 
        :param type: 

        :schema: KotsApiIdentityconfigsSpecDexConnectorsValue
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "config": config,
            "id": id,
            "name": name,
            "type": type,
        }

    @builtins.property
    def config(self) -> typing.Any:
        '''
        :schema: KotsApiIdentityconfigsSpecDexConnectorsValue#config
        '''
        result = self._values.get("config")
        assert result is not None, "Required property 'config' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def id(self) -> builtins.str:
        '''
        :schema: KotsApiIdentityconfigsSpecDexConnectorsValue#id
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''
        :schema: KotsApiIdentityconfigsSpecDexConnectorsValue#name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: KotsApiIdentityconfigsSpecDexConnectorsValue#type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KotsApiIdentityconfigsSpecDexConnectorsValue(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kots.KotsApiIdentityconfigsSpecDexConnectorsValueFrom",
    jsii_struct_bases=[],
    name_mapping={"secret_key_ref": "secretKeyRef"},
)
class KotsApiIdentityconfigsSpecDexConnectorsValueFrom:
    def __init__(
        self,
        *,
        secret_key_ref: typing.Optional["KotsApiIdentityconfigsSpecDexConnectorsValueFromSecretKeyRef"] = None,
    ) -> None:
        '''
        :param secret_key_ref: SecretKeySelector selects a key of a Secret.

        :schema: KotsApiIdentityconfigsSpecDexConnectorsValueFrom
        '''
        if isinstance(secret_key_ref, dict):
            secret_key_ref = KotsApiIdentityconfigsSpecDexConnectorsValueFromSecretKeyRef(**secret_key_ref)
        self._values: typing.Dict[str, typing.Any] = {}
        if secret_key_ref is not None:
            self._values["secret_key_ref"] = secret_key_ref

    @builtins.property
    def secret_key_ref(
        self,
    ) -> typing.Optional["KotsApiIdentityconfigsSpecDexConnectorsValueFromSecretKeyRef"]:
        '''SecretKeySelector selects a key of a Secret.

        :schema: KotsApiIdentityconfigsSpecDexConnectorsValueFrom#secretKeyRef
        '''
        result = self._values.get("secret_key_ref")
        return typing.cast(typing.Optional["KotsApiIdentityconfigsSpecDexConnectorsValueFromSecretKeyRef"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KotsApiIdentityconfigsSpecDexConnectorsValueFrom(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kots.KotsApiIdentityconfigsSpecDexConnectorsValueFromSecretKeyRef",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "name": "name", "optional": "optional"},
)
class KotsApiIdentityconfigsSpecDexConnectorsValueFromSecretKeyRef:
    def __init__(
        self,
        *,
        key: builtins.str,
        name: typing.Optional[builtins.str] = None,
        optional: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''SecretKeySelector selects a key of a Secret.

        :param key: The key of the secret to select from. Must be a valid secret key.
        :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
        :param optional: Specify whether the Secret or its key must be defined.

        :schema: KotsApiIdentityconfigsSpecDexConnectorsValueFromSecretKeyRef
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
        }
        if name is not None:
            self._values["name"] = name
        if optional is not None:
            self._values["optional"] = optional

    @builtins.property
    def key(self) -> builtins.str:
        '''The key of the secret to select from.

        Must be a valid secret key.

        :schema: KotsApiIdentityconfigsSpecDexConnectorsValueFromSecretKeyRef#key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent.

        More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?

        :schema: KotsApiIdentityconfigsSpecDexConnectorsValueFromSecretKeyRef#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def optional(self) -> typing.Optional[builtins.bool]:
        '''Specify whether the Secret or its key must be defined.

        :schema: KotsApiIdentityconfigsSpecDexConnectorsValueFromSecretKeyRef#optional
        '''
        result = self._values.get("optional")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KotsApiIdentityconfigsSpecDexConnectorsValueFromSecretKeyRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kots.KotsApiIdentityconfigsSpecGroups",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "role_ids": "roleIds"},
)
class KotsApiIdentityconfigsSpecGroups:
    def __init__(
        self,
        *,
        id: builtins.str,
        role_ids: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param id: 
        :param role_ids: 

        :schema: KotsApiIdentityconfigsSpecGroups
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "id": id,
            "role_ids": role_ids,
        }

    @builtins.property
    def id(self) -> builtins.str:
        '''
        :schema: KotsApiIdentityconfigsSpecGroups#id
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_ids(self) -> typing.List[builtins.str]:
        '''
        :schema: KotsApiIdentityconfigsSpecGroups#roleIds
        '''
        result = self._values.get("role_ids")
        assert result is not None, "Required property 'role_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KotsApiIdentityconfigsSpecGroups(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kots.KotsApiIdentityconfigsSpecIngressConfig",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "ingress": "ingress", "node_port": "nodePort"},
)
class KotsApiIdentityconfigsSpecIngressConfig:
    def __init__(
        self,
        *,
        enabled: builtins.bool,
        ingress: typing.Optional["KotsApiIdentityconfigsSpecIngressConfigIngress"] = None,
        node_port: typing.Optional["KotsApiIdentityconfigsSpecIngressConfigNodePort"] = None,
    ) -> None:
        '''
        :param enabled: 
        :param ingress: 
        :param node_port: 

        :schema: KotsApiIdentityconfigsSpecIngressConfig
        '''
        if isinstance(ingress, dict):
            ingress = KotsApiIdentityconfigsSpecIngressConfigIngress(**ingress)
        if isinstance(node_port, dict):
            node_port = KotsApiIdentityconfigsSpecIngressConfigNodePort(**node_port)
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
        }
        if ingress is not None:
            self._values["ingress"] = ingress
        if node_port is not None:
            self._values["node_port"] = node_port

    @builtins.property
    def enabled(self) -> builtins.bool:
        '''
        :schema: KotsApiIdentityconfigsSpecIngressConfig#enabled
        '''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(builtins.bool, result)

    @builtins.property
    def ingress(
        self,
    ) -> typing.Optional["KotsApiIdentityconfigsSpecIngressConfigIngress"]:
        '''
        :schema: KotsApiIdentityconfigsSpecIngressConfig#ingress
        '''
        result = self._values.get("ingress")
        return typing.cast(typing.Optional["KotsApiIdentityconfigsSpecIngressConfigIngress"], result)

    @builtins.property
    def node_port(
        self,
    ) -> typing.Optional["KotsApiIdentityconfigsSpecIngressConfigNodePort"]:
        '''
        :schema: KotsApiIdentityconfigsSpecIngressConfig#nodePort
        '''
        result = self._values.get("node_port")
        return typing.cast(typing.Optional["KotsApiIdentityconfigsSpecIngressConfigNodePort"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KotsApiIdentityconfigsSpecIngressConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kots.KotsApiIdentityconfigsSpecIngressConfigIngress",
    jsii_struct_bases=[],
    name_mapping={
        "host": "host",
        "path": "path",
        "annotations": "annotations",
        "tls_secret_name": "tlsSecretName",
    },
)
class KotsApiIdentityconfigsSpecIngressConfigIngress:
    def __init__(
        self,
        *,
        host: builtins.str,
        path: builtins.str,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tls_secret_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host: 
        :param path: 
        :param annotations: 
        :param tls_secret_name: 

        :schema: KotsApiIdentityconfigsSpecIngressConfigIngress
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "host": host,
            "path": path,
        }
        if annotations is not None:
            self._values["annotations"] = annotations
        if tls_secret_name is not None:
            self._values["tls_secret_name"] = tls_secret_name

    @builtins.property
    def host(self) -> builtins.str:
        '''
        :schema: KotsApiIdentityconfigsSpecIngressConfigIngress#host
        '''
        result = self._values.get("host")
        assert result is not None, "Required property 'host' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''
        :schema: KotsApiIdentityconfigsSpecIngressConfigIngress#path
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def annotations(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''
        :schema: KotsApiIdentityconfigsSpecIngressConfigIngress#annotations
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tls_secret_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiIdentityconfigsSpecIngressConfigIngress#tlsSecretName
        '''
        result = self._values.get("tls_secret_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KotsApiIdentityconfigsSpecIngressConfigIngress(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kots.KotsApiIdentityconfigsSpecIngressConfigNodePort",
    jsii_struct_bases=[],
    name_mapping={"port": "port"},
)
class KotsApiIdentityconfigsSpecIngressConfigNodePort:
    def __init__(self, *, port: jsii.Number) -> None:
        '''
        :param port: 

        :schema: KotsApiIdentityconfigsSpecIngressConfigNodePort
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "port": port,
        }

    @builtins.property
    def port(self) -> jsii.Number:
        '''
        :schema: KotsApiIdentityconfigsSpecIngressConfigNodePort#port
        '''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KotsApiIdentityconfigsSpecIngressConfigNodePort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kots.KotsApiIdentityconfigsSpecStorage",
    jsii_struct_bases=[],
    name_mapping={"postgres_config": "postgresConfig"},
)
class KotsApiIdentityconfigsSpecStorage:
    def __init__(
        self,
        *,
        postgres_config: typing.Optional["KotsApiIdentityconfigsSpecStoragePostgresConfig"] = None,
    ) -> None:
        '''
        :param postgres_config: 

        :schema: KotsApiIdentityconfigsSpecStorage
        '''
        if isinstance(postgres_config, dict):
            postgres_config = KotsApiIdentityconfigsSpecStoragePostgresConfig(**postgres_config)
        self._values: typing.Dict[str, typing.Any] = {}
        if postgres_config is not None:
            self._values["postgres_config"] = postgres_config

    @builtins.property
    def postgres_config(
        self,
    ) -> typing.Optional["KotsApiIdentityconfigsSpecStoragePostgresConfig"]:
        '''
        :schema: KotsApiIdentityconfigsSpecStorage#postgresConfig
        '''
        result = self._values.get("postgres_config")
        return typing.cast(typing.Optional["KotsApiIdentityconfigsSpecStoragePostgresConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KotsApiIdentityconfigsSpecStorage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kots.KotsApiIdentityconfigsSpecStoragePostgresConfig",
    jsii_struct_bases=[],
    name_mapping={
        "database": "database",
        "host": "host",
        "password": "password",
        "user": "user",
        "port": "port",
    },
)
class KotsApiIdentityconfigsSpecStoragePostgresConfig:
    def __init__(
        self,
        *,
        database: builtins.str,
        host: builtins.str,
        password: "KotsApiIdentityconfigsSpecStoragePostgresConfigPassword",
        user: builtins.str,
        port: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param database: 
        :param host: 
        :param password: 
        :param user: 
        :param port: 

        :schema: KotsApiIdentityconfigsSpecStoragePostgresConfig
        '''
        if isinstance(password, dict):
            password = KotsApiIdentityconfigsSpecStoragePostgresConfigPassword(**password)
        self._values: typing.Dict[str, typing.Any] = {
            "database": database,
            "host": host,
            "password": password,
            "user": user,
        }
        if port is not None:
            self._values["port"] = port

    @builtins.property
    def database(self) -> builtins.str:
        '''
        :schema: KotsApiIdentityconfigsSpecStoragePostgresConfig#database
        '''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def host(self) -> builtins.str:
        '''
        :schema: KotsApiIdentityconfigsSpecStoragePostgresConfig#host
        '''
        result = self._values.get("host")
        assert result is not None, "Required property 'host' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> "KotsApiIdentityconfigsSpecStoragePostgresConfigPassword":
        '''
        :schema: KotsApiIdentityconfigsSpecStoragePostgresConfig#password
        '''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast("KotsApiIdentityconfigsSpecStoragePostgresConfigPassword", result)

    @builtins.property
    def user(self) -> builtins.str:
        '''
        :schema: KotsApiIdentityconfigsSpecStoragePostgresConfig#user
        '''
        result = self._values.get("user")
        assert result is not None, "Required property 'user' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiIdentityconfigsSpecStoragePostgresConfig#port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KotsApiIdentityconfigsSpecStoragePostgresConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kots.KotsApiIdentityconfigsSpecStoragePostgresConfigPassword",
    jsii_struct_bases=[],
    name_mapping={"value": "value", "value_encrypted": "valueEncrypted"},
)
class KotsApiIdentityconfigsSpecStoragePostgresConfigPassword:
    def __init__(
        self,
        *,
        value: typing.Optional[builtins.str] = None,
        value_encrypted: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param value: 
        :param value_encrypted: 

        :schema: KotsApiIdentityconfigsSpecStoragePostgresConfigPassword
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if value is not None:
            self._values["value"] = value
        if value_encrypted is not None:
            self._values["value_encrypted"] = value_encrypted

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiIdentityconfigsSpecStoragePostgresConfigPassword#value
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value_encrypted(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiIdentityconfigsSpecStoragePostgresConfigPassword#valueEncrypted
        '''
        result = self._values.get("value_encrypted")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KotsApiIdentityconfigsSpecStoragePostgresConfigPassword(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kots.KotsApiIngressconfigsSpec",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "ingress": "ingress", "node_port": "nodePort"},
)
class KotsApiIngressconfigsSpec:
    def __init__(
        self,
        *,
        enabled: builtins.bool,
        ingress: typing.Optional["KotsApiIngressconfigsSpecIngress"] = None,
        node_port: typing.Optional["KotsApiIngressconfigsSpecNodePort"] = None,
    ) -> None:
        '''
        :param enabled: 
        :param ingress: 
        :param node_port: 

        :schema: KotsApiIngressconfigsSpec
        '''
        if isinstance(ingress, dict):
            ingress = KotsApiIngressconfigsSpecIngress(**ingress)
        if isinstance(node_port, dict):
            node_port = KotsApiIngressconfigsSpecNodePort(**node_port)
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
        }
        if ingress is not None:
            self._values["ingress"] = ingress
        if node_port is not None:
            self._values["node_port"] = node_port

    @builtins.property
    def enabled(self) -> builtins.bool:
        '''
        :schema: KotsApiIngressconfigsSpec#enabled
        '''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(builtins.bool, result)

    @builtins.property
    def ingress(self) -> typing.Optional["KotsApiIngressconfigsSpecIngress"]:
        '''
        :schema: KotsApiIngressconfigsSpec#ingress
        '''
        result = self._values.get("ingress")
        return typing.cast(typing.Optional["KotsApiIngressconfigsSpecIngress"], result)

    @builtins.property
    def node_port(self) -> typing.Optional["KotsApiIngressconfigsSpecNodePort"]:
        '''
        :schema: KotsApiIngressconfigsSpec#nodePort
        '''
        result = self._values.get("node_port")
        return typing.cast(typing.Optional["KotsApiIngressconfigsSpecNodePort"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KotsApiIngressconfigsSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kots.KotsApiIngressconfigsSpecIngress",
    jsii_struct_bases=[],
    name_mapping={
        "host": "host",
        "path": "path",
        "annotations": "annotations",
        "tls_secret_name": "tlsSecretName",
    },
)
class KotsApiIngressconfigsSpecIngress:
    def __init__(
        self,
        *,
        host: builtins.str,
        path: builtins.str,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tls_secret_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host: 
        :param path: 
        :param annotations: 
        :param tls_secret_name: 

        :schema: KotsApiIngressconfigsSpecIngress
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "host": host,
            "path": path,
        }
        if annotations is not None:
            self._values["annotations"] = annotations
        if tls_secret_name is not None:
            self._values["tls_secret_name"] = tls_secret_name

    @builtins.property
    def host(self) -> builtins.str:
        '''
        :schema: KotsApiIngressconfigsSpecIngress#host
        '''
        result = self._values.get("host")
        assert result is not None, "Required property 'host' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''
        :schema: KotsApiIngressconfigsSpecIngress#path
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def annotations(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''
        :schema: KotsApiIngressconfigsSpecIngress#annotations
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tls_secret_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiIngressconfigsSpecIngress#tlsSecretName
        '''
        result = self._values.get("tls_secret_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KotsApiIngressconfigsSpecIngress(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kots.KotsApiIngressconfigsSpecNodePort",
    jsii_struct_bases=[],
    name_mapping={"port": "port"},
)
class KotsApiIngressconfigsSpecNodePort:
    def __init__(self, *, port: jsii.Number) -> None:
        '''
        :param port: 

        :schema: KotsApiIngressconfigsSpecNodePort
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "port": port,
        }

    @builtins.property
    def port(self) -> jsii.Number:
        '''
        :schema: KotsApiIngressconfigsSpecNodePort#port
        '''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KotsApiIngressconfigsSpecNodePort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kots.KotsApiInstallationSpec",
    jsii_struct_bases=[],
    name_mapping={
        "channel_id": "channelId",
        "channel_name": "channelName",
        "encryption_key": "encryptionKey",
        "known_images": "knownImages",
        "released_at": "releasedAt",
        "release_notes": "releaseNotes",
        "update_cursor": "updateCursor",
        "version_label": "versionLabel",
        "yaml_errors": "yamlErrors",
    },
)
class KotsApiInstallationSpec:
    def __init__(
        self,
        *,
        channel_id: typing.Optional[builtins.str] = None,
        channel_name: typing.Optional[builtins.str] = None,
        encryption_key: typing.Optional[builtins.str] = None,
        known_images: typing.Optional[typing.Sequence["KotsApiInstallationSpecKnownImages"]] = None,
        released_at: typing.Optional[datetime.datetime] = None,
        release_notes: typing.Optional[builtins.str] = None,
        update_cursor: typing.Optional[builtins.str] = None,
        version_label: typing.Optional[builtins.str] = None,
        yaml_errors: typing.Optional[typing.Sequence["KotsApiInstallationSpecYamlErrors"]] = None,
    ) -> None:
        '''InstallationSpec defines the desired state of InstallationSpec.

        :param channel_id: 
        :param channel_name: 
        :param encryption_key: 
        :param known_images: 
        :param released_at: 
        :param release_notes: 
        :param update_cursor: 
        :param version_label: 
        :param yaml_errors: 

        :schema: KotsApiInstallationSpec
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if channel_id is not None:
            self._values["channel_id"] = channel_id
        if channel_name is not None:
            self._values["channel_name"] = channel_name
        if encryption_key is not None:
            self._values["encryption_key"] = encryption_key
        if known_images is not None:
            self._values["known_images"] = known_images
        if released_at is not None:
            self._values["released_at"] = released_at
        if release_notes is not None:
            self._values["release_notes"] = release_notes
        if update_cursor is not None:
            self._values["update_cursor"] = update_cursor
        if version_label is not None:
            self._values["version_label"] = version_label
        if yaml_errors is not None:
            self._values["yaml_errors"] = yaml_errors

    @builtins.property
    def channel_id(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiInstallationSpec#channelID
        '''
        result = self._values.get("channel_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def channel_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiInstallationSpec#channelName
        '''
        result = self._values.get("channel_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_key(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiInstallationSpec#encryptionKey
        '''
        result = self._values.get("encryption_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def known_images(
        self,
    ) -> typing.Optional[typing.List["KotsApiInstallationSpecKnownImages"]]:
        '''
        :schema: KotsApiInstallationSpec#knownImages
        '''
        result = self._values.get("known_images")
        return typing.cast(typing.Optional[typing.List["KotsApiInstallationSpecKnownImages"]], result)

    @builtins.property
    def released_at(self) -> typing.Optional[datetime.datetime]:
        '''
        :schema: KotsApiInstallationSpec#releasedAt
        '''
        result = self._values.get("released_at")
        return typing.cast(typing.Optional[datetime.datetime], result)

    @builtins.property
    def release_notes(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiInstallationSpec#releaseNotes
        '''
        result = self._values.get("release_notes")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update_cursor(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiInstallationSpec#updateCursor
        '''
        result = self._values.get("update_cursor")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_label(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiInstallationSpec#versionLabel
        '''
        result = self._values.get("version_label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def yaml_errors(
        self,
    ) -> typing.Optional[typing.List["KotsApiInstallationSpecYamlErrors"]]:
        '''
        :schema: KotsApiInstallationSpec#yamlErrors
        '''
        result = self._values.get("yaml_errors")
        return typing.cast(typing.Optional[typing.List["KotsApiInstallationSpecYamlErrors"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KotsApiInstallationSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kots.KotsApiInstallationSpecKnownImages",
    jsii_struct_bases=[],
    name_mapping={"image": "image", "is_private": "isPrivate"},
)
class KotsApiInstallationSpecKnownImages:
    def __init__(
        self,
        *,
        image: typing.Optional[builtins.str] = None,
        is_private: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param image: 
        :param is_private: 

        :schema: KotsApiInstallationSpecKnownImages
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if image is not None:
            self._values["image"] = image
        if is_private is not None:
            self._values["is_private"] = is_private

    @builtins.property
    def image(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiInstallationSpecKnownImages#image
        '''
        result = self._values.get("image")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_private(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: KotsApiInstallationSpecKnownImages#isPrivate
        '''
        result = self._values.get("is_private")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KotsApiInstallationSpecKnownImages(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kots.KotsApiInstallationSpecYamlErrors",
    jsii_struct_bases=[],
    name_mapping={"path": "path", "error": "error"},
)
class KotsApiInstallationSpecYamlErrors:
    def __init__(
        self,
        *,
        path: builtins.str,
        error: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param path: 
        :param error: 

        :schema: KotsApiInstallationSpecYamlErrors
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "path": path,
        }
        if error is not None:
            self._values["error"] = error

    @builtins.property
    def path(self) -> builtins.str:
        '''
        :schema: KotsApiInstallationSpecYamlErrors#path
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def error(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiInstallationSpecYamlErrors#error
        '''
        result = self._values.get("error")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KotsApiInstallationSpecYamlErrors(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kots.KotsApiLicenseSpec",
    jsii_struct_bases=[],
    name_mapping={
        "app_slug": "appSlug",
        "license_id": "licenseId",
        "signature": "signature",
        "channel_id": "channelId",
        "channel_name": "channelName",
        "customer_name": "customerName",
        "endpoint": "endpoint",
        "entitlements": "entitlements",
        "is_airgap_supported": "isAirgapSupported",
        "is_geoaxis_supported": "isGeoaxisSupported",
        "is_git_ops_supported": "isGitOpsSupported",
        "is_identity_service_supported": "isIdentityServiceSupported",
        "is_snapshot_supported": "isSnapshotSupported",
        "is_support_bundle_upload_supported": "isSupportBundleUploadSupported",
        "license_sequence": "licenseSequence",
        "license_type": "licenseType",
    },
)
class KotsApiLicenseSpec:
    def __init__(
        self,
        *,
        app_slug: builtins.str,
        license_id: builtins.str,
        signature: builtins.str,
        channel_id: typing.Optional[builtins.str] = None,
        channel_name: typing.Optional[builtins.str] = None,
        customer_name: typing.Optional[builtins.str] = None,
        endpoint: typing.Optional[builtins.str] = None,
        entitlements: typing.Optional[typing.Mapping[builtins.str, "KotsApiLicenseSpecEntitlements"]] = None,
        is_airgap_supported: typing.Optional[builtins.bool] = None,
        is_geoaxis_supported: typing.Optional[builtins.bool] = None,
        is_git_ops_supported: typing.Optional[builtins.bool] = None,
        is_identity_service_supported: typing.Optional[builtins.bool] = None,
        is_snapshot_supported: typing.Optional[builtins.bool] = None,
        is_support_bundle_upload_supported: typing.Optional[builtins.bool] = None,
        license_sequence: typing.Optional[jsii.Number] = None,
        license_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''LicenseSpec defines the desired state of LicenseSpec.

        :param app_slug: 
        :param license_id: 
        :param signature: 
        :param channel_id: 
        :param channel_name: 
        :param customer_name: 
        :param endpoint: 
        :param entitlements: 
        :param is_airgap_supported: 
        :param is_geoaxis_supported: 
        :param is_git_ops_supported: 
        :param is_identity_service_supported: 
        :param is_snapshot_supported: 
        :param is_support_bundle_upload_supported: 
        :param license_sequence: 
        :param license_type: 

        :schema: KotsApiLicenseSpec
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "app_slug": app_slug,
            "license_id": license_id,
            "signature": signature,
        }
        if channel_id is not None:
            self._values["channel_id"] = channel_id
        if channel_name is not None:
            self._values["channel_name"] = channel_name
        if customer_name is not None:
            self._values["customer_name"] = customer_name
        if endpoint is not None:
            self._values["endpoint"] = endpoint
        if entitlements is not None:
            self._values["entitlements"] = entitlements
        if is_airgap_supported is not None:
            self._values["is_airgap_supported"] = is_airgap_supported
        if is_geoaxis_supported is not None:
            self._values["is_geoaxis_supported"] = is_geoaxis_supported
        if is_git_ops_supported is not None:
            self._values["is_git_ops_supported"] = is_git_ops_supported
        if is_identity_service_supported is not None:
            self._values["is_identity_service_supported"] = is_identity_service_supported
        if is_snapshot_supported is not None:
            self._values["is_snapshot_supported"] = is_snapshot_supported
        if is_support_bundle_upload_supported is not None:
            self._values["is_support_bundle_upload_supported"] = is_support_bundle_upload_supported
        if license_sequence is not None:
            self._values["license_sequence"] = license_sequence
        if license_type is not None:
            self._values["license_type"] = license_type

    @builtins.property
    def app_slug(self) -> builtins.str:
        '''
        :schema: KotsApiLicenseSpec#appSlug
        '''
        result = self._values.get("app_slug")
        assert result is not None, "Required property 'app_slug' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def license_id(self) -> builtins.str:
        '''
        :schema: KotsApiLicenseSpec#licenseID
        '''
        result = self._values.get("license_id")
        assert result is not None, "Required property 'license_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def signature(self) -> builtins.str:
        '''
        :schema: KotsApiLicenseSpec#signature
        '''
        result = self._values.get("signature")
        assert result is not None, "Required property 'signature' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def channel_id(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiLicenseSpec#channelID
        '''
        result = self._values.get("channel_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def channel_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiLicenseSpec#channelName
        '''
        result = self._values.get("channel_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def customer_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiLicenseSpec#customerName
        '''
        result = self._values.get("customer_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def endpoint(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiLicenseSpec#endpoint
        '''
        result = self._values.get("endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def entitlements(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, "KotsApiLicenseSpecEntitlements"]]:
        '''
        :schema: KotsApiLicenseSpec#entitlements
        '''
        result = self._values.get("entitlements")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, "KotsApiLicenseSpecEntitlements"]], result)

    @builtins.property
    def is_airgap_supported(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: KotsApiLicenseSpec#isAirgapSupported
        '''
        result = self._values.get("is_airgap_supported")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def is_geoaxis_supported(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: KotsApiLicenseSpec#isGeoaxisSupported
        '''
        result = self._values.get("is_geoaxis_supported")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def is_git_ops_supported(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: KotsApiLicenseSpec#isGitOpsSupported
        '''
        result = self._values.get("is_git_ops_supported")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def is_identity_service_supported(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: KotsApiLicenseSpec#isIdentityServiceSupported
        '''
        result = self._values.get("is_identity_service_supported")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def is_snapshot_supported(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: KotsApiLicenseSpec#isSnapshotSupported
        '''
        result = self._values.get("is_snapshot_supported")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def is_support_bundle_upload_supported(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: KotsApiLicenseSpec#isSupportBundleUploadSupported
        '''
        result = self._values.get("is_support_bundle_upload_supported")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def license_sequence(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: KotsApiLicenseSpec#licenseSequence
        '''
        result = self._values.get("license_sequence")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def license_type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiLicenseSpec#licenseType
        '''
        result = self._values.get("license_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KotsApiLicenseSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kots.KotsApiLicenseSpecEntitlements",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "is_hidden": "isHidden",
        "title": "title",
        "value": "value",
        "value_type": "valueType",
    },
)
class KotsApiLicenseSpecEntitlements:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        is_hidden: typing.Optional[builtins.bool] = None,
        title: typing.Optional[builtins.str] = None,
        value: typing.Any = None,
        value_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param description: 
        :param is_hidden: 
        :param title: 
        :param value: 
        :param value_type: 

        :schema: KotsApiLicenseSpecEntitlements
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if is_hidden is not None:
            self._values["is_hidden"] = is_hidden
        if title is not None:
            self._values["title"] = title
        if value is not None:
            self._values["value"] = value
        if value_type is not None:
            self._values["value_type"] = value_type

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiLicenseSpecEntitlements#description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_hidden(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: KotsApiLicenseSpecEntitlements#isHidden
        '''
        result = self._values.get("is_hidden")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiLicenseSpecEntitlements#title
        '''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Any:
        '''
        :schema: KotsApiLicenseSpecEntitlements#value
        '''
        result = self._values.get("value")
        return typing.cast(typing.Any, result)

    @builtins.property
    def value_type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KotsApiLicenseSpecEntitlements#valueType
        '''
        result = self._values.get("value_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KotsApiLicenseSpecEntitlements(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Kotsairgap1(
    cdk8s.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kots.Kotsairgap1",
):
    '''Airgap is the Schema for the airgap API.

    :schema: kots.api.airgap
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        metadata: typing.Any = None,
        spec: typing.Optional[KotsApiAirgapSpec] = None,
    ) -> None:
        '''Defines a "kots.api.airgap" API object.

        :param scope: the scope in which to define this object.
        :param id: a scope-local name for the object.
        :param metadata: 
        :param spec: AirgapSpec defines the desired state of AirgapSpec.
        '''
        props = Kotsairgap1Props(metadata=metadata, spec=spec)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="manifest") # type: ignore[misc]
    @builtins.classmethod
    def manifest(
        cls,
        *,
        metadata: typing.Any = None,
        spec: typing.Optional[KotsApiAirgapSpec] = None,
    ) -> typing.Any:
        '''Renders a Kubernetes manifest for "kots.api.airgap".

        This can be used to inline resource manifests inside other objects (e.g. as templates).

        :param metadata: 
        :param spec: AirgapSpec defines the desired state of AirgapSpec.
        '''
        props = Kotsairgap1Props(metadata=metadata, spec=spec)

        return typing.cast(typing.Any, jsii.sinvoke(cls, "manifest", [props]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.Any:
        '''Renders the object to Kubernetes JSON.'''
        return typing.cast(typing.Any, jsii.invoke(self, "toJson", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="GVK")
    def GVK(cls) -> cdk8s.GroupVersionKind:
        '''Returns the apiVersion and kind for "kots.api.airgap".'''
        return typing.cast(cdk8s.GroupVersionKind, jsii.sget(cls, "GVK"))


@jsii.data_type(
    jsii_type="kots.Kotsairgap1Props",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata", "spec": "spec"},
)
class Kotsairgap1Props:
    def __init__(
        self,
        *,
        metadata: typing.Any = None,
        spec: typing.Optional[KotsApiAirgapSpec] = None,
    ) -> None:
        '''Airgap is the Schema for the airgap API.

        :param metadata: 
        :param spec: AirgapSpec defines the desired state of AirgapSpec.

        :schema: kots.api.airgap
        '''
        if isinstance(spec, dict):
            spec = KotsApiAirgapSpec(**spec)
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if spec is not None:
            self._values["spec"] = spec

    @builtins.property
    def metadata(self) -> typing.Any:
        '''
        :schema: kots.api.airgap#metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Any, result)

    @builtins.property
    def spec(self) -> typing.Optional[KotsApiAirgapSpec]:
        '''AirgapSpec defines the desired state of AirgapSpec.

        :schema: kots.api.airgap#spec
        '''
        result = self._values.get("spec")
        return typing.cast(typing.Optional[KotsApiAirgapSpec], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kotsairgap1Props(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Kotsapplication1(
    cdk8s.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kots.Kotsapplication1",
):
    '''Application is the Schema for the application API.

    :schema: kots.api.application
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        metadata: typing.Any = None,
        spec: typing.Optional[KotsApiApplicationSpec] = None,
    ) -> None:
        '''Defines a "kots.api.application" API object.

        :param scope: the scope in which to define this object.
        :param id: a scope-local name for the object.
        :param metadata: 
        :param spec: ApplicationSpec defines the desired state of ApplicationSpec.
        '''
        props = Kotsapplication1Props(metadata=metadata, spec=spec)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="manifest") # type: ignore[misc]
    @builtins.classmethod
    def manifest(
        cls,
        *,
        metadata: typing.Any = None,
        spec: typing.Optional[KotsApiApplicationSpec] = None,
    ) -> typing.Any:
        '''Renders a Kubernetes manifest for "kots.api.application".

        This can be used to inline resource manifests inside other objects (e.g. as templates).

        :param metadata: 
        :param spec: ApplicationSpec defines the desired state of ApplicationSpec.
        '''
        props = Kotsapplication1Props(metadata=metadata, spec=spec)

        return typing.cast(typing.Any, jsii.sinvoke(cls, "manifest", [props]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.Any:
        '''Renders the object to Kubernetes JSON.'''
        return typing.cast(typing.Any, jsii.invoke(self, "toJson", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="GVK")
    def GVK(cls) -> cdk8s.GroupVersionKind:
        '''Returns the apiVersion and kind for "kots.api.application".'''
        return typing.cast(cdk8s.GroupVersionKind, jsii.sget(cls, "GVK"))


@jsii.data_type(
    jsii_type="kots.Kotsapplication1Props",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata", "spec": "spec"},
)
class Kotsapplication1Props:
    def __init__(
        self,
        *,
        metadata: typing.Any = None,
        spec: typing.Optional[KotsApiApplicationSpec] = None,
    ) -> None:
        '''Application is the Schema for the application API.

        :param metadata: 
        :param spec: ApplicationSpec defines the desired state of ApplicationSpec.

        :schema: kots.api.application
        '''
        if isinstance(spec, dict):
            spec = KotsApiApplicationSpec(**spec)
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if spec is not None:
            self._values["spec"] = spec

    @builtins.property
    def metadata(self) -> typing.Any:
        '''
        :schema: kots.api.application#metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Any, result)

    @builtins.property
    def spec(self) -> typing.Optional[KotsApiApplicationSpec]:
        '''ApplicationSpec defines the desired state of ApplicationSpec.

        :schema: kots.api.application#spec
        '''
        result = self._values.get("spec")
        return typing.cast(typing.Optional[KotsApiApplicationSpec], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kotsapplication1Props(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Kotsconfig1(
    cdk8s.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kots.Kotsconfig1",
):
    '''Config is the Schema for the config API.

    :schema: kots.api.config
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        metadata: typing.Any = None,
        spec: typing.Optional[KotsApiConfigSpec] = None,
    ) -> None:
        '''Defines a "kots.api.config" API object.

        :param scope: the scope in which to define this object.
        :param id: a scope-local name for the object.
        :param metadata: 
        :param spec: ConfigSpec defines the desired state of ConfigSpec.
        '''
        props = Kotsconfig1Props(metadata=metadata, spec=spec)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="manifest") # type: ignore[misc]
    @builtins.classmethod
    def manifest(
        cls,
        *,
        metadata: typing.Any = None,
        spec: typing.Optional[KotsApiConfigSpec] = None,
    ) -> typing.Any:
        '''Renders a Kubernetes manifest for "kots.api.config".

        This can be used to inline resource manifests inside other objects (e.g. as templates).

        :param metadata: 
        :param spec: ConfigSpec defines the desired state of ConfigSpec.
        '''
        props = Kotsconfig1Props(metadata=metadata, spec=spec)

        return typing.cast(typing.Any, jsii.sinvoke(cls, "manifest", [props]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.Any:
        '''Renders the object to Kubernetes JSON.'''
        return typing.cast(typing.Any, jsii.invoke(self, "toJson", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="GVK")
    def GVK(cls) -> cdk8s.GroupVersionKind:
        '''Returns the apiVersion and kind for "kots.api.config".'''
        return typing.cast(cdk8s.GroupVersionKind, jsii.sget(cls, "GVK"))


@jsii.data_type(
    jsii_type="kots.Kotsconfig1Props",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata", "spec": "spec"},
)
class Kotsconfig1Props:
    def __init__(
        self,
        *,
        metadata: typing.Any = None,
        spec: typing.Optional[KotsApiConfigSpec] = None,
    ) -> None:
        '''Config is the Schema for the config API.

        :param metadata: 
        :param spec: ConfigSpec defines the desired state of ConfigSpec.

        :schema: kots.api.config
        '''
        if isinstance(spec, dict):
            spec = KotsApiConfigSpec(**spec)
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if spec is not None:
            self._values["spec"] = spec

    @builtins.property
    def metadata(self) -> typing.Any:
        '''
        :schema: kots.api.config#metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Any, result)

    @builtins.property
    def spec(self) -> typing.Optional[KotsApiConfigSpec]:
        '''ConfigSpec defines the desired state of ConfigSpec.

        :schema: kots.api.config#spec
        '''
        result = self._values.get("spec")
        return typing.cast(typing.Optional[KotsApiConfigSpec], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kotsconfig1Props(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Kotsconfigvalues1(
    cdk8s.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kots.Kotsconfigvalues1",
):
    '''App is the Schema for the app API.

    :schema: kots.api.configvalues
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        metadata: typing.Any = None,
        spec: typing.Optional[KotsApiConfigvaluesSpec] = None,
    ) -> None:
        '''Defines a "kots.api.configvalues" API object.

        :param scope: the scope in which to define this object.
        :param id: a scope-local name for the object.
        :param metadata: 
        :param spec: ConfigValuesSpec defines the desired state of ConfigValue.
        '''
        props = Kotsconfigvalues1Props(metadata=metadata, spec=spec)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="manifest") # type: ignore[misc]
    @builtins.classmethod
    def manifest(
        cls,
        *,
        metadata: typing.Any = None,
        spec: typing.Optional[KotsApiConfigvaluesSpec] = None,
    ) -> typing.Any:
        '''Renders a Kubernetes manifest for "kots.api.configvalues".

        This can be used to inline resource manifests inside other objects (e.g. as templates).

        :param metadata: 
        :param spec: ConfigValuesSpec defines the desired state of ConfigValue.
        '''
        props = Kotsconfigvalues1Props(metadata=metadata, spec=spec)

        return typing.cast(typing.Any, jsii.sinvoke(cls, "manifest", [props]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.Any:
        '''Renders the object to Kubernetes JSON.'''
        return typing.cast(typing.Any, jsii.invoke(self, "toJson", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="GVK")
    def GVK(cls) -> cdk8s.GroupVersionKind:
        '''Returns the apiVersion and kind for "kots.api.configvalues".'''
        return typing.cast(cdk8s.GroupVersionKind, jsii.sget(cls, "GVK"))


@jsii.data_type(
    jsii_type="kots.Kotsconfigvalues1Props",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata", "spec": "spec"},
)
class Kotsconfigvalues1Props:
    def __init__(
        self,
        *,
        metadata: typing.Any = None,
        spec: typing.Optional[KotsApiConfigvaluesSpec] = None,
    ) -> None:
        '''App is the Schema for the app API.

        :param metadata: 
        :param spec: ConfigValuesSpec defines the desired state of ConfigValue.

        :schema: kots.api.configvalues
        '''
        if isinstance(spec, dict):
            spec = KotsApiConfigvaluesSpec(**spec)
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if spec is not None:
            self._values["spec"] = spec

    @builtins.property
    def metadata(self) -> typing.Any:
        '''
        :schema: kots.api.configvalues#metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Any, result)

    @builtins.property
    def spec(self) -> typing.Optional[KotsApiConfigvaluesSpec]:
        '''ConfigValuesSpec defines the desired state of ConfigValue.

        :schema: kots.api.configvalues#spec
        '''
        result = self._values.get("spec")
        return typing.cast(typing.Optional[KotsApiConfigvaluesSpec], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kotsconfigvalues1Props(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Kotshelmchart1(
    cdk8s.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kots.Kotshelmchart1",
):
    '''HelmChart is the Schema for the helmchart API.

    :schema: kots.api.helmchart
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        metadata: typing.Any = None,
        spec: typing.Optional[KotsApiHelmchartSpec] = None,
    ) -> None:
        '''Defines a "kots.api.helmchart" API object.

        :param scope: the scope in which to define this object.
        :param id: a scope-local name for the object.
        :param metadata: 
        :param spec: HelmChartSpec defines the desired state of HelmChartSpec.
        '''
        props = Kotshelmchart1Props(metadata=metadata, spec=spec)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="manifest") # type: ignore[misc]
    @builtins.classmethod
    def manifest(
        cls,
        *,
        metadata: typing.Any = None,
        spec: typing.Optional[KotsApiHelmchartSpec] = None,
    ) -> typing.Any:
        '''Renders a Kubernetes manifest for "kots.api.helmchart".

        This can be used to inline resource manifests inside other objects (e.g. as templates).

        :param metadata: 
        :param spec: HelmChartSpec defines the desired state of HelmChartSpec.
        '''
        props = Kotshelmchart1Props(metadata=metadata, spec=spec)

        return typing.cast(typing.Any, jsii.sinvoke(cls, "manifest", [props]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.Any:
        '''Renders the object to Kubernetes JSON.'''
        return typing.cast(typing.Any, jsii.invoke(self, "toJson", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="GVK")
    def GVK(cls) -> cdk8s.GroupVersionKind:
        '''Returns the apiVersion and kind for "kots.api.helmchart".'''
        return typing.cast(cdk8s.GroupVersionKind, jsii.sget(cls, "GVK"))


@jsii.data_type(
    jsii_type="kots.Kotshelmchart1Props",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata", "spec": "spec"},
)
class Kotshelmchart1Props:
    def __init__(
        self,
        *,
        metadata: typing.Any = None,
        spec: typing.Optional[KotsApiHelmchartSpec] = None,
    ) -> None:
        '''HelmChart is the Schema for the helmchart API.

        :param metadata: 
        :param spec: HelmChartSpec defines the desired state of HelmChartSpec.

        :schema: kots.api.helmchart
        '''
        if isinstance(spec, dict):
            spec = KotsApiHelmchartSpec(**spec)
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if spec is not None:
            self._values["spec"] = spec

    @builtins.property
    def metadata(self) -> typing.Any:
        '''
        :schema: kots.api.helmchart#metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Any, result)

    @builtins.property
    def spec(self) -> typing.Optional[KotsApiHelmchartSpec]:
        '''HelmChartSpec defines the desired state of HelmChartSpec.

        :schema: kots.api.helmchart#spec
        '''
        result = self._values.get("spec")
        return typing.cast(typing.Optional[KotsApiHelmchartSpec], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kotshelmchart1Props(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Kotsidentity1(
    cdk8s.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kots.Kotsidentity1",
):
    '''Identity is the Schema for the identity document.

    :schema: kots.api.identity
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        metadata: typing.Any = None,
        spec: typing.Optional[KotsApiIdentitySpec] = None,
    ) -> None:
        '''Defines a "kots.api.identity" API object.

        :param scope: the scope in which to define this object.
        :param id: a scope-local name for the object.
        :param metadata: 
        :param spec: 
        '''
        props = Kotsidentity1Props(metadata=metadata, spec=spec)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="manifest") # type: ignore[misc]
    @builtins.classmethod
    def manifest(
        cls,
        *,
        metadata: typing.Any = None,
        spec: typing.Optional[KotsApiIdentitySpec] = None,
    ) -> typing.Any:
        '''Renders a Kubernetes manifest for "kots.api.identity".

        This can be used to inline resource manifests inside other objects (e.g. as templates).

        :param metadata: 
        :param spec: 
        '''
        props = Kotsidentity1Props(metadata=metadata, spec=spec)

        return typing.cast(typing.Any, jsii.sinvoke(cls, "manifest", [props]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.Any:
        '''Renders the object to Kubernetes JSON.'''
        return typing.cast(typing.Any, jsii.invoke(self, "toJson", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="GVK")
    def GVK(cls) -> cdk8s.GroupVersionKind:
        '''Returns the apiVersion and kind for "kots.api.identity".'''
        return typing.cast(cdk8s.GroupVersionKind, jsii.sget(cls, "GVK"))


@jsii.data_type(
    jsii_type="kots.Kotsidentity1Props",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata", "spec": "spec"},
)
class Kotsidentity1Props:
    def __init__(
        self,
        *,
        metadata: typing.Any = None,
        spec: typing.Optional[KotsApiIdentitySpec] = None,
    ) -> None:
        '''Identity is the Schema for the identity document.

        :param metadata: 
        :param spec: 

        :schema: kots.api.identity
        '''
        if isinstance(spec, dict):
            spec = KotsApiIdentitySpec(**spec)
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if spec is not None:
            self._values["spec"] = spec

    @builtins.property
    def metadata(self) -> typing.Any:
        '''
        :schema: kots.api.identity#metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Any, result)

    @builtins.property
    def spec(self) -> typing.Optional[KotsApiIdentitySpec]:
        '''
        :schema: kots.api.identity#spec
        '''
        result = self._values.get("spec")
        return typing.cast(typing.Optional[KotsApiIdentitySpec], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kotsidentity1Props(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Kotsidentityconfigs1(
    cdk8s.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kots.Kotsidentityconfigs1",
):
    '''IdentityConfig is the Schema for the identity config document.

    :schema: kots.api.identityconfigs
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        metadata: typing.Any = None,
        spec: typing.Optional[KotsApiIdentityconfigsSpec] = None,
    ) -> None:
        '''Defines a "kots.api.identityconfigs" API object.

        :param scope: the scope in which to define this object.
        :param id: a scope-local name for the object.
        :param metadata: 
        :param spec: 
        '''
        props = Kotsidentityconfigs1Props(metadata=metadata, spec=spec)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="manifest") # type: ignore[misc]
    @builtins.classmethod
    def manifest(
        cls,
        *,
        metadata: typing.Any = None,
        spec: typing.Optional[KotsApiIdentityconfigsSpec] = None,
    ) -> typing.Any:
        '''Renders a Kubernetes manifest for "kots.api.identityconfigs".

        This can be used to inline resource manifests inside other objects (e.g. as templates).

        :param metadata: 
        :param spec: 
        '''
        props = Kotsidentityconfigs1Props(metadata=metadata, spec=spec)

        return typing.cast(typing.Any, jsii.sinvoke(cls, "manifest", [props]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.Any:
        '''Renders the object to Kubernetes JSON.'''
        return typing.cast(typing.Any, jsii.invoke(self, "toJson", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="GVK")
    def GVK(cls) -> cdk8s.GroupVersionKind:
        '''Returns the apiVersion and kind for "kots.api.identityconfigs".'''
        return typing.cast(cdk8s.GroupVersionKind, jsii.sget(cls, "GVK"))


@jsii.data_type(
    jsii_type="kots.Kotsidentityconfigs1Props",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata", "spec": "spec"},
)
class Kotsidentityconfigs1Props:
    def __init__(
        self,
        *,
        metadata: typing.Any = None,
        spec: typing.Optional[KotsApiIdentityconfigsSpec] = None,
    ) -> None:
        '''IdentityConfig is the Schema for the identity config document.

        :param metadata: 
        :param spec: 

        :schema: kots.api.identityconfigs
        '''
        if isinstance(spec, dict):
            spec = KotsApiIdentityconfigsSpec(**spec)
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if spec is not None:
            self._values["spec"] = spec

    @builtins.property
    def metadata(self) -> typing.Any:
        '''
        :schema: kots.api.identityconfigs#metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Any, result)

    @builtins.property
    def spec(self) -> typing.Optional[KotsApiIdentityconfigsSpec]:
        '''
        :schema: kots.api.identityconfigs#spec
        '''
        result = self._values.get("spec")
        return typing.cast(typing.Optional[KotsApiIdentityconfigsSpec], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kotsidentityconfigs1Props(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Kotsingressconfigs1(
    cdk8s.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kots.Kotsingressconfigs1",
):
    '''IngressConfig is the Schema for the ingress config document.

    :schema: kots.api.ingressconfigs
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        metadata: typing.Any = None,
        spec: typing.Optional[KotsApiIngressconfigsSpec] = None,
    ) -> None:
        '''Defines a "kots.api.ingressconfigs" API object.

        :param scope: the scope in which to define this object.
        :param id: a scope-local name for the object.
        :param metadata: 
        :param spec: 
        '''
        props = Kotsingressconfigs1Props(metadata=metadata, spec=spec)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="manifest") # type: ignore[misc]
    @builtins.classmethod
    def manifest(
        cls,
        *,
        metadata: typing.Any = None,
        spec: typing.Optional[KotsApiIngressconfigsSpec] = None,
    ) -> typing.Any:
        '''Renders a Kubernetes manifest for "kots.api.ingressconfigs".

        This can be used to inline resource manifests inside other objects (e.g. as templates).

        :param metadata: 
        :param spec: 
        '''
        props = Kotsingressconfigs1Props(metadata=metadata, spec=spec)

        return typing.cast(typing.Any, jsii.sinvoke(cls, "manifest", [props]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.Any:
        '''Renders the object to Kubernetes JSON.'''
        return typing.cast(typing.Any, jsii.invoke(self, "toJson", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="GVK")
    def GVK(cls) -> cdk8s.GroupVersionKind:
        '''Returns the apiVersion and kind for "kots.api.ingressconfigs".'''
        return typing.cast(cdk8s.GroupVersionKind, jsii.sget(cls, "GVK"))


@jsii.data_type(
    jsii_type="kots.Kotsingressconfigs1Props",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata", "spec": "spec"},
)
class Kotsingressconfigs1Props:
    def __init__(
        self,
        *,
        metadata: typing.Any = None,
        spec: typing.Optional[KotsApiIngressconfigsSpec] = None,
    ) -> None:
        '''IngressConfig is the Schema for the ingress config document.

        :param metadata: 
        :param spec: 

        :schema: kots.api.ingressconfigs
        '''
        if isinstance(spec, dict):
            spec = KotsApiIngressconfigsSpec(**spec)
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if spec is not None:
            self._values["spec"] = spec

    @builtins.property
    def metadata(self) -> typing.Any:
        '''
        :schema: kots.api.ingressconfigs#metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Any, result)

    @builtins.property
    def spec(self) -> typing.Optional[KotsApiIngressconfigsSpec]:
        '''
        :schema: kots.api.ingressconfigs#spec
        '''
        result = self._values.get("spec")
        return typing.cast(typing.Optional[KotsApiIngressconfigsSpec], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kotsingressconfigs1Props(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Kotsinstallation1(
    cdk8s.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kots.Kotsinstallation1",
):
    '''Installation is the Schema for the installation API.

    :schema: kots.api.installation
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        metadata: typing.Any = None,
        spec: typing.Optional[KotsApiInstallationSpec] = None,
    ) -> None:
        '''Defines a "kots.api.installation" API object.

        :param scope: the scope in which to define this object.
        :param id: a scope-local name for the object.
        :param metadata: 
        :param spec: InstallationSpec defines the desired state of InstallationSpec.
        '''
        props = Kotsinstallation1Props(metadata=metadata, spec=spec)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="manifest") # type: ignore[misc]
    @builtins.classmethod
    def manifest(
        cls,
        *,
        metadata: typing.Any = None,
        spec: typing.Optional[KotsApiInstallationSpec] = None,
    ) -> typing.Any:
        '''Renders a Kubernetes manifest for "kots.api.installation".

        This can be used to inline resource manifests inside other objects (e.g. as templates).

        :param metadata: 
        :param spec: InstallationSpec defines the desired state of InstallationSpec.
        '''
        props = Kotsinstallation1Props(metadata=metadata, spec=spec)

        return typing.cast(typing.Any, jsii.sinvoke(cls, "manifest", [props]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.Any:
        '''Renders the object to Kubernetes JSON.'''
        return typing.cast(typing.Any, jsii.invoke(self, "toJson", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="GVK")
    def GVK(cls) -> cdk8s.GroupVersionKind:
        '''Returns the apiVersion and kind for "kots.api.installation".'''
        return typing.cast(cdk8s.GroupVersionKind, jsii.sget(cls, "GVK"))


@jsii.data_type(
    jsii_type="kots.Kotsinstallation1Props",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata", "spec": "spec"},
)
class Kotsinstallation1Props:
    def __init__(
        self,
        *,
        metadata: typing.Any = None,
        spec: typing.Optional[KotsApiInstallationSpec] = None,
    ) -> None:
        '''Installation is the Schema for the installation API.

        :param metadata: 
        :param spec: InstallationSpec defines the desired state of InstallationSpec.

        :schema: kots.api.installation
        '''
        if isinstance(spec, dict):
            spec = KotsApiInstallationSpec(**spec)
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if spec is not None:
            self._values["spec"] = spec

    @builtins.property
    def metadata(self) -> typing.Any:
        '''
        :schema: kots.api.installation#metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Any, result)

    @builtins.property
    def spec(self) -> typing.Optional[KotsApiInstallationSpec]:
        '''InstallationSpec defines the desired state of InstallationSpec.

        :schema: kots.api.installation#spec
        '''
        result = self._values.get("spec")
        return typing.cast(typing.Optional[KotsApiInstallationSpec], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kotsinstallation1Props(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Kotslicense1(
    cdk8s.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kots.Kotslicense1",
):
    '''License is the Schema for the license API.

    :schema: kots.api.license
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        metadata: typing.Any = None,
        spec: typing.Optional[KotsApiLicenseSpec] = None,
    ) -> None:
        '''Defines a "kots.api.license" API object.

        :param scope: the scope in which to define this object.
        :param id: a scope-local name for the object.
        :param metadata: 
        :param spec: LicenseSpec defines the desired state of LicenseSpec.
        '''
        props = Kotslicense1Props(metadata=metadata, spec=spec)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="manifest") # type: ignore[misc]
    @builtins.classmethod
    def manifest(
        cls,
        *,
        metadata: typing.Any = None,
        spec: typing.Optional[KotsApiLicenseSpec] = None,
    ) -> typing.Any:
        '''Renders a Kubernetes manifest for "kots.api.license".

        This can be used to inline resource manifests inside other objects (e.g. as templates).

        :param metadata: 
        :param spec: LicenseSpec defines the desired state of LicenseSpec.
        '''
        props = Kotslicense1Props(metadata=metadata, spec=spec)

        return typing.cast(typing.Any, jsii.sinvoke(cls, "manifest", [props]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.Any:
        '''Renders the object to Kubernetes JSON.'''
        return typing.cast(typing.Any, jsii.invoke(self, "toJson", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="GVK")
    def GVK(cls) -> cdk8s.GroupVersionKind:
        '''Returns the apiVersion and kind for "kots.api.license".'''
        return typing.cast(cdk8s.GroupVersionKind, jsii.sget(cls, "GVK"))


@jsii.data_type(
    jsii_type="kots.Kotslicense1Props",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata", "spec": "spec"},
)
class Kotslicense1Props:
    def __init__(
        self,
        *,
        metadata: typing.Any = None,
        spec: typing.Optional[KotsApiLicenseSpec] = None,
    ) -> None:
        '''License is the Schema for the license API.

        :param metadata: 
        :param spec: LicenseSpec defines the desired state of LicenseSpec.

        :schema: kots.api.license
        '''
        if isinstance(spec, dict):
            spec = KotsApiLicenseSpec(**spec)
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if spec is not None:
            self._values["spec"] = spec

    @builtins.property
    def metadata(self) -> typing.Any:
        '''
        :schema: kots.api.license#metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Any, result)

    @builtins.property
    def spec(self) -> typing.Optional[KotsApiLicenseSpec]:
        '''LicenseSpec defines the desired state of LicenseSpec.

        :schema: kots.api.license#spec
        '''
        result = self._values.get("spec")
        return typing.cast(typing.Optional[KotsApiLicenseSpec], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kotslicense1Props(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "KotsApiAirgapSpec",
    "KotsApiApplicationSpec",
    "KotsApiApplicationSpecGraphs",
    "KotsApiApplicationSpecGraphsQueries",
    "KotsApiApplicationSpecPorts",
    "KotsApiConfigSpec",
    "KotsApiConfigSpecGroups",
    "KotsApiConfigSpecGroupsItems",
    "KotsApiConfigSpecGroupsItemsDefault",
    "KotsApiConfigSpecGroupsItemsItems",
    "KotsApiConfigSpecGroupsItemsItemsDefault",
    "KotsApiConfigSpecGroupsItemsItemsValue",
    "KotsApiConfigSpecGroupsItemsTemplates",
    "KotsApiConfigSpecGroupsItemsValue",
    "KotsApiConfigSpecGroupsItemsWhen",
    "KotsApiConfigSpecGroupsWhen",
    "KotsApiConfigvaluesSpec",
    "KotsApiConfigvaluesSpecValues",
    "KotsApiHelmchartSpec",
    "KotsApiHelmchartSpecChart",
    "KotsApiHelmchartSpecExclude",
    "KotsApiHelmchartSpecOptionalValues",
    "KotsApiIdentitySpec",
    "KotsApiIdentitySpecRequireIdentityProvider",
    "KotsApiIdentitySpecRoles",
    "KotsApiIdentitySpecWebConfig",
    "KotsApiIdentitySpecWebConfigTheme",
    "KotsApiIdentityconfigsSpec",
    "KotsApiIdentityconfigsSpecClientSecret",
    "KotsApiIdentityconfigsSpecDexConnectors",
    "KotsApiIdentityconfigsSpecDexConnectorsValue",
    "KotsApiIdentityconfigsSpecDexConnectorsValueFrom",
    "KotsApiIdentityconfigsSpecDexConnectorsValueFromSecretKeyRef",
    "KotsApiIdentityconfigsSpecGroups",
    "KotsApiIdentityconfigsSpecIngressConfig",
    "KotsApiIdentityconfigsSpecIngressConfigIngress",
    "KotsApiIdentityconfigsSpecIngressConfigNodePort",
    "KotsApiIdentityconfigsSpecStorage",
    "KotsApiIdentityconfigsSpecStoragePostgresConfig",
    "KotsApiIdentityconfigsSpecStoragePostgresConfigPassword",
    "KotsApiIngressconfigsSpec",
    "KotsApiIngressconfigsSpecIngress",
    "KotsApiIngressconfigsSpecNodePort",
    "KotsApiInstallationSpec",
    "KotsApiInstallationSpecKnownImages",
    "KotsApiInstallationSpecYamlErrors",
    "KotsApiLicenseSpec",
    "KotsApiLicenseSpecEntitlements",
    "Kotsairgap1",
    "Kotsairgap1Props",
    "Kotsapplication1",
    "Kotsapplication1Props",
    "Kotsconfig1",
    "Kotsconfig1Props",
    "Kotsconfigvalues1",
    "Kotsconfigvalues1Props",
    "Kotshelmchart1",
    "Kotshelmchart1Props",
    "Kotsidentity1",
    "Kotsidentity1Props",
    "Kotsidentityconfigs1",
    "Kotsidentityconfigs1Props",
    "Kotsingressconfigs1",
    "Kotsingressconfigs1Props",
    "Kotsinstallation1",
    "Kotsinstallation1Props",
    "Kotslicense1",
    "Kotslicense1Props",
]

publication.publish()
