from refextract import extract_references_from_file
from difflib import SequenceMatcher

def extract_refs(file):
    refs_full = extract_references_from_file(file)
    return [r[0]['raw_ref'][0] for r in refs_full]


def match_names(a: str, b: str):
    match = SequenceMatcher(None, a, b).find_longest_match()
    return match.size > 16
