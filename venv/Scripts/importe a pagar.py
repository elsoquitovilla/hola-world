total_compra = 101
total_compra =importe_a_pagar
if total_compra >= 100:
    tasa_descuento = 10
    importe_descuento = ((total_compra * (tasa_descuento / 100))
    importe_a_pagar = total_compra – importe_descuento
    print importe_a_pagar
