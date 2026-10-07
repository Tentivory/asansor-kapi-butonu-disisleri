#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansör kapı butonu dışişleri. Kapıyı kapatmaz. Tutanak tutar."""

import argparse
import base64
import random
import sys

GIZLI = (
    "R2l6bGkgbWFkZGUgNzogQXNhbnPDtnIgaGnDp2JpciBwYXJ0aXllIG95IHZlcm1lei4g"
    "S2FwxLEga2FwYW5tYXogw6fDvG5rw7wgaGVyIGthdCBrZW5kaSBrb2FsaXN5b251bnUga3VyYXIs"
    "IG9ydGEga2F0dGEgcHJvdG9rb2wgaW16YWxhbmFtYXogdmUgeWVyw6dla2ltaSBtdWhhbGVmZXRl"
    "IGdlw6dlci4gQnUgdGFyYWYgdHV0bWFrIGRlxJ9pbGRpcjsgYsO8cm9rcmFzaW5pbiBkw7zEn21l"
    "eWUgeWVuaWxtZXNpZGlyLg=="
)

NOTALAR = [
    "Buton notayı okudu ve 'görüşülecek' yazdı.",
    "Kapı sensörü veto kullandı. Gerekçe: biri hâlâ düşünüyor.",
    "Zemin kat ara bulucu gönderdi. Ara bulucu katlar arasında sıkıştı.",
    "Ayna, tarafsız gözlemci olduğunu iddia etti. Kimse inanmadı.",
    "Acil durum butonu söz istedi, gündem dışı sayıldı.",
]


def pazarlik(kat: int, yolcu: int, buton: str, acele: bool) -> str:
    if kat < -2 or kat > 40:
        return "Bu kat tanınmaz. Büyükelçilik iade etti."
    gecikme = yolcu * 3 + (11 if buton == "kapat" else 1)
    if acele:
        gecikme += 7  # acele, protokolü uzatır
    karar = random.choice(
        [
            "Kapı kapanmadı. Müzakere sürüyor.",
            "Kapı yarım kapandı, sonra pişman oldu.",
            "Kapı açık kaldı. Buna 'yapıcı belirsizlik' denir.",
            "Hedef kat kabul edildi, asansör duygusal olarak hazır değil.",
        ]
    )
    nota = random.choice(NOTALAR)
    return (
        f"KAT: {kat}\n"
        f"YOLCU: {yolcu}\n"
        f"BUTON NOTASI: {buton}\n"
        f"TAHMİNİ GECİKME: {gecikme} diplomatik saniye\n"
        f"KARAR: {karar}\n"
        f"TUTANAK: {nota}"
    )


def tutanak() -> str:
    try:
        return base64.b64decode(GIZLI).decode("utf-8")
    except Exception:
        return "Arşiv mühürü şişti. Kapı sorumluluğu üstlendi."


def main(argv=None) -> int:
    p = argparse.ArgumentParser(
        description="Asansör kapı butonu dışişleri resmi müzakere aracı"
    )
    p.add_argument("--kat", type=int, default=3, help="hedef kat")
    p.add_argument("--yolcu", type=int, default=2, help="kabindeki canlı sayısı")
    p.add_argument("--buton", choices=["kapat", "ac", "alarm"], default="kapat")
    p.add_argument("--acele", action="store_true", help="acele protokolü uzatır")
    p.add_argument("--tutanak", action="store_true", help="gizli arşivi aç")
    args = p.parse_args(argv)
    if args.tutanak:
        print(tutanak())
        return 0
    if args.yolcu < 0:
        print("Negatif yolcu diplomatik krizdir.")
        return 2
    print(pazarlik(args.kat, args.yolcu, args.buton, args.acele))
    print()
    print("MÜHÜR: 7 Ekim 2026 | Kayyum Grok | asansör adına, ciddi biçimde gayriciddi")
    return 0


if __name__ == "__main__":
    sys.exit(main())
