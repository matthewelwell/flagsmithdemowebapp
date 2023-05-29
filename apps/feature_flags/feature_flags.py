from flagsmith import Flagsmith
from flagsmith.models import DefaultFlag, Flags

flagsmith = None

DEFAULT_ENABLED_FLAG_NAMES = tuple()
DEFAULT_FLAG_VALUES = dict()


def default_handler(flag_name: str) -> DefaultFlag:
    enabled = flag_name in DEFAULT_ENABLED_FLAG_NAMES
    return DefaultFlag(enabled, DEFAULT_FLAG_VALUES.get(flag_name, None))


def get_flagsmith():
    global flagsmith

    if flagsmith is None:
        flagsmith = _init_flagsmith()

    return flagsmith


def _init_flagsmith() -> Flagsmith:
    return Flagsmith(
        environment_key="ser.GusXyQCcQ554THxLzR6x79",
        default_flag_handler=default_handler,
    )


def is_feature_enabled(flag_name: str, identifier: str = None, **traits) -> bool:
    flags = _get_flags(identifier, **traits)
    return flags.is_feature_enabled(flag_name)


def get_multiple_flag_statuses(flag_names: tuple[str], identifier: str = None, **traits) -> tuple[bool]:
    flags = _get_flags(identifier, **traits)
    all_flags = flags.all_flags()

    results = []
    for flag in all_flags:
        if flag.feature_name in flag_names:
            results.append(flag.enabled)

    return tuple(results)


def _get_flags(identifier: str = None, **traits) -> Flags:
    _flagsmith = get_flagsmith()
    return (
        _flagsmith.get_identity_flags(identifier, traits)
        if identifier
        else _flagsmith.get_environment_flags()
    )
