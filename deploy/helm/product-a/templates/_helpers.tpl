{{- define "product-a-service.name" -}}
{{- .Chart.Name -}}
{{- end -}}

{{- define "product-a-service.fullname" -}}
{{- printf "%s-%s" .Release.Name .Chart.Name | trunc 63 | trimSuffix "-" -}}
{{- end -}}
