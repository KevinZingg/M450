from db_operations import get_bad_sites_from_db

def is_domain_safe(full_url: str) -> bool:
    bad_sites = get_bad_sites_from_db()
    if full_url in bad_sites:
        return False
    return True
