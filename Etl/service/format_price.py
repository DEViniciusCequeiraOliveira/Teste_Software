class FormatPrice:
    def format_str_price_to_float(self, price: str) -> float:
        try:
            return float(price.replace("R$ ", "").replace(",", "."))
        except:
            return 0