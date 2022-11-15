from service.format_price import FormatPrice


def test_format_str_price_to_float():
    valor_caso_um = FormatPrice().format_str_price_to_float("R$ 39,90")
    valor_caso_dois = FormatPrice().format_str_price_to_float("Não vai")
    valor_caso_tres = FormatPrice().format_str_price_to_float("R$ 1.240,92")

    assert valor_caso_um == 39.90
    assert valor_caso_dois == 0
    assert valor_caso_tres == 0
