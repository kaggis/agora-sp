# COLUMNS = ('collection', 'action', 'role', 'filter', 'check' 'fields', 'comment')
from agora import spec


def service_version_limited():
    service_version_all = []
    for (field, flags) in spec.SERVICE_VERSIONS['fields'].items():
        if '.flag.nowrite' not in flags:
            service_version_all.append(field)

    service_version_excluded = [
        'is_in_catalogue',
        'visible_to_marketplace'
    ]

    service_version_chosen = [x for x in service_version_all
                                if x not in service_version_excluded]
    return ','.join(service_version_chosen)


def get_rules():
    rules = [
        ('api/v2/services', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/services', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/services', 'list', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/services', 'list', 'observer', '*', '*', '*', '*'),
        ('api/v2/services', 'list', 'anonymous', '*', '*', '*', '*'),
        ('api/v2/services', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/services', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/services', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/services', 'retrieve', 'observer', '*', '*', '*', '*'),
        ('api/v2/services', 'retrieve', 'anonymous', '*', '*', '*', '*'),
        ('api/v2/services', 'create', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/services', 'create', 'admin', '*', '*', '*', '*'),
        ('api/v2/services', 'create', 'serviceadmin', '*', 'organisation_owned', '*', '*'),
        ('api/v2/services', 'update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/services', 'update', 'admin', '*', '*', '*', '*'),
        ('api/v2/services', 'update', 'serviceadmin', '*', 'owned', '*','*'),
        ('api/v2/services', 'partial_update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/services', 'partial_update', 'admin', '*', '*', '*', '*'),
        ('api/v2/services', 'partial_update', 'serviceadmin', '*', 'owned', '*','*'),
        ('api/v2/services', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/services', 'delete', 'superadmin', '*', '*', '*', '*'),

        ('api/v2/ext-services', 'list', 'anonymous', '*', '*', '*', '*'),
        ('api/v2/ext-services', 'retrieve', 'anonymous', '*', '*', '*', '*'),

        ('api/v2/service-types', 'list', 'anonymous', '*', '*', '*', '*'),
        ('api/v2/service-types', 'retrieve', 'anonymous', '*', '*', '*', '*'),

        ('api/v2/my-services', 'list', 'serviceadmin', 'filter_owned', '*', '*', '*'),
        ('api/v2/my-services', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),

        ('api/v2/service-trls', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/service-trls', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/service-trls', 'list', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/service-trls', 'list', 'observer', '*', '*', '*', '*'),
        ('api/v2/service-trls', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/service-trls', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/service-trls', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/service-trls', 'retrieve', 'observer', '*', '*', '*', '*'),
        ('api/v2/service-trls', 'create', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/service-trls', 'create', 'admin', '*', '*', '*', '*'),
        ('api/v2/service-trls', 'update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/service-trls', 'update', 'admin', '*', '*', '*', '*'),
        ('api/v2/service-trls', 'partial_update', 'admin', '*', '*', '*', '*'),
        ('api/v2/service-trls', 'partial_update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/service-trls', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/service-trls', 'delete', 'superadmin', '*', '*', '*', '*'),

        ('api/v2/service-categories', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/service-categories', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/service-categories', 'list', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/service-categories', 'list', 'observer', '*', '*', '*', '*'),
        ('api/v2/service-categories', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/service-categories', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/service-categories', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/service-categories', 'retrieve', 'observer', '*', '*', '*', '*'),
        ('api/v2/service-categories', 'create', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/service-categories', 'create', 'admin', '*', '*', '*', '*'),
        ('api/v2/service-categories', 'update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/service-categories', 'update', 'admin', '*', '*', '*', '*'),
        ('api/v2/service-categories', 'partial_update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/service-categories', 'partial_update', 'admin', '*', '*', '*', '*'),
        ('api/v2/service-categories', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/service-categories', 'delete', 'superadmin', '*', '*', '*', '*'),

        ('api/v2/institutions', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/institutions', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/institutions', 'list', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/institutions', 'list', 'observer', '*', '*', '*', '*'),
        ('api/v2/institutions', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/institutions', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/institutions', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/institutions', 'retrieve', 'observer', '*', '*', '*', '*'),
        ('api/v2/institutions', 'create', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/institutions', 'create', 'admin', '*', '*', '*', '*'),
        ('api/v2/institutions', 'update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/institutions', 'update', 'admin', '*', '*', '*', '*'),
        ('api/v2/institutions', 'partial_update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/institutions', 'partial_update', 'admin', '*', '*', '*', '*'),
        ('api/v2/institutions', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/institutions', 'delete', 'superadmin', '*', '*', '*', '*'),

        ('api/v2/user-roles', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/user-roles', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/user-roles', 'list', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/user-roles', 'list', 'observer', '*', '*', '*', '*'),
        ('api/v2/user-roles', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/user-roles', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/user-roles', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/user-roles', 'retrieve', 'observer', '*', '*', '*', '*'),
        ('api/v2/user-roles', 'create', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/user-roles', 'create', 'admin', '*', '*', '*', '*'),
        ('api/v2/user-roles', 'update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/user-roles', 'update', 'admin', '*', '*', '*', '*'),
        ('api/v2/user-roles', 'partial_update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/user-roles', 'partial_update', 'admin', '*', '*', '*', '*'),
        ('api/v2/user-roles', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/user-roles', 'delete', 'superadmin', '*', '*', '*', '*'),

        ('api/v2/user-customers', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/user-customers', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/user-customers', 'list', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/user-customers', 'list', 'observer', '*', '*', '*', '*'),
        ('api/v2/user-customers', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/user-customers', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/user-customers', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/user-customers', 'retrieve', 'observer', '*', '*', '*', '*'),
        ('api/v2/user-customers', 'create', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/user-customers', 'create', 'admin', '*', '*', '*', '*'),
        ('api/v2/user-customers', 'update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/user-customers', 'update', 'admin', '*', '*', '*', '*'),
        ('api/v2/user-customers', 'partial_update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/user-customers', 'partial_update', 'admin', '*', '*', '*', '*'),
        ('api/v2/user-customers', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/user-customers', 'delete', 'superadmin', '*', '*', '*', '*'),

        ('api/v2/custom-users', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/custom-users', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/custom-users', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/custom-users', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/custom-users', 'retrieve', 'serviceadmin', 'me', '*', '*', '*'),
        ('api/v2/custom-users', 'update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/custom-users', 'update', 'admin', '*', '*', '*', '*'),
        ('api/v2/custom-users', 'partial_update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/custom-users', 'partial_update', 'admin', '*', '*', '*', '*'),
        ('api/v2/custom-users', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/custom-users', 'delete', 'superadmin', '*', '*', '*', '*'),

        ('api/v2/service-admins', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/service-admins', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/service-admins', 'list', 'serviceadmin', 'manages_or_self_pending', '*', '*', '*'),
        ('api/v2/service-admins', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/service-admins', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/service-admins', 'retrieve', 'serviceadmin', '*', 'is_involved', '*', '*'),
        ('api/v2/service-admins', 'create', 'superadmin', '*', 'check_create_other', 'service,admin', '*'),
        ('api/v2/service-admins', 'create', 'admin', '*', 'check_create_other', 'service,admin', '*'),
        ('api/v2/service-admins', 'create', 'serviceadmin', '*', 'check_create_self', 'service', '*'),
        ('api/v2/service-admins', 'partial_update', 'superadmin', '*', 'check_update', 'state', '*'),
        ('api/v2/service-admins', 'partial_update', 'admin', '*', 'check_update', 'state', '*'),
        ('api/v2/service-admins', 'partial_update', 'serviceadmin', 'manages', 'check_update', 'state', '*'),
        ('api/v2/service-admins', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/service-admins', 'delete', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/service-admins', 'destroy', 'serviceadmin', '*', 'self_pending', '*', '*'),
        ('api/v2/service-admins', 'delete', 'serviceadmin', '*', 'self_pending', '*', '*'),



        ('api/v2/contact-information', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/contact-information', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/contact-information', 'list', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/contact-information', 'list', 'observer', '*', '*', '*', '*'),
        ('api/v2/contact-information', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/contact-information', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/contact-information', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/contact-information', 'retrieve', 'observer', '*', '*', '*', '*'),
        ('api/v2/contact-information', 'create', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/contact-information', 'create', 'admin', '*', '*', '*', '*'),
        ('api/v2/contact-information', 'update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/contact-information', 'update', 'admin', '*', '*', '*', '*'),
        ('api/v2/contact-information', 'partial_update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/contact-information', 'partial_update', 'admin', '*', '*', '*', '*'),
        ('api/v2/contact-information', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/contact-information', 'delete', 'superadmin', '*', '*', '*', '*'),

        ('api/v2/contact_information_internal', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/contact_information_internal', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/contact_information_internal', 'list', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/contact_information_internal', 'list', 'observer', '*', '*', '*', '*'),
        ('api/v2/contact_information_internal', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/contact_information_internal', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/contact_information_internal', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/contact_information_internal', 'retrieve', 'observer', '*', '*', '*', '*'),
        ('api/v2/contact_information_internal', 'create', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/contact_information_internal', 'create', 'admin', '*', '*', '*', '*'),
        ('api/v2/contact_information_internal', 'update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/contact_information_internal', 'update', 'admin', '*', '*', '*', '*'),
        ('api/v2/contact_information_internal', 'partial_update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/contact_information_internal', 'partial_update', 'admin', '*', '*', '*', '*'),
        ('api/v2/contact_information_internal', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/contact_information_internal', 'delete', 'superadmin', '*', '*', '*', '*'),

        ('api/v2/users', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/users', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/users', 'list', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/users', 'list', 'observer', '*', '*', '*', '*'),
        ('api/v2/users', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/users', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/users', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/users', 'retrieve', 'observer', '*', '*', '*', '*'),
        ('api/v2/users', 'create', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/users', 'create', 'admin', '*', '*', '*', '*'),
        ('api/v2/users', 'update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/users', 'update', 'admin', '*', '*', '*', '*'),
        ('api/v2/users', 'partial_update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/users', 'partial_update', 'admin', '*', '*', '*', '*'),
        ('api/v2/users', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/users', 'delete', 'superadmin', '*', '*', '*', '*'),

        ('api/v2/service-versions', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/service-versions', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/service-versions', 'list', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/service-versions', 'list', 'observer', '*', '*', '*', '*'),
        ('api/v2/service-versions', 'list', 'anonymous', '*', '*', '*', '*'),
        ('api/v2/service-versions', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/service-versions', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/service-versions', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/service-versions', 'retrieve', 'observer', '*', '*', '*', '*'),
        ('api/v2/service-versions', 'retrieve', 'anonymous', '*', '*', '*', '*'),
        ('api/v2/service-versions', 'create', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/service-versions', 'create', 'admin', '*', '*', '*', '*'),
        ('api/v2/service-versions', 'create', 'serviceadmin', '*', 'create_owns_service', service_version_limited(), '*'),
        ('api/v2/service-versions', 'update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/service-versions', 'update', 'admin', '*', '*', '*', '*'),
        ('api/v2/service-versions', 'update', 'serviceadmin', '*', 'update_owns_service', service_version_limited(), '*'),
        ('api/v2/service-versions', 'partial_update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/service-versions', 'partial_update', 'admin', '*', '*', '*', '*'),
        ('api/v2/service-versions', 'partial_update', 'serviceadmin', '*', 'update_owns_service', service_version_limited(), '*'),
        ('api/v2/service-versions', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/service-versions', 'delete', 'superadmin', '*', '*', '*', '*'),

        ('api/v2/service-status', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/service-status', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/service-status', 'list', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/service-status', 'list', 'observer', '*', '*', '*', '*'),
        ('api/v2/service-status', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/service-status', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/service-status', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/service-status', 'retrieve', 'observer', '*', '*', '*', '*'),
        ('api/v2/service-status', 'create', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/service-status', 'create', 'admin', '*', '*', '*', '*'),
        ('api/v2/service-status', 'update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/service-status', 'update', 'admin', '*', '*', '*', '*'),
        ('api/v2/service-status', 'partial_update', 'admin', '*', '*', '*', '*'),
        ('api/v2/service-status', 'partial_update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/service-status', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/service-status', 'delete', 'superadmin', '*', '*', '*', '*'),

        ('api/v2/components', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/components', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/components', 'list', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/components', 'list', 'observer', '*', '*', '*', '*'),
        ('api/v2/components', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/components', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/components', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/components', 'retrieve', 'observer', '*', '*', '*', '*'),
        ('api/v2/components', 'create', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/components', 'create', 'admin', '*', '*', '*', '*'),
        ('api/v2/components', 'create', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/components', 'update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/components', 'update', 'admin', '*', '*', '*', '*'),
        ('api/v2/components', 'partial_update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/components', 'partial_update', 'admin', '*', '*', '*', '*'),
        ('api/v2/components', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/components', 'delete', 'superadmin', '*', '*', '*', '*'),

        ('api/v2/component-implementations', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/component-implementations', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/component-implementations', 'list', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/component-implementations', 'list', 'observer', '*', '*', '*', '*'),
        ('api/v2/component-implementations', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/component-implementations', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/component-implementations', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/component-implementations', 'retrieve', 'observer', '*', '*', '*', '*'),
        ('api/v2/component-implementations', 'create', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/component-implementations', 'create', 'admin', '*', '*', '*', '*'),
        ('api/v2/component-implementations', 'create', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/component-implementations', 'update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/component-implementations', 'update', 'admin', '*', '*', '*', '*'),
        ('api/v2/component-implementations', 'partial_update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/component-implementations', 'partial_update', 'admin', '*', '*', '*', '*'),
        ('api/v2/component-implementations', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/component-implementations', 'delete', 'superadmin', '*', '*', '*', '*'),

        ('api/v2/component-implementation-details', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/component-implementation-details', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/component-implementation-details', 'list', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/component-implementation-details', 'list', 'observer', '*', '*', '*', '*'),
        ('api/v2/component-implementation-details', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/component-implementation-details', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/component-implementation-details', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/component-implementation-details', 'retrieve', 'observer', '*', '*', '*', '*'),
        ('api/v2/component-implementation-details', 'create', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/component-implementation-details', 'create', 'admin', '*', '*', '*', '*'),
        ('api/v2/component-implementation-details', 'create', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/component-implementation-details', 'update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/component-implementation-details', 'update', 'admin', '*', '*', '*', '*'),
        ('api/v2/component-implementation-details', 'partial_update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/component-implementation-details', 'partial_update', 'admin', '*', '*', '*', '*'),
        ('api/v2/component-implementation-details', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/component-implementation-details', 'delete', 'superadmin', '*', '*', '*', '*'),

        ('api/v2/component-implementation-detail-links', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/component-implementation-detail-links', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/component-implementation-detail-links', 'list', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/component-implementation-detail-links', 'list', 'observer', '*', '*', '*', '*'),
        ('api/v2/component-implementation-detail-links', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/component-implementation-detail-links', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/component-implementation-detail-links', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/component-implementation-detail-links', 'retrieve', 'observer', '*', '*', '*', '*'),
        ('api/v2/component-implementation-detail-links', 'create', 'superadmin', '*', 'unique', '*', '*'),
        ('api/v2/component-implementation-detail-links', 'create', 'admin', '*', 'unique', '*', '*'),
        ('api/v2/component-implementation-detail-links', 'create', 'serviceadmin', '*', 'create_owns_service_unique', '*', '*'),
        ('api/v2/component-implementation-detail-links', 'update', 'superadmin', '*', 'update_unique', '*', '*'),
        ('api/v2/component-implementation-detail-links', 'update', 'admin', '*', 'update_unique', '*', '*'),
        ('api/v2/component-implementation-detail-links', 'update', 'serviceadmin', '*', 'update_owns_service_unique', '*', '*'),
        ('api/v2/component-implementation-detail-links', 'partial_update', 'superadmin', '*', 'update_unique', '*', '*'),
        ('api/v2/component-implementation-detail-links', 'partial_update', 'admin', '*', 'update_unique', '*', '*'),
        ('api/v2/component-implementation-detail-links', 'partial_update', 'serviceadmin', '*', 'update_owns_service_unique', '*', '*'),
        ('api/v2/component-implementation-detail-links', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/component-implementation-detail-links', 'delete', 'superadmin', '*', '*', '*', '*'),

        ('api/v2/providers', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/providers', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/providers', 'list', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/providers', 'list', 'observer', '*', '*', '*', '*'),
        ('api/v2/providers', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/providers', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/providers', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/providers', 'retrieve', 'observer', '*', '*', '*', '*'),
        ('api/v2/providers', 'create', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/providers', 'update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/providers', 'partial_update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/providers', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/providers', 'delete', 'superadmin', '*', '*', '*', '*'),

        ('api/v2/access-policies', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/access-policies', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/access-policies', 'list', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/access-policies', 'list', 'observer', '*', '*', '*', '*'),
        ('api/v2/access-policies', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/access-policies', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/access-policies', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/access-policies', 'retrieve', 'observer', '*', '*', '*', '*'),
        ('api/v2/access-policies', 'create', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/access-policies', 'create', 'admin', '*', '*', '*', '*'),
        ('api/v2/access-policies', 'create', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/access-policies', 'update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/access-policies', 'update', 'admin', '*', '*', '*', '*'),
        ('api/v2/access-policies', 'partial_update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/access-policies', 'partial_update', 'admin', '*', '*', '*', '*'),
        ('api/v2/access-policies', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/access-policies', 'delete', 'superadmin', '*', '*', '*', '*'),

        ('api/v2/federation-members', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/federation-members', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/federation-members', 'list', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/federation-members', 'list', 'observer', '*', '*', '*', '*'),
        ('api/v2/federation-members', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/federation-members', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/federation-members', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/federation-members', 'retrieve', 'observer', '*', '*', '*', '*'),
        ('api/v2/federation-members', 'create', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/federation-members', 'create', 'admin', '*', '*', '*', '*'),
        ('api/v2/federation-members', 'update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/federation-members', 'update', 'admin', '*', '*', '*', '*'),
        ('api/v2/federation-members', 'partial_update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/federation-members', 'partial_update', 'admin', '*', '*', '*', '*'),
        ('api/v2/federation-members', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/federation-members', 'delete', 'superadmin', '*', '*', '*', '*'),
    ]
    return rules
