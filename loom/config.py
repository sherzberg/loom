from fabric.api import env, run, settings, hide

# Default system user
env.user = 'ubuntu'

# Default puppet environment
env.environment = 'prod'

# Default puppet module directory
env.puppet_module_dir = 'modules/'

# Default puppet version
# If loom_puppet_version is None, loom installs the latest version
env.loom_puppet_version = '3.1.1'

# Default librarian version
# If loom_librarian_version is None, loom installs the latest version
env.loom_librarian_version = '0.9.9'

# Default puppet base class to be included on all site.pp. Example: roles::base
env.loom_puppet_base_class = None


def host_roles(host_string):
    """
    Returns the role of a given host string.
    """
    roles = []
    for role, hosts in env.roledefs.items():
        if host_string in hosts and role not in roles:
            roles.append(role)
    return roles


def current_roles():
    return host_roles(env.host_string)


def has_puppet_installed():
    with settings(hide('warnings', 'running', 'stdout', 'stderr'), warn_only=True):
        result = run('which puppet')
    return result.succeeded
