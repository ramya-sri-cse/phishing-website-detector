from urllib.parse import urlparse
import re


def extract_features(url):

    parsed = urlparse(url)
    domain = parsed.netloc.lower()

    # Remove port number if present
    domain_without_port = domain.split(":")[0]

    # URLLength
    url_length = len(url)

    # DomainLength
    domain_length = len(domain_without_port)

    # IsDomainIP
    is_domain_ip = 1 if re.fullmatch(
        r"\d{1,3}(\.\d{1,3}){3}",
        domain_without_port
    ) else 0

    # NoOfSubDomain
    parts = domain_without_port.split(".")
    no_of_subdomain = max(len(parts) - 2, 0)

    # NoOfLettersInURL
    no_of_letters = sum(c.isalpha() for c in url)

    # NoOfDigitsInURL
    no_of_digits = sum(c.isdigit() for c in url)

    # NoOfEqualsInURL
    no_of_equals = url.count("=")

    # NoOfQMarkInURL
    no_of_qmark = url.count("?")

    # NoOfAmpersandInURL
    no_of_ampersand = url.count("&")

    # NoOfOtherSpecialCharsInURL
    special_chars = set("!#$%&'()*+,;:=?@[]^_`{|}~")
    no_of_other_special = sum(
        c in special_chars
        for c in url
    )

    # IsHTTPS
    is_https = 1 if parsed.scheme.lower() == "https" else 0

    return [
        url_length,
        domain_length,
        is_domain_ip,
        no_of_subdomain,
        no_of_letters,
        no_of_digits,
        no_of_equals,
        no_of_qmark,
        no_of_ampersand,
        no_of_other_special,
        is_https
    ]