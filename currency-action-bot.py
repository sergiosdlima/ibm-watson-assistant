#
#
# main() será executado quando você chamar essa ação
#
# @param As ações do Cloud Functions aceitam um único parâmetro, que deve ser um objeto JSON.
#
# @return A saída dessa ação, que deve ser um objeto JSON.
#
#
import requests

coins = {
    "Dólar Americano": "USD",
    "Dólar Canadense": "CAD",
    "Euro": "EUR",
    "Libra Esterlina": "GBP",
    "Peso Argentino": "ARS",
    "Bitcoin": "BTC",
    "Litecoin": "LTC",
    "Iene Japonês": "JPY",
    "Franco Suíço": "CHF",
    "Dólar Australiano": "AUD",
    "Yuan Chinês": "CNY",
    "Novo Shekel Israelense": "ILS",
    "Ethereum": "ETH",
    "XRP": "XRP",
    "Dogecoin": "DOGE",
    "Dólar de Cingapura": "SGD",
    "Dirham dos Emirados": "AED",
    "Coroa Dinamarquesa": "DKK",
    "Dólar de Hong Kong": "HKD",
    "Peso Mexicano": "MXN",
    "Coroa Norueguesa": "NOK",
    "Dólar Neozelandês": "NZD",
    "Zlóti Polonês": "PLN",
    "Riyal Saudita": "SAR",
    "Coroa Sueca": "SEK",
    "Baht Tailandês": "THB",
    "Nova Lira Turca": "TRY",
    "Dólar Taiuanês": "TWD",
    "Rand Sul-Africano": "ZAR",
    "Peso Chileno": "CLP",
    "Guarani Paraguaio": "PYG",
    "Peso Uruguaio": "UYU",
    "Peso Colombiano": "COP",
    "Sol do Peru": "PEN",
    "Boliviano": "BOB",
    "Rublo Russo": "RUB",
    "Rúpia Indiana": "INR",
}

def real_br_money_mask(my_value):
    a = "R${:,.2f}".format(float(my_value))
    b = a.replace(",","v")
    c = b.replace(".",",")
    return c.replace("v",".")

def main(dict):
    currency_code = coins.get(dict["currency"])
    
    if currency_code:
        r = requests.get("https://economia.awesomeapi.com.br/json/last/" + currency_code)
        if r.status_code == requests.codes.ok:
            quotation = r.json()[currency_code + "BRL"]
            brazilian_money = real_br_money_mask(quotation["ask"])
            return {"msg": "1 " + dict["currency"] + " equivale a " + brazilian_money + "."}
        else:
            return {"msg": r.text["message"]}
    else:
        return {"msg": "Moeda não encontrada."}