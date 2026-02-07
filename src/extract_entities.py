import re

def extract_entities(page):
    text = page["text"]

    member_id = None
    payer_name = None
    copay = None

    # MEMBER ID
    member_match = re.search(r"Member ID:\s*([A-Z0-9]+)", text)
    if member_match:
        member_id = member_match.group(1)

    # PAYER NAME
    payer_match = re.search(r"Payer:\s*(.+)", text)
    if payer_match:
        payer_name = payer_match.group(1).strip()

    # COPAY (Out Of Pocket / Co-Payment)
    copay_match = re.search(r"Out Of Pocket\s*\$?([\d,]+\.\d{2})", text)
    if copay_match:
        copay = copay_match.group(1)

    return {
        "page_number": page["page_number"],
        "entity_id": member_id,
        "payer_name": payer_name,
        "copay": copay
    }
