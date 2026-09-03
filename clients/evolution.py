import json
import os
import re
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


class EvolutionError(Exception):
    pass


def normalize_phone(phone: str) -> str:
    number = re.sub(r"\D", "", phone)
    if len(number) in (10, 11):
        number = f"55{number}"
    if len(number) < 12:
        raise EvolutionError("Telefone inválido para envio no WhatsApp.")
    return number


def send_text(phone: str, text: str) -> dict:
    base_url = os.environ.get("EVOLUTION_GO_URL", "").rstrip("/")
    api_key = os.environ.get("EVOLUTION_GO_API_KEY", "")
    if not base_url or not api_key:
        raise EvolutionError("EVOLUTION_GO_URL e EVOLUTION_GO_API_KEY precisam ser configuradas.")

    request = Request(
        f"{base_url}/send/text",
        data=json.dumps({"number": normalize_phone(phone), "text": text}).encode(),
        headers={"Content-Type": "application/json", "apikey": api_key},
        method="POST",
    )
    try:
        with urlopen(request, timeout=20) as response:
            return json.loads(response.read().decode() or "{}")
    except HTTPError as error:
        details = error.read().decode(errors="replace")
        raise EvolutionError(f"Evolution Go respondeu {error.code}: {details[:300]}") from error
    except URLError as error:
        raise EvolutionError(f"Não foi possível acessar a Evolution Go: {error.reason}") from error
