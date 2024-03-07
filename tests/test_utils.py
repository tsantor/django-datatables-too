import pytest
from django.contrib.auth.models import Permission

from django_perm_filter.utils import filter_perms


@pytest.mark.django_db
def test_filter_perms():
    qs = Permission.objects.all()
    results = filter_perms(qs)
    # Ensure that no permissions with the following codenames are returned
    codenames = [
        "view_permission",
        "create_permission",
        "change_permission",
        "delete_permission",
    ]
    assert all(not any(codename in perm.codename for codename in codenames) for perm in results)
