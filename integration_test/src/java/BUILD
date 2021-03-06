licenses(["notice"])

package(default_visibility = ["//visibility:public"])

filegroup(
    name = "test-data-files",
    srcs = glob(["org/apache/heron/integration_test/topology/**/*.json"]),
)

filegroup(
    name = "topology-test-data-files",
    srcs = glob(["org/apache/heron/integration_topology_test/topology/**/*.json"]),
)

java_library(
    name = "core",
    srcs = glob(
        ["org/apache/heron/integration_test/core/**/*.java"],
    ),
    deps = [
        "//heron/api/src/java:api-java",
        "//heron/api/src/java:api-java-low-level",
        "//storm-compatibility/src/java:storm-compatibility-java",
        "//heron/proto:proto_topology_java",
        "//third_party/java:jackson",
        "@commons_logging_commons_logging//jar",
        "@com_google_protobuf//:protobuf_java",
        "@org_apache_httpcomponents_http_client//jar",
        "@org_apache_httpcomponents_http_core//jar",
    ],
)

java_library(
    name = "common",
    srcs = glob(
        ["org/apache/heron/integration_test/common/**/*.java"],
    ),
    deps = [
        "//heron/api/src/java:api-java",
        "//heron/api/src/java:api-java-low-level",
        "//storm-compatibility/src/java:storm-compatibility-java",
        "//third_party/java:hadoop-core",
        "//third_party/java:jackson",
        "@commons_cli_commons_cli//jar",
        ":core"
    ],
)

java_library(
    name = "integration-tests-lib",
    srcs = glob(
       ["org/apache/heron/integration_test/topology/**/*.java"],
    ),
    deps = [
        "//heron/api/src/java:api-java",
        "//heron/api/src/java:api-java-low-level",
        "//storm-compatibility/src/java:storm-compatibility-java",
        "@com_googlecode_json_simple_json_simple//jar",
        "@commons_cli_commons_cli//jar",
        ":common",
        ":core"
    ],
)

java_library(
    name = "local-integration-tests-lib",
    srcs = glob(
       ["org/apache/heron/local_integration_test/topology/**/*.java"],
    ),
    deps = [
        "//heron/api/src/java:api-java",
        "//heron/api/src/java:api-java-low-level",
        "//storm-compatibility/src/java:storm-compatibility-java",
        ":common",
        ":core"
    ],
)

java_binary(
    name = "integration-tests-unshaded",
    srcs = glob(
       ["org/apache/heron/integration_test/topology/**/*.java"],
    ),
    deps = [
        "//heron/api/src/java:api-java",
        "//heron/api/src/java:api-java-low-level",
        "//storm-compatibility/src/java:storm-compatibility-java",
        "@commons_cli_commons_cli//jar",
        "@com_googlecode_json_simple_json_simple//jar",
        ":common",
        ":core"
    ],
)

genrule(
    name = "integration-tests",
    srcs = [":integration-tests-unshaded_deploy.jar"],
    outs = ["integration-tests.jar"],
    cmd = "cp $< $@",
)

java_binary(
    name = "local-integration-tests-unshaded",
    srcs = glob(
       ["org/apache/heron/local_integration_test/**/*.java"],
    ),
    deps = [
        "//heron/api/src/java:api-java",
        "//heron/api/src/java:api-java-low-level",
        "//storm-compatibility/src/java:storm-compatibility-java",
        ":common",
        ":core"
    ],
)

genrule(
    name = "local-integration-test",
    srcs = [":local-integration-tests-unshaded_deploy.jar"],
    outs = ["local-integration-tests.jar"],
    cmd = "cp $< $@",
)

java_library(
    name = "core-topology",
    srcs = glob(
        ["org/apache/heron/integration_topology_test/core/**/*.java"],
    ),
    deps = [
        "//heron/api/src/java:api-java",
        "//heron/api/src/java:api-java-low-level",
        "//storm-compatibility/src/java:storm-compatibility-java",
        "//heron/proto:proto_topology_java",
        "//third_party/java:jackson",
        "@commons_logging_commons_logging//jar",
        "@com_google_protobuf//:protobuf_java",
        "@org_apache_httpcomponents_http_client//jar",
        "@org_apache_httpcomponents_http_core//jar",
    ],
)

java_library(
    name = "common_topology_test",
    srcs = glob(
        ["org/apache/heron/integration_topology_test/common/**/*.java"],
    ),
    deps = [
        "//heron/api/src/java:api-java",
        "//heron/api/src/java:api-java-low-level",
        "//storm-compatibility/src/java:storm-compatibility-java",
        "//third_party/java:hadoop-core",
        "//third_party/java:jackson",
        "@commons_cli_commons_cli//jar",
        ":core",
        ":core-topology"
    ],
)

java_library(
    name = "integration-topology-tests-lib",
    srcs = glob(
       ["org/apache/heron/integration_topology_test/topology/**/*.java"],
    ),
    deps = [
        "//heron/api/src/java:api-java",
        "//heron/api/src/java:api-java-low-level",
        "//storm-compatibility/src/java:storm-compatibility-java",
        "@com_googlecode_json_simple_json_simple//jar",
        "@commons_cli_commons_cli//jar",
        ":common_topology_test",
        ":common",
        ":core",
        ":core-topology"
    ],
)

java_binary(
    name = "integration-topology-tests-unshaded",
    srcs = glob(
       ["org/apache/heron/integration_topology_test/topology/**/*.java"],
    ),
    deps = [
        "//heron/api/src/java:api-java",
        "//heron/api/src/java:api-java-low-level",
        "//storm-compatibility/src/java:storm-compatibility-java",
        "@commons_cli_commons_cli//jar",
        "@com_googlecode_json_simple_json_simple//jar",
        ":common_topology_test",
        ":common",
        ":core",
        ":core-topology"
    ],
)

genrule(
    name = "integration-topology-tests",
    srcs = [":integration-topology-tests-unshaded_deploy.jar"],
    outs = ["integration-topology-tests.jar"],
    cmd = "cp $< $@",
)
