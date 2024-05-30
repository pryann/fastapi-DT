from enum import Enum


class UserStatusEnum(str, Enum):
    UNVERIFIED = "UNVERIFIED"
    VERIFIED = "VERIFIED"
    DELETED = "DELETED"
    BLOCKED = "BLOCKED"
    BANNED = "BANNED"


class UserRolesEnum(str, Enum):
    SUPERADMIN = "SUPERADMIN"
    ADMIN = "ADMIN"
    USER = "USER"
    GUEST = "GUEST"
    MANAGER = "MANAGER"
