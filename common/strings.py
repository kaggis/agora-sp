

# Error codes
OWNER_NOT_FOUND = 1
SERVICE_NOT_FOUND = 2
INVALID_UUID = 3
SERVICE_COMPONENTS_IMPLEMENTATION_NONMATCHING_UUID = 4
SERVICE_COMPONENT_INVALID_UUID = 5
SERVICE_DETAILS_NOT_FOUND = 6
SERVICE_COMPONENT_NO_IMPLEMENTATIONS = 7
SERVICE_COMPONENT_NOT_FOUND = 8
SERVICE_COMPONENT_IMPLEMENTATION_INVALID_UUID = 9
SERVICE_COMPONENT_IMPLEMENTATION_DETAILS_NOT_FOUND = 10
SLA_INVALID_UUID = 11
SLA_NOT_FOUND = 12
SLA_SERVICE_DETAILS_MISMATCH = 13
SLA_PARAMETER_INVALID_UUID = 14
SERVICE_DETAILS_OPTIONS_NOT_FOUND = 15
PAGE_NOT_FOUND = 16
SLA_PARAMETER_NOT_FOUND = 17
INVALID_QUERY_PARAMETER = 18
SERVICE_COMPONENT_NAME_NOT_PROVIDED = 19
SERVICE_COMPONENT_NAME_EMPTY = 20
SERVICE_COMPONENT_DESCRIPTION_NOT_PROVIDED = 21
SERVICE_COMPONENT_UUID_EXISTS = 22
SERVICE_COMPONENT_IMPLEMENTATION_NAME_NOT_PROVIDED = 23
SERVICE_COMPONENT_IMPLEMENTATION_NAME_EMPTY = 24
SERVICE_COMPONENT_IMPLEMENTATION_DESCRIPTION_NOT_PROVIDED = 25
SERVICE_COMPONENT_IMPLEMENTATION_UUID_EXISTS = 26
SERVICE_COMPONENT_IMPLEMENTATION_DETAIL_VERSION_NOT_PROVIDED = 27
SERVICE_COMPONENT_IMPLEMENTATION_DETAIL_CONFIGURATION_PARAMETERS_NOT_PROVIDED = 28
SERVICE_COMPONENT_IMPLEMENTATION_DETAIL_VERSION_EMPTY = 29
SERVICE_COMPONENT_IMPLEMENTATION_DETAIL_INVALID_UUID = 30
SERVICE_COMPONENT_IMPLEMENTATION_DETAILS_UUID_EXISTS = 31
SERVICE_COMPONENT_IMPLEMENTATION_NOT_FOUND = 32
SERVICE_COMPONENT_IMPLEMENTATION_DETAILS_UUID_NOT_PROVIDED = 33
SERVICE_DETAILS_COMPONENT_EXISTS = 34
EXTERNAL_SERVICE_NAME_NOT_PROVIDED = 35
EXTERNAL_SERVICE_NAME_EMPTY = 36
EXTERNAL_SERVICE_INVALID_UUID = 37
EXTERNAL_SERVICE_UUID_EXISTS = 38
SERVICE_DEPENDENCY_UUID_NOT_PROVIDED = 39
SERVICE_DEPENDENCY_INVALID_UUID = 40
SERVICE_DEPENDENCY_NOT_FOUND = 41
SERVICE_DEPENDENCY_EXISTS = 42
EXTERNAL_SERVICE_DEPENDENCY_UUID_NOT_PROVIDED = 43
EXTERNAL_SERVICE_DEPENDENCY_INVALID_UUID = 44
EXTERNAL_SERVICE_DEPENDENCY_NOT_FOUND = 45
EXTERNAL_SERVICE_DEPENDENCY_EXISTS = 46
EXTERNAL_SERVICE_DEPENDENCY_INSERTED = 47
USER_CUSTOMER_NAME_NOT_PROVIDED = 48
USER_CUSTOMER_ROLE_EMPTY = 49
USER_CUSTOMER_ROLE_NOT_PROVIDED = 50
USER_CUSTOMER_NAME_INVALID = 51
USER_CUSTOMER_INVALID_UUID = 52
USER_CUSTOMER_EXISTS = 53
SERVICE_NAME_NOT_PROVIDED = 54
SERVICE_OWNER_UUID_NOT_PROVIDED = 55
SERVICE_CONTACT_INFORMATION_UUID_NOT_PROVIDED = 56
SERVICE_NAME_EMPTY = 57
SERVICE_OWNER_INVALID_UUID = 58
SERVICE_CONTACT_INFORMATION_INVALID_UUID = 59
SERVICE_INVALID_UUID = 60
SERVICE_UUID_EXISTS = 61
SERVICE_OWNER_NOT_FOUND = 62
CONTACT_INFORMATION_NOT_FOUND = 63

# Info codes
SERVICE_OWNER_INSTITUTION = 1
SERVICE_OWNER_INFORMATION = 2
SERVICE_COMPONENTS_INFORMATION = 3
SERVICE_COMPONENT_IMPLEMENTATIONS_INFORMATION = 4
SERVICE_COMPONENT_IMPLEMENTATION_DETAILS = 5
SLA_INFORMATION = 6
SLA_PARAMETER_INFORMATION = 7
SERVICE_OPTIONS = 8
SERVICE_LIST = 9
SERVICE_INFORMATION = 10
SERVICE_DETAIL_INFORMATION = 11
SERVICE_DEPENDENCIES_INFORMATION = 12
SERVICE_EXTERNAL_DEPENDENCIES_INFORMATION = 13
SERVICE_COMPONENT_INSERTED = 14
SERVICE_COMPONENT_IMPLEMENTATION_INSERTED = 15
SERVICE_COMPONENT_IMPLEMENTATION_DETAILS_INSERTED = 16
SERVICE_DETAILS_COMPONENT_INSERTED = 17
EXTERNAL_SERVICE_INSERTED = 18
SERVICE_DEPENDENCY_INSERTED = 19
USER_CUSTOMER_INSERTED = 20
SERVICE_INSERTED = 21

# Status codes
OK_200 = 0
NOT_FOUND_404 = 1
NO_CONTENT_204 = 2
CREATED_201 = 3
FORBIDDEN_403 = 4
REJECTED_405 = 5
CONFLICT_409 = 6