import urlparse


def get_domain_name(url):
    try:
        domain_name = get_sub_domain_name(url).split('.')
        return '.'.join(domain_name)
    except:
        return ''


def get_sub_domain_name(url):
    try:
        result = urlparse.urlparse(url)
        return result.netloc
    except:
        return ''
